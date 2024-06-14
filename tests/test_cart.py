from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(swag, username, password):
    WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    swag.find_element(By.ID, "password").send_keys(password)
    swag.find_element(By.ID, "login-button").click()

# Cenário: Checkout com carrinho vazio
def test_empty_cart_checkout(swag):
    """
    Cenário: Checkout com carrinho vazio
    Dado que o usuário está na página de login
    Quando o usuário faz login com "standard_user" e "secret_sauce"
    E o usuário clica no ícone do carrinho
    E o usuário clica em "Checkout"
    E o usuário preenche as informações de checkout e clica em "Continue"
    E o usuário clica em "Finish"
    Então o usuário deve ver a mensagem "Thank you for your order!"
    """
    login(swag, "standard_user", "secret_sauce")
    
    swag.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    swag.find_element(By.ID, "checkout").click()
    
    fill_checkout_info(swag, "Sueber", "Fantinato Passos", "3080-000") # type: ignore
    
    swag.find_element(By.ID, "finish").click()
    
    complete_message = WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert complete_message.text == "Thank you for your order!"
