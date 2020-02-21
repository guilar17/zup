from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PesquisarAdicionarCarrinhoCompra:

    def __init__(self, context):
        self.driver = context.driver

        ###SELETORES###
        self.id_campo_busca = "h_search-input"
        self.btn_busca_produto = "h_search-btn"

    def acessar_pagina_url(self, context, url):
        context.driver.get(url)
        element = context.wait.until(
            EC.presence_of_element_located((By.ID, self.id_campo_busca)))

    def informa_nome_produto(self, produto):
        self.driver.find_element(By.ID, self.id_campo_busca).send_keys(produto)

    def aciona_btn_busca_produto(self):
        self.driver.find_element(By.ID, self.btn_busca_produto).click()
