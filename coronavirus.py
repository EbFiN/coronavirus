import requests
from bs4 import BeautifulSoup
import re

my_list1 = []
my_list2 = []
l = 0
city = input('Enter a city to see a information : ')
Get = requests.get('https://www.worldometers.info/coronavirus/country/' + city + "/")
one = BeautifulSoup(Get.text, 'html.parser')
information1 = one.find_all('h1')
information2 = one.find_all('div', attrs={'class': 'maincounter-number'})
for i in information1:
    m = re.sub('\s+', '', i.text).strip()
    my_list1.append(m)
for ii in information2:
    l = re.sub('\s+', '', ii.text).strip()
    my_list2.append(l)
my_list3 = my_list1[1:]
g = len(my_list2)
for i in range(0, g):
    print(my_list3[i], ":", my_list2[i])

input('enter for exit')