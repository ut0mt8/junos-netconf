#!/usr/bin/python
import sys
import difflib
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree

user='rancid'
password='xxxx'

def get_conf(host, filter_xml, exclude):
  dev = Device(host=host,user=user,password=password)
  dev.open()
  root = dev.rpc.get_config(filter_xml=filter_xml)
  dev.close()
  root.attrib.pop('changed-localtime')
  root.attrib.pop('changed-seconds')
  for child in root.findall(".//name"):
    if child.text in exclude:
      parent = child.getparent()
      parent.getparent().remove(parent)
  return etree.tostring(root)

def compare_conf(host1, host2, path, exclude=[]):
  flist = path.split('/')
  filter_xml = etree.Element('configuration')
  current_xml = filter_xml
  for f in flist:
    current_xml = etree.SubElement(current_xml,f)

  conf1 = get_conf(host1, filter_xml, exclude)
  conf2 = get_conf(host2, filter_xml, exclude)
  if conf1 != conf2:
    conf1 = conf1.splitlines(1)
    conf2 = conf2.splitlines(1)
    diff =  difflib.unified_diff(conf1, conf2)
    print ''.join(diff)

compare_conf('fw-dc1-01', 'fw-dc2-01', 'groups', ['node0','node1','uplk-admin','uplk-custs'])
compare_conf('fw-dc1-01', 'fw-dc2-01', 'routing-options')
compare_conf('fw-dc1-01', 'fw-dc2-01', 'security/policies' )
compare_conf('fw-dc1-01', 'fw-dc2-01', 'applications')


