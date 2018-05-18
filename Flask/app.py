#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:48:08 2018

@author: coiadoml
"""
import os
from flask import Flask, render_template, request
from pymongo import MongoClient


#app.config['MONGO_DBNAME'] = 'DataEngineering'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017'
app = Flask(__name__)

address = []
client = MongoClient('mongodb', 27017)
db = client.DataEngineering

@app.route('/search', methods=['GET', 'POST'])
def search():
    monuments = db.monumentsParis
    title = request.form['title']
    title =" "+title
    list = monuments.find( { 'title':title } )
    return render_template('index.html',links= list)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    _items = db.monumentsParis.find()
    items=[item for item in _items]
    return render_template('index.html',links = items)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
