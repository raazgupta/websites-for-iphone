#import the necessary libraries
import urllib2
import re
from BeautifulSoup import BeautifulSoup

f = open('webContent.txt', 'w')

def printCheck(sen):
	if sen.parent.name != "script" and sen.string != None and len(sen.string) != 0 and sen.string != '\n':
		f.write(sen.string + '\n')
		#var = raw_input("Press enter")
		
def recursiveFind(soup):
	try:
		#print soup.name
		soupName = 1
	except:
		noName = 1
	if type(soup).__name__ == 'NavigableString':
		printCheck(soup)
	try:
		for content in soup.contents:
			recursiveFind(content)
	except:
		noContent = 1


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
#Loop through everything and find and print the Navigable Strings

recursiveFind(soup)

f.close()
