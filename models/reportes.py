from utils.db import db
from dataclasses import dataclass

@dataclass
class Delati_reporte(db.Model):
    reporte_id: int
    reporte_name: str
    reporte_name_qry: str    
    reporte_descripcion: str    
    reporte_qry: str    
 
    reporte_id=db.Column(db.Integer,primary_key=True)
    reporte_name=db.Column(db.String(30))
    reporte_name_qry=db.Column(db.String(40))    
    reporte_descripcion=db.Column(db.String(60))    
    reporte_qry=db.Column(db.String(1000))    
    
    
    def __init__(self,reporte_name,reporte_name_qry,reporte_descripcion,reporte_qry):
        self.reporte_name=reporte_name
        self.reporte_name_qry=reporte_name_qry        
        self.reporte_descripcion=reporte_descripcion        
        self.reporte_qry=reporte_qry        
        
        