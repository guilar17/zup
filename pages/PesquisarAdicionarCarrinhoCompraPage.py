import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PesquisarAdicionarCarrinhoCompra:

    def __init__(self, context):
        self.driver = context.driver

        ###SELETORES###
        self.id_campo_busca = "h_search-input"
        self.id_btn_busca_produto = "h_search-btn"
        self.css_lista_resultados = "#content-middle > div > div > div > div > div > .product-grid-item > div h2"
        self.css_primeiro_produto_lista = "#content-middle > div > div > div > div > div > .product-grid-item:nth-child(1)"
        self.id_btn_comprar = "btn-buy"
        self.id_btn_continuar = "btn-continue"
        self.class_produto_cesta = "link-default"
        self.class_titulo_carrinho = "page-title"
        self.class_btn_carrinho = "crt-icon"
        self.class_msg_carrinho_vazio = "empty-crt"
        self.xpath_msg_nenhum_encontrado = "//*[@id='content-middle']/div[6]/div/div/div/div[2]/span[1]/span/span[1]"

    def acessar_pagina_url(self, context, url):
        context.driver.get(url)
        element = context.wait.until(
            EC.presence_of_element_located((By.ID, self.id_campo_busca)))

    def informa_nome_produto(self, produto):
        self.driver.find_element(By.ID, self.id_campo_busca).send_keys(produto)

    def aciona_btn_busca_produto(self):
        self.driver.find_element(By.ID, self.id_btn_busca_produto).click()

    def verifica_lista_resultados(self, produto):
        lista = self.driver.find_elements(By.CSS_SELECTOR, self.css_lista_resultados)
        for item in lista:
            assert produto in item.text

    def seleciona_primeiro_produto_lista(self, context):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(By.CSS_SELECTOR, self.css_primeiro_produto_lista))
        self.driver.find_element(By.CSS_SELECTOR, self.css_primeiro_produto_lista).click()
        element = context.wait.until(
            EC.presence_of_element_located((By.ID, self.id_btn_comprar)))

    def seleciona_btn_comprar(self, context):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(By.ID, self.id_btn_comprar))
        self.driver.find_element(By.ID, self.id_btn_comprar).click()

    def seleciona_btn_continuar(self, context):
        element = context.wait.until(EC.presence_of_element_located((By.ID, self.id_btn_continuar)))
        self.driver.find_element(By.ID, self.id_btn_continuar).click()

    def verifica_produto_no_carrinho(self, context, produto):
        element = context.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, self.class_produto_cesta)))
        assert produto in str(
            self.driver.find_element(By.CLASS_NAME, self.class_produto_cesta).get_attribute("title")).lower()

    def verifica_exibicao_tela_carrinho(self):
        assert self.driver.find_element(By.CLASS_NAME, self.class_titulo_carrinho).text == "minha cesta"

    def verifica_nenhum_resultado_encontrado(self, context):
        assert "Ops!" in self.driver.find_element(By.XPATH, self.xpath_msg_nenhum_encontrado).text

    def aciona_carrinho_vazio(self):
        self.driver.find_element(By.CLASS_NAME, self.class_btn_carrinho).click()

    def verifica_mgs_carrinho_vazio(self):
        assert self.driver.find_element(By.CLASS_NAME, self.class_msg_carrinho_vazio).text == "sua cesta está vazia"
