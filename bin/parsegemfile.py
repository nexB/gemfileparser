#!/usr/bin/env python

import sys
sys.path.insert(0, '../gemfileparser')

from gemfileparser import GemfileParser

if len(sys.argv) < 2:
    print "Usage : parsegemfile <input file>"
    sys.exit(0)

parsed = GemfileParser(sys.argv[1])
output = parsed.parse()
for key, value in output.items():
    print key, ":"
    for item in value:
        print "\t", item
