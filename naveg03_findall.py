# File: naveg03.py
# Author: Paulr

from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup( f, 'lxml')

''''
tag_list = soup.find_all('ul')
print(tag_list)


tag_list = soup.find_all(['ul','class']'limit=2)
print(tag_list)



print(soup.find_all(string=True))

print(soup.find_all(string='rabbit'))
print(soup.find_all(string=['rabbit','çorvo'])

'''

print(soup.find_all('div', class_='name'))