from win32 import win32print
from win32 import win32api
import os
from selenium import webdriver
import time

def print_pdf():
    lista_impressoras = win32print.EnumPrinters(2)
    i = 0
    for imp in (lista_impressoras):
        #print(imp)
        if str(imp[2]).startswith('KONICA'):
            impressora = imp
            print(imp)
            break
        i+=1

    win32print.SetDefaultPrinter(impressora[2])

    caminho = r"downloads"
    lista_arquivos = os.listdir(caminho)

    for arquivo in lista_arquivos:
        win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
  
"""
def download_pdf(current_user_url):
    print(current_user_url)

    download_dir = "C:\\Users\\eului\\OneDrive\\Documentos\\Documentos\\Repositorios Git\\projeto-autoatendimento\\downloads" # for linux/*nix, download_dir="/usr/Public"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
    "download.default_directory": download_dir, #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    #https://transito.mg.gov.br/veiculos/documentos-de-veiculos/imprimir-crlv/exibir_crlve
    driver.get(current_user_url)
    time.sleep(10)
"""
