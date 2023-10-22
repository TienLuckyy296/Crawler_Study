import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

web = 'https://www.audible.com/search'
# path = 'D:\\Working\\study\\chromedriver'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(web)
driver.maximize_window()

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')

products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')
book_title = []
book_author = []
book_length = []

print('products == ;; == ' , products)
for product in products:
    book_title.append(product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text)
    book_author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
    book_length.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)
    
driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)