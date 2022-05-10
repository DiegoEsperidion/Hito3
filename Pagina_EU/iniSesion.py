
from selenium import webdriver
import time

email = "jiginab129@carsik.com"
contraseña = "4gatos#!"
url = "https://totamona.com/es/iniciar-sesion"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")


driver.get(url)

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(contraseña)

