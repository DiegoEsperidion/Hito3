# Hito3
Los scripts hechos en clases

Este es el codigo hecho en clases:

from selenium import webdriver

nombre = "Anonimo"
apellido = "Contreras"
codigo_postal = "28001"
email = "jiginab129@carsik.com"
contraseña = "4gatos#!"

url = "https://www.comunidadmsm.es/Acceso?startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAYBI7RLEMDAwMDAwMDAwMDAwMDAwAAAA7OJINnBSupgrSpzp2lt9fxpuebkUqiAmSqJl8392phOvCxN8z67abyxq6rKPqXBoz0DsFatBU1ex6_7OEAK6d1Q7poVwcLgVurRsMhcwg73Un9Ui6NydRFypV0b6eRJGlNWPaY9KYT2fSrZ0TWo4N4FsUWaZExAJoDwTciTbGLQLQhWgnM9C3p0S1Ida6S1mxNRp8CAAfKkpsW10uJdu3C7Bv5UnmQ7JnyaHJbygIiOGwTdMtON-3wSxWF_DtZ2nxWIjeMapcMWHXdJ24g7vdXY89a93d4g_qRM1JW-IVEcNZUCcDJG76ij9snQKGq5-jDPb_syUKQsFFY_oXMfwS-GVpdD1QQg7f1iIDK705yOuXkuf9aG_smRli25ssb-ZslDBeI0_6Fy_GGY_xc7KyBz6RGi0BPCiPXdSLyk5z6kCkMRHGhDG1Jsr0TNpRWrKP6P5fo9-QgCW0GP2z6t7pRgRvBocIVFCzbge9RilVtOyzX-7aJhvlfwv8avlCQZTWHwknAGaok-QRj8fQD8kNyUSPCOcazsTCfac0WOdLbaWA_v81Z00rol8fOxixO6mOBr4IZK8YgFuQGY4U7z8GwHXMjOiHxZYN23yBCgIoF8dr4RDlAaxREs0WP1Zg9nZvCNPgaQc4vDZmxww16n35VE%253D%26login_hint%3Dcervecistas%25407011o000000m3Th.com_ga%253D840869586.1650483674"
driver= webdriver.Chrome("C:\Users\199779494\Documents\webdriver")

driver.get(url)

# Seleccionamos el boton "REGISTRO" de la pagina
driver.find_element_by_class_name("btn-ap btn-reg").click()
driver.find_element_by_id("fname").send_keys(nombre)
driver.find_element_by_id("lname").send_keys(apellido)
driver.find_element_by_id("postal").send_keys(codigo_postal)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("reemail").send_keys(email)
driver.find_element_by_id("password").send_keys(contraseña)

driver.find_element_by_id("comunicaciones").click()
driver.find_element_by_class_name("politicapriv").click()

driver.find_element_by_class_name("btn-ap").click()


Este es el codigo correspondiente a crear una cuenta en una pagina extranjera, el problema de esto fue que la actividad empezo en el laboratorio y por tanto no hay posibilidad de hacer mas. Sin embargo se entendio el procedimiento del trabajo y es posible continuar hasta terminarlo.

Otro problema es que no se ha podido probar el codigo debido a que no existian maquinas virtuales incorporados en los computadores del lab. Es probable que para la proxima traiga mi PC para que no vuelva a tener estos problemas. Un saludo.


