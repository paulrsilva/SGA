from bs4 import BeautifulSoup
with open('arquivo04.html','r') as f:
    soup = BeautifulSoup(f,"lxml")
    #print(soup.prettify())

    # tag = soup.find('li')
    # print(tag)


    # tag = soup.find(string='deer')
    # print(tag)
    #
    # tag = soup.find(id='primaryconsumers')
    # print(tag)
    #
    # tag = soup.find(attrs={'class':'primaryconsumerlist'})
    # print(tag)
    #
    # tag = soup.find('li', attrs={'class':'producerlist'})
    # print(tag)

    def is_secondary_consumers(tag):
        return tag.has_attr('id') and tag.get('id')=='secondaryconsumers'

    secondary_consumer = soup.find((is_secondary_consumers))

    print(secondary_consumer)