import requests
from bs4 import BeautifulSoup


url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    item_name = i.find('h4', class_='card-title').text.strip('\n')
    item_price = i.find('h5').text
    print(f'{count}) Price: {item_price}, Item Name: {item_name}')
    count += 1
