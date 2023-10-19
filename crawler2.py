from selenium import webdriver
website = 'https://www.adamchoi.co.uk/overs/detailed'
# path nay la duong dan den thu muc chromedriver download ve tren may cua minh
path = 'C:\\Users\\TienLN\\Downloads\\chromedriver-win64'
driver = webdriver.Chrome()
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

#driver.quit()