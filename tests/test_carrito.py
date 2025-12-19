from selenium.webdriver import webdriver
from selenium import webdriver
import pytest
from pages.inventory_pages import InventoryPage
from pages.carrito_pages import CarritoPage 


@pytest.mark.parametrize("usuario, password", [("standard_user", "secret_sauce")])
def test_inventory(login_in_driver, usuario, password):

    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        #Agregar al carrito el primer producto
        inventory_page.agregar_primer_producto_al_carrito()
        
        #Abrir carrito
        inventory_page.abrir_carrito()

        #Validar que el carrito tenga un producto
        carrito_page = carrito_page(driver)

        producto_en_carrito = carrito_page.obtener_producto_carrito()
        assert len(producto_en_carrito) == 1


    except Exception as e:
        print(f"Ocurrió un error durante la prueba: {e}")
        raise
    

