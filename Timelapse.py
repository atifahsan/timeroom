#!/usr/bin/python

from SideCar import SideCar
import xmptags
import os
import glob
import sys

class Timelapse:
    """Class to represent a timelapse"""

    def __init__(self, path):
        self.filenames = [] # list of XMP filenames
        self.sidecars = []  # list of SideCar objects
        self.keyframes = [] # indexes of keyframes in sidecars[]
        self.ignore_grads = False
        self.ignore_curves = False

        os.chdir(path)
        for filename in sorted(glob.glob('*.[xX][mM][pP]')):
            self.filenames.append(filename)

    def readSideCars(self):
        if len(self.filenames) < 2:
            raise StandardError('Minimum of 2 sidecars required (found %d)' % (len(self.filenames)))

        self.sidecars = []
        self.keyframes = []

        for filename in self.filenames:
            sidecar = SideCar(filename)
            self.sidecars.append(sidecar)
            if sidecar.getRating():
                self.keyframes.append(self.sidecars.index(sidecar))

    def saveSideCars(self):
        for sidecar in self.sidecars:
            sidecar.save()

    def _evChanged(self, a, b):
        """Has the EV changed?  Check f/stop, shutter speed and ISO."""
        return (a.getFNumber() != b.getFNumber()
                or a.getExposureTime() != b.getExposureTime()
                or a.getISOSpeedRating() != b.getISOSpeedRating())

    def _interpolate(self, seq, schema):
        # Determine keys to interpolate
        keys = []
        for key in schema:
            t, d = schema[key]
            if t <= xmptags.DataType.MAX_TWEENABLE:
                keys.append(key)

        a = 0               # index of start keyframe (in seq)
        b = len(seq) - 1    # index of end keyframe (in seq)
        factor = len(seq) - 1

        for key in keys:
            orig = seq[a].get(key)
            dest = seq[b].get(key)

            if (dest == None or orig == None):
    #            logger.debug("skipping %s because a keyframe is None", key)
                continue

    #        logger.info("tweening %s from %s to %s across %s files", key, orig, dest, factor)
            for idx, xmp in enumerate(seq[a+1:b]):
                dlt = dest - orig
                inc = dlt / float(factor)
                value = type(dest)(orig + inc * (idx + 1))
    #            print '%s: Changing %s from %s to %s (+%s)' % (xmp.filename, key, xmp.get(key), value, inc)
    #            print '%s: Changing %s from %s to %s (+%s)' % ('filename', key, xmp.get(key), value, inc)
    #            logger.info("%s: Changing %s from %s to %s (+%.2f)", 'filename', key, xmp.get(key), value, inc)
                xmp.set(key, value)

    def initialize(self):
        last_sidecar = None

        self.keyframes = []
        for sidecar in self.sidecars:
            # White balance and point curves hack
            sidecar.set('Temperature', 5500)
            sidecar.set('Tint', 6)
            if last_sidecar:
                if self._evChanged(last_sidecar, sidecar):
                    last_sidecar.setRating(2)
                    sidecar.setRating(3)
                    self.keyframes.append(self.sidecars.index(last_sidecar))
                    self.keyframes.append(self.sidecars.index(sidecar))
                else:
                    sidecar.setRating(0)
            last_sidecar = sidecar
        self.sidecars[0].setRating(1)
        self.sidecars[-1].setRating(1)
        self.keyframes.insert(0, 0)                         # first keyframe
        self.keyframes.append(len(self.sidecars)-1)         # last keyframe
        self.keyframes = sorted(list(set(self.keyframes)))  # remove duplicates

    def process(self):
        if len(self.keyframes) < 2:
            raise StandardError('Minimum of 2 keyframes required (found %d).  Did you forget to initialize?' % (len(self.keyframes)))

        i = iter(self.keyframes)
        b = i.next()
        try:
            while (True):
                a = b         # index of starting xmp in sidecars
                b = i.next()  # index of ending xmp in sidecars

                seq = self.sidecars[a:b+1]
                cnt = len(seq) - 1

#                print '%s: Start keyframe, rating = %d' % (self.sidecars[a].filename, self.sidecars[a].getRating())
#                logger.info('%s: Start keyframe, rating = %d' % (self.sidecars[a].filename, self.sidecars[a].getRating()))

                # Interpolate top-level CRS settings
                self._interpolate(seq, xmptags.CRS_TAGS)

                if not self.ignore_grads:
                    # Interpolate GradientBasedCorrections (& CorrectionMasks)
                    gbcslist = []
                    cmslist = []
                    for gbc in self.sidecars[a].GradientBasedCorrections:
                        gbcslist.append([])
                        cmslist.append([])

                    for xmp in seq:
                        # Generate list of GBCs and associated CMs
                        n = len(xmp.GradientBasedCorrections)
                        if n != len(gbcslist):
                            raise StandardError('%s has %d GradientBasedCorrections, expected %d (%s).  Exiting.' % (xmp.filename,
                                                                                                                     n,
                                                                                                                     len(gbcslist),
                                                                                                                     self.sidecars[a].filename))
                        for idx, gbc in enumerate(xmp.GradientBasedCorrections):
                            gbcslist[idx].append(gbc)
                            cmslist[idx].append(gbc.CorrectionMasks[0])

                    # Do interpolation
                    for gbcs in gbcslist:
#                        print 'Interpolating GBCs'
                        self._interpolate(gbcs, xmptags.CRS_GBC_TAGS)
                    for cms in cmslist:
#                        print 'Interpolating CMs'
                        self._interpolate(cms, xmptags.CRS_GBC_CM_TAGS)

                if not self.ignore_curves:
                    # Interpolate ToneCurves
                    tcslist = []
                    for idx, tc in enumerate(self.sidecars[a].ToneCurves):
                        tcslist.append([])
                        for tcp in tc:
                            tcslist[idx].append([])
                    if len(tcslist) != 4 or len(self.sidecars[b].ToneCurves) != 4:
                        raise StandardError('%s has %d ToneCurvePV2012s, expecting 4!  Exiting.' % (xmp.filename, len(tcslist)))

                    for xmp in seq:
                        # Generate lists of TC points
                        n = len(xmp.ToneCurves)
                        if n != len(tcslist):
                            raise StandardError('%s has %d ToneCurvePV2012s, expecting 4!  Exiting.' % (xmp.filename, n))
                        for color, tc in enumerate(xmp.ToneCurves):
                            if len(tc) != len(tcslist[color]):
                                raise StandardError('%s has %d ToneCurvePV2012(%d) points, expecting %d!  Exiting.' % (xmp.filename,
                                                                                                                       len(tc),
                                                                                                                       color,
                                                                                                                       len(tcslist[color])))
                            for idx, tcp in enumerate(tc):
                                tcslist[color][idx].append(tcp)

                    # Do interpolation
                    for color, tc in enumerate(tcslist):
#                        print 'Interpolating TC color', color
                        for tcps in tc:
                            self._interpolate(tcps, xmptags.CRS_TC_TAGS)

#                print '%s: End keyframe, rating = %d' % (self.sidecars[b].filename, self.sidecars[b].getRating())
#                logger.info('%s: End keyframe, rating = %d' % (sidecars[b].filename, sidecars[b].getRating()))
        except StopIteration, e:
            pass
