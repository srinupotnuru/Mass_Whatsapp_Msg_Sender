
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
import time
import xlrd
import numpy as np
import pandas as pd
from PIL import Image
import PIL
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
d = webdriver.Chrome(executable_path="C:\Dev\webdriver\chromedriver",options=options)

def send(num,d,message):
    d.get(
        f'https://web.whatsapp.com/send?phone={num}&text={message}')
    d.implicitly_wait(3)
    time.sleep(20)
    try:
        d.switch_to_alert().accept()
    except Exception as e:
        pass
    try:
        
        sendButton = d.find_element_by_xpath(
        '//span[@data-icon="send"]')
        sendButton.click()
        time.sleep(3)
        d.switch_to.alert.accept()
    except NoAlertPresentException:
        print("Alert Box Handled..")


training_data = pd.read_excel(
    "contacts.xlsx", header=None)
X_train = training_data.as_matrix()
for val in X_train:
    send(("91"+str(val)),d,"*We are Done*")
