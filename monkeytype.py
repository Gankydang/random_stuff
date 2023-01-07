from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://monkeytype.com/')
driver.find_element(By.XPATH, '//*[@id="cookiePopup"]/div[2]/div[2]/div[2]').click()
sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="testConfig"]/div/div[3]/div[2]').click()
sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="testConfig"]/div/div[6]/div[2]/span').click()
sleep(0.5)
text_elem = driver.find_element(By.XPATH, '//*[@id="words"]')
text = text_elem.text.replace('\n', ' ')
input_elem = driver.find_element(By.XPATH, '//*[@id="wordsInput"]')
input_elem.send_keys(text)
input('Press enter when done...')
driver.close()
