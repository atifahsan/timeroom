#!/usr/bin/python
# Currently this script will increase the Exposure2012 level by 1

import argparse
import os, sys, math, time, datetime, logging
from SideCar import SideCar

# Create logger
LOG_FILENAME = 'timeroom.log'
logger = logging.getLogger("TimeRoom")
logging.basicConfig(filename=LOG_FILENAME, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)

# Define arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('sidecars', metavar='sidecars', type=str, nargs='+',
                   help='a list of xmp files to process (will be ordered alphabetically)')

args = parser.parse_args()

args.sidecars.sort()
logger.info("File list: %s", args.sidecars)

sidecars = []

for item in args.sidecars:
  logger.info("Loading %s...", item)
  xmp = SideCar(item)
  sidecars.append(xmp)

logger.info("Successfully loaded %s files.", len(sidecars))

for item in sidecars:
  print item.get("RawFileName")