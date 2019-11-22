from app import db


class Medicao(db.Model):
    __tablename__ = "medicoes"

    id = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.DateTime)
    temperatura = db.Column(db.Float)
    umidade = db.Column(db.Integer)

    def __init__(self, id, hora, temperatura, umidade):
        self.id = id
        self.hora = hora
        self.temperatura = temperatura
        self.umidade = umidade
