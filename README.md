# Bem vindo ao Projeto Saucedemo QA!

<p align="center">
  <img src='https://github.com/SueberDEV/PROJETO1_Selenium-Pyth_ExpertQAon_/blob/main/IMG/Swag%20Labs%20-%20Google%20Chrome.jpg' width='350'>
  </p>

Este repositório contém casos de teste automatizados para a aplicação [SauceDemo](https://www.saucedemo.com/) utilizando Selenium e PyTest. Este projeto foi desenvolvido como parte do primeiro projeto da academia EXPERT QA, ministrada pelo Paulo Oliveira.


# Sobre o SauceDemo >>

[SauceDemo](https://www.saucedemo.com/) é um site de comércio eletrônico utilizado para fins de teste. A aplicação permite que os testadores pratiquem a automação de testes em um ambiente simulado de e-commerce, incluindo funcionalidades de login, navegação, adição e remoção de produtos do carrinho e processos de checkout.


##  Estrutura do Repositório

**tests/**: Contém todos os arquivos de teste.

-    **conftest.py**: Configurações e fixtures para os testes.
-   **test_login.py**: Casos de teste relacionados ao login.
-   **test_purchase.py**: Casos de teste relacionados ao fluxo de compra.
-   **test_cart.py**: Casos de teste relacionados ao carrinho de compras.
-   **test_navigation.py**: Casos de teste relacionados à navegação do site.

## Configuração

1 - Crie um ambiente virtual e instale as dependências: 

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

2 - Execute os testes:

    pytest



# Casos de Teste


### Login

-   **Login válido**: Verifica se o usuário pode fazer login com credenciais corretas.
-   **Login inválido**: Verifica a mensagem de erro ao tentar fazer login com credenciais incorretas.
-   **Usuário bloqueado**: Verifica a mensagem de erro ao tentar fazer login com um usuário bloqueado.

### Fluxo de Compra

-   **Fluxo completo de compra**: Verifica se o usuário pode adicionar produtos ao carrinho, realizar o checkout e completar a compra.

### Carrinho de Compras

-   **Checkout com carrinho vazio**: Verifica se o usuário pode realizar o checkout sem adicionar produtos ao carrinho.

### Navegação

-   **Logout do usuário**: Verifica se o usuário pode fazer logout corretamente.

## Sobre o Projeto

Este projeto foi desenvolvido como parte da academia EXPERT QA, ministrada pelo Paulo Oliveira. É o primeiro projeto do curso e visa demonstrar habilidades em automação de testes utilizando Selenium e PyTest. Através dos testes criados, é possível validar diversos cenários de uso da aplicação SauceDemo, incluindo login, fluxo de compra, manipulação do carrinho de compras e navegação.

## Autor

-   **Suéber F. Passos** - [LinkedIn](https://www.linkedin.com/in/sueberfp) - [GitHub](https://github.com/SueberDEV)
<br>
<br>




<p align="center">
   < Thanks! > <br>
  <img src='https://i.gifer.com/Za3R.gif' width='350'>
  </p>

