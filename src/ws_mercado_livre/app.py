# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:26:28 2024
Modificado em: 11/09/2024

@author: jny_jhow
"""

#app_final
from variables import *
from functions import *


def main():
    lista_ofertas = pfun_ml_get_products()
    df_ofertas = pfun_get_df(lista_ofertas)


if __name__ == '__main__':
    inicio_programa = datetime.today().strftime('%d/%m/%Y %Hh%Mm%Ss')
    print(f'\n>>>>>>>>>> [{VAR_PLATAFORMA}] [ INICIO DO PROGRAMA EM: {inicio_programa} ] <<<<<<<<<<\n')
    start = time()
    pfun_check_dir(VAR_PATH_RESULT_AUX)
    main()
    end = time()
    tempo_execucao = round(end - start, VAR_DECIMAL_FORMAT)
    print('-'*VAR_SLEEP_10*VAR_SLEEP_10)
    print(f'\n[{my_carteira_teorica}] PROJETO EXECUTADO EM: >>>>> {tempo_execucao}s\n')
    print('-'*VAR_SLEEP_10*VAR_SLEEP_10)