
from selenium import webdriver
import time


email = "plynchp_v454k@chyju.com"
contraseña_Actu = "4gatos#!"
contraseña_Nueva = "Esprt12345"

url = "https://totamona.com/es/datos-personales"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

#para el inicio de sesion

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(contraseña_Actu)

time.sleep(5)
driver.find_element_by_xpath('//*[@id="submit-login"]/div').click()

#empezar el cambio de contraseña
time.sleep(20)
driver.find_element_by_name("password").send_keys(contraseña_Actu)
driver.find_element_by_name("new_password").send_keys(contraseña_Nueva)

driver.find_element_by_xpath('//*[@id="customer-form"]/div[1]/div[1]/div/label/span[1]').click()
driver.find_element_by_xpath('//*[@id="customer-form"]/div[1]/div[3]/div/label/span[1]').click()

time.sleep(5)

driver.find_element_by_xpath("//button[@type='submit']").click()
