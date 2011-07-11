#import the necessary libraries
import urllib2
import re
from BeautifulSoup import BeautifulSoup

#Enter the website you want to parse. Not doing any error checking
#at this point
urlStr  = raw_input("Enter the website url:")
#print spaces after the input
print
print

#Opening site content and converting to BeautifulSoup format
page = urllib2.urlopen(urlStr)
soup = BeautifulSoup(''.join(page))

#first just trying to find the title in the header tag and 
#printing nothing if no title found
try:
	titleTag = soup.html.title
	print titleTag.string
except:
	noTitleError = True
	
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
				print sen
				print
				# if sen.parent.name == 'a':
					# print sen.parent['href']
		except:
			encodingError = True
except:
	noBodyError = True