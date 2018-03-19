from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

"""
- using chrome webdriver v.2.37 (headless)
- running headless chrome: https://intoli.com/blog/running-selenium-with-headless-chrome/
"""

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('webdriver/chromedriver', chrome_options=options)

driver.get('http://www.afl.com.au')
fixtures_url = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div[1]/div/div[3]/div/div/ul/li[3]/a[@href="/fixture"]')

assert fixtures_url.text.lower().strip() == 'fixtures', 'captured incorrect menu item!'

hov = ActionChains(driver).move_to_element(fixtures_url)
hov.perform()

time.sleep(3)

ps = driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div[1]/div/div[3]/div/div/ul/li[3]/div/div/ul/li[1]/div/ul/li[1]/a')
for e in ps:
	print('now text:', e.text)