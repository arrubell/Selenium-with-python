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
driver.get("https://www.eccouncil.org/")
time.sleep(5)
#navigate to get training

GetTraining = driver.find_element(By.XPATH,"//a[@href='/get-certified-with-ec-council-with-form/?utm_source=ecc-menu&utm_medium=header&utm_campaign=ecc-menu-header']")
# GetTraining = driver.find_element(By.XPATH("//a[@href='/get-certified-with-ec-council-with-form/?utm_source=ecc-menu&utm_medium=header&utm_campaign=ecc-menu-header']"))
driver.find_element(By.XPATH, "/get-certified-with-ec-council-with-form/?utm_source=ecc-menu&utm_medium=header&utm_campaign=ecc-menu-header']")
GetTraining.click()
time.sleep(5)


