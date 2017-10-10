# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#url = input('Enter url here: ')
url = 'http://py4e-data.dr-chuck.net/known_by_Alani.html'
counter = input("Enter count: ")
position = input("Enter position here: ")
lst = []
for i in range(1, int(position)):
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "lxml")
	tags = soup('a')
	count = 0
	for tag in tags:
		count += 1

		if (count == 18):
			url = tag.get('href', None)
			lst.append(url)

print(lst[int(counter)-1])









