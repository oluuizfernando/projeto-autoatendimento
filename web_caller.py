import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

from downloader import download_pdf
from printer import print_pdf
import customtkinter as ctk

def slow_type(element: WebElement, text: str, delay: float=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

def go_print(entries, what_frame = 0, entries_list = None):
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) #Keep window opened
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--unsafely-treat-insecure-origin-as-secure')
    options.add_argument('--allow-running-insecure-content')
    
    options.accept_insecure_certs = True
    driver = webdriver.Chrome(service=service, options=options)

    url = ''
    if what_frame == 1:
        url = "https://ibitelecom.com.br/boletos/"
        driver.get(url)
        box = driver.find_element(By.ID, "cpf")
        slow_type(box, entries[0].get(), 0.1)
        button = driver.find_element(By.CLASS_NAME, 'evc_mk_btn')
        button.click()
        time.sleep(15)
        pdf_link = driver.find_element(By.XPATH, '//*[@id="table-faturas"]/tbody/tr[2]/td[5]/a[1]')
        download_pdf(pdf_link.get_attribute("href"))
        print_pdf()
    elif what_frame == 2:
        url = "https://transito.mg.gov.br/veiculos/documentos-de-veiculos/imprimir-crlv"
        driver.get(url)
        placa_box = driver.find_element(By.ID, "placa")
        renavam_box = driver.find_element(By.ID, "renavam")
        cpf_cnpj_box = driver.find_element(By.ID, "cpf-cnpj")
        crv_box = driver.find_element(By.ID, 'numero-crv')
        slow_type(placa_box, entries[0].get(), 0.1)
        slow_type(renavam_box, entries[1].get(), 0.1)
        slow_type(cpf_cnpj_box, entries[2].get(), 0.1)
        slow_type(crv_box, entries[3].get(), 0.1)
        #button = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
        #button.click()
    elif what_frame == 3:
        url = "https://transito.mg.gov.br/veiculos/situacao-do-veiculo/emitir-de-extrato-de-multas"
        driver.get(url)
        placa_box = driver.find_element(By.ID, "placa")
        renavam_box = driver.find_element(By.ID, "renavam")
        slow_type(placa_box, entries[0].get(), 0.1)
        slow_type(renavam_box, entries[1].get(), 0.1)
        button = driver.find_element(By.XPATH, '//*[@id="content"]/form/button')
        button.click()
    elif what_frame == 4:
        url = "https://ipva1.fazenda.mg.gov.br/ipvaonline/executeConsultaIpvaPorRenavamConsolidadoAnoExercicio.action"
        driver.get(url)
        renavam_box = driver.find_element(By.ID, 'renavam')
        slow_type(renavam_box, entries[0].get(), 0.1)
        button = driver.find_element(By.ID, 'anoExercicio-button')
        button.click()
        button = driver.find_element(By.XPATH, '//*[@id="anoExercicio-menu"]/li[2]/a') #muda apenas o numero 2 pro 3 em diante
        button.click()
        button = driver.find_element(By.XPATH, '//*[@id="anchor"]/div[2]')
        button.click()
        #button = driver.find_element(By.CLASS_NAME, 'ui-link')
        #button.click()
    elif what_frame == 5:
        url = "https://login.vivo.com.br/loginmarca/appmanager/marca/publicoNovoLogin"
        driver.get(url)
        login_box = driver.find_element(By.ID, 'cpfOuEmail_we')
        slow_type(login_box, entries[0].get(), 0.1)
        senha_box = driver.find_element(By.ID, 'input_password')
        slow_type(senha_box, entries[1].get(), 0.1)
        button = driver.find_element(By.ID, 'btn-entrar-login-we')
        button.click()
        time.sleep(9)
        button = driver.find_element(By.XPATH, '//*[@id="vcMVMHomeAmDocsPage_homeIntegracaoAem"]/div/div[1]/div/div/div/a/img')
        button.click()
        driver.get('https://meuvivo.vivo.com.br/content/vivo/meu-vivo/minhas-contas/2--via-de-conta.html')
        time.sleep(3)
        button = driver.find_element(By.CLASS_NAME, 'atom-three-dot-button')
        button.click()
        button = driver.find_element(By.XPATH, '//*[@id="widget-content"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/div/div[1]/ul/li[2]/a/span')
        button.click()
        button = driver.find_element(By.XPATH, '//*[@id="icon"]/iron-icon')
        button.click()
    if entries_list != None:
        for e in entries_list:
            e.delete(0, ctk.END)

    