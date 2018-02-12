#!/usr/bin/env python
# encoding: utf-8
# File name: main.py
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.
"""
__author__= "Paulino R. e Silva"

import kivy

from kivy.app import App
from kivy.uix.widget import Widget

class MySga(Widget):
    pass

class SgaApp(App):
    def build(self):
        return MySga()

if __name__ =='__main__':
    SgaApp().run()
