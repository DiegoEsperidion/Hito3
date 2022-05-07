from selenium import webdriver

username =  "15067932k"
password = "060482"

url = "https://postulacion.beneficiosestudiantiles.cl/login/index.php"

driver = webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_name("campo_rut").send_keys(username)
driver.find_element_by_name("campo_password").send_keys(password)
driver.find_element_by_css_selector(".btn-secundario").click()

print("logged in logrado")
