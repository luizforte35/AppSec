from src.database import conectar


from .database import conectar

def excluir_senha(id_senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM senhas WHERE id = ?",
        (id_senha,)
    )

    registros_afetados = cursor.rowcount

    conexao.commit()
    conexao.close()

    return registros_afetados
