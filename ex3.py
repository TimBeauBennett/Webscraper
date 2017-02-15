import requests
from bs4 import BeautifulSoup

# -- We use requests to get the html - it's stored as a 'Response' object
r = requests.get("http://www.bom.gov.au/sa/forecasts/state.shtml")
##print(type(r))


# -- Now we convert the Response object to bytes using the content function
r = r.content
##print(type(r))


# -- Now we use BS4 to create a BeautifulSoup object
soup = BeautifulSoup(r, "html.parser")#.encode('ascii', 'ignore')
##print(type(soup))


# -- Now we create a 'ResultSet' object with some part of the page - here the content
##content = soup.find_all(id="content")

# -- Let's prepare the forecasts
content = soup.find_all("p")
forecasts = content[4:8]
str_forecasts = []

for i in forecasts:
    str_forecasts.append(str(i)[3:-4])


# -- Let's do the same for the headings
headings = soup.find_all("h2")
days = headings[1:5]
str_days = []

for i in days:
    str_days.append(str(i)[4:-5])



count = 0

for i in str_forecasts:
    print(str_days[count], ':\n\n', i, '\n')
    count += 1

# -- Next we need to pull out the town temperatures we want
# These are in a table, Pandas does this better, but Im gonna stick with BS4 to learn it better.
# Revision on prior line -- BS4 is NOT the best for this -- pandas 100%
# Also, Sometimes there is a 'min' and 'max' column, and sometimes just a 'max'
# I'll probably have to write up a if clause there, eg:
# if min print min -- else pass
# print max
#
# The format I want is this:
#
# Adelaide  Min: 18 C   Max: 28 C   Partly Cloudy
# Kadina    Min: 16 C   Max: 29 C   Partly Cloudy
# Kingscote Min: 16 C   Max: 22 C   Possible Morning Shower
#
# etc.
##
##t = requests.get("http://www.bom.gov.au/sa/forecasts/towns.shtml")
##t = t.content
##soup2 = BeautifulSoup(t, "html.parser")
##
##table = soup2.find_all('table')
####print((table))
####rows = table.find_all('tr')
##
##for tr in table:
##    td = tr.find_all('td')
##    row = [i.text for i in td]
##    print(row)

import pandas as pd

dfs = pd.read_html("http://www.bom.gov.au/sa/forecasts/towns.shtml")
for df in dfs:
    print(df)





#apparently I can't make a result set from a result set :(
##sub_content = content.find_all("p")
##print(type(sub_content))

##print(sub_content)
##
##print(len(sub_content))



#print(links)
