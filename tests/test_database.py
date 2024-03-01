import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def db():
   engine = create_engine(
       "sqlite:///:memory:", connect_args={"check_same_thread": False}
   )
   TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base = declarative_base()
   Base.metadata.create_all(bind=engine)
   return TestSession()

@pytest.fixture
def setup_db(session):
    session.execute("""CREATE TABLE competicoes (
            id INTEGER PRIMARY KEY,
            titulo VARCHAR(99) NOT NULL,
            data_fim TEXT NULL
        )""")
    session.execute("""CREATE TABLE pontuacoes (
            id INTEGER PRIMARY KEY,
            competicao_id INTEGER NOT NULL,
            atleta VARCHAR(99) NOT NULL,
            valor DECIMAL(2,3) NOT NULL,
            unidade VARCHAR(1) NOT NULL,
            FOREIGN KEY(competicao_id) REFERENCES competicoes(id)
        )""")
    session.execute('INSERT INTO competicoes VALUES ("Nado livre - 200 metros"), ("Salto livre")')
    session.connection.commit()
