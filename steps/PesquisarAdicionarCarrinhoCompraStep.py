from datetime import time

from behave import *

@given(u'que eu tenha acessado o comércio online "{url}"')
def step_impl(context, url):
    context.PesquisaAdicionaCarrinhoCompra.acessar_pagina_url(context, url)


@when(u'eu informar no campo de busca o nome de um "{produto}" existente')
def step_impl(context, produto):
    context.PesquisaAdicionaCarrinhoCompra.informa_nome_produto(produto)


@when(u'realizar a busca')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.aciona_btn_busca_produto()


@then(u'o sistema deve apresentar uma lista de resultados com "{produto}"(s) que correspondem ao informado na busca')
def step_impl(context, produto):
    context.PesquisaAdicionaCarrinhoCompra.verifica_lista_resultados(produto)


@given(u'realizado a busca de um "{produto}" existente')
def step_impl(context, produto):
    context.PesquisaAdicionaCarrinhoCompra.informa_nome_produto(produto)
    context.PesquisaAdicionaCarrinhoCompra.aciona_btn_busca_produto()


@when(u'eu selecionar o produto na lista')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.seleciona_primeiro_produto_lista(context)


@when(u'acionar a opção para adicionar o produto ao carrinho de compras')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.seleciona_btn_comprar(context)
    context.PesquisaAdicionaCarrinhoCompra.seleciona_btn_continuar(context)


@then(u'o sistema deve adicionar o "{produto}" ao carrinho de compras')
def step_impl(context, produto):
    context.PesquisaAdicionaCarrinhoCompra.verifica_produto_no_carrinho(context, produto)


@given(u'adicionado o produto ao carrinho de compras')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.seleciona_primeiro_produto_lista(context)
    context.PesquisaAdicionaCarrinhoCompra.seleciona_btn_comprar(context)


@when(u'eu selecionar a opção para ir ao carrinho de compras')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.seleciona_btn_continuar(context)


@then(u'o sistema deve abrir a tela de visualização do carrinho de compras')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.verifica_exibicao_tela_carrinho()


@then(u'exibir o(s) "{produto}"(s) adicionado(s)')
def step_impl(context, produto):
    context.PesquisaAdicionaCarrinhoCompra.verifica_produto_no_carrinho(context, produto)


@when(u'eu informar no campo de busca o nome de um "{produto}" inexistente ou inválido')
def step_impl(context, produto):
    context.PesquisaAdicionaCarrinhoCompra.informa_nome_produto(produto)


@then(u'o sistema deve apresentar mensagem que nenhum resultado foi encontrado')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.verifica_nenhum_resultado_encontrado(context)


@when(u'eu selecionar a opção para ir ao carrinho de compras vazio')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.aciona_carrinho_vazio()


@then(u'o sistema deve apresentar mensagem que a cesta está vazia')
def step_impl(context):
    context.PesquisaAdicionaCarrinhoCompra.verifica_mgs_carrinho_vazio()

