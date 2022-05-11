from selenium import webdriver
import time

telefono = "986734782"
email = "himeji2482@eoscast.com"
contraseña = "4gatos#!"

url = "https://www.centralgamer.cl/customer/registration"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)
#ingreso los datos
driver.find_element_by_name("customer[email]").send_keys(email)
driver.find_element_by_name("customer[phone]").send_keys(telefono)
driver.find_element_by_name("customer[password]").send_keys(contraseña)
driver.find_element_by_name("customer[password_confirmation]").send_keys(contraseña)
driver.find_element_by_id("register_customer").click()
