# : Books Data Scraper
# Website: http://books.toscrape.com
# Kaam:
# Title, price, availability scrape karna.
# Multiple pages scrape karke CSV me save karna.
# Concepts: pagination handling, CSV export.

import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "http://books.toscrape.com"
titles = []
prices = []
availabilities = []

while True:

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    # print(r)
    # print(soup.prettify())
    data = soup.find_all("article", class_="product_pod")

    for i in data:

        title = i.h3.a["title"]
        price = i.find("p", class_="price_color").get_text().strip()
        availability = i.find("p", class_="instock availability").get_text().strip()

        titles.append(title)
        prices.append(price)
        availabilities.append(availability)
        # print(f"{title} , {price} , {availability}")

    new_p = soup.find("li", class_="next")
    if new_p:
        np = new_p.a["href"]
        url = urljoin(url, np)
    else:
        break

# print(len(titles))
df = pd.DataFrame({

    "TITLE" : titles ,
    "PRICE" : prices ,
    "AVAILBLITY_STATUS" : availabilities

})

# print(df)
# df.to_csv("Books_Prices.csv")




