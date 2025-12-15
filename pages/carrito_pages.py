from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CarritoPage:
    #URL
    URL = "https://www.saucedemo.com/cart.html"

    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")
    _SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def agregar_articulo(self, producto_index=0):
        productos = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        if producto_index < len(productos):
            add_button = productos[producto_index].find_element(By.TAG_NAME, "button")
            add_button.click()
        return self
    
    def hacer_clic_checkout(self):
        checkout_button = self.driver.find_element(*self._CHECKOUT_BUTTON)
        checkout_button.click()
        return self
    
    def eliminar_articulo(self, index=0):
        cart_items = self.driver.find_elements(*self._CART_ITEMS)
        if index < len(cart_items):
            remove_button = cart_items[index].find_element(*self._REMOVE_BUTTON)
            remove_button.click()
        return self
    
    def ir_a_carrito(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return self 
    
    def carrito_vacio(self):
        cart_items = self.driver.find_elements(*self._CART_ITEMS)
        return len(cart_items) == 0 
    
    def obtener_articulos_carrito(self):
        return self.driver.find_elements(*self._CART_ITEMS) 
    
    def cerrar_navegador(self):
        self.driver.quit()
    
    
