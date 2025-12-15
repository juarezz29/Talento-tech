from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    #URL
    URL = "https://www.saucedemo.com/"

    _PRODUCT_CONTAINER = (By.CLASS_NAME, "inventory_item")  
    _FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)       
    
    def verificar_producto(self):
        self.wait.until(EC.presence_of_all_elements_located(self._PRODUCT_CONTAINER))
        return self
    
    
    def cerrar_navegador(self):
        self.driver.quit()
    
    
