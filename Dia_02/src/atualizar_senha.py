
from .database import conectar

def atualizar_senha(id_senha, nova_senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE senhas SET senha = ? WHERE id = ?",
        (nova_senha, id_senha)
    )

    registros_afetados = cursor.rowcount

    conexao.commit()
    conexao.close()

    return registros_afetados
