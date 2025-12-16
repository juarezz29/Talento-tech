import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver, usuario, password):
    from pages.login_pages import LoginPage 
    login_page = LoginPage(driver)
    LoginPage(driver).abrir_pagina().login_completo(usuario, password)
    return driver

@pytest.fixture
def test_carrito(driver):
    from pages.carrito_pages import CarritoPage
    carrito_page = CarritoPage(driver)
    carrito_page.agregar_articulo()
    return driver

@pytest.fixture
def test_filtro(driver):
    from pages.filtro_pages import FiltroPage
    filtro_page = FiltroPage(driver)
    filtro_page.verificar_orden_precios("Price (low to high)")
    return driver

@pytest.fixture
def test_inventory(driver):
    from pages.inventory_pages import InventoryPage
    inventory_page = InventoryPage(driver)
    inventory_page.verificar_producto()
    return driver

@pytest.fixture
def test_menu(driver):
    from pages.menu_pages import MenuPage
    menu_page = MenuPage(driver)
    menu_page.abrir_menu()
    return driver