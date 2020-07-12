from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine('postgresql+pg8000://{}:{}@localhost:5433/chat'.format(os.getenv("DB_USER"),
                                                                              os.getenv("DB_PASSWORD")),
                       convert_unicode=True)

def connection():
    return scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

def createTables(Base):
    Base.metadata.create_all(bind=engine)


