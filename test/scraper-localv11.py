import urllib2
import re
from BeautifulSoup import BeautifulSoup

def printCheck(word):
	try:
		if word.parent.name != 'script' and len(word) > 0 and word != '\n':
			print word
			var = raw_input("Press enter")
	except:
		soupStructureError = True

urlStr = 'http://online.wsj.com/article/SB10001424052702304911104576445650566902060.html?mod=WeekendHeader_Rotator'

page = urllib2.urlopen(urlStr)

soup = BeautifulSoup(''.join(page))


body = soup.html.body
regEx = re.compile(r'[\w]+')
senList = body.findAll(text=regEx)

print len(senList)

#purge the soup of waste
pos = 0
for sen in senList:
	if sen.parent.name == 'script' or len(sen) == 0 or sen == '\n':
		del senList[pos]
	pos = pos + 1

print len(senList)

#Now go through the senList and print only sens that are greater 
# than 3 words or are lesser but have 3rd sen from it which is 
#greater
for pos in range(0, len(senList)-2):
	sen1 = senList[pos]
	sen2 = senList[pos+1]
	sen3 = senList[pos+2]
	
	words1 = sen1.split(' ')
	words2 = sen2.split(' ')
	words3 = sen3.split(' ')
	
	if len(words1) > 3:
		print sen1
		raw_input("Press enter")
	else:
		lenwords2 = len(words2)
		lenwords3 = len(words3)
		if lenwords2 > 3 or lenwords3 > 3:
			print sen1
			raw_input("Press enter")

print senList[-2]
print senList[-1]
		
