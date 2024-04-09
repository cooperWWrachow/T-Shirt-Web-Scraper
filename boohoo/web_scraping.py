from bs4 import BeautifulSoup
import requests

size  = input("input size and max price: ").upper()
url = f"https://www.boohooman.com/us/search?q=oversized%20tshirt&prefn1=classification&prefv1=boohooMAN%20Tall%7CMain%20Collection&prefn2=sizeRefinement&prefv2={size}&sz=80"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

item_count = int(doc.find(class_="search-results-count-txt").string)
per_page = 80

items_found = {}

for start in range(0, item_count, per_page):
    url = f"https://www.boohooman.com/us/search?q=oversized%20tshirt&prefn1=classification&prefv1=boohooMAN%20Tall%7CMain%20Collection&prefn2=sizeRefinement&prefv2=XL&start={start}&sz={per_page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find_all(class_="product-tile-name")

    

url = f"https://www.boohooman.com/us/search?q=oversized%20tshirt&prefn1=classification&prefv1=boohooMAN%20Tall%7CMain%20Collection&prefn2=sizeRefinement&prefv2=XL&start=0&sz=80"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

div = doc.find_all(class_="product-tile-name")
print(div)
