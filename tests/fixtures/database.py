from unittest.mock import patch

import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text


@pytest.fixture(scope="session", autouse=True)
def create_session():
    engine = create_engine(
        "sqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def mock_boostrap(create_session):
    with patch('src.database.boostrap') as mock_session:
        mock_session.return_value = create_session
        yield mock_session


@pytest.fixture(scope="session", autouse=True)
def setup_db(create_session):
    with create_session() .connection() as con:
        con.execute(text("""CREATE TABLE competicoes (
                id INTEGER PRIMARY KEY,
                titulo VARCHAR(99) NOT NULL,
                data_fim TEXT NULL
            )"""))
        con.execute(text("""CREATE TABLE pontuacoes (
                id INTEGER PRIMARY KEY,
                competicao_id INTEGER NOT NULL,
                atleta VARCHAR(99) NOT NULL,
                valor DECIMAL(2,3) NOT NULL,
                unidade VARCHAR(1) NOT NULL,
                FOREIGN KEY(competicao_id) REFERENCES competicoes(id)
            )"""))
        con.execute(text('INSERT INTO competicoes(titulo) VALUES ("Nado livre - 200 metros"), ("Salto livre")'))
    yield
