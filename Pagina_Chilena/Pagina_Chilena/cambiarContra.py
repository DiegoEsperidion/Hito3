from selenium import webdriver
import time

email = "plynchp_v454k@chyju.com"
contraseña_Actual = "4gatos#!"
contraseña_Nueva = "Prismatic015254"
url = "https://www.centralgamer.cl/customer/edit"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)
#Entrar a la pagina 
driver.find_element_by_name("customer[email]").send_keys(email)
driver.find_element_by_name("customer[password]").send_keys(contraseña_Actual)
driver.find_element_by_xpath('//*[@id="submit_login"]').click()
#Darle a editar
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/div/a").click()
#Ingreso de nuevos datos y guardar
driver.find_element_by_name("customer[password]").send_keys(contraseña_Nueva)
driver.find_element_by_name("customer[password_confirmation]").send_keys(contraseña_Nueva)
driver.find_element_by_xpath('//*[@id="register_customer"]').click()
