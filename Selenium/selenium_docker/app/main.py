from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(10)

driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

driver.get('https://python.org')
print(driver.page_source)
print('teste')