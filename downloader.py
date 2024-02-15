from selenium import webdriver
import time
from pathlib import Path
import requests

"""def download_pdf(current_user_url):
    download_dir = "/downloads" # for linux/*nix, download_dir="/usr/Public"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
    "download.default_directory": download_dir, #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    
    driver.get(current_user_url)
    print('Download feito com sucesso!')
    print(current_user_url)
    time.sleep(10)
"""
def download_pdf(current_user_url):
    filename = Path('downloads/arquivo.pdf')
    url = current_user_url
    response = requests.get(url)
    time.sleep(4)
    filename.write_bytes(response.content)

if __name__ == '__main__':
    pass