# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:26:28 2024
Modificado em: 11/09/2024

@author: jny_jhow
"""

from variables import *
from functions import *
from prometheus_client import CollectorRegistry, Counter, Gauge, push_to_gateway

PUSHGATEWAY_ADDRESS = "pushgateway:9091"
registry = CollectorRegistry()

log_counter = Counter(
    "app_logs_total", "Contagem de logs de eventos", ["event"], registry=registry
)
execution_time = Gauge(
    "app_execution_time_seconds", "Tempo de execução do programa", registry=registry
)


def main():
    lista_ofertas = pfun_ml_get_products()
    df_ofertas = pfun_get_df(lista_ofertas)


if __name__ == "__main__":
    inicio_programa = datetime.today().strftime("%d/%m/%Y %Hh%Mm%Ss")
    log_counter.labels(
        event="inicio_programa"
    ).inc()
    push_to_gateway(PUSHGATEWAY_ADDRESS, job="app_mercado_livre", registry=registry)

    print(
        f"\n>>>>>>>>>> [{VAR_PLATAFORMA}] [ INICIO DO PROGRAMA EM: {inicio_programa} ] <<<<<<<<<<\n"
    )

    start = time()
    pfun_check_dir(VAR_PATH_RESULT_AUX)
    main()
    end = time()
    tempo_execucao = round(end - start, VAR_DECIMAL_FORMAT)

    execution_time.set(tempo_execucao)
    push_to_gateway(PUSHGATEWAY_ADDRESS, job="app_mercado_livre", registry=registry)

    log_counter.labels(event="fim_programa").inc()
    push_to_gateway(PUSHGATEWAY_ADDRESS, job="app_mercado_livre", registry=registry)

    print("-" * VAR_SLEEP_10 * VAR_SLEEP_10)
    print(f"\n[{my_carteira_teorica}] PROJETO EXECUTADO EM: >>>>> {tempo_execucao}s\n")
    print("-" * VAR_SLEEP_10 * VAR_SLEEP_10)
