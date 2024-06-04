from services.restaurante_service import (
    listar_restaurantes, buscar_restaurante_por_nome,
    criar_restaurante, atualizar_restaurante,
    deletar_restaurante
)
from services.reserva_service import (
    listar_reservas, buscar_reserva_por_nome,
    criar_reserva, atualizar_reserva,
    deletar_reserva
)

def menu():
    print("Sistema de Reserva de Restaurante")
    print("1. Gerenciar Restaurantes")
    print("2. Gerenciar Reservas")
    print("0. Sair")

def menu_restaurantes():
    print("1. Listar Restaurantes")
    print("2. Adicionar Restaurante")
    print("3. Atualizar Restaurante")
    print("4. Deletar Restaurante")
    print("0. Voltar")

def menu_reservas():
    print("1. Listar Reservas")
    print("2. Adicionar Reserva")
    print("3. Atualizar Reserva")
    print("4. Deletar Reserva")
    print("0. Voltar")

def gerenciar_restaurantes():
    while True:
        menu_restaurantes()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            restaurantes = listar_restaurantes()
            for restaurante in restaurantes:
                print(restaurante)
        elif escolha == '2':
            nome = input("Nome: ")
            cozinha = input("Cozinha: ")
            horario_funcionamento = input("Horário de Funcionamento: ")
            novo_restaurante = {
                "nome": nome,
                "cozinha": cozinha,
                "horario_funcionamento": horario_funcionamento
            }
            criar_restaurante(novo_restaurante)
            print("Restaurante adicionado com sucesso!")
        elif escolha == '3':
            nome_restaurante = input("Nome do Restaurante: ")
            restaurante = buscar_restaurante_por_nome(nome_restaurante)
            if restaurante:
                nome = input(f"Nome ({restaurante['nome']}): ") or restaurante['nome']
                cozinha = input(f"Cozinha ({restaurante['cozinha']}): ") or restaurante['cozinha']
                horario_funcionamento = input(f"Horário de Funcionamento ({restaurante['horario_funcionamento']}): ") or restaurante['horario_funcionamento']
                dados_atualizados = {
                    "nome": nome,
                    "cozinha": cozinha,
                    "horario_funcionamento": horario_funcionamento
                }
                atualizar_restaurante(nome_restaurante, dados_atualizados)
                print("Restaurante atualizado com sucesso!")
            else:
                print("Restaurante não encontrado.")
        elif escolha == '4':
            nome_restaurante = input("Nome do Restaurante: ")
            if deletar_restaurante(nome_restaurante):
                print("Restaurante deletado com sucesso!")
            else:
                print("Restaurante não encontrado.")
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")

def gerenciar_reservas():
    while True:
        menu_reservas()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            reservas = listar_reservas()
            for reserva in reservas:
                print(reserva)
        elif escolha == '2':
            nome_restaurante = input("Nome do Restaurante: ")
            data = input("Data (AAAA-MM-DD): ")
            horario = input("Horário (HH:MM): ")
            numero_pessoas = input("Número de Pessoas: ")
            nova_reserva = {
                "nome_restaurante": nome_restaurante,
                "data": data,
                "horario": horario,
                "numero_pessoas": numero_pessoas
            }
            criar_reserva(nova_reserva)
            print("Reserva adicionada com sucesso!")
        elif escolha == '3':
            nome_restaurante = input("Nome do Restaurante: ")
            data = input("Data (AAAA-MM-DD): ")
            reserva = buscar_reserva_por_nome(nome_restaurante, data)
            if reserva:
                horario = input(f"Horário ({reserva['horario']}): ") or reserva['horario']
                numero_pessoas = input(f"Número de Pessoas ({reserva['numero_pessoas']}): ") or reserva['numero_pessoas']
                dados_atualizados = {
                    "data": data,
                    "horario": horario,
                    "numero_pessoas": numero_pessoas
                }
                atualizar_reserva(nome_restaurante, data, dados_atualizados)
                print("Reserva atualizada com sucesso!")
            else:
                print("Reserva não encontrada.")
        elif escolha == '4':
            nome_restaurante = input("Nome do Restaurante: ")
            data = input("Data (AAAA-MM-DD): ")
            if deletar_reserva(nome_restaurante, data):
                print("Reserva deletada com sucesso!")
            else:
                print("Reserva não encontrada.")
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            gerenciar_restaurantes()
        elif escolha == '2':
            gerenciar_reservas()
        elif escolha == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
