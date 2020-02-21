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

if "temp" not in form or "hum" not in form or "rain" not in form:
    print("ERRO: Todos os parâmetros são obrigatórios.")
    sys.exit()

temperatura = form["temp"].value
umidade = form["hum"].value
chuva = form["rain"].value
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
    user = "ifba_sensors",
    passwd = "",
    database = "ifba_sensors"
)

# Faz a insercao
mycursor = mydb.cursor()
sql = "INSERT INTO medicoes (temperatura, umidade, chuva) VALUES (%s, %s, %s)"
val = (temperatura, umidade, chuva)
mycursor.execute(sql, val)
mydb.commit()

# Mensagem final
print("Temperatura: %f C\nUmidade: %f %%\nChuva: %d" % (temperatura, umidade, chuva))
