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

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


#engine = sqlalchemy.create_engine('sqlite:///aaa.db', echo=True)
engine = sqlalchemy.create_engine('sqlite:///:memory:', echo= True) #用:memory:表示使用临时放入内在的数据库，调试时很方便,echo=True表示打开SQLalchemy日志

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)

session = Session()

# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
#
# session.add(ed_user)
#
# session.commit()


'''建立关系'''


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship("Address", order_by=Address.id, back_populates='user')
#对数据表作了修改，要重新creat_all一下
Base.metadata.create_all(engine)


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

