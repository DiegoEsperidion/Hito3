from selenium import webdriver
import time

nombre = "Anonimo"
apellido = "Contreras"
codigo_postal = "28001"
email = "jiginab129@carsik.com"
contraseña = "4gatos#!"

url = "https://www.weplay.cl/customer/account/create/"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id("firstname").send_keys(nombre)
driver.find_element_by_id("lastname").send_keys(apellido)
driver.find_element_by_id("email_address").send_keys(email)
driver.find_element_by_id("password").send_keys(contraseña)
driver.find_element_by_id("password-confirmation").send_keys(contraseña)
