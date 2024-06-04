from services.restaurante_service import (criar_restaurante, atualizar_restaurante, listar_restaurantes, deletar_restaurante)
from services.reserva_service import (criar_reserva, listar_reservas, atualizar_reserva, deletar_reserva)

def menu():
    print("Sistema de Reservas de Restaurantes")
    print("1. Gerenciar Restaurante")
    print("2. Gerenciar Reserva")
    print("0. Sair")

def menu_restaurante():
    print("1. Listar Restaurantes")
    print("2. Incluir Restaurante")
    print("3. Atualizar dados de um Restaurante")
    print("4. Deletar Restaurante")
    print("0. Voltar")

def menu_reserva():
    print("1. Listar Reservas")
    print("2. Adicionar Reserva")
    print("3. Atualizar Reserva")
    print("4. Deletar Reserva")
    print("0. Voltar")  

def gerenciar_restaurante ():
    
    restaurante_opcao = int(input("Escolha uma opção: "))
    if(restaurante_opcao == 1):
        listar_restaurantes()
    elif(restaurante_opcao == 2):
        nome_restaurante = input("Nome do restaurante: ")
        cozinha_restaurante = input("Tipo de Cozinha: ")
        horario_func = input("Horário de Funcionamento: ")
        avaliacao = input("Avaliação do Restaurante: ")

        
