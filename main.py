import schedule
from time import sleep
from services.reserva_service import (
    adicionar_reserva, atualizar_reserva, excluir_reserva,
    buscar_reserva, listar_reservas, enviar_lembrete
)
from services.restaurante_service import (
    listar_restaurantes, adicionar_restaurante, atualizar_restaurante, excluir_restaurante
)
from utils.validators import obter_input, validar_data, validar_horario, validar_email, validar_cpf
from utils.colors import Cor 
import os

def menu_inicial():
    print(Cor.CIANO + "=" * 55 + Cor.RESET)
    print(Cor.VERMELHO + " ---->>> BEM VINDO AO RESERVA JÁ <<<---- ")
    print("          1 - GERENCIAR RESERVAS ")
    print("          2 - GERENCIAR RESTAURANTES ")
    print("          3 - SAIR ")
    print(Cor.CIANO + "=" * 55 + Cor.RESET)

def exibir_menu_reservas():
    print("\nMENU:")
    print("1. ADICIONAR RESERVA")
    print("2. ATUALIZAR RESERVA")
    print("3. EXCLUIR RESERVA")
    print("4. LISTAR UMA RESERVA")
    print("5. LISTAR TODAS AS RESERVAS")
    print("6. VOLTAR AO MENU ANTERIOR")

def exibir_menu_restaurantes():
    print("\nMENU:")
    print("1. ADICIONAR RESTAURANTE")
    print("2. LISTAR RESTAURANTES")
    print("3. ATUALIZAR RESTAURANTE")
    print("4. EXCLUIR RESTAURANTE")
    print("5. VOLTAR AO MENU ANTERIOR")

def main():
    schedule.every().day.at("08:00").do(enviar_lembrete)
    
    while True:
        schedule.run_pending()
        menu_inicial()
        try:
            opcao_inicial = int(input("INFORME UMA OPÇÃO: "))
        except ValueError:
            print(f"{Cor.VERMELHO}😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!{Cor.RESET}")
            continue

        if opcao_inicial == 1:
            while True:
                exibir_menu_reservas()
                opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                if opcao == "1":
                    print("Mostrando todos os nossos restaurantes...\n")
                    sleep(2)
                    listar_restaurantes()
                    restaurante = input("DIGITE O NOME DO RESTAURANTE ESCOLHIDO:\n>>>").upper()
                    nome = input(" DIGITE O SEU NOME COMPLETO:\n>>>").upper()
                    cpf = obter_input(validar_cpf, " DIGITE O SEU CPF:\n>>>", "CPF invalido!!")
                    data = obter_input(validar_data, " DIGITE A DATA (DD/MM/AAAA):\n>>>", "Data inválida! Use o formato DD/MM/AAAA.")
                    horario = obter_input(validar_horario, " DIGITE O HORÁRIO (HH:MM):\n>>>", "Horário inválido! Use o formato HH:MM.")
                    pessoasPorMesa = int(input("DIGITE A QUANTIDADE DE PESSOAS POR MESA:\n>>>"))
                    email = obter_input(validar_email, "DIGITE SEU EMAIL:\n>>>", "Email inválido!")
                    adicionar_reserva(nome, cpf, data, horario, pessoasPorMesa, restaurante, email)
                elif opcao == "2":
                    cpf = obter_input(validar_cpf, " DIGITE O SEU CPF:\n>>>", "CPF invalido!!")
                    nova_data = obter_input(validar_data, "DIGITE A NOVA DATA (DD/MM/AAAA):\n>>>", "Data inválida! Use o formato DD/MM/AAAA.")
                    novo_horario = obter_input(validar_horario, "DIGITE O NOVO HORÁRIO (HH:MM):\n>>>", "Horário inválido! Use o formato HH:MM.")
                    pessoasPorMesa = int(input("DIGITE A NOVA QUANTIDADE DE PESSOAS POR MESA: "))
                    atualizar_reserva(cpf, nova_data, novo_horario, pessoasPorMesa)
                elif opcao == "3":
                    cpf = input("DIGITE O CPF QUE CONSTA NA RESERVA A SER EXCLUÍDA:\n>>>").upper()
                    data = obter_input(validar_data, "DIGITE A DATA QUE CONSTA NA RESERVA A SER EXCLUÍDA (DD/MM/AAAA):\n>>>", "Data inválida! Use o formato DD/MM/AAAA.")
                    restaurante = input("DIGITE O NOME DO RESTAURANTE QUE CONSTA NA RESERVA A SER EXCLUÍDA:\n>>>").upper()
                    excluir_reserva(cpf, data, restaurante)
                elif opcao == "4":
                    cpf = input("DIGITE O CPF QUE CONSTA NA RESERVA:\n>>>")
                    buscar_reserva(cpf)
                elif opcao == '5':
                    listar_reservas()
                elif opcao == "6":
                    print("VOLTAR AO MENU ANTERIOR...")
                    sleep(3)
                    break
                else:
                    print(f"{Cor.VERMELHO}😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!{Cor.RESET}")
        elif opcao_inicial == 2:
            while True:
                exibir_menu_restaurantes()
                opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                if opcao == "1":
                    nome = input(" DIGITE O NOME DO RESTAURANTE: \n>>>")
                    cozinha = input(" DIGITE O TIPO DE COZINHA: \n>>>")                  
                    horario = input(" DIGITE O HORÁRIO DE FUNCIONAMENTO:\n>>>")
                    avaliacao = input(" DIGITE A AVALIACAO DO RESTAURANTE: \n>>>")
                    adicionar_restaurante(nome, cozinha, horario, avaliacao)
                elif opcao == "2":
                    listar_restaurantes()
                elif opcao == "3":
                    nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
                    novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                    nova_cozinha = input("DIGITE O NOVO TIPO DE COZINHA: ")
                    novo_horario = input("DIGITE O NOVO HORÁRIO DE FUNCIONAMENTO:\n>>>")
                    nova_avaliacao = input("DIGITE A NOVA AVALIAÇÃO DO RESTAURANTE: ")
                    atualizar_restaurante(nome_antigo, novo_nome, nova_cozinha, novo_horario, nova_avaliacao)
                elif opcao == "4":
                    nome = input("DIGITE O NOME DO RESTAURANTE A SER EXCLUÍDO:\n>>>")
                    excluir_restaurante(nome)          
                elif opcao == "5":
                    print("VOLTAR AO MENU ANTERIOR...")
                    sleep(3)
                    break
                else:
                    print(f"{Cor.VERMELHO}😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!{Cor.RESET}")
            
        elif opcao_inicial == 3:
            print("🚀 SAINDO...")
            sleep(3)
            break
        else:
            print(f"{Cor.VERMELHO}😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!{Cor.RESET}")

if __name__ == "__main__":
    main()
