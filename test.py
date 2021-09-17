#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random

url = 'https://evermos.com/home/' 
tab_url = 'https://www.google.com'     
dirpath = os.getcwd()
chrome_dir = "{}/chromedriver".format(dirpath)
driver = webdriver.Chrome(executable_path =chrome_dir)
driver.maximize_window()
driver.get(url)
time.sleep(5)
notss =  driver.find_elements_by_class_name("masuk")
notss[0].click()
time.sleep(5)
telp = driver.find_elements_by_class_name("inputText__input")
telp[0].send_keys('621223334444')
telp[1].send_keys('password')
login =  driver.find_elements_by_class_name("btn--large")
login[0].click()
time.sleep(5)
home =  driver.find_elements_by_class_name("appNav__item")
home[2].click()
time.sleep(5)
salin =  driver.find_elements_by_class_name("storeFront__option")
salin[2].click()
time.sleep(5)
driver.execute_script("alert('Terimakasih. Semoga berkenan')")
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
print('Good bye')
driver.close()
