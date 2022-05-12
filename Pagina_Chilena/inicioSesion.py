from selenium import webdriver
import time

email = "591f8a09d0@catdogmail.live"
contraseña_Actual = "4gatos#!"
contraseña_Nueva = "Prismatic015254"
url = "https://www.centralgamer.cl/customer/login"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)
#Entrar a la pagina 
driver.find_element_by_name("customer[email]").send_keys(email)
driver.find_element_by_name("customer[password]").send_keys(contraseña_Actual)
driver.find_element_by_xpath('//*[@id="submit_login"]').click()