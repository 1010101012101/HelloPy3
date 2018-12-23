import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    addresses = relationship("Address", back_populates='user',cascade='all, delete, delete-orphan')

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


engine = sqlalchemy.create_engine('sqlite:///:memory:', echo= True)
Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)

session = Session()

jack = User(name='jack', fullname='Jack Bean', password='giffdd')
jack.addresses = [
    Address(email_address='jack@google.com'),
    Address(email_address='j25@yahoo.com')
]
session.add(jack)
session.commit()


#jack = session.query(User).filter_by(name='jack').one()
#print("jack:",jack)
#print("jack.address:", jack.addresses)

from sqlalchemy.orm import subqueryload
jack = session.query(User).\
                        options(subqueryload(User.addresses)).\
                        filter_by(name='jack').one()

from sqlalchemy.orm import joinedload
jack = session.query(User).\
                        options(joinedload(User.addresses)).\
                         filter_by(name='jack').one()