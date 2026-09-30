from selenium import webdriver #importar selenium
from selenium.webdriver.common.by import By # agregar funcion by
import time #modulo de tiempo para pausar

def test_login_exitoso():

    driver = webdriver.Chrome() #abrir chrome

    driver.get("https://www.saucedemo.com/") #agregar pagina

    time.sleep(2) #pausa en segundos

    usuario = driver.find_element(By.ID,"user-name") # para colocar el usuario
    password = driver.find_element(By.ID,"password") # para que coloque la contraseña
    boton_loggin = driver.find_element(By.ID,"login-button") #para que oprimar el boton de click 

    #completa el formulario
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    # se logea
    boton_loggin.click()

    #validar el url despues del login
    #assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    titulo = driver.find_element(By.CLASS_NAME,"app_logo") #para que busque la etiqueta del logo

    #valida si esta el logo 
    assert titulo.text == "Swag Labs"

    time.sleep(2)
    driver.quit() #cerrar navegador