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
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.widget import Widget

Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')

class Sga(AnchorLayout):
    pass


class SgaApp(App):
    def build(self):
        return Sga()

if __name__ =='__main__':
    SgaApp().run()
