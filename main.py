from flask import Flask,render_template
# from sqlalchemy package we can import create_engine,Column, String, Integer, Date,asc
from sqlalchemy import create_engine,Column, String, Integer, Date,asc, Sequence

# from sqlalchemy package we can import declarativ_base
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy package we can import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import *

from config import Config
from app import routes,featureRequestManager, featureRequestService

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/FeatureRequestDetails')
def featureRequestDetails():
    """ featureRequestDetails function is used to display featureRequestDetails html page"""
    return render_template('featureRequestDetails.html')

@app.route('/')
def featureRequestForm():
    """ featureRequestForm function is used to display featureRequestForm html page"""
    return render_template('featureRequestForm.html')

if __name__ == '__main__':
  app.run()
