import re
from bs4 import BeautifulSoup
import requests

user_input  = input("input size, color, max price with a space in between each: ")
filters = user_input.split()

size = filters[0].upper()
color = filters[1]
max_price = int(filters[2])


url = f"https://www.boohooman.com/us/search?q=oversized%20tshirt&prefn1=classification&prefv1=boohooMAN%20Tall%7CMain%20Collection&prefn2=sizeRefinement&prefv2={size}&sz=80"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

total_pages = int(doc.find(class_="pagination-info js-pagination-info hidden-on-mobile hidden-on-tablet-portrait").string.strip()[10:])
per_page = 80

items_found = {}
count = 0

# iterate through each page based on total total items per page and page count
for page in range(total_pages):
    start = page * per_page
    # if user requests a color, adjust url accordingly
    if color != "None":
        url = f"https://www.boohooman.com/us/search?q=oversized%20tshirt&prefn1=classification&prefv1=boohooMAN%20Tall%7CMain%20Collection&prefn2=color&prefv2={color}&prefn3=sizeRefinement&prefv3={size}&start={start}&sz={per_page}"
    else:
        url = f"https://www.boohooman.com/us/search?q=oversized%20tshirt&prefn1=classification&prefv1=boohooMAN%20Tall%7CMain%20Collection&prefn2=sizeRefinement&prefv2={size}&start={start}&sz={per_page}"
    
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="search-result-content js-search-result-content")

    # all instances where there is a string within a tag that states "oversized"
    items = div.find_all(string = re.compile("Oversized"))
    for item in items:
        # correct URL is several parents up the tree
        parents = item.parent.parent.parent
        link_class = parents.find(class_="product-image js-product-image load-bg").a
        link = "https://www.boohooman.com" + link_class['data-href']
        
        next_parent = item.find_parent(class_="grid-tile")

        # handles products NOT on sale (dont have a sales price)
        try:
            sale_price = next_parent.find(class_="product-sales-price product-sales-price-percent")
            price = int(sale_price.contents[0].strip().replace("$", "")[:-3])
            if price <= max_price:
                items_found[item.replace("\n", "")] = {"price": price, "link": link}
                count += 1
            else:
                continue
        except:
            pass
        
print(items_found)
print(f"There are {count} items on sale!")

    
