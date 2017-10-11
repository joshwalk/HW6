import requests
from bs4 import BeautifulSoup

base_url = 'http://py4e-data.dr-chuck.net/comments_42.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

span_list = []
spans = soup.find_all('span')
for span in spans:
    span_list.append(int(span.text))

print(sum(span_list))
