import requests
import datetime
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
content = soup.find_all("p")
##print(type(content))
##print(len(content))

forecasts = content[4:8]

str_forecasts = []

for i in forecasts:
    str_forecasts.append(str(i)[3:-4])

today = datetime.date.today()

for i in str_forecasts:

    if today.isoweekday() == 1:
        day = "Monday"
    elif today.isoweekday() == 2:
        day = "Tuesday"
    elif today.isoweekday() == 3:
        day = "Wednesday"
    elif today.isoweekday() == 4:
        day = "Thursday"
    elif today.isoweekday() == 5:
        day = "Friday"
    elif today.isoweekday() == 6:
        day = "Saturday"
    elif today.isoweekday() == 7:
        day = "Sunday"
    else:
        print("You done broke it")
    
    print('\n', day, "\t:", i)
    today += datetime.timedelta(days=1)

    

#apparently I can't make a result set from a result set :(
##sub_content = content.find_all("p")
##print(type(sub_content))

##print(sub_content)
##
##print(len(sub_content))



#print(links)
