import requests
from bs4 import BeautifulSoup


base_url = 'https://www.digikala.com/search/category-usb-flash-memory/'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='c-product-box c-promotion-box js-product-box is-plp')
count = 1
for i in items:
    item_name = i.find('div', class_='c-product-box__title').text.strip()
    item_model = i.find('div', class_='c-product-box__title-en').text.strip()
    item_price = i.find('div', class_='c-price__value-wrapper').text.strip()
    print(f'{count}) Name: {item_name}')
    print(f'\tModel: {item_model}, Price: {item_price}')
    count += 1


pages = soup.find('ul', class_='c-pager__items')
npages = []
links = pages.find_all('a', class_='c-pager__item')
for link in links:
    x = link.get('href')
    npages.append(x)
for i in range(2, len(npages)):
    new_url = base_url + "?pageno=" + str(i)
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='c-product-box c-promotion-box js-product-box is-plp')
    for i in items:
        item_name = i.find('div', class_='c-product-box__title').text.strip()
        item_model = i.find('div', class_='c-product-box__title-en').text.strip()
        item_price = i.find('div', class_='c-price__value-wrapper').text.strip()
        print(f'{count}) Name: {item_name}')
        print(f'\tModel: {item_model}, Price: {item_price}')
        count += 1
