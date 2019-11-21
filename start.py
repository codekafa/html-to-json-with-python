from bs4 import BeautifulSoup
import requests
from htmlp import HTMLtoJSONParser

payload = {'api_key': "a16664752a16525df548cf51c5cf8093", 'url':"https://www.arabam.com/ikinci-el/otomobil"}
r = requests.get('http://api.scraperapi.com', params=payload)

soup = BeautifulSoup(r.text, 'html.parser')

table  = soup.find_all('table')[0]

j = HTMLtoJSONParser.to_json(str(table),False)

print(j)
