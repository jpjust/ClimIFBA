import pytz
import base64
import matplotlib
from app import app
from io import BytesIO
from flask import request
from sqlalchemy import and_
import matplotlib.dates as dates
from matplotlib.figure import Figure
from app.models.tables import Medicao
from datetime import datetime, timedelta
from matplotlib.pyplot import legend, rcParams


# Retorna o código base64 da imagem no formato PNG
def Graphic():
    # Define o timezone da plotagem e da hora que recebe do servidor
    matplotlib.rcParams['timezone'] = 'America/Bahia'
    tz_servidor = pytz.timezone('PST8PDT')

    # Obtém os dados
    if request.method == "POST":
        data = getDate()
        primeiro_dia = data[0]
        ultimo_dia = data[1]
        primeiro_dia = primeiro_dia.astimezone(tz_servidor)
        ultimo_dia = ultimo_dia.astimezone(tz_servidor)
        medicoes = Medicao.query.filter(and_(Medicao.hora >= primeiro_dia), (Medicao.hora <= ultimo_dia)).order_by(
            Medicao.id.desc())
    else:
        ultimo_dia = datetime.now() - timedelta(days=1)
        ultimo_dia = ultimo_dia.astimezone(tz_servidor)
        medicoes = Medicao.query.filter(Medicao.hora >= ultimo_dia).order_by(Medicao.id.desc())

    # Se não houver medições, retorna nulo
    if medicoes.count() == 0:
        return 0

    temperaturas = []
    umidades = []
    x = []

    # Coleta as medições
    for m in medicoes:
        temperaturas.insert(0, m.temperatura)
        umidades.insert(0, m.umidade)
        hora = m.hora.replace(tzinfo=tz_servidor)
        x.insert(0, hora)

    # Cria um objeto Figure sem usar o pyplot
    fig = Figure()
    plt = fig.subplots()

    # Plota os dados
    plt.plot(x, temperaturas, 'k-', color='red')  # linha contínua vermelha
    plt2 = plt.twinx()
    plt2.plot(x, umidades, 'k-', color='blue')  # linha contínua azul

    # Ajusta títulos e formatação
    plt.set_title("Medições")
    plt.grid(True)
    plt.set_xlabel("Horário")
    plt.tick_params(axis="y", labelcolor="red")
    plt.set_ylabel("Temperatura (°C)", color="red")
    plt2.set_ylabel("Umidade do ar (%)", color="blue")
    plt2.tick_params(axis="y", labelcolor="blue")
    fig.autofmt_xdate()
    plt.xaxis.set_major_formatter(dates.DateFormatter('%d/%m/%Y - %H:%M'))
    fig.tight_layout()

    # Buffer temporário
    buf = BytesIO()
    fig.savefig(buf, format="png", transparent=True)

    # Embute o conteúdo no html
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


# Altera as datas para o gráfico
def getDate():
    # Obtém as datas fornecidas pelo usuário
    data_inicial, horario_inicial = request.form["dinicial"].split("T")
    data_final, horario_final = request.form["dfinal"].split("T")

    # Faz um splot() nas datas para inserí-las no datetme
    ano_final, mes_final, dia_final = map(int, data_final.split("-"))
    hora_final, minuto_final = map(int, horario_final.split(":"))
    ano_inicial, mes_inicial, dia_inicial = map(int, data_inicial.split("-"))
    hora_inicial, minuto_inicial = map(int, horario_inicial.split(":"))
    segundo_final = segundo_inicial = mili_final = mili_inicial = 0

    # Gera as derradeiras datas
    d_final = datetime(ano_final, mes_final, dia_final, hora_final, minuto_final, segundo_final, mili_final)
    d_inicial = datetime(ano_inicial, mes_inicial, dia_inicial, hora_inicial, minuto_inicial, segundo_inicial,
                         mili_inicial)
    datas = d_inicial, d_final

    # Retorna tupla com as 2 datas
    return datas
