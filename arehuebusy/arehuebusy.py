#!/usr/bin/python
from phue import Bridge
from pprint import pprint
from rgb_xy import Converter
from rgb_xy import GamutC
import sys
import rgb_xy
import logging
import json
import yaml
import os
from os.path import expanduser

__version__ = "0.9.0"

def main():
   config={}
   try:
      config_file = os.path.join(expanduser("~"), ".arehuebusy.yml")
      with open(config_file, 'r') as f:
	 config=yaml.load(f)
   except Exception as e:
      print "Error loading config.yml"
      print e
      sys.exit(2)

   valid_status = config["status"].keys()
   if len(sys.argv) < 2 or sys.argv[1] not in valid_status:
      print "Missing or invalid status"
      print "Usage: arehuebusy <%s>" % (','.join(valid_status))
      sys.exit(2)

   status = sys.argv[1]

   logging.basicConfig()
   b = Bridge (config["bridge_ip"])
   b.connect()
   status_config = config["status"][status]
   print status_config["color"]
   print "Setting %s to %s, brightness %s . . ." % (config["light"], status_config["color"], status_config["brightness"])
   converter = Converter(GamutC)
   x,y = converter.hex_to_xy(status_config["color"])
   busy_light = b.get_light_objects('name')[config["light"]]
   busy_light.xy=[x,y] 
   busy_light.brightness=status_config["brightness"]
