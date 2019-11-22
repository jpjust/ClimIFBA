import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure


def Graphic():
   # Generate the figure **without using pyplot**.
   fig = Figure()
   ax = fig.subplots()
   ax.plot([1, 2])
   # Save it to a temporary buffer.
   buf = BytesIO()
   fig.savefig(buf, format="png")
   # Embed the result in the html output.
   data = base64.b64encode(buf.getbuffer()).decode("ascii")
   return f"{data}"