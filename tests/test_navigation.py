from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(swag, username, password):
    WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    swag.find_element(By.ID, "password").send_keys(password)
    swag.find_element(By.ID, "login-button").click()

# Cenário: Logout do usuário
def test_logout(swag):
    """
    Cenário: Logout do usuário
    Dado que o usuário está logado
    Quando o usuário clica no menu de navegação
    E o usuário clica em "Logout"
    Então o usuário deve ser redirecionado para a página de login
    """
    login(swag, "standard_user", "secret_sauce")
    
    swag.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(swag, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    
    login_button = WebDriverWait(swag, 10).until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert login_button is not None
