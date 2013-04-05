#!/usr/bin/python

import argparse
import os, sys, math, time, datetime, logging
from SideCar import SideCar
import xmptags

def evChanged(a, b):
    """Has the EV changed?  Check f/stop, shutter speed and ISO."""
    return (a.getFNumber() != b.getFNumber()
            or a.getExposureTime() != b.getExposureTime()
            or a.getISOSpeedRating() != b.getISOSpeedRating())

def interpolate(seq, schema):
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
            logger.debug("skipping %s because a keyframe is None", key)
            continue

        logger.info("tweening %s from %s to %s across %s files", key, orig, dest, factor)
        for idx, xmp in enumerate(seq[a+1:b]):
            dlt = dest - orig
            inc = dlt / factor
            value = orig + inc * (idx + 1)
#            print '%s: Changing %s from %s to %s (+%s)' % (xmp.filename, key, xmp.get(key), value, inc)
#            print '%s: Changing %s from %s to %s (+%s)' % ('filename', key, xmp.get(key), value, inc)
            logger.info("%s: Changing %s from %s to %s (+%s)", 'filename', key, xmp.get(key), value, inc)
            xmp.set(key, value)


# Create logger
LOG_FILENAME = 'timeroom.log'
logger = logging.getLogger("TimeRoom")
logging.basicConfig(filename=LOG_FILENAME, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Define arguments
parser = argparse.ArgumentParser(description='Interpolate CRS values in a time lapse sequence of XMP sidecars.')
parser.add_argument('--init', dest='init', action='store_true', default=False,
                   help='detect and initialize keyframes based on EV changes')
parser.add_argument('sidecars', metavar='sidecars', type=str, nargs='+',
                   help='a list of xmp files to process (will be ordered alphabetically)')

args = parser.parse_args()

if len(args.sidecars) < 2:
    print 'Expect 2 sidecars minimum, exiting.'
    sys.exit(1)

args.sidecars.sort(key=len)
logger.info("File list: %s", args.sidecars)


# Create Sidecar objects for all files
sidecars = []
keyframes = []

for filename in args.sidecars:
    logger.info("Loading %s...", filename)
    xmp = SideCar(filename)
    sidecars.append(xmp)
    if not args.init and xmp.getRating():
        keyframes.append(sidecars.index(xmp))

logger.info("Successfully loaded %s files.", len(sidecars))


if args.init:
    # Detect and initialise keyframes based on EV changes
    last_xmp = None
    keyframes.append(0)
    for xmp in sidecars:
        if last_xmp:
            if evChanged(last_xmp, xmp):
                last_xmp.setRating(2)
                xmp.setRating(3)
                keyframes.append(sidecars.index(last_xmp))
                keyframes.append(sidecars.index(xmp))
            else:
                xmp.setRating(0)
        last_xmp = xmp
    sidecars[0].setRating(1)
    sidecars[-1].setRating(1)
    keyframes.append(sidecars.index(sidecars[-1]))

    for i in keyframes:
        xmp = sidecars[i]
        if xmp.getRating():
            print '%s: f/%d %s ISO=%d rating=%d' % (xmp.filename,
                                                    xmp.getFNumber(),
                                                    xmp.getExposureTime(),
                                                    xmp.getISOSpeedRating(),
                                                    xmp.getRating())
        xmp.save()

    print 'Initialised %d keyframes.' % (len(keyframes))
    sys.exit(0)


else:

    # Interpolate CRS values between keyframes
    i = iter(keyframes)
    b = i.next()
    try:
        while (True):
            a = b         # index of starting xmp in sidecars
            b = i.next()  # index of ending xmp in sidecars

            seq = sidecars[a:b+1]
            cnt = len(seq) - 1

            print '%s: Start keyframe, rating = %d' % (sidecars[a].filename, sidecars[a].getRating())

            # Interpolate top-level CRS settings
            interpolate(seq, xmptags.CRS_TAGS)

            # Interpolate GradientBasedCorrections & CorrectionMasks
            gbcslist = []
            cmslist = []
            for gdb in sidecars[a].GradientBasedCorrections:
                gbcslist.append([])
                cmslist.append([])
            for xmp in seq:
                n = len(xmp.GradientBasedCorrections)
                if n != len(gbcslist):
                    print '%s has %d GradientBasedCorrections, expected %d (%s).  Exiting.' % (xmp.filename,
                                                                                               n,
                                                                                               len(gbcslist),
                                                                                               sidecars[a].filename)
                    sys.exit(1)
                for idx, gbc in enumerate(xmp.GradientBasedCorrections):
                    gbcslist[idx].append(gbc)
                    cmslist[idx].append(gbc.CorrectionMasks[0])

            for gbcs in gbcslist:
                print 'Interpolating GBCs'
                interpolate(gbcs, xmptags.CRS_GBC_TAGS)

            for cms in cmslist:
                print 'Interpolating CMs'
                interpolate(cms, xmptags.CRS_GBC_CM_TAGS)

            print '%s: End keyframe, rating = %d' % (sidecars[b].filename, sidecars[b].getRating())
    except StopIteration:
        pass

    logger.info("Saving")
    for xmp in sidecars:
        xmp.save()

logger.info("Exiting successfully")
