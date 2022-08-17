from flask import Blueprint, request,jsonify
from models.reportes import Delati_reporte
reportes = Blueprint('reportes',__name__)

@reportes.route('/reportes', methods=['GET'])
def getReportes():
    if request.method=='GET':
        data      = {}
        reportes=Delati_reporte.query.all()        
        data["reportes"]=reportes
        return jsonify(data)
    



    
