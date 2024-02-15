from win32 import win32print
from win32 import win32api
import os

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