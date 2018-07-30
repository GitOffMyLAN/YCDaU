#!/bin/python/
from optparse import OptionParser
import os, sys, re, subprocess
# Set the command arguments
parser = OptionParser()
parser.add_option("-c", "--config", dest="filename",
                  help="File that has the channel and download info", metavar="FILE")
parser.add_option("-a", "--add", dest="array",
                  help="To add a new youtube channel and any other info", metavar="ARRAY")
parser.add_option("-i", "--index", dest="index",
                  help="to set the index to which to read the file from, say to skip the entry 10 in your list then -i 10", metavar="")
parser.add_option("-s", "--spec-internet", dest="downloadSpeed",
                 help="To set the script to download at a set download speed")
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
    if options.index != None:
        i = int(options.index)
    else:
        i = 0
    while i < len(config_array):
        print(i)
        if options.downloadSpeed != None:
         command = "youtube-dl -r " + option.downloadSpeed + " -o '" + str(config_array[i][0]).replace('"', '') + "/%(title)s.%(ext)s'" + str(config_array[i][2]).replace('"', '') + str(config_array[i][1]).replace('"', '') 
        command = "youtube-dl -o '" + str(config_array[i][0]).replace('"', '') + "/%(title)s.%(ext)s'" + str(config_array[i][2]).replace('"', '') + str(config_array[i][1]).replace('"', '')
        print(command)
        os.system(command)
        i = i + 1
    config_file.close()
if options.array != None:
    print("Adding Youtube Channels")
    array = options.array.split(',')
    file = open(array[0], 'a')
    adding = "," + str(array)
    file.write(adding)
if options.init != None:
    print("Seting up init and configs")
    os.system("touch ~/youtube")
