#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.
"""
__author__= "Paulino R. e Silva"

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString,Tag



''''
with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html.parser')

print(soup_string)
'''

''''
with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html5lib')
print(soup_string)
'''

'''
r = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/')
soup = BeautifulSoup(r.text,'lxml')
print(soup)
'''

# with open('arquivo.html', 'r') as f:
#     soup= BeautifulSoup(f, 'html.parser')

# tag=soup.title
# print(tag)
# print(tag.name)

# print(soup.p['class'])
# print(soup.p.attrs)
# print(soup.a['href'])
# print(soup.a.get('href'))

# print(soup.prettify())
# print(soup.get_text())
# print(soup.p.get_text())

# print(soup.p.b.string)

'''
with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f, 'lxml')
print(soup.title)
print(soup.head.title)
print(soup.a)
print(soup.a.img)
print(soup.td)
print(soup.tr)
print(soup.tr.td)
print(soup.tr.attrs)
print(soup.td['class'])
print(soup.td['class'][0])
'''

with open('arquivo02.html','r') as f:
    soup = BeautifulSoup(f,'lxml')

#print(soup.prettify())

#print(soup.table.contents)

'''

print(len(soup.contents))
print(soup.table.contents[1])
print(soup.table.contents[1].text)
print(soup.table.contents[1].span)
print(soup.table.contents[1].span.string)

for child in soup.table.contents:
    if child.name =='tr':
        print(child)

print(type(soup.children))

# for chld in soup.children:
#     print(chld)

for child in soup.footer.children:
    print(child)

for child in soup.footer.p.children:
    if child.name=='a':
        print(child.get('href'))

#acessando descendentes em arvores

print(len(list(soup.children)))
print(len(list(soup.descendants)))
'''

# for tag in soup.descendants:
#     if isinstance(tag,NavigableString):
#         print(tag)
#     else:
#         print(tag.name)


# for tag in soup.descendants:
#     if isinstance(tag,Tag):
#         print(tag)
#

# for string in soup.aside.strings:
#     print(repr(string))


for string in soup.aside.stripped_strings:
    print(repr(string))
