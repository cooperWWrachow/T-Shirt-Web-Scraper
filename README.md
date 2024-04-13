Using Python's BeautifulSoup library, I have developed a web scraper to retrieve desired data from one of my routinely used online shops, boohooMAN.com. 
I tend to buy a lot of oversized t-shirts specifically from the site, but there are some bugs in the websites functionality. 
For example, I tend to only buy the shirts on sale, but when I set a filter for the maximum price range, it takes into account the 
PREVIOUS price prior to the sale price. Therefore, if a product was $20, and its on sale for $10, the product is not shown if I set a maximum price to $15. 

Solution:
I developed a webscraper for this request, that handles the shirt size, maximum price, AND a color option (optional). Once the HTML is parsed, it organizes
everything in a dictionary. I then place all the contents of that dictionary into an Excel spreadsheet. When i run the program, the previous contents of 
the spreadsheet are erased, and the new contents are filled in in an organized manor. Once saved, the script opens up that specific file and shows me 
the items such as - Name, Price, and the clickable hyperlink URL. I also provided a count just to show how many products are available.

Below are a few screenshots of the process:

After running the command "py web_scraping.py", the user is asked for specifics. In this example I chose "xl 15 blue":

![image](https://github.com/cooperWWrachow/T-Shirt-Web-Scraper/assets/135729317/89beefe1-9d14-4f05-9895-d7cd5796739a)

Only a few seconds later, the Excel spreadsheet is populated appearing on my screen:

![image](https://github.com/cooperWWrachow/T-Shirt-Web-Scraper/assets/135729317/8b8238ba-d309-4d7e-80f9-3a2680f2522c)


