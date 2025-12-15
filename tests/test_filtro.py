from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_container(login_in_driver):
    driver = login_in_driver
    wait = WebDriverWait(driver, 10)

    try:
        # Verificar que el usuario está logueado (en página de inventario)
        assert '/inventory.html' in driver.current_url, "No se completó el login"
        print("✓ Login exitoso")

        # Esperar y verificar que el filtro sea visible
        filtro = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
        assert filtro is not None, "Filtro no encontrado"
        print("✓ Filtro encontrado")
        
        # Click en el filtro para abrir opciones
        filtro.click()
        
        # Esperar opciones dentro del filtro
        opciones = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product_sort_container option")))
        assert len(opciones) >= 3, f"El filtro no contiene suficientes opciones. Encontradas: {len(opciones)}"
        print(f"✓ Filtro tiene {len(opciones)} opciones")
        
        # Seleccionar opción "Price (low to high)"
        for opcion in opciones:
            if opcion.get_attribute("value") == "lohi":
                opcion.click()
                print("✓ Opción 'Price (low to high)' seleccionada")
                break
        else:
            raise AssertionError("Opción 'Price (low to high)' no encontrada en el filtro")
        
    except AssertionError as e:
        print(f" Error en test_product_container: {e}")
        raise
    finally:
        driver.quit()


    
     