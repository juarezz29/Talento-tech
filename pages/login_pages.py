from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    #URL
    URL = "https://www.saucedemo.com/"

    _USER_INPUT= (By.ID, "user-name")
    _PASS_INPUT= (By.ID, "password")
    _LOGIN_BUTTON= (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def ingresar_usuario(self, usuario):
        user_input = self.wait.until(EC.visibility_of_all_elements_located(self._USER_INPUT))
        user_input = user_input[0]
        user_input.clear()
        user_input.send_keys(usuario)
        return self
    
    def ingresar_contraseña(self, password):
        pass_input = self.wait.until(EC.visibility_of_element_located(self._PASS_INPUT))
        pass_input.clear()
        pass_input.send_keys(password)
        return self
    
    def hacer_clic_button(self):
        clic_button = self.driver.find_element(*self._LOGIN_BUTTON)
        clic_button.click()
        return self
    
    def login_completo(self, usuario, password):
        self.abrir_pagina()
        self.ingresar_usuario(usuario)
        self.ingresar_contraseña(password)
        time.sleep(2)
        self.hacer_clic_button()
        return self
    
    def cerrar_navegador(self):
        self.driver.quit()