import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')

web = 'https://www.audible.com/search'
# path = 'D:\\Working\\study\\chromedriver'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get(web)
# driver.maximize_window()

# pagination: section 33
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
lastpage = int(pages[-2].text)

current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= lastpage:
    time.sleep(2)
    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')

    products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

    for product in products:
        title = product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text
        book_title.append(title)
        print(title)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)
    
    current_page = current_page + 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass
    
driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_pagination_section33.csv', index=False)