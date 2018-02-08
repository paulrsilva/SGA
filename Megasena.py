#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.
"""

tipoAposta = "Megasena"
numeros_disponiveis = tuple(range(1, 61))
total_num_jogados = 0
combinacoes = 0

# class tipoAposta:
#     def __init__(self):
#         self.tipoAposta = "Megasena"
#         self.numeros_disponiveis = list(range(1,61))
#         self.total_num_jogados = 0
#         self.combinacoes = 0


class Aposta:
    def __init__(self):
        self.tipoAposta = tipoAposta
        self.numeros_disponiveis = numeros_disponiveis #numeros disponiveis no tipo de jogo
        self._numeros_apostados = []
        #self.quant_num_apostados = len(jogo)+1
        #self.set_jogo(jogo)


    def set_12num_6jogos(self,numeros):
        if(not(isinstance(numeros,list) and (len(numeros)<=12))):
            raise ValueError("Número de Números Inválido para a Aposta {}".format(numeros))
        self.numeros_apostados=numeros

    def set_jogo(self,numeros):
        if(not(isinstance(numeros,list) and (len(numeros)<=12))):
            raise ValueError("Número de Números Inválido para a Aposta {}".format(numeros))
        self._numeros_apostados=numeros


    def _get_jogo(self):
        return self._numeros_apostados

    jogo = property(fget=_get_jogo, fset=set_jogo)
