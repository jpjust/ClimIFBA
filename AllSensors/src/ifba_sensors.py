#!/usr/bin/python2
# coding:utf-8
'''
Created on 30 de nov de 2018

@author: João Paulo Just Peixoto <joao.just@ifba.edu.br>
'''
import mysql.connector  # pip install mysql-connector
import cgi, cgitb
import sys

#cgitb.enable()
print("Content-type: text/html\n")

# Pega os dados via GET
form = cgi.FieldStorage()

if "id" not in form or "temp" not in form or "hum" not in form or "rain" not in form:
    print("ERRO: Todos os parametros sao obrigatorios.")
    sys.exit()

id = form["id"].value
temperatura = form["temp"].value
umidade = form["hum"].value
chuva = form["rain"].value
id = int(id)
temperatura = float(temperatura)
umidade = float(umidade)
chuva = int(chuva)

# Se ambos temperatura e umidade foram 0, provavelmente há algo errado
if temperatura == umidade == 0:
    print("ERRO: Dados inválidos.")
    sys.exit()

# Conecta no banco
mydb = mysql.connector.connect(
    host = "mysql.just.pro.br",
    user = "",
    passwd = "",
    database = "ifba_sensors"
)

# Faz a insercao
mycursor = mydb.cursor()
sql = "INSERT INTO medicoes (no, temperatura, umidade, chuva) VALUES (%s, %s, %s, %s)"
val = (id, temperatura, umidade, chuva)
mycursor.execute(sql, val)
mydb.commit()

# Mensagem final
print("Sensor: %d\nTemperatura: %.2f C\nUmidade: %.2f %%\nChuva: %d" % (id, temperatura, umidade, chuva))
