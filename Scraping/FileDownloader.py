from bs4 import BeautifulSoup
import requests
import pickle

with open('websites.pickle', 'rb') as f:
    websites = pickle.load(f)
with open('names.pickle', 'rb') as f:
    names = pickle.load(f)

files = []
for website in websites:
    URL = BeautifulSoup(requests.get(website).text, "lxml")
    Contain = URL.find_all('p',class_='embed_download')
    Link = Contain[0].find_all('a')
    files.append(Link[0]['href'])
    

print(files)
with open('files.pickle', 'wb') as f:
    pickle.dump(files, f)