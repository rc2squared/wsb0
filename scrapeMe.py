import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('results.csv', 'w'))
f.writerow(['buyer', 'price'])

pages = []

for i in range(1, 5):
    url = 'http://econpy.pythonanywhere.com/ex/00' + str(i) + '.html'
    pages.append(url)

for buyer_info in pages:
    page = requests.get(buyer_info)
    soup = BeautifulSoup(page.text, 'html.parser')

    names = []
    prices = []

    buyerColumns = soup.find_all(title='buyer-name')
    for name in buyerColumns:
        names = names.append(name.text)

    buyerPrices = soup.find_all(class_='item-price')
    for price in buyerPrices:
        prices = prices.append(price.text)

    f.writerow([names, prices])
