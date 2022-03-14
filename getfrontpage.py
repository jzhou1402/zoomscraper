import requests
import time
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import re

out = open("webinfo.csv", "w")

url = "https://www.shopify.com/"
headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"

# print(requests.get(url = 'https://trustradius.com/products/zoominfo/reviews').text)
# print(resp.content)

resp = (requests.get(url='https://www.shopify.com/').text)
time.sleep(0.3)

soup = BeautifulSoup(resp, 'html.parser')
text = soup.find_all(text=True)
for i in text:
    line = ''.join(filter(str.isalnum, i))
    if line != "":
        print(line)