#!/usr/bin/python
# usage: $ ./xml-xmp.py -i test-pics/img-20121124.xmp
# Currently this script will increase the Exposure2012 level by 1

import getopt, sys
import datetime, logging
import xml.etree.ElementTree as ET

# Create logger
LOG_FILENAME = 'timeroom.log'
logger = logging.getLogger("timeroom")
logging.basicConfig(filename=LOG_FILENAME, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)

opts, args = getopt.getopt(sys.argv[1:], "i:")
infile = None

if len(opts) < 1:
  assert False, "please specify an inpute file with '-i filename.xmp'"

for o, a in opts:
  if o == "-i":
    infile = a

tree = ET.parse(infile)


ET.register_namespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
ET.register_namespace("aux", "http://ns.adobe.com/exif/1.0/aux/")
ET.register_namespace("crs", "http://ns.adobe.com/camera-raw-settings/1.0/")
ET.register_namespace("x", "adobe:ns:meta/")
ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
ET.register_namespace("exif", "http://ns.adobe.com/exif/1.0/")
ET.register_namespace("lrt", "http://lrtimelapse.com/")
ET.register_namespace("photoshop", "http://ns.adobe.com/photoshop/1.0/")
ET.register_namespace("tiff", "http://ns.adobe.com/tiff/1.0/")
ET.register_namespace("xmp", "http://ns.adobe.com/xap/1.0/")
ET.register_namespace("xmpMM", "http://ns.adobe.com/xap/1.0/mm/")
ET.register_namespace("stEvt", "http://ns.adobe.com/xap/1.0/sType/ResourceEvent#")

root = tree.getroot()
rdfElement = root.find("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF")
descriptionsElements = rdfElement.findall("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description")
# TODO: the values can be either child elements or attributes on the Description
# element. So, we need to try a get AND and find. One of them should work.
val = descriptionsElements[0].get("{http://ns.adobe.com/camera-raw-settings/1.0/}Exposure2012")
if (val == None):
  valElement = descriptionsElements[1].find("{http://ns.adobe.com/camera-raw-settings/1.0/}Exposure2012")
  logger.info("element value = %s", valElement.text)
  # Increment Exposure level by 1
  valElement.text = str(float(valElement.text)+1)
else:
  logger.info("attribute value = %s", val)
  # Increment Exposure level by 1
  descriptionsElements[0].set("{http://ns.adobe.com/camera-raw-settings/1.0/}Exposure2012", str(float(val)+1))

tree.write(infile)