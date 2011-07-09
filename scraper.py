import urllib2
import re
from BeautifulSoup import BeautifulSoup

urlStr = 'http://www.kalzumeus.com/2011/07/08/business-psychology/'

page = urllib2.urlopen(urlStr)

soup = BeautifulSoup(''.join(page))

letterRegEx = re.compile(r'\w+')

#find the body of the html 
body = soup.html.body

senList = soup.findAll(text=letterRegEx)

for sen in senList:
	try:
		if sen.parent.name != 'script':
			print sen
			if sen.parent.name == 'a':
				print sen.parent['href']
	except:
		print "error encoding"
