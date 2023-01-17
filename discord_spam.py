from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep

email = ''
psw = ''
server_name = ''
chat_name = ''
num_of_msg = 0
msg = ''

driver = webdriver.Chrome()
url = 'https://discord.com/channels/@me'
driver.get(url)
sleep(3)

# login to discord
driver.find_element(By.XPATH, '//*[@id="uid_5"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="uid_8"]').send_keys(psw)
driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
sleep(10)

# select server and chat
driver.find_element(By.XPATH, f"//div[normalize-space(@aria-label)  = '{server_name}']").click()
driver.find_element(By.XPATH, f"//div[contains(text(), '{chat_name}')]").click()

# send text
text_box_elem = driver.find_element(By.XPATH, "//div[@role = 'textbox']")
for i in range(num_of_msg):
    try:
        text_box_elem.send_keys(msg, Keys.ENTER)
    except ElementNotInteractableException:
        driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[3]/div[2]/div/div/form/div[2]/button').click()
        sleep(1)
        continue

input('Press enter when done...')