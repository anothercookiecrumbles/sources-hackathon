import sqlalchemy 
from sqlalchemy.orm import sessionmaker

class DbAdapter:

    engine = None
    session = None

    # always needs a username or password, else it'll go boom. 
    @classmethod
    def init(self, dialect, driver, host, database, username, password):
        if not driver.strip():
            driver = ''
        else:
            driver = '+{}'.format(driver.strip())  # handle awkward syntax here, instead of relying on the client. 
                                            # perhaps it makes sense to have a case statement based on dialect? 
        try:
            if not dialect or not host or not database or not username or not password:
                raise Exception("Dialect, host, database, username, and password are all mandatory parameters.")
            self.engine = sqlalchemy.create_engine("{}{}://{}:{}@{}/{}". \
                                format(dialect, driver, username, password, host, database))
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
        except: # yeah, we should support specific exception types, like login error, but meh. 
            print('unable to initialise the db_adaptor')

    # possible todo: support multiple parallel database connections, and store instances in a dict. 
    @staticmethod
    def get_session():
        if DbAdapter.session:
            return DbAdapter.session
        else:  
            print("DbAdapter not initialised.")
            raise Exception("SQLEngine hasn't been initialised.")

