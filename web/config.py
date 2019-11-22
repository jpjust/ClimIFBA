DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:///storage.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True

"""import matplotlib.pyplot
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]
matplotlib.pyplot.plot(meses, valores, color="black")
matplotlib.pyplot.bar(meses, valores, color="red")
matplotlib.pyplot.title('Faturamento no primeiro semestre de 2017')
matplotlib.pyplot.xlabel('Meses')
matplotlib.pyplot.ylabel('Faturamento em R$')
matplotlib.pyplot.ylim(100000, 120000)
matplotlib.pyplot.savefig('graph.png')
matplotlib.pyplot.show()
############################################"""
"""import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route("/")
def hello():
   # Generate the figure **without using pyplot**.
   fig = Figure()
   ax = fig.subplots()
   ax.plot([1, 2])
   # Save it to a temporary buffer.
   buf = BytesIO()
   fig.savefig(buf, format="png")
   # Embed the result in the html output.
   data = base64.b64encode(buf.getbuffer()).decode("ascii")
   return f"<img src='data:image/png;base64,{data}'/>"""
