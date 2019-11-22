# import graphic
from flask import render_template
from app import app
import numpy as np
import matplotlib.pyplot as plt


# graph = Graphic()

def Graphic():
    data1 = [10, 5, 2, 4, 6, 8]
    data2 = [1, 2, 4, 8, 7, 4]
    x = 10 * np.array(range(len(data1)))

    plt.plot(x, data1, 'go')  # green bolinha
    plt.plot(x, data1, 'k:', color='orange')  # linha pontilha orange

    plt.plot(x, data2, 'r^')  # red triangulo
    plt.plot(x, data2, 'k--', color='blue')  # linha tracejada azul

    plt.axis([-10, 60, 0, 11])
    plt.title("Mais incrementado")

    plt.grid(True)
    plt.xlabel("eixo horizontal")
    plt.ylabel("Eixo y")
    # plt.savefig('/teste.png', format='png')
    img = plt.savefig('/home/joao/Área de trabalho/Projetos Python/ClimIFBA/app/controllers/graphics/teste.png',
                      format='png')
    return img


@app.route("/", defaults={"graph": None})
def index(graph):
    return render_template("index.html", graph=Graphic())
