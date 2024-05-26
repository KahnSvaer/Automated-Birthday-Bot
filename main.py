import random

import time

import pandas as pd
import datetime as dt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def message_friend(message_to_send, to_target):
    chrome_profile_path = "C:/Users/ASUS/AppData/Local/Google/Chrome/User Data"
    chrome_driver_path = "C:/Users/ASUS/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    profile_name = "Profile 2"

    options = Options()
    options.add_argument(f"user-data-dir={chrome_profile_path}")
    options.add_argument("profile-directory=" + profile_name)
    options.add_argument('--remote-debugging-pipe')

    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    driver.get("https://web.whatsapp.com")
    target = f'"{to_target}"'

    wait = WebDriverWait(driver, 100)
    contact_path = '//span[contains(@title,' + target + ')]'
    contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
    contact.click()
    message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
    message_box.send_keys(message_to_send + Keys.ENTER + Keys.ENTER)
    time.sleep(1)
    driver.close()


def get_message(name):
    with open("messages.txt") as file:
        message_template_list = file.readlines()
    message_template = random.choice(message_template_list)
    return f"{message_template.strip()} -BDayBot @{name}"


DATASET_PATH = "BDayBotDataset.csv"
data = pd.read_csv(DATASET_PATH, names=["name", "date"]).dropna().reset_index().drop('index', axis=1)
data["date"] = pd.Series([dt.datetime.strptime(record_date, "%d-%m-%Y") for record_date in data["date"]])

currant_date = dt.datetime.now()

for index, record in data.iterrows():
    if record["date"].month == currant_date.month and record["date"].day == currant_date.day:
        message = get_message(record['name'].split()[0])
        message_friend(message, "CIC mates")
