from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome()
driver.get('https://mail.google.com/')
wait = WebDriverWait(driver,5)
arg = "//input[@class = 'whsOnd zHQkBf']"
input_box = wait.until(EC.presence_of_element_located((By.XPATH,arg)))
#Enter your username
string = '<mail ID>'
#Enter your password
password = '<password>'
input_box.send_keys(string)
input_box.send_keys(Keys.ENTER)
time.sleep(3)
input_box = wait.until(EC.presence_of_element_located((By.XPATH,arg)))
input_box.send_keys(password)
input_box.send_keys(Keys.ENTER)
time.sleep(3)
arg = "//div[@class='T-I J-J5-Ji T-I-KE L3']"
input_box = wait.until(EC.presence_of_element_located((By.XPATH,arg)))
input_box.click()
