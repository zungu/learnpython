#!/usr/bin/python

from sys import argv

script, filename = argv

j = open(filename)

print j.read()