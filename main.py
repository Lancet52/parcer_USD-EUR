import requests
from bs4 import BeautifulSoup

def dollar():
    req = requests.get("https://ru.investing.com/currencies/usd-rub")

    src = req.text

    soup = BeautifulSoup(src, "html.parser")
    items = (soup.find('div',class_='desktop:relative desktop:bg-white').find('div',class_='relative flex').find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6'))

    final=str(items)
    es=final.split('>')
    final=es[2]
    return final.split('<')[0]

def euro():
    req = requests.get("https://ru.investing.com/currencies/eur-rub")

    src = req.text

    soup = BeautifulSoup(src, "html.parser")
    items = (soup.find('div',class_='desktop:relative desktop:bg-white').find('div',class_='relative flex').find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6'))

    final=str(items)
    es=final.split('>')
    final=es[2]
    return final.split('<')[0]


print(dollar())
print(euro())


