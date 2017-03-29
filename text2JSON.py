#!/usr/bin/env python

""" text2JSON.py: The single command line argument is the path to a text file of
        the format exported by clicking on the 'Save Text' button on
	http://syssci.renci.org/sort/. The result is another file with the same
	path except with the extension '.json' that contains a JSON object 
	equivalent to what you would have gotten if you'd clicked on the 'Save
	JSON' button. See https://github.com/steve9000gi/sort for details.
"""

import sys
import os
import json

def generate_outfilename(infilename):
    """ Output file gets the same name as input file except with the extension
            (probably '.txt') replaced with '.json'.
    """
    return os.path.splitext(infilename)[0] + '.json'

def convert_list_to_dict(lst):
    """ Actual argument 'lst' is expected to be a sequence of strings 
            conceptually divided into subclusters by empty strings. The first 
	    subcluster is expected not to be preceded by an empty string.  More
	    than one empty string element in a row will cause an error. The
	    first string in each subcluster is expected to have a colon as its
	    final character, which is stripped off, after which that first
	    string is used as the key in a key-value pair. The remaining strings
	    in each subcluster are placed into a list which is used as the value
	    in the key-value pair corresponding to that subcluster.
    """
    dct = {}
    i = 0
    lst_len = len(lst)
    while i < lst_len: 
        key = lst[i]
        key = key[:-1]
        vals = []
        i += 1
        while len(lst[i]) != 0:
            vals.append(lst[i])
	    i += 1
        dct[key] = vals
        i += 1
    return dct

def get_list_from_file(infilename):
    """ Read the file into a list of strings, removing the newlines.
    """
    with open(infilename) as f:
        lst = f.readlines()
    return [x.strip() for x in lst]


# main:
infilename = sys.argv[1]
outfilename = generate_outfilename(infilename)
print sys.argv[0] + ': ' + infilename + ' -> ' + outfilename

lst = get_list_from_file(infilename)
with open(outfilename, 'w') as outfile:
    json.dump(convert_list_to_dict(lst), outfile)


