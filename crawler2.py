import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
website = 'https://www.adamchoi.co.uk/overs/detailed'

# path = 'D:\\Working\\study\\chromedriver'
path = 'C:\\Users\\TienLN\\Downloads\\chromedriver-win64'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome()
driver.get(website)

all_matches_button = driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, "tr")
print(matches)
for match in matches :
    print(match.text)

time.sleep(3000)
#driver.quit()