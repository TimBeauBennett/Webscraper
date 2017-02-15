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

    

#apparently I can't make a result set from a result set :(
##sub_content = content.find_all("p")
##print(type(sub_content))

##print(sub_content)
##
##print(len(sub_content))



#print(links)
