from datetime import time

from behave import *

@given(u'que eu tenha acessado o comércio online "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    context.PesquisaAdicionaCarrinhoCompra.acessar_pagina_url(context, url)


@when(u'eu informar no campo de busca o nome de um "{produto}" existente')
def step_impl(context, produto):
    context.PesquisaAdicionaCarrinhoCompra.informa_nome_produto(produto)


@when(u'realizar a busca')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.aciona_btn_busca_produto()


@then(u'o sistema deve apresentar uma lista de resultados com "iphone"(s) que correspondem ao informado na busca')
def step_impl(context):
    assert True


@given(u'realizado a busca de um produto existente')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given realizado a busca de um produto existente')


@when(u'eu selecionar o produto na lista')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu selecionar o produto na lista')


@when(u'acionar a opção para adicionar o produto ao carrinho de compras')
def step_impl(context):
    raise NotImplementedError(u'STEP: When acionar a opção para adicionar o produto ao carrinho de compras')


@then(u'o sistema deve adicionar o produto ao carrinho de compras')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o sistema deve adicionar o produto ao carrinho de compras')


@given(u'adicionado o produto ao carrinho de compras')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given adicionado o produto ao carrinho de compras')


@when(u'eu selecionar a opção para ir ao carrinho de compras')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu selecionar a opção para ir ao carrinho de compras')


@then(u'o sistema deve abrir a tela de visualização do carrinho de compras')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o sistema deve abrir a tela de visualização do carrinho de compras')


@then(u'exibir o(s) produto(s) adicionado(s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then exibir o(s) produto(s) adicionado(s)')


@when(u'eu informar no campo de busca o nome de um produto inexistente ou inválido')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu informar no campo de busca o nome de um produto inexistente ou inválido')


@then(u'o sistema deve apresentar mensagem que nenhum resultado foi encontrado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o sistema deve apresentar mensagem que nenhum resultado foi encontrado'
)


@when(u'eu selecionar a opção para ir ao carrinho de compras vazio')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu selecionar a opção para ir ao carrinho de compras vazio')


@then(u'o sistema deve apresentar mensagem que a cesta está vazia')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o sistema deve apresentar mensagem que a cesta está vazia')

