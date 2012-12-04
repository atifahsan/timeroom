#!/usr/bin/python
# Currently this script will increase the Exposure2012 level by 1

import argparse
import os, sys, math, time, datetime, logging
from SideCar import SideCar
import crstags
from glob import glob

def noEasing(t, b, c, d):
  return c * t / d + b;

# Create logger
LOG_FILENAME = 'timeroom.log'
logger = logging.getLogger("TimeRoom")
logging.basicConfig(filename=LOG_FILENAME, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Define arguments
parser = argparse.ArgumentParser(description='Interpolate CRS values in a time lapse sequence of XMP sidecars.')
parser.add_argument('sidecars', metavar='sidecars', type=str, nargs='+',
                   help='a list of xmp files to process (will be ordered alphabetically)')

args = parser.parse_args()
print "args", args.sidecars[0]
s = glob(args.sidecars[0])
s.sort()
s.sort(key=len)
print "Files: ", s
logger.info("File list: %s", s)

sidecars = []

for item in s:
  logger.info("Loading %s...", item)
  xmp = SideCar(item)
  sidecars.append(xmp)

logger.info("Successfully loaded %s files.", len(sidecars))

#Determine keys to tween
keys = []
for key in crstags.CRS_TAGS:
  t, d = crstags.CRS_TAGS[key]
  if ( t < 4 ):
    keys.append(key)

for key in keys:
  ##### tween (convert to method)
  orig = sidecars[0].get(key)
  dest = sidecars[ len(sidecars) - 1 ].get(key)
  if (dest == None or orig == None):
    logger.debug("skipping %s because a keyframe is None", key)
    continue
  size = float(len(sidecars)-1)

  logger.info("tweening %s from %s to %s across %s files", key, orig, dest, size)
  for idx, item in enumerate(sidecars):
    factor = noEasing(idx, 0, 1, size);
    value = orig + ( dest - orig ) * factor
    item.set( key, value )
  ##### end tween

# Save the data
logger.info("Saving...")
for item in sidecars:
  item.save()

logger.info("Done")
print "Done"
