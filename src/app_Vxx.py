###################
# This function get the distribution of VXX front and back month futures


import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.ipathetn.com/US/16/en/details.app?instrumentId=259118")
content = request.content
soup = BeautifulSoup(content, "html.parser")
#element = soup.find("span", {"class":"woocommerce-Price-amount amount"})
element = soup.find("extgrid", {"id": "dollarweights_table", "ignorehash":"true"})
date_element = soup.find("h2",{"style":"margin-bottom:10px;"})

string_element = str(element)
string_date_element = str(date_element)

date_label=string_date_element[58:68]
front_month_label = string_element[28:50]
front_month_value = float(string_element[53:58])/100
back_month_label = string_element[64:86]
back_month_value = float(string_element[89:94])/100
control_string = string_element[20:110]

print(date_label)
print(front_month_label)
print(front_month_value)
print(back_month_label)
print(back_month_value)
print(control_string)
