#!/usr/local/bin/python

import sys
import random
"""
if len(sys.argv) < 2:
	print "Enter Username: ",
	username = sys.stdin.readline()
else: username = sys.argv[1]

if username[-1] == '\n': username = username[:-1]
"""

words=[]
#datafile = open("/usr/local/share/genpw.words", "r")
datafile = open("/usr/share/dict/words", "r")
words = datafile.readlines()
nol = len(words)

chars = ['1','2','3','4','5','6','7','8','9','0','-','+']

random.seed()
firstword = words[random.randrange(nol)]
secondword = words[random.randrange(nol)]
#number = chars[random.randrange(len(chars))]
number = "-"
if firstword[-1] == '\n':
	firstword = firstword[:-1]
if secondword[-1] == '\n':
	secondword = firstword[:-1]

print "%s%s%s" % (firstword,number,secondword)
