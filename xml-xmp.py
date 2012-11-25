#!/usr/bin/python

import getopt, sys
import datetime
import xml.etree.ElementTree as ET

opts, args = getopt.getopt(sys.argv[1:], "i:")
infile = None

if len(opts) < 1:
  assert False, "please specify an inpute file with '-i filename.xmp'"

for o, a in opts:
  if o == "-i":
    infile = a

tree = ET.parse(infile)

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
root[0][1][2].text = '1'
tree.write('output.xml')