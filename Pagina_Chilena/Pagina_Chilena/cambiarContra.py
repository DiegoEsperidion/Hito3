from selenium import webdriver
import time

email = "plynchp_v454k@chyju.com"
contraseña_Actual = "4gatos#!"
contraseña_Nueva = "Prismatic015254"
url = "https://www.weplay.cl/customer/account/edit/changepass/1/"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)
#Entrar a la pagina 
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(contraseña_Actual)
#TIempo de espera para resolver el captCHa
time.sleep(60)

driver.find_element_by_id("current-password").send_keys(contraseña_Actual)
driver.find_element_by_id("password").send_keys(contraseña_Nueva)
driver.find_element_by_id("password-confirmation").send_keys(contraseña_Nueva)
time.sleep(10)
driver.find_element_by_xpath('//*[@title="Guardar"]').click()
