from .database import conectar

def buscar_senha(id_senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT * FROM senhas WHERE id = ?", 
        (id_senha,)
    )
    resultado = cursor.fetchone()
    conexao.close()

    return resultado
        
        
def buscar_servicos():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        "SELECT id, servico FROM senhas"
    )
    resultados = cursor.fetchall()
    conexao.close()

    return resultados
    