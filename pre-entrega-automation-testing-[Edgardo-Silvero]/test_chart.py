from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_agregado():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

        
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    time.sleep(2)
    
    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_loggin = driver.find_element(By.ID,"login-button")
            
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    
    boton_loggin.click()
    
    wait.until(EC.url_contains("inventory.html"))

    agregar_producto = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

    agregar_producto.click()


    contador = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert contador.text == "1", f"El contador debería ser 1 y es {contador.text}"

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()

    time.sleep(2)

    producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert producto.text == "Sauce Labs Backpack", f"Producto incorrecto: {producto.text}"

    time.sleep(5)
    driver.quit()
