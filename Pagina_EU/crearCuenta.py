from selenium import webdriver
import time

nombre = "Anonimo"
apellido = "Contreras"
email = "jiginab129@carsik.com"
contraseña = "4gatos#!"

url = "https://totamona.com/es/iniciar-sesion?create_account=1"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_name("firstname").send_keys(nombre)
driver.find_element_by_name("lastname").send_keys(apellido)
driver.find_element_by_name("email").send_keys(email)

#Los bloques de aceptar las condiciones los agrego manualmente
driver.find_element_by_xpath('//*[@id="customer-form"]/footer/div[2]/div/label/span[1]').click()

time(3)

driver.find_element_by_class_name("btn-default signin-text register-btn").click()
