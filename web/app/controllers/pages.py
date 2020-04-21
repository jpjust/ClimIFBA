from flask import request
from flask import render_template
from app.controllers.graphic import Graphic, pytz
from datetime import datetime, timedelta


# Index
def index():
    # Datas para preenchimento do formulário
    tz_local = pytz.timezone('America/Bahia')
    if request.method != "POST":
        dfinal = str(datetime.now().astimezone(tz_local)).replace(" ", "T")[:16]
        dinicial = str((datetime.now() - timedelta(days=1)).astimezone(tz_local)).replace(" ", "T")[:16]
    else:
        dfinal = request.form["dfinal"]
        dinicial = request.form["dinicial"]

    return render_template("index.html", graph=Graphic(), dfinal=dfinal, dinicial=dinicial)
