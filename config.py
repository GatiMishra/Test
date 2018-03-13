import os
# from sqlalchemy package we can import create_engine
from sqlalchemy import create_engine
# from sqlalchemy package we can import declarativ_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Config(object): 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # SET database connection string
    #db_string = "postgres://postgres:Password0@localhost:5432/featureapp"
    #Need to uncomment when using cloud database
    #db_string = "postgres://myadmin:Password0@featureapp.postgres.database.azure.com:5432/featureappdb"
    db_string = "postgres://myadmin@featureapp:Password0@featureapp.postgres.database.azure.com:5432/featureappdb"
    #db_string = "dbname='featureappdb' user='myadmin' host='featureapp.postgres.database.azure.com’ password='Password0' port='5432' sslmode='true'"
    # an Engine, which the Session will use for connection
    db = create_engine(db_string)
    # Declarative, which allows us to create classes that include directives to describe the actual database table 
    # they will be mapped to.
    # We create the base class using the declarative_base().“base”, we can define any number of mapped classes.
    base = declarative_base()
    table= 'FeatureRequestApp'
    # create a configured "Session" class
    Session= sessionmaker(db)

    # Setting Urls for feature request form page and details page
    featureHomePageURL= 'http://127.0.0.1:5000/'
    featureListPageURL= 'http://127.0.0.1:5000/FeatureRequestDetails'


