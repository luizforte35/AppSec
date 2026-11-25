import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "senha.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            servico TEXT NOT NULL,
            senha TEXT NOT NULL,
            criado_em TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conexao.commit()
    conexao.close()