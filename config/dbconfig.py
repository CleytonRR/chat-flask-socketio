from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+pg8000://postgres:docker@localhost:5433/chat', convert_unicode=True)

def connection():
    return scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

def createTables(Base):
    Base.metadata.create_all(bind=engine)


