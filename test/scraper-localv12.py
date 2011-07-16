#import the necessary libraries
import urllib2
import re
from BeautifulSoup import BeautifulSoup

def printCheck(sen):
	if sen.parent.name != "script" and sen.string != None and len(sen.string) != 0 and sen.string != '\n':
		if sen.parent.name != 'a':
			print sen.string
		else:
			hrefId = sen.parent['href']
			print "<a href='"+hrefId+"'>"+sen.string+"</a>"
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
	printCheck(titleTag.string)	
except:
	noTitleError = True
	
#Now the tough part
#Create a regular expressions that searchs for a string of 7 words
wordsRegEx = re.compile(r'[\w]+\s[\w]+\s[\w]+\s[\w]+\s[\w]+')

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
				printCheck(sen)
				
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
							if currentSen.parent.name != 'script' and currentSen.string != "":
								printCheck(currentSen.string)
						currentSen = currentSen.next
		except:
			print "encoding error"
except:
	noBodyError = True