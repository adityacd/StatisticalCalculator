from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////web/Sqlite-Data/Movies_Database.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()