#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
from BeautifulSoup import BeautifulSoup
import urllib2
import re

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/html\n"
print

def main():
	
	form = cgi.FieldStorage()
	if form.has_key("website") and form["website"] != "":
		print form["website"].value
		urlStr = form["website"].value
		page = urllib2.urlopen(urlStr)
		soup = BeautifulSoup(''.join(page))
		print soup.prettify()
	else:
		print "<h1>Error! Please enter a website</h1>"
		
main()