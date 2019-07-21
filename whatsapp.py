from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome() 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 20) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = ''
  
# Replace the below string with your own message 
string = "<Message>"
  
x_arg = "//span[@title ='<Reciever Name>']"
#defining the path for the reciever
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 
group_title.click() 
#class path
inp_xpath = "//div[@class ='_2S1VP copyable-text selectable-text']"
input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath))) 
for i in range(50): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(1) 
