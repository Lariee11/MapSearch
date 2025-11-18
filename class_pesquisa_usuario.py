from class_navegador import Navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class PesquisaUsuario(Navegador):

    def __init__(self, pesquisa):
        super().__init__(pesquisa)

    def campo_de_pesquisa(self, elemento):
        elemento_encontrado = self.driver.find_element(By.NAME, elemento)
        elemento_encontrado.clear()
        return elemento_encontrado

    def realizando_pesquisa(self, informacao, elemento):
        campo_de_pesquisa = self.campo_de_pesquisa(elemento)
        campo_de_pesquisa.clear()
        campo_de_pesquisa.send_keys(informacao)
        campo_de_pesquisa.send_keys(Keys.ENTER)
        time.sleep(2)

        self.driver.save_screenshot(f'{informacao}.png')