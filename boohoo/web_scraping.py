import re
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
    url = f"https://www.boohooman.com/us/search?q=oversized%20tshirt&prefn1=classification&prefv1=boohooMAN%20Tall%7CMain%20Collection&prefn2=sizeRefinement&prefv2={size}&start={start}&sz={per_page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="search-result-content js-search-result-content")

    # all instances where there is a string within a tag that states "oversized"
    items = div.find_all(string = re.compile("Oversized"))
    
    for item in items:
        # title of product is WITHIN an <a> tag so that is the parent
        parents = item.parent.parent.parent
        link_class = parents.find(class_="product-image js-product-image load-bg").a
        link = "https://www.boohooman.com" + link_class['data-href']
        
        next_parent = item.find_parent(class_="grid-tile")

        try:
            sale_price = next_parent.find(class_="product-sales-price product-sales-price-percent")
            price = int(sale_price.contents[0].strip().replace("$", "")[:-3])
            items_found[item] = {"price": price, "link": link}
        except:
            pass
        
print(items_found)

    
