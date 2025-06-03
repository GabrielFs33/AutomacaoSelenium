from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usuarioCadastro = "TheGreatPedrin"
senhaCadastro = "27489563"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

def abrirSignup():
    driver.get("https://demoblaze.com/")
    wait = WebDriverWait(driver, 10)
    signupButton = wait.until(EC.element_to_be_clickable((By.ID, "signin2")))
    signupButton.click()
    wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
    return wait

def AbrirLogin():
    driver.get("https://demoblaze.com/")
    wait = WebDriverWait(driver, 10)
    loginButton = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
    loginButton.click()
    wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
    return wait

def preencherEnviarSignup(username, password):
    driver.find_element(By.ID, "sign-username").clear()
    if username is not None:
        driver.find_element(By.ID, "sign-username").send_keys(username)
    driver.find_element(By.ID, "sign-password").clear()
    if password is not None:
        driver.find_element(By.ID, "sign-password").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]").click()

def preencherEnviarLogin(username, password):
    driver.find_element(By.ID, "loginusername").clear()
    if username is not None:
        driver.find_element(By.ID, "loginusername").send_keys(username)
    driver.find_element(By.ID, "loginpassword").clear()
    if password is not None:
        driver.find_element(By.ID, "loginpassword").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]").click()

def realizarLogout():
    try:
        wait = WebDriverWait(driver, 10)
        logoutButton = wait.until(EC.element_to_be_clickable((By.ID, "logout2")))
        logoutButton.click()
        print("🔨🔨🔨Logout realizado com sucesso.")
    except Exception as e:
        print(f"🔨🔨🔨 Erro ao tentar fazer logout: {e}")


def fecharAlertaPendente():
    try:
        alert = driver.switch_to.alert
        print(f"🔨🔨🔨 Alerta anterior detectado: {alert.text}")
        alert.accept()
    except:
        pass

def verificarAlertaEsperado(textoEsperado, nomeCenario):
    try:
        wait = WebDriverWait(driver, 10)
        alert = wait.until(EC.alert_is_present())
        alertaTexto = alert.text
        assert alertaTexto == textoEsperado, f"Texto do alerta inesperado: {alertaTexto}"
        print(f"✅🔨🔨🔨 {nomeCenario}: {alertaTexto}")
        alert.accept()
    except Exception as e:
        print(f"❌🔨🔨🔨 {nomeCenario} falhou: {e}")

def cenario1():
    fecharAlertaPendente()
    abrirSignup()
    preencherEnviarSignup(usuarioCadastro, senhaCadastro)
    verificarAlertaEsperado("Sign up successful.", "Cenário 1 - Cadastro válido")

def cenario2():
    fecharAlertaPendente()
    abrirSignup()
    preencherEnviarSignup(None, senhaCadastro)
    verificarAlertaEsperado("Please fill out Username and Password.", "Cenário 2 - Usuário vazio")

def cenario3():
    fecharAlertaPendente()
    abrirSignup()
    preencherEnviarSignup(usuarioCadastro, None)
    verificarAlertaEsperado("Please fill out Username and Password.", "Cenário 3 - Senha vazia")

def cenario4():
    fecharAlertaPendente()
    AbrirLogin()
    preencherEnviarLogin(usuarioCadastro, senhaCadastro)
    try:
        wait = WebDriverWait(driver, 10)
        usuarioLogado = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        assert usuarioCadastro in usuarioLogado.text, f"Nome do usuário incorreto: {usuarioLogado.text}"
        print(f"✅🔨🔨🔨 Cenário 4 - Login com credenciais válidas: {usuarioLogado.text}")
    except Exception as e:
        print(f"❌🔨🔨🔨Cenário 4 - Falha no login com credenciais válidas: {e}")

def cenario5():
    fecharAlertaPendente()
    AbrirLogin()
    usuarioInvalido = "Cleide"
    preencherEnviarLogin(usuarioInvalido,senhaCadastro)
    verificarAlertaEsperado("User does not exist.", "Cenário 5 - Usuário inválido e senha válida")

def cenario6():
    fecharAlertaPendente()
    AbrirLogin()
    senhaInvalida = "789"
    preencherEnviarLogin(usuarioCadastro,senhaInvalida)
    verificarAlertaEsperado("Wrong password.", "Cenário 6 - Usuário válido e senha inválida")

def cenario7():
    fecharAlertaPendente()
    AbrirLogin()
    preencherEnviarLogin(usuarioCadastro,None)
    verificarAlertaEsperado("Please fill out Username and Password.", "Cenário 7 - Usuario preenchido e senha vazia")

def cenario8():
    fecharAlertaPendente()
    AbrirLogin()
    preencherEnviarLogin(None,senhaCadastro)
    verificarAlertaEsperado("Please fill out Username and Password.", "Cenário 8 - Usuario vazio e senha preenchida")

def cenario9():
    fecharAlertaPendente()
    AbrirLogin()
    usuarioNaoCadastrado = "SionReiDelas"
    senhaNaoCadastrada = "337"
    preencherEnviarLogin(usuarioNaoCadastrado,senhaNaoCadastrada)
    verificarAlertaEsperado("User does not exist.", "Cenario 9 - Usuario e senha não cadastrados")

def cenario10():
    fecharAlertaPendente()
    AbrirLogin()
    preencherEnviarLogin(None,None)
    verificarAlertaEsperado("Please fill out Username and Password.", "Cenário 10 - Usuario e senha não preenchidos")


cenario1()
time.sleep(2)

cenario2()
time.sleep(2)

cenario3()
time.sleep(2)

cenario4()
time.sleep(2)

realizarLogout()
time.sleep(3)

cenario5()
time.sleep(2)

cenario6()
time.sleep(2)

cenario7()
time.sleep(2)

cenario8()
time.sleep(2)

cenario9()
time.sleep(2)

cenario10()
time.sleep(2)


#🔨🔨🔨
driver.quit()