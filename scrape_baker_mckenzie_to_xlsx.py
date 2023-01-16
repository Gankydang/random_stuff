from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from time import time
import pandas as pd
import os
import re

start_time = time()

def scrape():
    WEBSITE = 'https://resourcehub.bakermckenzie.com/en/resources/data-privacy-security'
    driver = webdriver.Chrome()
    driver.get(WEBSITE)
    country_li = get_countries(driver)

    for country in country_li:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div/select'))
        select.select_by_visible_text(country)
        current_url = driver.current_url
        topic_url_li = get_topics_url(driver)
        data_dict = {}

        for topic_url in topic_url_li:
            driver.get(topic_url)
            sleep(1)

            if present('//*[contains(text(), "Error Code: 500")]', driver):
                driver.get(current_url)
                sleep(3)
                continue

            topic_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[1]').text
            data_dict[topic_name] = {}

            qn_elems = driver.find_elements(By.XPATH, '//*[@class = "section__heading"]')
            ans_elems = driver.find_elements(By.XPATH, '//*[@class = "rte"]')

            for qn_elem, ans_elem in zip(qn_elems, ans_elems):
                qn = qn_elem.text
                ans = ans_elem.text
                data_dict[topic_name][qn] = ans

        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/h2/a').click()
        print(str(round((country_li.index(country) + 1) / len(country_li) * 100, 1)) + ' complete')
        sleep(1)
        yield country, data_dict
    driver.close()

def present(xp, driver):
    try:
        driver.find_element(By.XPATH, xp)
    except:
        return False
    else:
        return True

def get_countries(driver):
    country_li = []
    element = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div/select')
    all_options = element.find_elements(By.TAG_NAME, 'option')
    for option in all_options:
        country_li.append(option.get_attribute('text'))
    country_li = country_li[2:3]
    return country_li

def get_topics_url(driver):
    topic_li = []
    a_elems = driver.find_elements(By.XPATH, '//*[@class = "tree-navigation__list"]//a')
    for a in a_elems:
        topic_li.append(a.get_attribute('href'))
    topic_li = topic_li[2:3]
    return topic_li

def df_style(val):
   return "font-weight: normal"

def make_xl_file(country, data_dict):
    data_df = pd.DataFrame.from_dict(data_dict, orient='index')

    stacked_df = data_df.stack()
    stacked_df = stacked_df.reset_index()
    stacked_df.columns = ['Topics', 'Questions', 'Answers']
    stacked_df['Last Updated'] = stacked_df.apply(lambda row: re.search(r'\d\d? [A-Za-z]+ \d{4}', row.Answers).group() if re.search(r'\d\d? [A-Za-z]+ \d{4}', row.Answers) is not None else "",axis=1)
    stacked_df['Answers'] = stacked_df['Answers'].apply(lambda row: row.split("]\n")[1] if (']\n') in row else row)
    columnsTitles = ['Topics', 'Questions', 'Last Updated', 'Answers']
    stacked_df = stacked_df.reindex(columns=columnsTitles)
    stacked_df = stacked_df.groupby(['Topics', 'Questions'])
    stacked_df = stacked_df.first()
    stacked_df = (stacked_df.style.applymap_index(df_style))

    writer = pd.ExcelWriter(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'Global_Data_Privacy_&_Security_Handbook-{country}.xlsx'), engine='xlsxwriter')
    stacked_df.to_excel(writer, sheet_name='Sheet1', startrow=0, header=True, index=True)
    writer.save()

if __name__ == '__main__':
    for country, data_dict in scrape():
        make_xl_file(country, data_dict)

end_time = time()
print(f'Time elapsed {(end_time - start_time) / 60} minutes')
