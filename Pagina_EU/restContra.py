from selenium import webdriver
import time


email = "d462bdc6c4@catdogmail.live"

url = "https://totamona.com/es/datos-personales"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div/a').click()
time.sleep(3)
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_xpath('//*[@id="content"]/section/div/form/section/div/div[2]/button').click()
