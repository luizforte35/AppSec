from src.database import conectar


def salva_senha(servico, secure_pass):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
    "INSERT INTO senhas (servico, senha) VALUES (?, ?)",
    (servico, secure_pass)
)

    conexao.commit()
    conexao.close()
