import sqlite3
import logging
import time 

import src.gerar_senha as gerar_senha
import src.salva_senha as salva_senha

from src.buscas import buscar_senha
from src.database import conectar, criar_tabela
from src.buscas import buscar_servicos
from src.atualizar_senha import atualizar_senha
from src.deletar_senha import excluir_senha



criar_tabela()

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    encoding="utf-8"
)

while True:
    print("\n===== SECURE PASSWORD MANAGER =====")
    print("[1] Gerar senha")
    print("[2] Buscar senha pelo ID")
    print("[3] Listar serviços")
    print("[4] Atualizar senha")
    print("[5] Excluir senha")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo do programa...")
        break
    elif opcao == "1":
        servico = input("Digite o nome do serviço: ").strip()

        if not servico:
            print("Serviço inválido.")
            continue

        try:
            length = int(input("Digite o tamanho da senha: "))

            if length < 8 or length > 64:
                print("O tamanho deve estar entre 8 e 64.")
                continue

        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        senha_gerada = gerar_senha.gerar_senhas(length)
        salva_senha.salva_senha(servico, senha_gerada)
        


    elif opcao == "2":
        print("===== BUSCAR SENHA PELO ID =====")
        
        try:    
            id_senha = int(input("Digite o ID da senha: "))  
            
            if id_senha <= 0:
                print("ID inválido.")
                continue
            elif id_senha > 1000:
                print("ID muito grande. Por favor, insira um ID menor que 1000.")
                continue
            elif id_senha != int(id_senha):
                print("ID inválido. Por favor, insira um número inteiro.")
                continue
            else:
                resultado = buscar_senha(id_senha)
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
            
        if resultado is not None:
            print(f"ID: {resultado[0]}")
            print(f"Serviço: {resultado[1]}")
            print(f"Senha: {resultado[2]}")
            print(f"Criado em: {resultado[3]}")
            time.sleep(5)
        else:
            print("Registro não encontrado.")

    elif opcao == "3":
        print("===== LISTAR SERVIÇOS =====")
        try:
            resultados = buscar_servicos()
            logging.info("Serviços consultados com sucesso!.")
            
            if resultados:
                print(f"{'ID':<8}{'Serviço':<25}")
                print("-" * 40)
                for id_senha, servico in resultados:
                    print(f"{id_senha:<8}{servico:<25}")

                print("-" * 40) 
                print(f"Total de registros: {len(resultados)}")
                time.sleep(5)

            else:
                print("Nenhum serviço encontrado.")
        except sqlite3.Error:
            logging.error("Falha ao consultar serviços.")
            print("Não foi possível consultar os serviços.")
    elif opcao == "4":
        print("===== ATUALIZAR SENHA =====")        
        try:    
            id_senha = int(input("Digite o ID da senha: "))  
            if id_senha <= 0 :
                print("ID invalido")
                logging.warning("Tentativa de atualizar registro inexistente.")
                continue         
        except ValueError:
            print("Entre com um ID valido!")
            continue
        
        
        try:
            length = int(input("Digite o tamanho da nova senha: "))

            if length < 8 or length > 64:
                print("Comprimento inválido.")
                continue
            
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
        
        nova_senha = gerar_senha.gerar_senhas(length)

        
        try:
            registros_afetados = atualizar_senha(id_senha, nova_senha)
        
        except sqlite3.Error:
            logging.error("Falha ao atualizar credencial.")
            print("Não foi possível atualizar a senha.")
            continue


                
        if registros_afetados == 1:
            print("Senha atualizada com sucesso!.")
            logging.info("Credencaial atualizada com sucesso.")
            time.sleep(2)
            
        else:
            print("Registro não encontrado!.")
            logging.warning("Tentativa de atualizar registro inexistente.")
        
    
        
    elif opcao == "5":
        print("===== EXCLUIR SENHA =====")

        try:
            id_senha = int(input("Digite o ID da senha: "))

            if id_senha <= 0:
                print("ID inválido.")
                continue

        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        resultado = buscar_senha(id_senha)

        if id_senha is None:
            print("Registro não encontrado.")
            continue

        print(f"Serviço: {resultado[1]}")

        confirmacao = input("Confirmar exclusão? [S/N]: ").strip().lower()

        if confirmacao != "s":
            print("Exclusão cancelada.")
            continue