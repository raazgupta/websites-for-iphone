#import the necessary libraries
import urllib2
import re
from BeautifulSoup import BeautifulSoup

def printCheck(sen):
	print sen
	var = raw_input("Press enter")
	
#Pass it a list of para contents
def printContents(contents):
	for content in contents:
		if type(content).__name__ == 'NavigableString':
			printCheck(content)
		try:
			newContents = content.contents
			printContents(newContents)
		except:
			noContents = True


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

	#find all paragraphs in the soup
	paraList = body.findAll('p')
		
	for para in paraList:
		paraContents = para.contents
		printContents(paraContents)
except:
	noBodyError = True