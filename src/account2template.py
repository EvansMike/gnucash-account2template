#!/bin/env python2

# Convert an exported account to an account template.
# The exported account contains no data but it does contain import matching rules
# and the header nees to be slightly modified.



from lxml import etree
from lxml import objectify
import os
import sys


class a2t(object):
    def __init__(self):
        return
        

        
    def convert(self, infile):
        
        tree = etree.parse(infile)
        root = tree.getroot()
        namespace = root.nsmap
        namespace['gnc-act'] = 'http://www.gnucash.org/XML/gnc-act'
        #root.nsmap = namespace
        to_clear = []
        for child in root.iter():
            if child.text == "import-map-bayes":
                print  "Removing element named =",child.text, child.values()
                p = child.getparent()
                to_clear.append(p)
            if child.text == "import-map":
                print  "Removing element named =",child.text, child.values()
                p = child.getparent()
                to_clear.append(p)
        
        # remove the commodities
        for child in root.iter():
            print child.tag
            if child.tag == '{http://www.gnucash.org/XML/gnc}commodity':
                to_clear.append(child)
        # Now delete our collection of Elements
        for p in to_clear:
            p.clear()
        tree.write('output.gnucash.xea')
        # replace the entire header section using just ordinary file parsing
        f = open('output.gnucash.xea', 'rb')
        # Find the line with 'ROOT' in it then delete from the NEXT line up
        
        
        
       
        return



if __name__ == "__main__":
    try:
        infile = sys.argv[1]
        print "Opening", infile
    except:
        print "No input file specified"
        quit(1)
    app = a2t()
    app.convert(infile)
