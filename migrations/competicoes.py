
import sqlite3

# Abre a conexão
connection_obj = sqlite3.connect('competicoes.db')

connection = connection_obj.cursor()

connection.execute("DROP TABLE IF EXISTS COMPETICOES")

competicoes_table = """CREATE TABLE competicoes (
            id INTEGER PRIMARY KEY,
            titulo VARCHAR(99) NOT NULL,
            data_fim TEXT NULL
        )"""

pontuacoes_table = """CREATE TABLE pontuacoes (
            id INTEGER PRIMARY KEY,
            competicao_id INTEGER NOT NULL,
            atleta VARCHAR(99) NOT NULL,
            valor DECIMAL(2,3) NOT NULL,
            unidade VARCHAR(1) NOT NULL
        )"""

connection.execute(competicoes_table)
connection.execute(pontuacoes_table)

print("Tabelas criadas com sucesso.")

# Fecha a conexão
connection_obj.close()
