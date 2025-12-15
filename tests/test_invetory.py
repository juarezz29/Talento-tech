from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory_page_elements(login_in_driver):
    driver = login_in_driver

    try:
        # Verificar que el título de la página de inventario sea correcto
        inventory_title = driver.find_element(By.CLASS_NAME, "title").text
        assert inventory_title == "Products", "El título de la página de inventario no es correcto."

        # Verificar que haya al menos un producto listado en la página de inventario
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos en la página de inventario."

        print("Elementos de la página de inventario validados correctamente")

    except AssertionError as e:
        print(f"Error en test_inventory_page_elements: {e}")
        raise