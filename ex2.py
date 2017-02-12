from bs4 import BeautifulSoup
import urllib.request

source = urllib.request.urlopen("http://www.bom.gov.au/sa/forecasts/state.shtml").encode("ascii", "ignore")

print(type(source))

soup = BeautifulSoup(source, "lxml")

print(soup.prettify())

# today = soup.ul
# #today = soup.find(class="synopsis")
#
# print(today)
