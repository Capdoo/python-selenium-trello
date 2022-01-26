#Importanción de librerias
from selenium import webdriver
import time

TIEMPO_ESPERA = 3
EMAIL = "mazher_2014@hotmail.com"
PASSWORD = "passwordpruebas"

driver = webdriver.Chrome('./chromedriver')
#1. Ingresar al home
driver.get('https://trello.com/es')


#2. Click en iniciar sesión
driver.find_element_by_link_text("Iniciar sesión").click()
time.sleep(TIEMPO_ESPERA)
user_box = driver.find_element_by_name("user")
pass_box = driver.find_element_by_name("password")
submit_button = driver.find_element_by_id("login")


user_box.send_keys(EMAIL)
pass_box.send_keys(PASSWORD)
submit_button.click()

time.sleep(TIEMPO_ESPERA)


pass_box_2 = driver.find_element_by_name("password")
pass_box_2.send_keys(PASSWORD)
submit_button_2 = driver.find_element_by_id("login-submit")
submit_button_2.click()


# PRIMERA PRUEBA : Dentro de la página principal

time.sleep(TIEMPO_ESPERA)
time.sleep(TIEMPO_ESPERA)
driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div[2]/button/span/span').click()
time.sleep(TIEMPO_ESPERA)

time.sleep(TIEMPO_ESPERA)

driver.find_element_by_xpath('/html/body/div[2]/div/section/div/nav/ul/li[1]/button/span[2]').click()
#espacio_nombre.send_keys("nuevo espacio 1")

time.sleep(TIEMPO_ESPERA)
titulo_box = driver.find_element_by_xpath('/html/body/div[2]/div/section/div/form/div[1]/label/input')
time.sleep(TIEMPO_ESPERA)
titulo_box.send_keys("tablero_prueba_1")
#driver.execute_script("arguments[0].innerText = 'Empresa pequeña'", select_combo)

time.sleep(TIEMPO_ESPERA)

driver.find_element_by_xpath('/html/body/div[2]/div/section/div/form/button').click()

time.sleep(TIEMPO_ESPERA)
time.sleep(TIEMPO_ESPERA)
driver.maximize_window()
time.sleep(TIEMPO_ESPERA)
driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div[1]/button[4]/span[1]').click()
time.sleep(TIEMPO_ESPERA)
driver.find_element_by_xpath('/html/body/div[5]/div/section/div/div/div[1]/div/div[2]/div[2]/button').click()
time.sleep(TIEMPO_ESPERA)
driver.find_element_by_xpath('/html/body/div[5]/div/section/div/div/div[2]/form/button').click()


time.sleep(TIEMPO_ESPERA)
