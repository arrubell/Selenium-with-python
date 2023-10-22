import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.maximize_window()
#navigate to the url
driver.get("https://joinborderguard.bgb.gov.bd/")
time.sleep(5)
#navigate to the url
about_us = driver.find_element(By.XPATH,"//a[@tabindex='0']")
about_us.click()
time.sleep(7)

#home
home = driver.find_element(By.XPATH,"//img[contains(@class,'hidden')]")
home.click()
time.sleep(7)

#circular
cir = driver.find_element(By.XPATH,"//*[@id='root']")
cir.click()
time.sleep(5)


