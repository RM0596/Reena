import requests
from bs4 import BeautifulSoup
web = requests.get("https://www.merchantgenius.io")
soup = BeautifulSoup(web.content,"html.parser")
#print(soup.prettify())
print(soup.find_all('img'))