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