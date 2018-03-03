import requests
import csv
import datetime
from bs4 import BeautifulSoup

def pager():
    # Create a list for pages
    pages = []
    #  Create a range of pages at the website and append each to the page list
    for i in range(0, 6):
        url = 'http://econpy.pythonanywhere.com/ex/00' + str(i) + '.html'
        pages.append(url)
    return pages

def scrape(pages):
    # Request a GET from pager
    page = requests.get(pages)
    # Set up soup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Create a list for buyer names and a list for prices
    names = []
    prices = []

    # Append buyer names to the name list
    buyerColumns = soup.find_all(title='buyer-name')
    for name in buyerColumns:
        names.append(name.text)

    # Append prices to the price list
    buyerPrices = soup.find_all(class_='item-price')
    for price in buyerPrices:
        prices.append(price.text)

    # Create a list of results
    results = []

    # Pair the names list with the price list and put them in the results list
    for result in zip(names, prices):
        results.append(result)

    return results

# Use existing Python datetime function for today's date
date = datetime.date.today()
# Create a csv file with a name that reflects today's date
w = csv.writer(open('results' + str(date) + '.csv', 'w', newline=''))
pages = pager()
for page in pages:
    results = scrape(page)
    for i, result in enumerate(results):
        w. writerow(result)
print(pages)

