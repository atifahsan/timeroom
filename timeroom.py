#!/usr/bin/python

import argparse
import logging
from Timelapse import Timelapse
import sys

# Create logger
LOG_FILENAME = 'timeroom.log'
logger = logging.getLogger("TimeRoom")
logging.basicConfig(filename=LOG_FILENAME, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Define arguments
parser = argparse.ArgumentParser(description='Interpolate CRS values in a time lapse sequence of XMP sidecars.')
parser.add_argument('--init', dest='init', action='store_true', default=False,
                   help='detect and initialize keyframes based on EV changes')
parser.add_argument('--ignore-grads', dest='ignore_grads', action='store_true', default=False,
                   help='ignore graduated filters')
parser.add_argument('--ignore-curves', dest='ignore_curves', action='store_true', default=False,
                   help='ignore tone curves')
parser.add_argument('path', metavar='path', type=str,
                   help='path containing xmp files')
args = parser.parse_args()

timelapse = Timelapse(args.path)
timelapse.readSideCars()

timelapse.ignore_grads = args.ignore_grads
timelapse.ignore_curves = args.ignore_curves

if args.init:
    timelapse.initialize()
else:
    timelapse.process()

sys.exit(0)
