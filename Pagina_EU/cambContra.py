
from selenium import webdriver
import time


contraseña_Actu = "Esprt12345"
contraseña_Nueva = "4gatos#!"

url = "https://totamona.com/es/iniciar-sesion?create_account=1"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_name("password").send_keys(contraseña_Actu)
driver.find_element_by_name("new_password").send_keys(contraseña_Nueva)

driver.find_element_by_xpath('//*[@id="customer-form"]/div[1]/div[1]/div/label/span[1]').click()
driver.find_element_by_xpath('//*[@id="customer-form"]/div[1]/div[3]/div/label/span[1]').click()

time(5)

driver.find_ement_by_class_name("btn-default signin-text register-btn").click()
