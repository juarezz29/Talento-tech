from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FiltroPage:
    #URL
    URL = "https://www.saucedemo.com/cart.html"

    _FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    _PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")   


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def seleccionar_filtro(self, valor):
        filtro = self.wait.until(EC.presence_of_element_located(self._FILTER_DROPDOWN))
        filtro.click()
        opciones = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product_sort_container option")))
        for opcion in opciones:
            if opcion.get_attribute("value") == valor:
                opcion.click()
                break
        return self

    def verificar_orden_precios(self, ascendente=True):
        precios = self.obtener_precios_productos()
        precios_ordenados = sorted(precios)
        if not ascendente:
            precios_ordenados.reverse()
        return precios == precios_ordenados
    
    def cerrar_navegador(self):
        self.driver.quit()