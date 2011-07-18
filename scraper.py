#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi
from BeautifulSoup import BeautifulSoup
import urllib2
import re

# enable debugging
import cgitb
cgitb.enable(1)

#function to check whether the sentence being printed is empty
#print the sentence inside the right tags
def printCheck(sen, tag, urlStr):
	#Gracefully fail
	try:
		#Do not print out any text found in <script> and <style> tags or is empty
		if sen.parent.name != "script" and sen.parent.name != 'style' and sen.string != None and len(sen.string) != 0 and sen.string != '\n':
			#Print out a hyperlink instead of plain text if the parent is <a> tag
			if sen.parent.name != 'a':
				print "<"+tag+">"+sen.string+"</"+tag+">"
			else:	
				hrefId = sen.parent['href']
				#Make sure the hyperlink contains the website and previous elements. Website tells scraper the website to scrape
				#Previous tells scraper where the back button should point to
				#Do do some funny recursive logic that this entails, only 1 level of Back and Forth is allowed
				#After that the previous element is empty
				print "<a href='http://www.soulofmachine.com/cgi/scraper.py?website="+hrefId+"&previous=http://www.soulofmachine.com/cgi/scraper.py?website="+urlStr+"'>"+sen.string+"</a>"
	except:
		printError = True

# print out the type of content on the site
print "Content-Type: text/html\n"


# website scraper function. Takes in a variable of type BeautifulSoup
def scraper(soup, urlStr, previousPage):

	#Print the header for the page
	print "<html>"
	print "<head>"
	
	#print the styling information
	print '<link rel="stylesheet" type="text/css" href="http://www.soulofmachine.com/css/iphone.css" />'
	print '<meta name="viewport" content="user-scalable=yes, width=device-width" />'

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
	
	#Print the Back button
	print "<a href='"+previousPage+"'>Back</a>"
	
	#Print out the title in h1 font
	print "<h1>", titleStr, "</h1>"
		
	#Now the tough part
	#Create a regular expressions that searchs for a string of 7 words
	wordsRegEx = re.compile(r'[\w,:()]+\s[\w,:()]+\s[\w,:()]+\s[\w,:()]+\s[\w,:()]+\s[\w,:()]+\s[\w,:()]+')

	#find the body of the html 
	try:
		body = soup.html.body

		#find all sentences in body that have 7 or more words
		senList = body.findAll(text=wordsRegEx)

		#find the length of senList
		wordLen = len(senList)
		
		#print out each sentence, gracefully in paras
		for wordPos in range(0, wordLen):
			try:
				sen = senList[wordPos]
				#Check that the sentence isn't a part of javascript
				if sen.parent.name != 'script':
					printCheck(sen, 'p', urlStr)
					
					#Check if this is the last element of senList, then do nothing
					if wordPos != (wordLen - 1):
						#Go through the soup to find small than 7 words and print
						#this happens until you find the next set of 7 words or more
						currentSen = sen.next
						next7Sen = senList[wordPos+1]
						while currentSen != next7Sen:
							#Check whethet the next element is a string and if so
							#print it. Otherwise skip it
							if type(currentSen).__name__ == 'NavigableString':
								printCheck(currentSen, 'p', urlStr)
							currentSen = currentSen.next
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
	
	#Print a link to the previous page
	previousPage = ""
	if form.has_key("previous") and form["previous"] != "":
		previousPage = form["previous"].value
		
	
	# The previous page has a text box called 'website'
	if form.has_key("website") and form["website"] != "":
		# Store the url in urlStr
		urlStr = form["website"].value
		
		# For the lazy or dumb among us, if the url is Copy & Paste Link then change to 
		# http://news.ycombinator.com/
		if urlStr == "Copy & Paste Link":
			urlStr = "http://news.ycombinator.com/"
		
		# Gracefully kill a wrong url
		try: 
			page = urllib2.urlopen(urlStr)
			soup = BeautifulSoup(''.join(page))
			
			#call the scraper function to find and print the relevant text
			scraper(soup, urlStr, previousPage)
			
		except:
			wrongUrlError = 1
	else:
		print "<h1>Error! Please enter a website</h1>"
		
main()