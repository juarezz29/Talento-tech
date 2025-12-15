from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_menu(login_in_driver):
    driver = login_in_driver
    wait = WebDriverWait(driver, 10)
    try:
        # Verificar que el usuario está logueado (en página de inventario)
        assert '/inventory.html' in driver.current_url, "No se completó el login"
        print("✓ Login exitoso")

        # Esperar y verificar que el botón de menú sea visible
        menu_button = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
        assert menu_button is not None, "Botón de menú no encontrado"
        print("✓ Botón de menú encontrado")

        # Hacer clic en el botón de menú
        menu_button.click()

        # Esperar y verificar que la opción "Logout" sea visible
        logout_link = wait.until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))
        assert logout_link is not None, "Opción 'Logout' no encontrada en el menú"
        print("✓ Opción 'Logout' encontrada en el menú")
    except AssertionError as e:
        print(f" Error en test_menu: {e}")
        raise
    finally:
        driver.quit()

    

