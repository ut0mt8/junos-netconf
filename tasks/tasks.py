#!/usr/bin/python
from invoke import run, task
from jconfig import Jconfig

@task
def migrate_fw(trigram, subnetid, clid):

    t_path = 'templates/migration-fw/dc2/'
    t_vars = {
      'trigram': trigram,
      'subnetid': '101',
      'vlanid':'1601',
      'rd': '101'
    } 

    j = Jconfig('srx-dc3-01', t_vars=t_vars)
    j.loadconf(t_path+'fw/interfaces.conf')
    j.loadconf(t_path+'fw/routing-options.conf')
    j.loadconf(t_path+'fw/nat.conf')
    j.loadconf(t_path+'fw/security.conf')
    j.askcommit()

    t_vars['routerid'] = '12';
    j = Jconfig('sr-dc3-02', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/l3vpn-policies.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-slave.conf')
    j.loadconf(t_path+'sr/routing-instance.conf')
    j.askcommit()

    t_vars['routerid'] = '11';
    j = Jconfig('sr-dc3-01', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/l3vpn-policies.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-master.conf')
    j.loadconf(t_path+'sr/routing-instance.conf')
    j.askcommit()


@task
def new_client(trigram, subnetid, clid):

    t_path = 'templates/new-dc3/'
    t_vars = {
      'trigram': trigram,
      'subnetid': subnetid,
      'vlanid':'15'+clid,
      'admvlanid':'20'+clid,
      'rd': '20'+clid,
    } 

    j = Jconfig('srx-dc3-01', t_vars=t_vars)
    j.loadconf(t_path+'fw/interfaces.conf')
    j.loadconf(t_path+'fw/routing-options.conf')
    j.loadconf(t_path+'fw/nat.conf')
    j.loadconf(t_path+'fw/security.conf')
    j.askcommit()

    t_vars['routerid'] = '12';
    j = Jconfig('sr-dc3-02', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/l3vpn-policies.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-slave.conf')
    j.loadconf(t_path+'sr/routing-instance.conf')
    j.askcommit()

    t_vars['routerid'] = '11';
    j = Jconfig('sr-dc3-01', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/l3vpn-policies.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-master.conf')
    j.loadconf(t_path+'sr/routing-instance.conf')
    j.askcommit()


@task
def clean_vrf(trigram, rd):

    t_path = 'templates/clean-vrf/'
    t_vars = {
      'trigram': trigram,
      'rd': rd,
    } 
    
    #for router in ['sr-dc3-02', 'sr-dc3-01', 'sr-dc2-02', 'sr-dc2-01']:
    for router in ['sr-dc3-02', 'sr-dc3-01']:
        j = Jconfig(router, t_vars=t_vars)
	j.loadconf(t_path+'sr/l3vpn-policies.xml')
	j.loadconf(t_path+'sr/routing-instance.xml')
	j.loadconf(t_path+'sr/routing-instance.conf')
        j.commit()


@task
def show_conf(host):
    j = Jconfig(host)
    print j.getconf()


