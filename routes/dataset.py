from flask import Blueprint, request,jsonify
from models.dataset import Dataset
dataset = Blueprint('dataset',__name__)

@dataset.route('/dataset', methods=['GET'])
def getDataset():
    if request.method=='GET':
        data      = {}
        dataset=Dataset.query.all()        
        data["dataset"]=dataset
        return jsonify(data)   


    
