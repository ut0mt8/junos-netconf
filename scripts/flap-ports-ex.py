#!/usr/bin/python

import sys
from jnpr.junos.utils.config import Config
from jnpr.junos.factory import loadyaml
from jnpr.junos import Device
from jnpr.junos.op.phyport import *

if len(sys.argv) > 2:
    print 'wrong number of arguments. Please read the how-to.txt'
    sys.exit(2)

dev = Device(sys.argv[1], user='rancid', password='xxxx')
dev.open()
ports = PhyPortTable(dev).get()

print "Port,Status,Flapped" 
 
for port in ports:
    print("%s,%s,%s" % (port.key, port.oper, port.flapped))
dev.close()


