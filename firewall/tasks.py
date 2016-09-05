#!/usr/bin/python
from invoke import run, task
from jconfig import Jconfig

@task
def configure_fw():

    t_path = 'files/'

    j = Jconfig('fw-dc1-01')
    j.loadconf(t_path+'xml/applications.xml')
    j.loadconf(t_path+'xml/address-book.xml')
    j.loadconf(t_path+'xml/rules.xml')
    j.loadconf(t_path+'applications.conf')
    j.loadconf(t_path+'address-book.conf')
    j.loadconf(t_path+'rules.conf')
    j.askcommit()

    j = Jconfig('fw-dc2-01')
    j.loadconf(t_path+'xml/applications.xml')
    j.loadconf(t_path+'xml/address-book.xml')
    j.loadconf(t_path+'xml/rules.xml')
    j.loadconf(t_path+'applications.conf')
    j.loadconf(t_path+'address-book.conf')
    j.loadconf(t_path+'rules.conf')
    j.askcommit()

