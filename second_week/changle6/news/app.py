#/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,render_template,abort

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files/<filename>')
def files_index(filename):
    return render_template('file.html',filename=filename)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run()
