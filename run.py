#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html', myString="Sist.Ger.Apostas", my_list=[1,2,3,4,5,6])

if __name__ == '__main__':
    app.run(debug=True)