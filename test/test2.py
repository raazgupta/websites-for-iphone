#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/html\n"
print

def main():
	
	form = cgi.FieldStorage()
	if form.has_key("firstname") and form["firstname"] != "":
		print "<h1>Hello", form["firstname"].value, "</h1>"
	else:
		print "<h1>Error! Please enter a first name</h1>"
		
main()