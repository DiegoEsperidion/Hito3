from selenium import webdriver
import time

nombre = "El Pollo"
apellido = "Polluelo"
email = "plynchp_v454k@chyju.com"
contraseña = "4gatos#!"

url = "https://totamona.com/es/iniciar-sesion?create_account=1"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_name("firstname").send_keys(nombre)
driver.find_element_by_name("lastname").send_keys(apellido)
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(contraseña)
#Los bloques de aceptar las condiciones 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="customer-form"]/footer/div[2]/div/label/span[1]').click()

time.sleep(5)

driver.find_element_by_xpath("//button[@type='submit']").click()
