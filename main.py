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

try:

    # A class featureapprequests will be the class to which we map 'FeatureRequestApp' table.
    class FeatureRequestApp(Config.base):
        # A class using Declarative  needs a __tablename__ attribute, and one Column which is a primary key 
        __tablename__= Config.table
        __table_args__ = {'extend_existing': True}        
        featureId=Column('id', Integer, Sequence('feature_id_seq'),unique=True,primary_key=True)
        title = Column(String(250),unique=True)
        description = Column(String(1000))
        client = Column(String(100)) 
        clientPriority = Column(Integer())
        targetDate = Column(Date())
        productArea = Column(String(100))
        # __init__ is a special method in Python classes, it is the constructor method for a class
        # __init__ is called when ever an object of the class is constructed.
        def __init__(self, title, description, client, clientpriority, targetdate, productarea):
            self.title = title
            self.description = description
            self.client = client
            self.clientPriority = clientpriority
            self.targetDate = targetdate
            self.productArea = productarea

    # The declarative_base() base class contains a MetaData object where newly defined Table objects are collected.  
    # This object is to be accessed  for MetaData-specific operations.Such as, to issue CREATE statements for all tables.
    Config.base.metadata.create_all(Config.db)
    
except ArgumentError as argexp:
    print('missing connection string or primary key', argexp)

except UnboundExecutionError as unexp:
    print('SQL was attempted without a database connection to execute it on', unexp)

except IndexError as indexerror:
    print('Missing Table Name', indexerror)

except TypeError as typeerror:
    print('Check Params', typeerror)

except TimeoutError as timeout:
    print('Connection TimedOut', timeout)

if __name__ == '__main__':
  app.run()
