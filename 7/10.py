from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///10.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

users_data = [
    User(name='Иван', age=25),
    User(name='Мария', age=30),
    User(name='Алексей', age=35)
]

session.add_all(users_data)
session.commit()

for user in session.query(User).all():
    print(user.id, user.name, user.age)

session.close()
