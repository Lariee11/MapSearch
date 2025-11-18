from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging


class Navegador:
    def __init__(self, link_pesquisa):
        opcao_pesquisa = Options()
        opcao_pesquisa.add_argument("--headless")
        opcao_pesquisa.add_argument("--window-size=1920,1080")
        opcao_pesquisa.add_argument("--log-level=3")
        opcao_pesquisa.add_experimental_option('excludeSwitches', ['enable-logging'])
        logging.getLogger('urllib3').setLevel(logging.WARNING)
        # LOGGER.setLevel(logging.WARNING)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                       options=opcao_pesquisa)
        self.link_pesquisa = link_pesquisa
        self.driver.get(link_pesquisa)
        time.sleep(2)

    def encontrando_elemento(self, elemento):
        elemento_encontrado = self.driver.find_element(By.XPATH, elemento)
        elemento_encontrado.clear()
        return elemento_encontrado

    def pesquisando(self, informacao, elemento):
        campo_de_pesquisa = self.encontrando_elemento(elemento)
        campo_de_pesquisa.send_keys(informacao)
        campo_de_pesquisa.send_keys(Keys.ENTER)
        print('Realizando as Pesquisas...')
        time.sleep(2)

        self.driver.save_screenshot(f'{informacao}.png')
        print('Pesquisas Realizadas!')
        print('Gerando Link...')

    def obtendo_link(self):
        self.link_pesquisa = self.driver.current_url
        return print(f"Link da pesquisa do Usuário: \033[93m\033[1m{self.link_pesquisa}\033[0m")

