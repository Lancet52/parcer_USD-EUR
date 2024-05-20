import requests
from bs4 import BeautifulSoup


# Курс доллара биржевой
def dollar():
    req = requests.get("https://ru.investing.com/currencies/usd-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (
        soup.find('div', class_='desktop:relative desktop:bg-white')
        .find('div', class_='relative flex')
        .find('div', class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
        .find('div','text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'))
    return items.text


# Динамика курса доллара в абсолютных числах
def dollar_din():
    req = requests.get("https://ru.investing.com/currencies/usd-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (
        soup.find('div', class_='desktop:relative desktop:bg-white')
        .find('div', class_='relative flex')
        .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
        .find('div', 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main').find('span'))
    return items.text

# Динамика курса доллара в процентах
def dollar_din_percent():
    req = requests.get("https://ru.investing.com/currencies/usd-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (
        soup.find('div', class_='desktop:relative desktop:bg-white')
        .find('div', class_='relative flex')
        .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
        .find('div', 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main').find_all('span')[1])
    return items.text


# Курс евро биржевой
def euro():
    req = requests.get("https://ru.investing.com/currencies/eur-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (soup.find('div',class_='desktop:relative desktop:bg-white')
             .find('div',class_='relative flex')
             .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
             .find('div','text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'))


    return items.text


# Динамика курса евро в абсолютных числах
def euro_din():
    req = requests.get("https://ru.investing.com/currencies/eur-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (
        soup.find('div', class_='desktop:relative desktop:bg-white')
        .find('div', class_='relative flex')
        .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
        .find('div', 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main').find('span'))
    return items.text

# Динамика курса евро в процентах
def euro_din_percent():
    req = requests.get("https://ru.investing.com/currencies/eur-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (
        soup.find('div', class_='desktop:relative desktop:bg-white')
        .find('div', class_='relative flex')
        .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
        .find('div', 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main').find_all('span')[1])
    return items.text


# Курс юаня биржевой
def cny():
    req = requests.get("https://ru.investing.com/currencies/cny-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (soup.find('div',class_='desktop:relative desktop:bg-white')
             .find('div',class_='relative flex')
             .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
             .find('div','text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'))
    return items.text


# Динамика курса юаня в абсолютных числах
def cny_din():
    req = requests.get("https://ru.investing.com/currencies/cny-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (
        soup.find('div', class_='desktop:relative desktop:bg-white')
        .find('div', class_='relative flex')
        .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
        .find('div', 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main').find('span'))
    return items.text

# Динамика курса юаня в процентах
def cny_din_percent():
    req = requests.get("https://ru.investing.com/currencies/cny-rub")

    src = req.text

    soup = BeautifulSoup(src, "lxml")
    items = (
        soup.find('div', class_='desktop:relative desktop:bg-white')
        .find('div', class_='relative flex')
        .find('div',class_='mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6')
        .find('div', 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main').find_all('span')[1])
    return items.text

print(dollar())
print(dollar_din())
print(dollar_din_percent())
print('  ')
print(euro())
print(euro_din())
print(euro_din_percent())
print('  ')
print(cny())
print(cny_din())
print(cny_din_percent())




