from bs4 import BeautifulSoup
from bs4 import Tag

with open('arquivo03.html', 'r') as f:
    soup=BeautifulSoup(f,"lxml")
    # print(soup.prettify())
    # print(len(list(soup.descendants)))
    # print(soup.div.next_element.next_element.next_element.next_element)
    # print( '--')
    # print(soup.li.previous_element.previous_element)

'''
for e in soup.ul.next_elements:
    if isinstance(e, Tag):
        print(e)
'''

for e in soup.li.previous_elements:
    print(repr(e))