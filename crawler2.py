import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/overs/detailed'

# path = 'D:\\Working\\study\\chromedriver'
path = 'C:\\Users\\TienLN\\Downloads\\chromedriver-win64'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome()
driver.get(website)

all_matches_button = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
score = []
away_team = []

print(matches)
for match in matches :
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home = match.find_element(By.XPATH,'./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)

driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('txt/football_data.csv', index=False)
print(df)