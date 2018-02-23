# coding=utf-8


from flask import Flask
import flask
import os
import requests
import json

app = Flask(__name__)



@app.route('/submit', methods=['POST'])
def check_answers():

    for item in flask.request.form.items():
        key, value = item
        print(key)


    return """<html>
<head><title>404 Not Found</title></head>
<body bgcolor="white">
<center><h1>404 🦆 Not Found</h1></center>
<hr><center>nginx/1.10.3</center>
</body>"""

    return json.dumps(flask.request.form)

@app.route('/')
def hello():

    random_person = {"results":[{"gender":"female","name":{"title":"mrs","first":"caitlin","last":"cruz"},"location":{"street":"2450 green lane","city":"norwich","state":"isle of wight","postcode":"C8 7JE"},"email":"caitlin.cruz@example.com","login":{"username":"blueduck680","password":"harvest","salt":"M7fXj5Pz","md5":"44b45fe7ff2799cbe4d6d1638166a3bf","sha1":"ed4f68933d4c69e7dc8b9f76ef560184e98ea9cd","sha256":"95efdb7bf1e8799dd36f0cbe8907132dafcb280792f4dc30f1de4863a98ad77a"},"dob":"1978-05-11 20:53:23","registered":"2005-03-01 20:18:38","phone":"0101 058 0273","cell":"0789-559-820","id":{"name":"NINO","value":"TG 58 28 74 O"},"picture":{"large":"https://randomuser.me/api/portraits/women/92.jpg","medium":"https://randomuser.me/api/portraits/med/women/92.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/92.jpg"},"nat":"GB"}],"info":{"seed":"7b7b323e7d37d926","results":1,"page":1,"version":"1.1"}}

    attributes = {"name":"Ulberto", "surname":"Ortzen", "email":"uortzen0@blogger.com", "gender":"Male", "ip":"115.193.70.3"}

    items = [
        {
            "html":"name.html",
            "name":"name",
            "value": "Ulberto Beton"
        },

        {
            "html":"gender.html",
            "name":"gender",
            "value": "Male"
        },

        {
            "html":"age.html",
            "name":"age",
            "value":"17",
        },

        {
            "html":"birthdate.html",
            "name":"birthdate",
            "value": "08/04/1964"
        },

        {
            "html":"zipcode.html",
            "name":"Zip Code",
            "value": "91745"
        },

        {
            "html":"ip.html",
            "name":"IP address",
            "value": "115.193.70.3"
        },

        {
            "html":"ssn.html",
            "name":"Social Security Number",
            "value": "750030703"
        },

        {
            "html":"number.html",
            "name":"Phone Number",
            "value": "101 058 273"
        },

        {
            "html":"preference.html",
            "name":"Color",
            "value": "Cyan"
        },

        {
            "html":"email.html",
            "name":"Email",
            "value": "caitlin.cruz@example.com"
        }
    ]
    return flask.render_template("index.html", items=items)


if __name__ == '__main__':
    app.run()