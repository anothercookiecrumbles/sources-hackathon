from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, Sequence, String, Time
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from db_adapter import DbAdapter

Base = declarative_base()

class Security(Base):
    __tablename__ = 'security_features'

    id = Column(Integer, primary_key=True) 
    name = Column(String)
    url = Column(String)
    ssl = Column(String)
    security_entity_id = Column(Integer)
    issued_by = Column(String)
    issued_to = Column(String)
    
    def __init__(self, name, url, ssl, security_entity_id,issued_by,issued_to):
        self.name = name
        self.url = url
        self.ssl = ssl
        self.security_entity_id = security_entity_id
        self.issued_by = issued_by
        self.issued_to = issued_to

    def insert(self):
        DbAdapter.get_session().add(self)
        DbAdapter.get_session().commit()
        print('hereto')
        try:    
            return self.id
        except IntegrityError:
            DbAdapter.get_session().rollback()

