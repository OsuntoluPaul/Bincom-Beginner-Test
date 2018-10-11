"""
NAME:   OSUNTOLU PAUL ADEDIRAN
EMAIL:  neptunecody@gmail.com
PHONE:  09025111684

Question A: Extracting colors from a webpage
"""

#import regular expression, urllib library, numpy
import re
import urllib, urllib2

#open webpage file using urllib.urlopen and read using the .read()
file = urllib.urlopen("python_class_test.html")
file = file.read()

#define a function for the regular expression matched
def expression():

    #create a pattern to match the color
    pattern = re.compile(r'<td>([A-Z]+, \w.+?)</td>')

    #find all matched pattern
    matches = re.findall(pattern, file)

    #iterate through the patterns matched and extract the colors
    for match in matches:

        items = match.split(" ")
        print items

expression()
