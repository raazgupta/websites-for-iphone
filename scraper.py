import urllib2
import re
from BeautifulSoup import BeautifulSoup

urlStr = 'http://www.hanselman.com/blog/WhyTheAskObamaTweetWasGarbledOnScreenKnowYourUTF8UnicodeASCIIAndANSIDecodingMrPresident.aspx'

page = urllib2.urlopen(urlStr)

soup = BeautifulSoup(''.join(page))

sentenceRegEx = re.compile(r'\w+\s\w+\s\w+\s\w+\s\w+')

senList = soup.findAll(text=sentenceRegEx)

for sen in senList:
	print sen
