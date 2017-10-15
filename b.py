import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Lyla.html"

# loops through first 6 pages following link of position 18
count = 6
while count >= 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup('a')
    url = a_tags[17].get('href', None) # reassigns url to href of 18th link
    count -= 1

# prints contents of 18th link on 7th page
print(a_tags[17].text)
