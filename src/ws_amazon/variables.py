# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:45:12 2024
Modificado em: 23/09/2024

@author: jny_jhow
"""

# variables
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
from datetime import datetime
import platform

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##### inicializando script ----------------------------------------------------
my_carteira_teorica = 'ws_amazon'
VAR_CARTEIRA_TEORICA = my_carteira_teorica.lower()

VAR_PATH_PRINCIPAL = os.getcwd()
VAR_PATH_ENV = f'{VAR_PATH_PRINCIPAL}/.env'
VAR_PATH_RESULT = f'{VAR_PATH_PRINCIPAL}/result'
VAR_PATH_LOGS = f'{VAR_PATH_PRINCIPAL}/logs'
VAR_DECIMAL_FORMAT = 2
VAR_PATH_DRIVER = "drivers/chromedriver.exe"
VAR_TIPO_SELENIUM = 1
VAR_TIPO_WSL = False

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if platform.system() == 'Windows':
    VAR_PLATAFORMA = 'WINDOWS'
    
elif platform.system() == 'Linux':
    VAR_PLATAFORMA = 'LINUX'
    VAR_TIPO_SELENIUM = 2
    
else:
    VAR_PLATAFORMA = 'OTHERS'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

try:
    VAR_USER = os.getlogin()
    
except:

    import pwd
    VAR_USER = pwd.getpwuid(os.getuid())[0]
    VAR_TIPO_SELENIUM = 2

if VAR_TIPO_WSL:
    VAR_TIPO_SELENIUM = 1

VAR_AGUARDAR_X_MINUTOS = 1
VAR_SLEEP_1 = 1
VAR_SLEEP_2 = 2
VAR_SLEEP_5 = 5
VAR_SLEEP_10 = 10
VAR_SLEEP_20 = 20
VAR_SLEEP_MAX = 60 * VAR_AGUARDAR_X_MINUTOS

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

data_hj = datetime.today().strftime('%Y_%m_%d')
VAR_PATH_RESULT_AUX = f'{VAR_PATH_RESULT}/{data_hj}/'

if VAR_TIPO_SELENIUM == 2:
    VAR_PATH_DRIVER = "drivers/chromedriver"

print(f'\n>>>>>>>>>> [{VAR_TIPO_SELENIUM}] UTILIZANDO PLATAFORMA: {VAR_PLATAFORMA} <<<<<<<<<<\n')
