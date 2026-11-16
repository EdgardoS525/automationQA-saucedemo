from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_inventory(driver):
    logger.info("Iniciando prueba de login")
    login_page = LoginPage(driver)
    logger.info("Iniciando prueba de inventario")
    inventory_page = InventoryPage(driver)
    
    driver.get("https://www.saucedemo.com/")
    logger.info("Pagina abierta correctamente")

    login_page.login("standard_user","secret_sauce")
    logger.info("Ingreso de credenciales")

    logger.info("Iniciando prueba de productos")
    productos = inventory_page.obtener_productos()

    assert len(productos) > 0

    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
    assert inventory_page.obtener_precio_primer_producto() == "$29.99"
    logger.info("Prueba de productos correcta")

    assert inventory_page.menu_visible()
    logger.info("Prueba de menu")
    assert inventory_page.filtro_visible()
    logger.info("Prueba de filtros")