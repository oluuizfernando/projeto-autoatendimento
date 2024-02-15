from selenium import webdriver
import time

def download_pdf(current_user_url):
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
    print('Download feito com sucesso!')
    print(current_user_url)
    time.sleep(10)