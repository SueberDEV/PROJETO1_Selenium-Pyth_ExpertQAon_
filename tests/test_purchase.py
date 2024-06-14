from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(swag, username, password):
    WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    swag.find_element(By.ID, "password").send_keys(password)
    swag.find_element(By.ID, "login-button").click()

def add_product_to_cart(swag, product_id):
    WebDriverWait(swag, 10).until(EC.element_to_be_clickable((By.ID, product_id))).click()

def fill_checkout_info(swag, first_name, last_name, postal_code):
    WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
    swag.find_element(By.ID, "last-name").send_keys(last_name)
    swag.find_element(By.ID, "postal-code").send_keys(postal_code)
    swag.find_element(By.ID, "continue").click()

# Cenário: Fluxo completo de compra
def test_purchase_flow(swag: WebDriver):
    """
    Cenário: Fluxo completo de compra
    Dado que o usuário está na página de login
    Quando o usuário faz login com "standard_user" e "secret_sauce"
    E o usuário adiciona 6 produtos ao carrinho
    E o usuário clica no ícone do carrinho
    E o usuário remove 1 produto do carrinho
    Então o carrinho deve mostrar 5 produtos
    Quando o usuário clica em "Checkout"
    E o usuário preenche as informações de checkout e clica em "Continue"
    E o usuário clica em "Finish"
    Então o usuário deve ver a mensagem "Thank you for your order!"
    """
    login(swag, "standard_user", "secret_sauce")
    
    products = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-fleece-jacket",
        "add-to-cart-sauce-labs-onesie",
        "add-to-cart-test.allthethings()-t-shirt-(red)"
    ]
    
    for product in products:
        add_product_to_cart(swag, product)
    
    cart_badge = WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "6"
    
    swag.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    remove_product_from_cart(swag, "remove-sauce-labs-bike-light") # type: ignore
    cart_badge = WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "5"
    
    swag.find_element(By.ID, "checkout").click()
    
    fill_checkout_info(swag, "Sueber", "Fantinato Passos", "3080-000")
    
    swag.find_element(By.ID, "finish").click()
    
    complete_message = WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert complete_message.text == "Thank you for your order!"
