#!/usr/bin/python

import xml.etree.ElementTree as ET
import xmptags
from fractions import Fraction
import sys

# Register Namespaces
NS_MAP = {
  "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
  "aux": "http://ns.adobe.com/exif/1.0/aux/",
  "crs": "http://ns.adobe.com/camera-raw-settings/1.0/",
  "x": "adobe:ns:meta/",
  "dc": "http://purl.org/dc/elements/1.1/",
  "exif": "http://ns.adobe.com/exif/1.0/",
  "lrt": "http://lrtimelapse.com/",
  "photoshop": "http://ns.adobe.com/photoshop/1.0/",
  "tiff": "http://ns.adobe.com/tiff/1.0/",
  "xmp": "http://ns.adobe.com/xap/1.0/",
  "xmpMM": "http://ns.adobe.com/xap/1.0/mm/",
  "stEvt": "http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
}

for ns in NS_MAP:
  ET.register_namespace(ns, NS_MAP[ns])


class SideCarLevel:
    """Class to represent a level in an XMP RAW sidecar file"""

    def __init__(self, root, ns, schema):
        self.root = root
        self.ns = ns
        self.schema = schema

    def _getDefault(self, key, ns, schema):
        """Return default value for key in schema"""
        t, d = schema[key]
        return d

    def _formatGet(self, key, value, ns, schema):
        """Return value with the correct datatype, or default value"""
        if value == None:
            return self._getDefault(key, ns, schema)

        t, d = schema[key]
        if t == xmptags.DataType.INT:
            return int(float(value))
        elif t == xmptags.DataType.REAL:
            return float(value)
        elif t == xmptags.DataType.SINT:
            if value[0] == '+':
                value = value[1:]
            return int(float(value))
        elif t == xmptags.DataType.RATIONAL:
            return Fraction(value)
        elif t == xmptags.DataType.STRING:
            return value
        else:
            return self._getDefault(key, ns, schema)

    def _get(self, key, ns, schema):
        """Get key in specified namespace, schema"""
        value = self.root.get("{{{0}}}{1}".format(NS_MAP[ns], key))

        return self._formatGet(key, value, ns, schema)

    def get(self, key, ns=None):
        """Get key in specified namespace, default schema"""
        if ns == None: ns = self.ns
        return self._get(key, ns, self.schema)

    def _set(self, key, value, ns, schema):
        if value == None or value == "None":
            value = ""

        self.root.set("{{{0}}}{1}".format(NS_MAP[ns], key), str(value))

    def set(self, key, value, ns=None):
        """Set key to value in specified namespace, default schema"""
        if ns == None: ns = self.ns
        return self._set(key, value, ns, self.schema)

class GradientBasedCorrection(SideCarLevel):
    """Class to represent a Lightroom GBC"""

    def __init__(self, root):
        SideCarLevel.__init__(self, root, 'crs', xmptags.CRS_GBC_TAGS)

        # Add list of CMs
        self.CorrectionMasks = []
        for cm in self.root.iter("{{{0}}}li".format(NS_MAP['rdf'])):
            self.CorrectionMasks.append(SideCarLevel(cm, 'crs', xmptags.CRS_GBC_CM_TAGS))

class ToneCurvePoint(SideCarLevel):
    """Class to represent a Lightroom ToneCurvePV2012 point"""
    def __init__(self, root):
        SideCarLevel.__init__(self, root, None, None)

    def _get(self):
        """Get point as [x, y] co-ordinates"""
        xy = self.root.text.split(', ')
        xy[0] = int(xy[0])
        xy[1] = int(xy[1])
        return xy

    def get(self, key):
        """Get x or y point"""
        x, y = self._get()

        if key == 'ToneCurvePV2012X':
            return x
        elif key == 'ToneCurvePV2012Y':
            return y
        else:
            return None

    def set(self, key, value):
        """Set x or y point"""
        x, y = self._get()

        if key == 'ToneCurvePV2012X':
            x = value
        elif key == 'ToneCurvePV2012Y':
            y = value

        self.root.text = "%d, %d" % (x, y)

class SideCarCorruptError(Exception):
    def __init__(self, filename, reason):
        self.filename = filename
        self.reason = reason

    def __str__(self):
        return '%s corrupt (%s)' % (self.filename, self.reason)

class SideCar(SideCarLevel):
    """Class to represent an XMP RAW sidecar file"""

    def __init__(self, filename):
        self.filename = filename
        self.tree = ET.parse(filename)
        self.curvesCount = 0

        path = "{{{0}}}RDF/{{{1}}}Description".format(NS_MAP['rdf'], NS_MAP['rdf'])
        SideCarLevel.__init__(self, self.tree.find(path), 'crs', xmptags.CRS_TAGS)

        # Add list of ToneCurves
        self.ToneCurves = []
        for idx, color in enumerate(['', 'Red', 'Green', 'Blue']):
            path = "{{{0}}}ToneCurvePV2012{1}".format(NS_MAP['crs'], color)
            tcroot = self.root.find(path)
            self.ToneCurves.append([])
            if tcroot == None:
                continue
            self.curvesCount = self.curvesCount + 1
            for point in tcroot.iter("{{{0}}}li".format(NS_MAP['rdf'])):
                self.ToneCurves[idx].append(ToneCurvePoint(point))
        if self.curvesCount > 0 and self.curvesCount < 4: # expect none missing or all missing
            raise SideCarCorruptError(filename, 'ToneCurvePV2012 has %d curves (expect 0 or 4)' % (self.curvesCount))

        # Add list of GBCs
        self.GradientBasedCorrections = []
        path = "{{{0}}}GradientBasedCorrections".format(NS_MAP['crs'])
        gbcroot = self.root.find(path)
        if gbcroot != None:
            for gbc in gbcroot.iter("{{{0}}}Description".format(NS_MAP['rdf'])):
                self.GradientBasedCorrections.append(GradientBasedCorrection(gbc))

    def getExposureTime(self):
        """Returns the exposure time"""
        return self._get('ExposureTime', 'exif', xmptags.EXIF_TAGS)

    def getFNumber(self):
        """Returns the aperture value"""
        return self._get('FNumber', 'exif', xmptags.EXIF_TAGS)

    def getISOSpeedRating(self):
        """Returns the ISO speed"""
        key = 'ISOSpeedRatings'
        ns = 'exif'
        path = "{{{0}}}{1}/{{{2}}}Seq/{{{3}}}li".format(NS_MAP[ns],
                                                        key,
                                                        NS_MAP['rdf'],
                                                        NS_MAP['rdf'])
        value = self.root.find(path).text
        return self._formatGet(key, value, ns, xmptags.EXIF_TAGS)

    def getRating(self):
        """Returns the XMP Rating"""
        return self._get('Rating', 'xmp', xmptags.XMP_TAGS)

    def setRating(self, value):
        """Sets the XMP Rating"""
        self._set('Rating', value, 'xmp', xmptags.XMP_TAGS)

    def getCurvesCount(self):
        """Returns the number of curves (should be 0 or 4)"""
        return self.curvesCount

    def getGradientsCount(self):
        """Returns the number of gradient based corrections"""
        return len(self.GradientBasedCorrections)

    def save(self):
        self.tree.write(self.filename)
