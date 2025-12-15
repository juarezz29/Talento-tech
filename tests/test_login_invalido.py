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
        driver.find_element(By.ID, "user-name").send_keys("standard_shoppyer")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Validación de mensaje de error
        error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert error_message == "Epic sadface: Username and password do not match any user in this service", "El mensaje de error no es el esperado."
        print("Validación de inicio de sesión inválido exitosa")    
    except AssertionError as e:
        print(f"Error en test_login_invalido: {e}")
        raise   
    finally:
        time.sleep(2)
        driver.quit()   
