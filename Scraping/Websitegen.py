from bs4 import BeautifulSoup
import requests
import pickle

URL2 = 'https://fiscalianl.gob.mx/estadisticas/#tab-408e2395d13cec87a70'
URL2 = BeautifulSoup(requests.get(URL2).text, "lxml")
web = []
for product in URL2.find_all('div', class_='fusion-post-wrapper'):
    for prod in product.find_all('h2'):
        for link in prod.find_all('a'):
            web.append(link['href'])
with open('websites.pickle', 'wb') as f:
    pickle.dump(web, f)