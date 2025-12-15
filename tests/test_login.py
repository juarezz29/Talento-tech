from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_login_validation(login_in_driver):
    driver = login_in_driver

    #Espera implícita
    driver.implicitly_wait(5)

    try:
        # Validación de la redirección de la página
        assert '/inventory.html' in driver.current_url, "No se redirigió correctamente a la página de inventario."
        print("Inicio de sesión exitoso y validado correctamente")

    except AssertionError as e:
        print(f"Error en test_login_validation: {e}")
        raise

    finally:
        time.sleep(2)
        driver.quit()
