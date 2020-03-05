#!/usr/bin/python3
# coding:utf-8
'''
Created on 30 de nov de 2018

@author: João Paulo Just Peixoto <joao.just@ifba.edu.br>
@author: Danilo Santos
'''
import serial   # pip install pyserial
import time
import urllib.request
import urllib.parse
import serial.tools.list_ports

port = "/dev/ttyACM0"
debug = True
intervalo = 300 # Intervalo entre as medições em segundos
ser = 0

while True:
    try:
        # Abre a porta serial, caso não tenha sido aberta antes
        if not ser:
            ser = serial.Serial(port, 9600, timeout=0)
            time.sleep(1)

        # Faz a leitura e tratamento dos dados
        dados = ser.readline()
        linha = dados.decode("ascii")
        if "ALLSENSORS.SINK:" in linha:
            header, dados = linha.split(":")
            id, temp, um = dados.split(";")
            id = int(id)
            temp = float(temp)
            um = float(um)
            chuva = 0    # Para uso futuro
            if debug:
                print("--\nSensor: %d\nTemperatura: %.2f C\nUmidade: %.2f %%\nChuva: %d" % (id, temp, um, chuva))
            # Monta a URL e envia os dados para o webservice
            params = urllib.parse.urlencode({'id': id, 'temp': temp, 'hum': um, 'rain': chuva})
            url = "http://just.pro.br/ifba_sensors.py?%s" % params
            conteudoweb = urllib.request.urlopen(url)
            #time.sleep(intervalo - 1)

        # Limpa o buffer de entrada para fazer uma nova leitura
        ser.flushInput()
    except serial.SerialException:
        print("Erro ao fazer leitura serial.")
    except urllib.error.URLError:
        print("Erro ao fazer a requisição HTTP.")
    except ValueError:
        pass
    time.sleep(1)
