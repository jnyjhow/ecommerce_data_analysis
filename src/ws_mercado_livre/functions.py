# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:28:48 2024
Modificado em: 21/09/2024

@author: jny_jhow
"""

# functions
import os
import warnings

warnings.filterwarnings("ignore")

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

        dados["ecommerce"] = "mercado_livre"
        dados["page"] = count

        def safe_get_text(element, default=""):
            return element.get_text(strip=True) if element else default

        def safe_get_attribute(element, attribute, default=""):
            return element.get(attribute, default) if element else default

        image_url = safe_get_attribute(
            div_aux.find("img", class_="poly-component__picture"), "data-src"
        )

        offer_type = safe_get_text(
            div_aux.find("span", class_="poly-component__highlight")
        )
        offer_style = safe_get_attribute(
            div_aux.find("span", class_="poly-component__highlight"), "style"
        )

        product_name = safe_get_text(div_aux.find("a", class_="poly-component__title"))
        product_link = safe_get_attribute(
            div_aux.find("a", class_="poly-component__title"), "href"
        )

        seller_name = (
            safe_get_text(div_aux.find("span", class_="poly-component__seller"))
            .replace("Loja oficial", "")
            .strip()
        )

        original_price = safe_get_text(
            div_aux.find("s", class_="andes-money-amount--previous")
        )

        current_price_element = div_aux.find("div", class_="poly-price__current")
        current_price = (
            safe_get_text(
                current_price_element.find(
                    "span", class_="andes-money-amount__fraction"
                )
            )
            if current_price_element
            else ""
        )

        discount = safe_get_text(
            div_aux.find("span", class_="andes-money-amount__discount")
        )
        installments = safe_get_text(
            div_aux.find("span", class_="poly-price__installments")
        )
        extra_discount = safe_get_text(
            div_aux.find("span", class_="poly-rebates__discount")
        )
        shipping = safe_get_text(div_aux.find("div", class_="poly-component__shipping"))

        # print(f"Imagem do Produto: {image_url}")
        # print(f"Oferta: {offer_type} (Estilo: {offer_style})")
        # print(f"Produto: {product_name}")
        # print(f"Link do Produto: {product_link}")
        # print(f"Vendedor: {seller_name}")
        # print(f"Preço Original: {original_price}")
        # print(f"Preço Atual: {current_price}")
        # print(f"Desconto: {discount}")
        # print(f"Parcelamento: {installments}")
        # print(f"Desconto Adicional: {extra_discount}")
        # print(f"Frete: {shipping}")

        dados["product_link"] = product_link
        dados["product_image"] = image_url
        dados["product_title"] = product_name
        dados["previous_price"] = original_price
        dados["current_price"] = current_price

        dados["discount"] = discount
        dados["installments"] = installments
        dados["seller"] = seller_name

        print(dados)

    except Exception as e:
        print(f"Erro ao processar item: {e}")
        print(dados)
        dados = {}

    return dados


def pfun_ml_get_products():

    url = "https://www.mercadolivre.com.br/ofertas"
    scraper = cloudscraper.create_scraper(delay=VAR_SLEEP_10, browser="chrome")
    content = scraper.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    if soup == None:
        sys.exit()

    next_button = soup.find(class_="andes-pagination__button--next")
    a_tag = next_button.find("a") if next_button else None

    svg_height = (
        int(a_tag.find("svg").get("height"))
        if a_tag and a_tag.find("svg") and a_tag.find("svg").get("height")
        else None
    )
    if svg_height == None:
        sys.exit()

    lista_ofertas = []
    for count in range(1, svg_height + 1):

        if count > 1:
            next_button = soup.find(class_="andes-pagination__button--next")
            url = (
                next_button.find("a")["href"]
                if next_button and next_button.find("a")
                else None
            )
            content = scraper.get(url)
            soup = BeautifulSoup(content.text, "html.parser")

        if soup == None:
            continue

        print(f"{count}: {url}")

        divs_promotion_item = soup.select('div[class*="poly-card "]')
        # divs_promotion_item = soup.find_all(class_='andes-card')

        for promotion_item in divs_promotion_item:
            dados = pfun_ml_get_product(count, promotion_item)
            # check_dados = dados.get('product_title', False)
            if len(dados) > 0:
                lista_ofertas.append(dados)

    print("-" * VAR_SLEEP_10 * VAR_SLEEP_10)
    return lista_ofertas


def pfun_get_df(lista_aux):

    df_aux = pd.DataFrame(lista_aux).reset_index(drop=True)
    df_aux.drop_duplicates(inplace=True)
    print(df_aux.shape)
    print(df_aux.head())
    print(df_aux.tail())

    return df_aux
