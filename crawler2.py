from selenium import webdriver
website = 'https://www.adamchoi.co.uk/overs/detailed'
# path nay la duong dan den thu muc chromedriver download ve tren may cua minh
path = 'D:\\Working\\study\\chromedriver'
driver = webdriver.Chrome()
driver.get(website)

driver.quit()