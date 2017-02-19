import requests
from bs4 import BeautifulSoup
import pandas as pd

file = open('SA_weather1.txt', 'w')

##------------------------------------------------------------

r = requests.get("http://www.bom.gov.au/sa/forecasts/state.shtml")
r = r.content
soup = BeautifulSoup(r, "html.parser")

content = soup.find_all("p")
forecasts = content[4:8]
str_forecasts = []

for i in forecasts:
    str_forecasts.append(str(i)[3:-4])

headings = soup.find_all("h2")
days = headings[1:5]
str_days = []

for i in days:
    str_days.append(str(i)[4:-5])

count = 0

for i in str_forecasts:
    file.write(str_days[count])
    file.write(':\n')
    # The BOM site has a weird format on some days - this line cleans it up.
    s = " ".join(i.split())
    file.write(s)
    file.write('\n\n')
    count += 1

##------------------------------------------------------------

# -- Next we need to pull out the town temperatures we want

##------------------------------------------------------------

dfs = pd.read_html("http://www.bom.gov.au/sa/forecasts/towns.shtml")

Locations = [dfs[0].loc[0], dfs[2].loc[0], dfs[3].loc[0], dfs[8].loc[0], dfs[8].loc[2],
             dfs[9].loc[1], dfs[10].loc[0], dfs[10].loc[2], dfs[11].loc[0], dfs[12].loc[0],
             dfs[12].loc[2], dfs[13].loc[0], dfs[13].loc[1], dfs[14].loc[3]]

for i in Locations:
    if i['Location'] == 'Clare':
        x = '\t\t'
    elif i['Location'] == 'Kimba':
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


#----------------------------------------

# -- Now a multi-page parse for our maritime forecasts

#----------------------------------------

site_list = ['http://www.bom.gov.au/sa/forecasts/far-west-coast.shtml',
             'http://www.bom.gov.au/sa/forecasts/upper-west-coast.shtml',
             'http://www.bom.gov.au/sa/forecasts/lower-west-coast.shtml',
             'http://www.bom.gov.au/sa/forecasts/central-coast.shtml',
             'http://www.bom.gov.au/sa/forecasts/spencer-gulf.shtml',
             'http://www.bom.gov.au/sa/forecasts/investigator-strait.shtml',
             'http://www.bom.gov.au/sa/forecasts/gulf-st-vincent.shtml',
             'http://www.bom.gov.au/sa/forecasts/south-central-coast.shtml',
             ]

def generate_forecast():
    
    for x in site_list:
        m = requests.get(x)
        m = m.content
        soup2 = BeautifulSoup(m, 'html.parser')

        region_raw = soup2.find_all("h1")
        region_raw = str(region_raw[0])[4:-5]
        region = region_raw.split(":")[0]

        marine_days = soup2.find_all("h2")
        marine_today = marine_days[1]
        marine_today_str = str(marine_today)[4:-5]

        marine_data = soup2.find_all("span")
        data_list = list(marine_data)[0:3]
        new_marine_list = []
        for d in data_list:
            new_marine_list.append(str(d)[6:-7])

        to_write = "\n" + region + ":\n" + marine_today_str + ':' + '\nWind:\t' + new_marine_list[0] + '\nSeas:\t' + new_marine_list[1] + '\nSwell:\t' + new_marine_list[2] + "\n"
        file.write(to_write)

generate_forecast()

# --------------------------------------------------------------------

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

file.close()
file = open('SA_weather1.txt', 'r')
email_content = file.read()
file.close()

fromaddress = 'miketheweatherrobot@gmail.com'
toaddress = 'bennett.tim@gmail.com'

msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = "The Best Weather Report!"
msg.attach(MIMEText(email_content))

server = smtplib.SMTP('smtp.googlemail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('miketheweatherrobot@gmail.com', 'Adventuret1m3!')
server.sendmail(fromaddress, toaddress, msg.as_string())
server.quit()





# --BELOW THIS IS OLD CODE-----------------------------------------------------

##m = requests.get("http://www.bom.gov.au/sa/forecasts/far-west-coast.shtml")
##m = m.content
##soup2 = BeautifulSoup(m, 'html.parser')
##
##region_raw = soup2.find_all("h1")
##region_raw = str(region_raw[0])[4:-5]
##region = region_raw.split(":")[0]
##
##marine_days = soup2.find_all("h2")
##marine_today = marine_days[1]
##marine_today_str = str(marine_today)[4:-5]
##
##marine_data = soup2.find_all("span")
##data_list = list(marine_data)[0:3]
##new_marine_list = []
##for d in data_list:
##    new_marine_list.append(str(d)[6:-7])
##
##print("\n")
##print(region, ":")
##print(marine_today_str, ':')
##print('Wind:\t', new_marine_list[0])
##print('Seas:\t', new_marine_list[1])
##print('Swell:\t', new_marine_list[2])













