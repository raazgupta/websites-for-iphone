#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
from BeautifulSoup import BeautifulSoup
import urllib2
import re

# enable debugging
import cgitb
cgitb.enable(1)

# print out the type of content on the site
print "Content-Type: text/html\n"


# website scraper function. Takes in a variable of type BeautifulSoup
def scraper(soup):

	#Print the header for the page
	print "<html>"
	print "<head>"
	
	#print the styling information
	print '<link rel="stylesheet" type="text/css" href="http://www.soulofmachine.com/css/iphone.css" media="only screen and (max-width: 480px)" />'
	print '<meta name="viewport" content="user-scalable=no, width=device-width" />'

	#first just trying to find the title in the header tag and 
	#printing nothing if no title found
	titleStr = ""
	try:
		titleTag = soup.html.title
		titleStr = titleTag.string
		#print the title tag in the header
		print "<title>", titleStr, "</title>"
	except:
		noTitleError = True
		
	#Close the header tag
	print "</head>"
	
	#Open the body tag
	print "<body>"
	
	#Print out the title in h1 font
	print "<h1>", titleStr, "</h1>"
		
	#Now the tough part
	#Create a regular expressions that searchs for a string of 7 words
	wordsRegEx = re.compile(r'\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+')

	#find the body of the html 
	try:
		body = soup.html.body

		#find all sentences in body that have 7 or more words
		senList = body.findAll(text=wordsRegEx)

		#print out each sentence, gracefully in paras
		for sen in senList:
			try:
				#Check that the sentence isn't a part of javascript
				if sen.parent.name != 'script':
					print "<p>", sen, "</p>"
					# if sen.parent.name == 'a':
						# print sen.parent['href']
			except:
				encodingError = True
	except:
		noBodyError = True
		
	#Close the body
	print "</body>"
	#Close the html
	print "</html>"

# main function
def main():
	
	# Get the form fields from the previous page
	form = cgi.FieldStorage()
	
	# The previous page has a text box called 'website'
	if form.has_key("website") and form["website"] != "":
		# Store the url in urlStr
		urlStr = form["website"].value
		# Gracefully kill a wrong url
		try: 
			page = urllib2.urlopen(urlStr)
			soup = BeautifulSoup(''.join(page))
			
			#call the scraper function to find and print the relevant text
			scraper(soup)
			
		except:
			wrongUrlError = 1
	else:
		print "<h1>Error! Please enter a website</h1>"
		
main()