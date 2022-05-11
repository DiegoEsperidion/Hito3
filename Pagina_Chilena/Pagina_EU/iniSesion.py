
from selenium import webdriver
import time

email = "plynchp_v454k@chyju.com"
contraseña = "4gatos#!"
url = "https://totamona.com/es/iniciar-sesion"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")


driver.get(url)

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(contraseña)

time.sleep(5)
driver.find_element_by_xpath('//*[@id="submit-login"]/div').click()