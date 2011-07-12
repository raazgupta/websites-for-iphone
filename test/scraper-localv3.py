#import the necessary libraries
import urllib2
import re
from BeautifulSoup import BeautifulSoup

def printCheck(sen):
	if sen.parent.name != "script" and sen.string != None and len(sen.string) != 0 and sen.string != '\n':
		print sen.string
		#var = raw_input("Press enter")


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
#Create a regular expressions that searchs for a string of 7 words
wordsRegEx = re.compile(r'[\w]+\s[\w]+\s[\w]+\s[\w]+\s[\w]+')

#find the body of the html 
try:
	body = soup.html.body

	#find all sentences in body that have 5 or more words
	senList = body.findAll(text=wordsRegEx)

	#find the length of senList
	wordLen = len(senList)


	#Start from the first sentence that has atleast 5 words
	#Go through the soup until you find the last sentence that has atleast
	#5 words. Above all, have a good time! 
	currentSen = senList[0]
				
	#Do this until the last element of senList is found
	while currentSen != senList[wordLen-1]:
		#Check whethet the next element is a string and if so
		#print it. Otherwise skip it
		if type(currentSen).__name__ == 'NavigableString':
			printCheck(currentSen)
		currentSen = currentSen.next
except:
	noBodyError = True