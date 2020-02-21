#language:pt
Funcionalidade: Buscar produto no comércio online e adicionar ao carrinho

  Narrativa: Comércio online > Adicionar produto ao carrinho de compras
  Eu, como um usuário do site de compras
  Desejo buscar um produto
  Para que eu possa adicioná-lo ao carrinho de compras

  @cenario1
  Esquema do Cenário: Acessar o comércio online e buscar um produto existente.
    Dado que eu tenha acessado o comércio online "<url>"
    Quando eu informar no campo de busca o nome de um "<produto>" existente
    E realizar a busca
    Então o sistema deve apresentar uma lista de resultados com "<produto>"(s) que correspondem ao informado na busca
    Exemplos:
      | url                            | produto |
      | https://www.americanas.com.br/ | iphone  |

  @cenario2
  Esquema do Cenário: Adicionar produto desejado ao carrinho de compras.
    Dado que eu tenha acessado o comércio online "<url>"
    E realizado a busca de um "<produto>" existente
    Quando eu selecionar o produto na lista
    E acionar a opção para adicionar o produto ao carrinho de compras
    Então o sistema deve adicionar o "<produto>" ao carrinho de compras
    Exemplos:
      | url                            | produto |
      | https://www.americanas.com.br/ | iphone  |

  @cenario3
  Esquema do Cenário: Acessar o carrinho de compras e visualizar produtos adicionados
    Dado que eu tenha acessado o comércio online "<url>"
    E realizado a busca de um "<produto>" existente
    E adicionado o produto ao carrinho de compras
    Quando eu selecionar a opção para ir ao carrinho de compras
    Então o sistema deve abrir a tela de visualização do carrinho de compras
    E exibir o(s) "<produto>"(s) adicionado(s)
    Exemplos:
      | url                            | produto |
      | https://www.americanas.com.br/ | iphone  |

  @cenario4
  Esquema do Cenário: Acessar o comércio online e buscar um produto inexistente ou inválido.
    Dado que eu tenha acessado o comércio online "<url>"
    Quando eu informar no campo de busca o nome de um "<produto>" inexistente ou inválido
    E realizar a busca
    Então o sistema deve apresentar mensagem que nenhum resultado foi encontrado
    Exemplos:
      | url                            | produto           |
      | https://www.americanas.com.br/ | a90s809as8da0s9d8 |

  @cenario5
  Esquema do Cenário: Acessar o comércio online e acionar carrinho de compras vazio.
    Dado que eu tenha acessado o comércio online "<url>"
    Quando eu selecionar a opção para ir ao carrinho de compras vazio
    Então o sistema deve apresentar mensagem que a cesta está vazia
    Exemplos:
      | url                            |
      | https://www.americanas.com.br/ |