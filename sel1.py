from selenium import webdriver

username =  "PAMELA.CORTESF"
password = "060482nac"

url = "https://bibliografiadigital.aiep.cl/"

driver = webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_name("sam_usuario").send_keys(username)
driver.find_element_by_name("password_usuario").send_keys(password)
driver.find_element_by_css_selector(".btn").click()

print("logged in logrado")