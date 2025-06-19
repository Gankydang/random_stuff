from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.telegram.org/a/')

input('Press enter to start spam...')

text_box_xp = '//*[@id="editable-message-text"]'
text_box_elem = driver.find_element(By.XPATH, text_box_xp)

num_of_msg = 10 # CHANGE ACCORDING TO THE NUMBER OF MESSAGES YOU WANT TO SEND
msg = 'hi' # CHANGE ACCORDING TO THE MESSAGE YOU WANT TO SPAM
for i in range(num_of_msg):
    text_box_elem.send_keys(msg, Keys.ENTER)

input('Press enter when done...')
