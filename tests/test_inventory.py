from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.inventory_pages import InventoryPage

@pytest.mark.parametrize("usuario,password", [("standard_user", "secret_sauce")])

def test_inventory(login_in_driver, usuario, password):

    try:
        driver = login_in_driver

        inventory_page = InventoryPage(driver)
       #Verificar que los productos son visibles
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "No hay productos visibles en la pagina"

       #Verificar que el carrito de compras esta vacio
        assert inventory_page.obtener_carrito_vacio() == 0

       #Agregar un producto al carrito de compras
        inventory_page.agregar_producto_al_carrito_por_indice(0)

       #Verificar que el conteo del carrito de compras es 
        assert inventory_page.obtener_conteo_carrito() == 1, "El conteo del carrito de compras no es correcto despues de agregar un producto"


    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()
