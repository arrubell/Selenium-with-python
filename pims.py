import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)

driver.get("http://202.161.191.131:30010/login")
time.sleep(5)
driver.maximize_window()
driver.delete_all_cookies()


userid = driver.find_element(By.NAME, "email").send_keys("BP8505080490")
password = driver.find_element(By.NAME, "password").send_keys("12345")
element = driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-4thj0p']")
element_list = element.text.split(" ")
Total = int(element_list[0])+int(element_list[2])
capchabox = driver.find_element(By.XPATH, "//input[@name='captchaResult']").send_keys(str(Total))
time.sleep(5)
print(Total)
login = driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-1tfqlfq']").click()
time.sleep(5)
