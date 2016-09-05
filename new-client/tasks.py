#!/usr/bin/python
from invoke import run, task
from jconfig import Jconfig

@task(help={'trigram':'the trigram of the client', 'subnetid':'the third part of the private ip', 'clid':'client id the last two digit of the rd'})
def new_cust_dc1(trigram, subnetid, clid):

    t_path = 'templates/new-dc1/'
    t_vars = {
      'trigram': trigram,
      'subnetid': subnetid,
      'vlanid':'15'+clid,
      'admvlanid':'20'+clid,
      'rd': '20'+clid,
    } 

    t_vars['routerid'] = '13';
    j = Jconfig('sr-dc1-01.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-master-dc1.conf')
    j.loadconf(t_path+'sr/routing-instance-sr-dc1.conf')
    j.askcommit()

    t_vars['routerid'] = '14';
    j = Jconfig('sr-dc1-02.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-slave-dc1.conf')
    j.loadconf(t_path+'sr/routing-instance-sr-dc1.conf')
    j.askcommit()

    t_vars['routerid'] = '1';
    j = Jconfig('ar-dc2-01.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/vlan-if-master-dc2.conf')
    j.loadconf(t_path+'sr/routing-instance-ar-dc2.conf')
    j.askcommit()

    t_vars['routerid'] = '2';
    j = Jconfig('ar-dc2-02.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/vlan-if-slave-dc2.conf')
    j.loadconf(t_path+'sr/routing-instance-ar-dc2.conf')
    j.askcommit()

    j = Jconfig('fw-dc1-01.private.net', t_vars=t_vars)
    j.loadconf(t_path+'fw/interfaces-dc1.conf')
    j.loadconf(t_path+'fw/routing-options-dc1.conf')
    j.loadconf(t_path+'fw/bgp-dc1.conf')
    j.loadconf(t_path+'fw/nat.conf')
    j.loadconf(t_path+'fw/security-dc1.conf')
    j.askcommit()

    j = Jconfig('fw-dc2-01.private.net', t_vars=t_vars)
    j.loadconf(t_path+'fw/vlans-dc2.conf')
    j.loadconf(t_path+'fw/interfaces-dc2.conf')
    j.loadconf(t_path+'fw/routing-options-dc2.conf')
    j.loadconf(t_path+'fw/bgp-dc2.conf')
    j.loadconf(t_path+'fw/nat.conf')
    j.loadconf(t_path+'fw/security-dc2.conf')
    j.askcommit()


@task(help={'trigram':'the trigram of the client', 'subnetid':'the third part of the private ip', 'clid':'client id the last two digit of the rd'})
def new_cust_dc2(trigram, subnetid, clid):

    t_path = 'templates/new-dc2/'
    t_vars = {
      'trigram': trigram,
      'subnetid': subnetid,
      'vlanid':'15'+clid,
      'admvlanid':'20'+clid,
      'rd': '20'+clid,
    } 

    t_vars['routerid'] = '13';
    j = Jconfig('sr-dc1-01.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-master-dc1.conf')
    j.loadconf(t_path+'sr/routing-instance-sr-dc1.conf')
    j.askcommit()

    t_vars['routerid'] = '14';
    j = Jconfig('sr-dc1-02.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/groups.conf')
    j.loadconf(t_path+'sr/vlans.conf')
    j.loadconf(t_path+'sr/vlan-if-slave-dc1.conf')
    j.loadconf(t_path+'sr/routing-instance-sr-dc1.conf')
    j.askcommit()

    t_vars['routerid'] = '1';
    j = Jconfig('ar-dc2-01.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/vlan-if-master-dc2.conf')
    j.loadconf(t_path+'sr/routing-instance-ar-dc2.conf')
    j.askcommit()

    t_vars['routerid'] = '2';
    j = Jconfig('ar-dc2-02.corp.net', t_vars=t_vars)
    j.loadconf(t_path+'sr/vlan-if-slave-dc2.conf')
    j.loadconf(t_path+'sr/routing-instance-ar-dc2.conf')
    j.askcommit()

    j = Jconfig('fw-dc1-01.private.net', t_vars=t_vars)
    j.loadconf(t_path+'fw/interfaces-dc1.conf')
    j.loadconf(t_path+'fw/routing-options-dc1.conf')
    j.loadconf(t_path+'fw/bgp-dc1.conf')
    j.loadconf(t_path+'fw/nat.conf')
    j.loadconf(t_path+'fw/security-dc1.conf')
    j.askcommit()

    j = Jconfig('fw-dc2-01.private.net', t_vars=t_vars)
    j.loadconf(t_path+'fw/vlans-dc2.conf')
    j.loadconf(t_path+'fw/interfaces-dc2.conf')
    j.loadconf(t_path+'fw/routing-options-dc2.conf')
    j.loadconf(t_path+'fw/bgp-dc2.conf')
    j.loadconf(t_path+'fw/nat.conf')
    j.loadconf(t_path+'fw/security-dc2.conf')
    j.askcommit()


