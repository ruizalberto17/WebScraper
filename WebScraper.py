import numpy
import matplotlib
import requests
from datetime import datetime, date
import calendar
from bs4 import BeautifulSoup

class Search:
    def __init__(self):
        Search.symbol = input("What symbol would you like to look up: ")
        Search.start_date = input("What date would you like to start at (MM-DD-YYYY): ")
        Search.end_date = input("What date would you like to end at (MM-DD-YYYY): ")
        Search.frequency = input("What frequency would you like the data (1d, 1wk, 1mo): ")


requested_search = Search()
epoch_start = datetime.strptime(requested_search.start_date, "%m-%d-%Y").timestamp()
epoch_end = datetime.strptime(requested_search.end_date, "%m-%d-%Y").timestamp()
print(str(epoch_start))
print(str(epoch_end))

webpage_response = requests.get("https://finance.yahoo.com/quote/" + requested_search.symbol + "/history?period1=" + "1608076800" + "&period2=" + "1608163200" + 
                           "&interval=1d&filter=history&frequency=" + requested_search.frequency + "&includeAdjustedClose=true")

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
#print(soup)
trade_data = soup.find_all(attrs={"data-test":"historical-prices"})
print(trade_data)