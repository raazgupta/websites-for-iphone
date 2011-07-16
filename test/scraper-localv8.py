import urllib2
import re
from BeautifulSoup import BeautifulSoup
import string

urlStr = raw_input('Enter webpage:')
page = urllib2.urlopen(urlStr)
soup = BeautifulSoup(''.join(page))

#find the title from the title tag
#this could fail then just do the normal processing
titleTags = soup.findAll('title')
titleStr = ""
if len(titleTags) > 0:
	titleStr = titleTags[0].string

#if titleStr is empty then just do normal processing
if len(titleStr) > 0:	
	#Strip any weird characters
	exclude = set(string.punctuation)
	
	titleStr = ''.join(ch for ch in titleStr if ch not in exclude)

	#find all the words
	titleWords = titleStr.split(' ')
	while '' in titleWords:
		titleWords.remove('')

	lenWords = len(titleWords)

	#Go through body to find the title
	bodyTags = soup.findAll('body')
	
	if len(bodyTags) > 0:
		body = bodyTags[0]
		possibleCandidate = None
		
		for pos in range(0, lenWords-1):
			word1 = titleWords[pos]
			word2 = titleWords[pos+1]
			regEx = re.compile(word1+r'[\w ^\n]+'+word2)
			
			bodyTitles = body.findAll(text=regEx)
			
			
			
			for title in bodyTitles:
				
				if title.parent.name != 'script':
					if type(title).__name__ == 'NavigableString':
						possibleCandidate = title
						break
			
			if possibleCandidate != None:
				break

		print possibleCandidate

	else:
		print "No body tag found"
else:
	print "Title title tag found"

