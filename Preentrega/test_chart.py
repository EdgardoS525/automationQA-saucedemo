from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

def test_carrito():
    driver = webdriver.Chrome()
        
    driver.get("https://www.saucedemo.com/")
    
    time.sleep(2)

    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_loggin = driver.find_element(By.ID,"login-button")
            
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    
    boton_loggin.click()

    time.sleep(2)

    agregar_producto = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

    agregar_producto.click()


    time.sleep(2)
    driver.quit()
