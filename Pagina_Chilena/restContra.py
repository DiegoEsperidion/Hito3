from selenium import webdriver
import time


email = "d462bdc6c4@catdogmail.live"

url = "https://www.centralgamer.cl/customer/login"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="reset_password"]').click()
time.sleep(3)
driver.find_element_by_name("customer[email]").send_keys(email)
driver.find_element_by_xpath('//*[@id="submit_login"]').click()
