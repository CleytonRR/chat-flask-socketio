from sqlalchemy import Column, Integer, String
from config import dbconfig
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
connection = dbconfig.connection()
Base.query = connection.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True, nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(40), nullable=False)

    def __repr__(self):
        return 'User: {}'.format(self.name)

    def save(self):
        try:
            connection.add(self)
            connection.commit()
        except:
            connection.rollback()
            raise

if __name__ == '__main__':
    dbconfig.createTables(Base)
