import pytest
from selenium import webdriver

import pytest_html
import pathlib
import base64

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)


    yield driver

    driver.quit()
    
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return { "x-api-key": "x-api-key: pub_eeeaade4c21da85cda07bef9b688725ae5796d2be74b5e4fee5e7f9e477e1899"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            carpeta = pathlib.Path("reports/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)
            archivo = carpeta / f"{item.name}.png"

            driver.save_screenshot(str(archivo))

            imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
            report.extras = [
            pytest_html.extras.png(imagen, name="Screenshot")
            ]