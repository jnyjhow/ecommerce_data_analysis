# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:28:26 2024
Modificado em: 11/09/2024

@author: jny_jhow
"""

#variables
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
from datetime import datetime
import platform
import psutil

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##### inicializando script ----------------------------------------------------
my_carteira_teorica = 'ws_mercado_livre'
VAR_CARTEIRA_TEORICA = my_carteira_teorica.lower()

VAR_PATH_PRINCIPAL = os.getcwd()
VAR_PATH_ENV = f'{VAR_PATH_PRINCIPAL}/.env'
VAR_PATH_RESULT = f'{VAR_PATH_PRINCIPAL}/result'
VAR_PATH_LOGS = f'{VAR_PATH_PRINCIPAL}/logs'
VAR_DECIMAL_FORMAT = 2

VAR_LOGICAL = True
N_CORES = psutil.cpu_count(logical=VAR_LOGICAL)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if platform.system() == 'Windows':
    VAR_PLATAFORMA = 'WINDOWS'
    
elif platform.system() == 'Linux':
    VAR_PLATAFORMA = 'LINUX'
    
else:
    VAR_PLATAFORMA = 'OTHERS'
    
print(f'\n>>>>>>>>>> UTILIZANDO PLATAFORMA: {VAR_PLATAFORMA} <<<<<<<<<<\n')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

try:
    VAR_USER = os.getlogin()
    
except:

    import pwd
    VAR_USER = pwd.getpwuid(os.getuid())[0]

VAR_AGUARDAR_X_MINUTOS = 1
VAR_SLEEP_1 = 1
VAR_SLEEP_2 = 2
VAR_SLEEP_5 = 5
VAR_SLEEP_10 = 10
VAR_SLEEP_20 = 20
VAR_SLEEP_MAX = 60 * VAR_AGUARDAR_X_MINUTOS

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

data_hj = datetime.today().strftime('%Y_%m_%d')
VAR_PATH_RESULT_AUX = f'{VAR_PATH_RESULT}/{data_hj}/'
