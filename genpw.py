#!/usr/bin/env - python

import sys
import random

#datafile = open("/usr/local/share/genpw.words", "r")
datafile = open("/usr/share/dict/words", "r")
words = datafile.readlines()

chars = ['1','2','3','4','5','6','7','8','9','0','-','+']
chars = ['/','-','+']

random.seed()
firstword = random.choice(words)
secondword = random.choice(words)
number = random.choice(chars)

print "%s%s%s" % (firstword.strip(), number, secondword.strip())
