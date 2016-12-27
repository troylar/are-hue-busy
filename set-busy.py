#!/usr/bin/python
from phue import Bridge
from pprint import pprint
from rgb_xy import Converter
from rgb_xy import GamutC
import sys
import argparse
import rgb_xy
import logging
import json
import yaml

config={}
try:
   with open('config.yml', 'r') as f:
      config=yaml.load(f)
except Exception as e:
   print "Error loading config.yml"
   print e

parser = argparse.ArgumentParser(description="Set busy status color")
valid_status = config["status"].keys()
parser.add_argument("--status", help=','.join(valid_status))
args = parser.parse_args()
if not args.status or args.status not in valid_status:
   print "Missing or invalid status"
   parser.print_help()
   sys.exit(2)

logging.basicConfig()
b = Bridge (config["bridge_ip"])
b.connect()
status_config = config["status"][args.status]
print status_config["color"]
print "Setting %s to %s, brightness %s . . ." % (config["light"], status_config["color"], status_config["brightness"])
converter = Converter(GamutC)
x,y = converter.hex_to_xy(status_config["color"])
busy_light = b.get_light_objects('name')[config["light"]]
busy_light.xy=[x,y] 
busy_light.brightness=status_config["brightness"]
