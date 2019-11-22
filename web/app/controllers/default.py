import base64
from io import BytesIO

from flask import render_template
from app import app
import numpy as np
from matplotlib.figure import Figure

# Retorna o código base64 da imagem no formato PNG
def Graphic():
    # Dados
    data1 = [10, 5, 2, 4, 6, 8]
    data2 = [1, 2, 4, 8, 7, 4]
    x = 10 * np.array(range(len(data1)))

    # Cria um objeto Figure sem usar o pyplot
    fig = Figure()
    plt = fig.subplots()

    # Plota os dados
    plt.plot(x, data1, 'go')  # green bolinha
    plt.plot(x, data1, 'k:', color='orange')  # linha pontilha orange

    plt.plot(x, data2, 'r^')  # red triangulo
    plt.plot(x, data2, 'k--', color='blue')  # linha tracejada azul

    plt.axis([-10, 60, 0, 11])
    plt.set_title("Mais incrementado")

    plt.grid(True)
    plt.set_xlabel("eixo horizontal")
    plt.set_ylabel("Eixo y")

    # Buffer temporário
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embute o conteúdo no html
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

# Index
@app.route("/", defaults={"graph": None})
def index(graph):
    return render_template("index.html", graph=Graphic())
