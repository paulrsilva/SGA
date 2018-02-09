#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.
"""

class Jogo:
    def __init__(self):
        self._jogo = 0
    @property
    def jogo(self):
        return self._jogo
    @jogo.setter
    def jogo(self,numeros):
        self._jogo=numeros
