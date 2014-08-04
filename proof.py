# -*- coding: utf-8 -*-

import sqlalchemy
sqlalchemy.__version__

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

engine.execute("select 1").scalar()


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User ('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

User.__table__

User.__mapper__

Base.metadata.create_all(engine)


ed_user = User('ed', 'Ed Jones', 'edspassword')
ed_user.name

ed_user.fullname

ed_user.password

str(ed_user.id)

print ed_user.__repr__()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print our_user

ed_user is our_user

session.add_all([
    User('wendy', 'Wendy Williams', 'foobar'),
    User('ger', 'German Roccasalva', 'pencoso'),
    User('nati', 'Natalia Daldi', 'blah')])

ed_user.password = 'lapenca'

session.dirty

session.new

session.commit()


