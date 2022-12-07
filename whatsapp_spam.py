
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def find_elem(by, xp):
    found = False
    while not found:
        try:
            elem = driver.find_element(by, xp)
        except:
            continue
        else:
            found = True
    return elem

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

chat_name = 'Sanjeev' # CHANGE ACCORDING TO THE CHAT NAME YOU WANT TO SPAM

chat_image_xp = f'//*[contains(text(), "{chat_name}")]'
chat_image_elem = find_elem(By.XPATH, chat_image_xp)
sleep(3)
chat_image_elem.click()

text_box_xp = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
text_box_elem = find_elem(By.XPATH, text_box_xp)

num_of_msg = 50 # CHANGE ACCORDING TO THE NUMBER OF MESSAGES YOU WANT TO SEND
msg = 'hi' # CHANGE ACCORDING TO THE MESSAGE YOU WANT TO SPAM
for i in range(num_of_msg):
    text_box_elem.send_keys(msg, Keys.ENTER)

sleep(100)
