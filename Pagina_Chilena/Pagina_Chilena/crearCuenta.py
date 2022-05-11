from selenium import webdriver
import time

nombre = "El Pollo"
apellido = "Polluelo"
email = "plynchp_v454k@chyju.com"
contraseña = "4gatos#!"

url = "https://www.weplay.cl/customer/account/create/"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id("firstname").send_keys(nombre)
driver.find_element_by_id("lastname").send_keys(apellido)
driver.find_element_by_id("email_address").send_keys(email)
driver.find_element_by_id("password").send_keys(contraseña)
driver.find_element_by_id("password-confirmation").send_keys(contraseña)

time.sleep(15)

driver.find_element_by_xpath('//*[@id="form-validate"]/div[3]/div[1]/button').click()