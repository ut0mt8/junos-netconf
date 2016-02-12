#!/usr/bin/python
# RMZ 2014

import sys
from jnpr.junos.utils.config import Config
from jnpr.junos import Device

dev = Device(host='blm-sw-dc3-01', user='rancid', password='xxx' )

try:
  dev.open()
  results = LLDPNeighborTable(dev).get()
except Exception as err:
  print err
  sys.exit(1)

for r in results:
  print r

dev.close()

