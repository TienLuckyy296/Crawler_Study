import time
from selenium import webdriver
from selenium.webdriver.common.by import By
website = 'https://www.adamchoi.co.uk/overs/detailed'
# path nay la duong dan den thu muc chromedriver download ve tren may cua minh
path = 'C:\\Users\\TienLN\\Downloads\\chromedriver-win64'
driver = webdriver.Chrome()
driver.get(website)
time.sleep(3000)
all_matches_button = driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_element(By.TAG_NAME, "tr")
print(matches)
for match in matches :
    print(match.text)

time.sleep(3000)
#driver.quit()