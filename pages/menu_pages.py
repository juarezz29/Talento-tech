from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    #URL
    URL = "https://www.saucedemo.com/"

    _MENU_BUTTON= (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK= (By.ID, "logout_sidebar_link")
    _CLOSE_MENU_BUTTON= (By.ID, "react-burger-cross-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_menu(self):
        menu_button = self.wait.until(EC.element_to_be_clickable(self._MENU_BUTTON))
        menu_button.click()
        return self
    
    def hacer_clic_logout(self):
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_link.click()
        return self
    
    def cerrar_menu(self):
        close_menu_button = self.wait.until(EC.element_to_be_clickable(self._CLOSE_MENU_BUTTON))
        close_menu_button.click()
        return self
    
    def logout_completo(self):
        self.abrir_menu()
        self.hacer_clic_logout()
        return self 
    
    def cerrar_navegador(self):
        self.driver.quit()
    