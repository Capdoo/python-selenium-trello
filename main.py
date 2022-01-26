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
driver.find_element_by_xpath('//*[@data-test-id="header-member-menu-button"]').click()
time.sleep(TIEMPO_ESPERA)
driver.find_element_by_link_text("Perfil y visibilidad").click()
time.sleep(TIEMPO_ESPERA)


name_box = driver.find_element_by_name("username")
bio_box = driver.find_element_by_class_name("_2G_T79mYVTPcpm")

time.sleep(TIEMPO_ESPERA)
#submit_button = driver.find_element_by_class_name("_3cY-HMyZpdFgkA _3TTqkG5muwOzqZ _3Ik0JLsERwh6Ui _1Tu9wiuW4Te8Rx")
submit_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div[2]/div/div/div/form/button')



time.sleep(TIEMPO_ESPERA)
name_box.send_keys("2")
bio_box.send_keys("Descripción de prueba : biografía")
submit_button.click()


time.sleep(TIEMPO_ESPERA)
#driver.find_element_by_link_text("Guardar").click()


#driver.quit()