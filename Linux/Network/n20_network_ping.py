#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python2
import scapy.all as scapy
import optparse

def scapy_scan(ip):
    scapy.arping(ip)

scapy_scan("192.168.2.4/24")