#!/usr/bin/env python
import sys
 
#get all lines
for line in sys.stdin:
    
    #remove leading and trailing whitespace
    line = line.strip()

    #split the line
    words = line.split()

    #output tuples
    for word in words: 
        print '%s\t%s' % (word, "1")
