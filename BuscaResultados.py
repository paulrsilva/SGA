#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.
"""

__author__= "Paulino R. e Silva"

import requests
import zipfile
import os
import collections
from bs4 import BeautifulSoup
import sys
import codecs

STORAGE_PATH = "tmp/mega"
FILENAME = "resultados.zip"
FILE_PATH = os.path.join(STORAGE_PATH, FILENAME)
INSIDE_FILENAME = "d_megasc.htm"
URL = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip"


# verifica se existe a pasta tmp/mega. Senao cria ou apresenta erro
if not os.path.isdir(STORAGE_PATH):
    try:
        os.makedirs(STORAGE_PATH)
    except OSError:
        print("ERRO: Nao foi possivel criar o diretorio.\nVerifique!")
        sys.exit()

# baixando o arquivo de apostas da CEF
print("Baixando arquivo de resultados")
f = requests.get(URL)
with open(FILE_PATH,"wb") as myzip:
    myzip.write(f.content)
    myzip.close()
print("Extração de Arquivos Finalizada")

# verificando e extraindo os arquivos ZIP
if zipfile.is_zipfile(FILE_PATH):
    zip = zipfile.ZipFile(FILE_PATH)
    #todo Pegar nome de arquivo dinamicamente
    zip.extract(INSIDE_FILENAME)


# Abrindo arquivo para buscar resultados
# o arquivo html baixado da caixa está em codificação diferente da UTF-8
# Entao forcei o codec para abrir em ISO-8859-1
ARQUIVO_MEGA = codecs.open(INSIDE_FILENAME, 'r', "ISO-8859-1" )
soup = BeautifulSoup(ARQUIVO_MEGA,'lxml')
print(soup.title)

# Funções de contagem e mapeamento (usando o lambda)
tds = lambda node: [ x.text for x in node if x not in ('\n', ' ')]
nros = [ tds(x)[2:8] for x in soup.body.table.contents[2:] if x not in ('\n', ' ')]


print('Verificando os números mais usados...')

#cria um dicionário com os 60 números da aposta
usados = dict([ (x,0) for x in range (1,61)])

# itera os números somando 1 a cada repetição
for sorteio in nros:
    for nro in sorteio:
        usados[int(nro)] += 1

usados_ordenados = collections.OrderedDict([(y,usados[y]) for y in sorted(usados, key=usados.get, reverse=True)])

print("Os números que mais foram sorteados na Megasena:")
print("Dez   -  nº sorteios")
for k in usados_ordenados.keys():
    print("%02d   :    %i" %(k, usados_ordenados[k]))




