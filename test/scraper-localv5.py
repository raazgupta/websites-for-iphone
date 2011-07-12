#import the necessary libraries
import urllib2
import re
from BeautifulSoup import BeautifulSoup

def printCheck(sen):
	if sen.parent.name != "script" and sen.string != None and len(sen.string) != 0 and sen.string != '\n':
		print sen.string
		var = raw_input("Press enter")


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
	print
except:
	noTitleError = True
	
#Now the tough part


#find the body of the html 
try:
	body = soup.html.body

	currentSen = body
				
	#Do this until the last element of senList is found
	while currentSen != None:
		#Check whethet the next element is a string and if so
		#print it. Otherwise skip it
		if type(currentSen).__name__ == 'NavigableString':
			printCheck(currentSen)
		currentSen = currentSen.next
except:
	noBodyError = True