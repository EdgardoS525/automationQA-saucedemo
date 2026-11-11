from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

def test_titulo():

    driver = webdriver.Chrome()
    
    driver.get("https://www.saucedemo.com/")

    time.sleep(2)
    
    print("titulo:", driver.title)
    assert driver.title == "Swag Labs"

    time.sleep(2)
    driver.quit()

def test_inventario():
    driver = webdriver.Chrome()
        
    driver.get("https://www.saucedemo.com/")
    
    time.sleep(2)

    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_loggin = driver.find_element(By.ID,"login-button")
            
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    
    boton_loggin.click()

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print(f"Se encontraron {len(productos)} productos.")

    time.sleep(2)
    driver.quit()

def test_elementos_menu():
    driver = webdriver.Chrome()         
    driver.get("https://www.saucedemo.com/")
        
    time.sleep(2)
    
    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_loggin = driver.find_element(By.ID,"login-button")
                
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
        
    boton_loggin.click()

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú no está visible"

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert carrito.is_displayed(), "El ícono del carrito no está visible"

    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro no está visible"

    time.sleep(2)
    driver.quit()