from selenium import webdriver
import time

nombre = "Anonimo"
apellido = "Contreras"
codigo_postal = "28001"
email = "jiginab129@carsik.com"
contraseña = "4gatos#!"

url = "https://www.comunidadmsm.es/Acceso?startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAYBI7RLEMDAwMDAwMDAwMDAwMDAwAAAA7OJINnBSupgrSpzp2lt9fxpuebkUqiAmSqJl8392phOvCxN8z67abyxq6rKPqXBoz0DsFatBU1ex6_7OEAK6d1Q7poVwcLgVurRsMhcwg73Un9Ui6NydRFypV0b6eRJGlNWPaY9KYT2fSrZ0TWo4N4FsUWaZExAJoDwTciTbGLQLQhWgnM9C3p0S1Ida6S1mxNRp8CAAfKkpsW10uJdu3C7Bv5UnmQ7JnyaHJbygIiOGwTdMtON-3wSxWF_DtZ2nxWIjeMapcMWHXdJ24g7vdXY89a93d4g_qRM1JW-IVEcNZUCcDJG76ij9snQKGq5-jDPb_syUKQsFFY_oXMfwS-GVpdD1QQg7f1iIDK705yOuXkuf9aG_smRli25ssb-ZslDBeI0_6Fy_GGY_xc7KyBz6RGi0BPCiPXdSLyk5z6kCkMRHGhDG1Jsr0TNpRWrKP6P5fo9-QgCW0GP2z6t7pRgRvBocIVFCzbge9RilVtOyzX-7aJhvlfwv8avlCQZTWHwknAGaok-QRj8fQD8kNyUSPCOcazsTCfac0WOdLbaWA_v81Z00rol8fOxixO6mOBr4IZK8YgFuQGY4U7z8GwHXMjOiHxZYN23yBCgIoF8dr4RDlAaxREs0WP1Zg9nZvCNPgaQc4vDZmxww16n35VE%253D%26login_hint%3Dcervecistas%25407011o000000m3Th.com_ga%253D840869586.1650483674"
driver= webdriver.Chrome("/home/diertech/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id("onetrust-accept-btn-handler").click()

# Tiempo de espera para darle al boton "REGISTRO" de la pagina web
time.sleep(7)

driver.find_element_by_id("fname").send_keys(nombre)
driver.find_element_by_id("lname").send_keys(apellido)
driver.find_element_by_id("postal").send_keys(codigo_postal)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("reemail").send_keys(email)
driver.find_element_by_id("password").send_keys(contraseña)

#Los bloques de aceptar las condiciones los agrego manualmente
driver.find_element_by_class_name("btn-ap").click()