#!/usr/bin/python

import getopt, sys
import datetime, logging
import xml.etree.ElementTree as ET
import crstags

# Create logger
LOG_FILENAME = 'timeroom.log'
logger = logging.getLogger("SideCar")
logging.basicConfig(filename=LOG_FILENAME, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

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

class SideCar:
  """Class to represent an xmp RAW sidecar file"""
  filename, tree, root = None, None, None

  def __init__(self, filename):
    self.filename = filename
    self.tree = ET.parse(filename)
    self.root = self.tree.getroot()
    return

  def _getDefault(self, key):
    t, d = crstags.CRS_TAGS[key]
    return d

  def _formatGet(self, key, value):
    logger.debug("formatting get of value %s on key %s", value, key)
    if (value == None or value == 'None'): return self._getDefault(key)
    t, d = crstags.CRS_TAGS[key]
    if ( t == crstags.DataType.INT ):
      return int(float(value))
    elif ( t == crstags.DataType.REAL ):
      return float(value)
    elif ( t == crstags.DataType.SINT ):
      if ( value[0] == '+'): value = value[1:]
      return int(float(value))
    else:
      return self._getDefault(key)

  def _formatSet(self, key, value):
    logger.debug("formatting set of value %s on key %s", value, key)
    if (value == None or value == "None"): value = ""
    return str(value)

  def get(self, key):
    parentXPath, keyXPath, fullXPath = self._getPaths(key)

    element = self.root.find(fullXPath)
    if (element == None):
      parentElement = self.root.find(parentXPath)
      val = parentElement.get(keyXPath)
      r = self._formatGet(key, val)
      logger.debug("reading attribute %s = %s", key, r)
      return r
    else:
      r = self._formatGet(key, element.text)
      logger.debug("reading element %s = %s", key, r)
      return r

  def set(self, key, value):
    parentXPath, keyXPath, fullXPath = self._getPaths(key)

    element = self.root.find(fullXPath)
    if (element == None):
      parentElement = self.root.find(parentXPath)
      oldVal = parentElement.get(keyXPath)
      logger.debug("changing attribute %s = %s to %s", key, oldVal, value)
      parentElement.set(keyXPath, self._formatSet(key, value))
      return
    else:
      logger.debug("changing element value %s = %s to %s", key, element.text, value)
      element.text = self._formatSet(key, value)
      return

  def _getPaths(self, key):
    parentXPath = "{{{0}}}RDF/{{{1}}}Description".format( NS_MAP['rdf'], NS_MAP['rdf'])
    keyXPath = '{{{0}}}{1}'.format(NS_MAP['crs'], key)
    fullXPath = "{0}/{1}".format(parentXPath, keyXPath)
    return parentXPath, keyXPath, fullXPath

  def save(self):
    self.tree.write(self.filename)
    return
