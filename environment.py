import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from pages.PesquisarAdicionarCarrinhoCompraPage import *


def before_scenario(context):
    # ###Configurações do driver###
    chrome_options = webdriver.ChromeOptions()
    chrome_options.accept_untrusted_certs = True
    chrome_options.assume_untrusted_cert_issuer = True
    chrome_options.add_argument("headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("-allow-running-insecure-content")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)
    context.driver.set_window_size(1280, 768)
    context.driver.set_page_load_timeout(40)
    context.driver.implicitly_wait(10)
    context.driver.set_script_timeout(40)
    context.wait = WebDriverWait(context.driver, 40)
    context.action = ActionChains(context.driver)

    # ###instancia das classes####
    context.PesquisaAdicionaCarrinhoCompra = PesquisarAdicionarCarrinhoCompra(context)


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)

    elif step.status == "passed":
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


def after_scenario(context):
    context.driver.quit()
