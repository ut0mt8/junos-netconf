#!/usr/bin/python
# RMZ 2014

import sys, math
from jnpr.junos.utils.config import Config
from jnpr.junos import Device
from jnpr.junos.factory import loadyaml
globals().update(loadyaml('bgp-peer.yml'))


dev = Device(host='cr-xx-01', user='rancid', password='xxx' )
try:
  dev.open()
  results = BgpPeerTable(dev).get()
  cu = Config(dev)
except Exception as err:
  print err
  sys.exit(1)

for r in results:
  if r.peer_type == "External" and r.table == "inet.0" and r.policy != 'none' :
    neighbor,port = r.peer_address.split('+')
    ixt = r.policy.split('-')
    if ixt[1] == 'equinixix' and "RS" not in r.description :
      ix = ixt[1]
      prefix_limit = int(math.ceil(int(r.prefix_received)*1.25/10)*10)
      print("Peer: %s / %s, AS: %s, Pfx Received: %s / %s, IX : %s " % (neighbor, r.description, r.peer_as, r.prefix_received, prefix_limit, ix))
      cu.load("set protocols bgp group ipv4-%s-peer neighbor %s family inet unicast prefix-limit maximum %s" % (ix, neighbor, prefix_limit), format="set") 

cu.pdiff()
cu.commit()
dev.close()

