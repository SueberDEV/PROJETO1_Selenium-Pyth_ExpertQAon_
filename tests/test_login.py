from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(swag, username, password):
    WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    swag.find_element(By.ID, "password").send_keys(password)
    swag.find_element(By.ID, "login-button").click()

# Cenário: Login válido
def test_valid_login(swag):
    """
    Cenário: Login válido com credenciais corretas
    Dado que o usuário está na página de login
    Quando o usuário insere "standard_user" como username
    E o usuário insere "secret_sauce" como password
    E o usuário clica no botão de login
    Então o usuário deve ser redirecionado para a página de inventário
    """
    login(swag, "standard_user", "secret_sauce")
    WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.ID, "inventory_container")))
    assert "https://www.saucedemo.com/inventory.html" in swag.current_url

# Cenário: Login inválido
def test_invalid_login(swag):
    """
    Cenário: Login inválido com credenciais incorretas
    Dado que o usuário está na página de login
    Quando o usuário insere "invalid_user" como username
    E o usuário insere "invalid_password" como password
    E o usuário clica no botão de login
    Então o usuário deve ver uma mensagem de erro indicando que o login falhou
    """
    login(swag, "invalid_user", "invalid_password")
    error_message = WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
    assert "Epic sadface" in error_message.text

# Cenário: Usuário bloqueado
def test_blocked_user(swag):
    """
    Cenário: Login com usuário bloqueado
    Dado que o usuário está na página de login
    Quando o usuário insere "locked_out_user" como username
    E o usuário insere "secret_sauce" como password
    E o usuário clica no botão de login
    Então o usuário deve ver uma mensagem de erro indicando que o usuário está bloqueado
    """
    login(swag, "locked_out_user", "secret_sauce")
    error_message = WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
    assert error_message is not None
