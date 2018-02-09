#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.
"""

__author__= "Paulino R. e Silva"

import Megasena as megasena

class Aposta:
    def __init__(self,tipoAposta,numeros_disponiveis):
        self.tipoAposta=tipoAposta #nome do jogo
        self.numeros_disponiveis=numeros_disponiveis #lista com os jogos do tipo de jogo
        self.total_num_jogados=0 #total de números jogados
        self.combinacoes=0

    def define_aposta(self, **kwargs):
        self.tipoAposta=kwargs["tipoAposta"]
        self.numeros_disponiveis=kwargs["numeros_disponiveis"]

def jogo_12_6(jogo):
    jogo.a = "1 2 3 4 5 6"
    jogo.b = "7 8 9 10 11 12"
    return(jogo.a, jogo.b)

def pega_variaveis_modulo_aposta(modulo_aposta):
    module = globals().get(modulo_aposta,None)
    book={}
    if module:
        book = {key: value for key, value in module.__dict__.iteritems() if not (key.startswith('__') or key.startswith('_'))}
    return book


def main():
    aposta = Aposta(megasena.tipoAposta,megasena.numeros_disponiveis)
    book = pega_variaveis_modulo_aposta(megasena)
    aposta.define_aposta(**dict(zip(("tipoAposta", "numeros_disponiveis"), (megasena.tipoAposta, megasena.numeros_disponiveis))))
    print(aposta.tipoAposta)

    #apresentando tabela formatada da megasena
    varlista=""
    for i in aposta.numeros_disponiveis:
        if i<10:
            varlista = varlista + "0" + str((i)) + " "
        else:
            varlista = varlista + str((i))+" "
        if (i % 6 ==0):
            varlista=varlista+"\n"
    print(varlista)
    #fim apresentação tabela tosca

    entrada_numeros=[1,2,3,4,5,6,7,8,9,10,12]
    novaAposta = megasena.Aposta()
    novaAposta.jogo=entrada_numeros
    print(novaAposta.jogo)

    #print(novaAposta.quant_num_apostados)

    #megasena.Aposta.set_12num_6jogos(entrada_numeros)





if __name__ == '__main__':
    main()