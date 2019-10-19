import numpy as np
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import pandas as pd
import csv


browser = webdriver.Chrome(executable_path=r'C:/Users/Flags/Documents/PythonScripts/CodeAlex/chromedriver.exe') 
browser.get("https://fiscalianl.gob.mx/estadisticas/#tab-408e2395d13cec87a70")

# Wait 20 seconds for page to load
timeout = 60
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='nuevos-productos']/div[2]/div[3]/div[8]/input")))
except TimeoutException:
    print('Timed out waiting for page to load')
    browser.quit()

Search=browser.find_element_by_xpath("//*[@id='nuevos-productos']/div[2]/div[3]/div[8]/input")
Search.click()
try:
    WebDriverWait(browser, 2400).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="products"]/div[7759]/div/div[1]/img')))
except TimeoutException:
    print('Timed out waiting for page to load')
    browser.quit()
print("Search Results Page Loaded!")

titles=[]

URL1=BeautifulSoup(browser.page_source, 'html.parser')
print('Soup made!')
for item in URL1.find_all('div',class_='thumbnail'):
    for caption in item.find_all('img'):
        titles.append(caption['src']) 
print("Data Parsed")
mal=pd.DataFrame({'Data':titles})
print("Data in Dataframe")
mal.to_csv('links.csv')
print("Data Saved!")

EC.