#!/usr/bin/python

import getopt, sys
import datetime, logging
import xml.etree.ElementTree as ET

# Create logger
LOG_FILENAME = 'timeroom.log'
logger = logging.getLogger("SideCar")
logging.basicConfig(filename=LOG_FILENAME, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)

# Register Namespaces
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

class SideCar:
  """Class to represent an xmp RAW sidecar file"""
  filename = None
  data = {}

  def __init__(self, filename):
    self.filename = filename

    # open file
    self.tree = ET.parse(filename)
    return

  def get(self, key):
    root = self.tree.getroot()
    rdfElement = root.find("")

    parentXPath = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description"
    keyXPath = '{{http://ns.adobe.com/camera-raw-settings/1.0/}}{0}'.format(key)
    fullXPath = "{0}/{1}".format(parentXPath, keyXPath)

    element = root.find(fullXPath)
    if (element == None):
      parentElement = root.find(parentXPath)
      val = parentElement.get(keyXPath)
      logger.info("attribute value = %s", val)
      return val
    else:
      logger.info("element value = %s", element.text)
      return element.text

  def set(self, key, value):
    # save value (preserve format with element or attr)
    return

  def save(self):
    self.tree.write(self.filename)
    return




