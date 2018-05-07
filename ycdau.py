#!/bin/python/
from optparse import OptionParser
import os, sys
# Set the command arguments
parser = OptionParser()
parser.add_option("-c", "--config", dest="filename",
                  help="File that has the channel and download info", metavar="FILE")
parser.add_option("-a", "--add", dest="array",
                  help="To add a new youtube channel and any other info", metavar="ARRAY")
(options, args) = parser.parse_args()
print(options)
#finds the config file
if options.filename != None:
    print("Downloading Videos")
    config = options.filename
    print("Config file: %s" %format(config))
    config_file = open(config, 'r+')
    print(config_file.read())
if options.array != None:
    print("Adding Youtube Channels")
