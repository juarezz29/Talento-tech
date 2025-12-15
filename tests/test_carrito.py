from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito():
    driver = webdriver.Chrome()

    #Espera implícita
    driver.implicitly_wait(5)

    #Espera explícita (se usará después de navegar a la página)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")
        # Esperar a que el input de usuario esté presente antes de interactuar
        wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Validación de la redirección de la página
        assert '/inventory.html' in driver.current_url

        # Interacciones con la página de inventario
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        productos[0].find_element(By.TAG_NAME, "button").click()
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == '1'

    finally:
        time.sleep(2)
        driver.quit()
