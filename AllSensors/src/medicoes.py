#!/usr/bin/python2
# coding:utf-8
'''
Created on 30 de nov de 2018

@author: João Paulo Just Peixoto <joao.just@ifba.edu.br>
'''
import mysql.connector  # pip install mysql-connector
import cgi, cgitb
import sys

cgitb.enable()
print("Content-type: text/html\n")

# Conecta no banco
banco = mysql.connector.connect(
    host = "mysql.just.pro.br",
    user = "",
    passwd = "",
    database = "ifba_sensors"
)

# Faz a pesquisa das últimas 100 medições
cursor = banco.cursor()
cursor.execute("SET time_zone = '-3:00'")
cursor.execute("SELECT no, hora, temperatura, umidade, chuva FROM medicoes ORDER BY hora DESC LIMIT 100")
resultados = cursor.fetchall()

# Exibe os resultados da consulta
print("""
<html>
    <body>
        <h1>Ultimas 100 medicoes</h1>
        <table border="1">
            <tr>
                <td><strong>Sensor</strong></td>
                <td><strong>Hora</strong></td>
                <td><strong>Temperatura</strong></td>
                <td><strong>Umidade</strong></td>
                <td><strong>Chuva</strong></td>
            </tr>
""")
for medicao in resultados:
    #medicao[3] = "Sim" if medicao[3] == 1 else "Não"
    print("""
            <tr>
                <td align="center">%d</td>
                <td align="center">%s</td>
                <td align="center">%.2f C</td>
                <td align="center">%.2f %%</td>
                <td align="center">%s</td>
            <tr>
    """ % medicao)

# Finalização do HTML
print("""
        </table>
    </body>
</html>
""")
