# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:45:43 2024
Modificado em: 23/09/2024

@author: jny_jhow
"""

# functions
import os
import warnings
warnings.filterwarnings('ignore')

from variables import *

import sys

import pandas as pd
import numpy as np
import cloudscraper

from bs4 import BeautifulSoup
from time import sleep, time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
# import undetected_chromedriver as uc
# from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager


def pfun_check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass


def pfun_amazon_get_product(div_aux):
    
    dados = {}
    
    try:
        
        dados['asin'] = div_aux.get_attribute('data-asin')
        dados['deal_id'] = div_aux.get_attribute('data-deal-id')
        
        link = div_aux.find_element(By.CSS_SELECTOR, "a[data-testid='product-card-link']").get_attribute('href')
        dados['link'] = link
        
        title = div_aux.find_element(By.CSS_SELECTOR, "p[class*='ProductCard-module__title']").text
        dados['title'] = title
        
        image_url = div_aux.find_element(By.CSS_SELECTOR, "img").get_attribute('src')
        dados['image_url'] = image_url
        
        try:
            discount = div_aux.find_element(By.CSS_SELECTOR, "div[class^='style_badgeLabel']").text
            dados['discount'] = discount
        except:
            dados['discount'] = None
        
        print(dados)
        
    except Exception as e:
        print(f"Erro ao processar item: {e}")
        # print(dados)
        dados = {}
    
    return dados


def pfun_amazon_get_products():
    
    lista_ofertas = []
    url = 'https://www.amazon.com.br/deals?ref_=nav_cs_gb'
    
    try:
        driver, display = pfun_chrome_get_driver(VAR_TIPO_SELENIUM)
    except Exception as e:
        print(e)
        driver, display = None, None
        lista_ofertas = []

    if driver != None:
        
        pfun_get_driver_cookie(driver, url)
        
        lista_ofertas = []
        lista_erros = []
        for lista_oferta, lista_erro in pfun_scroll_to_bottom(driver, VAR_SLEEP_5):
            lista_ofertas.extend([oferta for oferta in lista_oferta if len(lista_oferta) > 0])
            lista_erros.extend([erro for erro in lista_erro if len(lista_erro) > 0])
    
    return lista_ofertas


def pfun_get_df(lista_aux):

    if len(lista_aux) > 0:

        df_aux = pd.DataFrame(lista_aux).reset_index(drop=True)
        df_aux_mod = df_aux.drop_duplicates().reset_index(drop=True)
        print(df_aux.shape)
        print(df_aux.head())
        print(df_aux.tail())
        
        return df_aux_mod


def pfun_chrome_get_driver(tipo=1, mostrar_driver=True):

    if (tipo == 1):

        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")

        VAR_PATH_CHROME_DRIVER = f"{VAR_PATH_PRINCIPAL}/{VAR_PATH_DRIVER}"
        service = Service(executable_path=VAR_PATH_CHROME_DRIVER)
        driver = webdriver.Chrome(service=service, options=options)

        display = None

    elif (tipo == 2):

        display = Display(visible=0, size=(1200, 800))
        display.start()
        print('\n>>>>> INICIANDO DISPLAY!!! <<<<<\n')

        options = Options()
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--start-maximized")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--incognito")

        VAR_PATH_CHROME_DRIVER = f"{VAR_PATH_PRINCIPAL}/{VAR_PATH_DRIVER}"
        print(VAR_PATH_CHROME_DRIVER)
        # service = Service(executable_path=VAR_PATH_CHROME_DRIVER)
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, options=options)
        driver = webdriver.Chrome(options=options)

    else:
        print('DRIVER NAO LOCALIZADO!!!')
        driver, display = None, None

    return driver, display


def pfun_driver_check_connection(driver, url, tempo_espera=2):
    check_conection = True
    while check_conection:
        try:

            driver.get(url)
            check_conection = False

        except:
            pass
    sleep(tempo_espera)


def pfun_close_selenium_driver(driver, display):
    
    try:
        
        driver.close()
        driver.quit()
    
    except:
        pass
    
    try:
        
        #pausando o display
        if display != None:
            print('\n>>>>> PAUSANDO DISPLAY!!! <<<<<\n')
            display.stop()
            
    except:
        pass


def pfun_get_driver_cookie(driver, url):
    pfun_driver_check_connection(driver, url)


def pfun_scroll_to_bottom(
        driver, 
        pause_time=2, 
        scroll_increment=500
        ):
    current_position = 0
    new_position = scroll_increment

    while True:
        driver.execute_script(f"window.scrollTo({current_position}, {new_position});")
        sleep(pause_time)

        current_position = new_position
        new_position += scroll_increment

        page_height = driver.execute_script("return document.body.scrollHeight")
        if current_position >= page_height:
            break
        
        divs_promotion_item = driver.find_elements(By.CSS_SELECTOR, "[data-testid='product-card']")
        lista_ofertas = []
        lista_erros = []
        for promotion_item in divs_promotion_item:
            
            dados = pfun_amazon_get_product(promotion_item)
            if len(dados) > 0:
                lista_ofertas.append(dados)
        
        yield lista_ofertas, lista_erros
