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
  root = None

  def __init__(self, filename):
    self.filename = filename
    self.tree = ET.parse(filename)
    self.root = self.tree.getroot()
    return

  def get(self, key):
    parentXPath, keyXPath, fullXPath = self._getPaths(key)

    element = self.root.find(fullXPath)
    if (element == None):
      parentElement = self.root.find(parentXPath)
      val = parentElement.get(keyXPath)
      logger.info("reading attribute %s = %s", key, val)
      return float(val)
    else:
      logger.info("reading element %s = %s", key, element.text)
      return float(element.text)

  def set(self, key, value):
    # save value (preserve format with element or attr)
    parentXPath, keyXPath, fullXPath = self._getPaths(key)

    element = self.root.find(fullXPath)
    if (element == None):
      parentElement = self.root.find(parentXPath)
      oldVal = parentElement.get(keyXPath)
      logger.info("changing attribute %s = %s to %s", key, oldVal, value)
      parentElement.set(keyXPath, str(value))
      return
    else:
      logger.info("changing element value %s = %s to %s", key, element.text, value)
      element.text = str(value)
      return

  def _getPaths(self, key):
    parentXPath = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF/{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description"
    keyXPath = '{{http://ns.adobe.com/camera-raw-settings/1.0/}}{0}'.format(key)
    fullXPath = "{0}/{1}".format(parentXPath, keyXPath)
    return parentXPath, keyXPath, fullXPath

  def save(self):
    self.tree.write(self.filename)
    return
