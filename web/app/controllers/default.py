from flask import render_template
from app import app
from app.models.tables import Medicao
import base64
from io import BytesIO
import matplotlib
from matplotlib.figure import Figure
import matplotlib.dates as dates
import pytz

# Retorna o código base64 da imagem no formato PNG
def Graphic():
    # Define o timezone da plotagem e da hora que recebe do servidor
    matplotlib.rcParams['timezone'] = 'America/Bahia'
    tz_servidor = pytz.timezone('PST8PDT')

    # Obtém os dados
    medicoes = Medicao.query.order_by(Medicao.id.desc()).limit(100)
    temperaturas = []
    umidades = []
    x = []

    for m in medicoes:
        temperaturas.insert(0, m.temperatura)
        hora = m.hora.replace(tzinfo=tz_servidor)
        x.insert(0, hora)

    # Cria um objeto Figure sem usar o pyplot
    fig = Figure()
    plt = fig.subplots()

    # Plota os dados
    #plt.plot(x, data1, 'go')  # green bolinha
    plt.plot(x, temperaturas, 'k-', color='red')  # linha tracejada vermelha

    #plt.plot(x, umidades, 'r^')  # red triangulo
    #plt.plot(x, umidades, 'k--', color='blue')  # linha tracejada azul

    # Ajusta títulos e formatação
    plt.set_title("Medições")
    plt.grid(True)
    plt.set_xlabel("Horário")
    plt.set_ylabel("Temperatura (°C)")

    fig.autofmt_xdate()
    plt.xaxis.set_major_formatter(dates.DateFormatter('%d/%m/%Y - %H:%M'))
    fig.tight_layout()

    # Buffer temporário
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embute o conteúdo no html
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

# Index
def padrao():
    return render_template("index.html", graph=Graphic())
