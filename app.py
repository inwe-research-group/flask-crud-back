from flask import Flask
from flask_cors import CORS
from utils.db import db
from routes.contacts import contacts
from routes.dataset import dataset
from routes.reportes import reportes
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)
app.register_blueprint(contacts)
app.register_blueprint(dataset)
app.register_blueprint(reportes)

with app.app_context():
    db.create_all()

if __name__== "__main__":    
    #app.run(host='0.0.0.0', debug=False, port=5000)
    app.run(debug=False)