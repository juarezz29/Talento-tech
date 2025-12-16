from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pytest
from pages.login_pages import LoginPage
from utils.datos import leer_csv_login


@pytest.mark.parametrize("usuario,password,", leer_csv_login("datos/data_login.csv"))

def test_login_validation(login_in_driver,usuario, password):

    driver = login_in_driver

    #Espera implícita
    driver.implicitly_wait(5)

   
        # Validación de la redirección de la página
    assert '/inventory.html' in driver.current_url, "No se redirigió correctamente a la página de inventario."
    print("Inicio de sesión exitoso y validado correctamente")

 
