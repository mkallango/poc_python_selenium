import selenium

class Navigations: 
    def __init__(self, driver):
        self.driver = driver
   
    def acessar_tela_inicial(self):
        self.driver.get('https://www.dbserver.com.br/')
