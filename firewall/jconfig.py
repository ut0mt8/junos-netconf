from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree
from lxml.builder import E
from jinja2 import Template
import sys

class Jconfig:

    def __init__(self, host, user='rancid', password='xxxxxxx', t_vars={}):
        self.host = host
        self.user = user
        self.password = password
        self.t_vars = t_vars

        self.dev = Device(host=self.host, user=self.user, password=self.password, gather_facts=False)
        try:
            self.dev.open()
            self.dev.timeout = 300
            self.cfg = Config(self.dev)
        except Exception as err:
            print err
            sys.exit(1)

    def loadconf(self, t_file):
        try:
            print "=> Loading file %s on %s" % (t_file, self.host)
            self.cfg.load(template_path=t_file, template_vars=self.t_vars, overwrite=False, merge=True)
        except Exception as err:
            print err

    def askcommit(self):
        try:
            print "== Configuration diff on %s" % (self.host)
            self.cfg.pdiff()
            answer = raw_input('Do you want to commit change ? [y/n]')
            if answer[0] == 'y':
                self.cfg.commit()
        except Exception as err:
            print err

    def commit(self):
        try:
            print "== Configuration diff on %s" % (self.host)
            self.cfg.pdiff()
            self.cfg.commit()
        except Exception as err:
            print err
    
    def getconf(self):
        try:
            conf = self.dev.rpc.get_configuration(dict(format='text'))
            return etree.tostring(conf, method="text")
        except Exception as err:
            print err
