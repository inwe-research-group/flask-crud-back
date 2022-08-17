from utils.db import db
from dataclasses import dataclass

@dataclass
class Dataset(db.Model):
    id_consulta: int
    descripcion: str
    sql_consulta: str    
    
    id_consulta=db.Column(db.Integer,primary_key=True)
    descripcion=db.Column(db.String(100))
    sql_consulta=db.Column(db.String(100))    
    
    def __init__(self,descripcion,sql_consulta):
        self.descripcion=descripcion
        self.sql_consulta=sql_consulta        