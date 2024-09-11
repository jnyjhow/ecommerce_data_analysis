# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:28:48 2024
Modificado em: 11/09/2024

@author: jny_jhow
"""

#functions
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


def pfun_check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass


def pfun_ml_get_product(count, div_aux):
    
    dados = {}
    
    try:
    
        dados['ecommerce'] = 'mercado_livre'
        dados['page'] = count
        
        link_container = div_aux.find(class_='promotion-item__link-container')
        dados['product_link'] = link_container['href'] if link_container else None
        
        img = div_aux.find(class_='promotion-item__img')
        dados['product_image'] = img['src'] if img else None
        
        title = div_aux.find(class_='promotion-item__title')
        dados['product_title'] = title.get_text(strip=True) if title else None
        
        prices = div_aux.select("div[class*='andes-money-amount-combo'] .andes-money-amount")
        
        if len(prices) >= 2:
            dados['previous_price'] = prices[0].get_text(strip=True)
            dados['current_price'] = prices[1].get_text(strip=True)
        else:
            dados['previous_price'] = np.nan
            dados['current_price'] = prices[0].get_text(strip=True) if prices else 0
        
        discount = div_aux.find(class_='promotion-item__discount-text')
        dados['discount'] = discount.get_text(strip=True) if discount else None
        
        installments = div_aux.find(class_='promotion-item__installments')
        dados['installments'] = installments.get_text(strip=True) if installments else np.nan
        
        seller = div_aux.find(class_='promotion-item__seller')
        dados['seller'] = seller.get_text(strip=True) if seller else np.nan
        
    except Exception as e:
        print(f"Erro ao processar item: {e}")
        print(dados)
        dados = {}
    
    return dados


def pfun_ml_get_products():
    
    url = 'https://www.mercadolivre.com.br/ofertas'
    scraper = cloudscraper.create_scraper(delay=VAR_SLEEP_10, browser='chrome')
    content = scraper.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    if soup == None:
        sys.exit()

    next_button = soup.find(class_='andes-pagination__button--next')
    a_tag = next_button.find('a') if next_button else None
    
    svg_height = int(a_tag.find('svg').get('height')) if a_tag and a_tag.find('svg') and a_tag.find('svg').get('height') else None
    if svg_height == None:
        sys.exit()

    lista_ofertas = []
    for count in range(1, svg_height + 1):
        
        if count > 1:
            next_button = soup.find(class_='andes-pagination__button--next')
            url = next_button.find('a')['href'] if next_button and next_button.find('a') else None
            content = scraper.get(url)
            soup = BeautifulSoup(content.text, 'html.parser')
        
        if soup == None:
            continue;
        
        print(f'{count}: {url}')
        divs_promotion_item = soup.find_all(class_='promotion-item')
        
        for promotion_item in divs_promotion_item:
            dados = pfun_ml_get_product(count, promotion_item)
            if len(dados) > 0:
                lista_ofertas.append(dados)
    
    print('-'*VAR_SLEEP_10*VAR_SLEEP_10)
    return lista_ofertas


def pfun_get_df(lista_aux):

    df_aux = pd.DataFrame(lista_aux).reset_index(drop=True)
    df_aux.drop_duplicates(inplace=True)
    print(df_aux.shape)
    print(df_aux.head())
    print(df_aux.tail())
    
    return df_aux

