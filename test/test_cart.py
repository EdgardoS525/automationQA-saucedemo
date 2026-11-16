from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_productos_json
from utils.logger import logger

def test_cart(driver):
    logger.info("Iniciando prueba de login")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    driver.get("https://www.saucedemo.com/")
    logger.info("Pagina abierta correctamente")

    login_page.login("standard_user","secret_sauce")
    logger.info("Ingreso de credenciales")
    
    producto = read_productos_json()[0]
    
    
    inventory_page.agregar_producto(producto["nombre"])
    logger.info("Inicio de prueba de carrito")
    
    assert inventory_page.obtener_contador_carrito() == "1"
    logger.info("Prueba de carrito correcta")
    
    inventory_page.ir_al_carrito()
    
    assert cart_page.obtener_nombre_producto() == producto["nombre"]
    
    assert cart_page.obtener_precio_producto() == producto["precio"]