import requests
import time
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

out = open("demo_out.csv", "w")
notfound = open("notfound.csv", "w")

url = "https://www.trustradius.com/products/zoominfo/reviews"
headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"

# print(requests.get(url = 'https://trustradius.com/products/zoominfo/reviews').text)
# print(resp.content)

file1 = open('demo.txt', 'r')

count = 0

for product in file1:
    
    resp = (requests.get(url='https://www.trustradius.com/products/' + product + '/reviews').text)
    time.sleep(0.3)

    if resp.find("403 Forbidden") == -1:
    # resp = requests.get(url, headers=headers)
    # print(resp.status_code)
        soup = BeautifulSoup(resp, 'html.parser')

        comparisons = soup.find("section", {"id": "comparisons"})
        if comparisons == []:
            notfound.write(product + 'n')
        else:
            categories = comparisons.find_all('h4')
            if categories == []:
                notfound.write(product + 'n')
            else:
                out.write(str(count) + ', ')
                out.write(product.rstrip() + ', ')
                for i in categories:
                    out.write(str(i.text.strip()) + ', ')
                out.write('\n')
                count += 1
                print(count)
    else:
        notfound.write(product + '\n')

