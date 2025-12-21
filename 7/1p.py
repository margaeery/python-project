from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///1p.db')
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(name="Пушкин")
author2 = Author(name="Толстой")

book1 = Book(title="Евгений Онегин", author_id=1)
book2 = Book(title="Руслан и Людмила", author_id=1)
book3 = Book(title="Война и мир", author_id=2)

session.add_all([author1, author2, book1, book2, book3])
session.commit()

books = session.query(Book).all()
for book in books:
    author = session.get(Author, book.author_id)
    print(book.title, author.name)

session.close()
