#!/bin/python/
from optparse import OptionParser
import os, sys, re, subprocess
# Set the command arguments
parser = OptionParser()
parser.add_option("-c", "--config", dest="filename",
                  help="File that has the channel and download info", metavar="FILE")
parser.add_option("-a", "--add", dest="array",
                  help="To add a new youtube channel and any other info", metavar="ARRAY")
(options, args) = parser.parse_args()
#finds the config file
if options.filename != None:
    print("Downloading Videos")
    config = options.filename
    print("Config file: %s" %format(config))
    config_file = open(config , 'r')
    config_array = []
    for line in config_file:
        config_array.append(line.replace('[', '').replace('\n', '').replace(']', '').split(','))
    i = 0
    while i < len(config_array):
        print(i)
        command = "youtube-dl -o '" + str(config_array[i][0]).replace('"', '') + "/%(title)s.%(ext)s'" + str(config_array[i][2]).replace('"', '') + str(config_array[i][1]).replace('"', '')
        print(command)
        os.system(command)
        i = i + 1
    config_file.close()
if options.array != None:
    print("Adding Youtube Channels")
    array = options.array.replace('[', '').replace('\n', '').replace(']', '').split(',')
    file = open(array[0], 'a')
    adding = "," + str(array)
    file.write(adding)
