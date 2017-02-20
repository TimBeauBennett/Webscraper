import requests
from bs4 import BeautifulSoup
import pandas as pd

file = open('Khama_weather.txt', 'w')

##------------------------------------------------------------

r = requests.get("http://www.bom.gov.au/sa/forecasts/state.shtml")
r = r.content
soup = BeautifulSoup(r, "html.parser")

content = soup.find_all("p")
forecast = content[4]

headings = soup.find_all("h2")
day = headings[1]

file.write(str(day)[4:-5])
file.write(':\n')
file.write(str(forecast)[3:-4])
file.write("\n\n")

##------------------------------------------------------------

# -- Next we need to pull out the town temperatures we want

##------------------------------------------------------------

dfs = pd.read_html("http://www.bom.gov.au/sa/forecasts/towns.shtml")

Locations = [dfs[8].loc[0], dfs[8].loc[2], dfs[9].loc[1], dfs[10].loc[0],
             dfs[11].loc[0], dfs[12].loc[0], dfs[12].loc[1], dfs[13].loc[0],
             dfs[13].loc[1], dfs[14].loc[0], dfs[2].loc[0], dfs[2].loc[2],
             dfs[1].loc[0], dfs[3].loc[0]]

for i in Locations:
    if i['Location'] == 'Clare':
        x = '\t\t'
    elif i['Location'] == 'Wudinna':
        x = '\t\t'
    elif i['Location'] == 'Kadina':
        x = '\t\t'
    elif i['Location'] == 'Ceduna':
        x = '\t\t'
    elif i['Location'] == 'Whyalla':
        x = '\t\t'
    else:
        x = '\t'

    if str(i['Min.']) == 'nan':
        Min1 = ''
        Min2 = ''
    else:
        Min1 = 'Min:'
        Min2 = i['Min.']
        
    string = i['Location'] + x + Min1 + Min2 + '\tMax:' + i['Max.'] + '\t' + i['Summary'] + '\n'
    file.write(string)

##file.close()
##file = open('Khama_weather.txt', 'r')
##print(file.read())
##file.close()

#----------------------------------------

# -- Now a multi-page parse for our maritime forecasts

#----------------------------------------

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

file.close()
file = open('Khama_weather.txt', 'r')
email_content = file.read()
file.close()

fromaddress = 'miketheweatherrobot@gmail.com'
toaddress = 'reid.khama@abc.net.au'

msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = "Today's Weather" # should put a date stamp here
msg.attach(MIMEText(email_content))

server = smtplib.SMTP('smtp.googlemail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('miketheweatherrobot@gmail.com', 'Adventuret1m3!')
server.sendmail(fromaddress, toaddress, msg.as_string())
server.quit()
