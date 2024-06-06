from utils.json_util import carregar_arquivo, salvar_arquivo
from utils.email_util import enviar_email
from utils.colors import Cor
from datetime import datetime, timedelta
from prettytable import PrettyTable
from config.settings import ARQUIVO_RESERVAS

def adicionar_reserva(nome, cpf, data, horario, pessoasPorMesa, restaurante, email):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    nova_reserva = {'nome': nome, 'cpf': cpf, 'pessoasPorMesa': pessoasPorMesa, 'data': data, 'horario': horario, 'restaurante': restaurante, 'email': email}
    reservas.append(nova_reserva)

    salvar_arquivo(ARQUIVO_RESERVAS, reservas)

    print(f"{Cor.VERDE}😎 RESERVA ADICIONADA COM SUCESSO!{Cor.RESET}")

    assunto = "Confirmação de Reserva"
    corpo = f"Olá {nome},\n\nSua reserva foi confirmada para o dia {data} às {horario} no restaurante {restaurante}.\n\nObrigado!"
    enviar_email(email, assunto, corpo)

def atualizar_reserva(cpf, nova_data, novo_horario, pessoasPorMesa):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)
    reserva_encontrada = False

    for reserva in reservas:
        if reserva['cpf'] == cpf:
            reserva['data'] = nova_data
            reserva['horario'] = novo_horario
            reserva['pessoasPorMesa'] = pessoasPorMesa
            reserva_encontrada = True
            break

    if reserva_encontrada:
        salvar_arquivo(ARQUIVO_RESERVAS, reservas)
        print(f"{Cor.VERDE}😙 RESERVA ATUALIZADA COM SUCESSO!{Cor.RESET}")
    else:
        print(f"{Cor.VERMELHO}😒 RESERVA NÃO ENCONTRADA.{Cor.RESET}")

def excluir_reserva(cpf, data, restaurante):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)
    reserva_encontrada = False
    
    for reserva in reservas:
        if ((reserva['cpf'] == cpf and reserva['data'] == data) and reserva['restaurante'] == restaurante):
            reservas.remove(reserva)
            salvar_arquivo(ARQUIVO_RESERVAS, reservas)  
            print(f"{Cor.VERDE}😡 RESERVA EXCLUÍDA COM SUCESSO!{Cor.RESET}")
            reserva_encontrada = True
            
    if not reserva_encontrada:
        print(f"{Cor.VERMELHO}😒 RESERVA NÃO ENCONTRADA.{Cor.RESET}")
    
def buscar_reserva(cpf):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    encontrado = False
    
    tabela = PrettyTable(['Nome', 'CPF', 'pessoasPorMesa', 'Data', 'Horário', 'Restaurante', 'Email'])
    
    for reserva in reservas:
        if (reserva['cpf'] == cpf):
            tabela.add_row([reserva['nome'], reserva['cpf'], reserva['pessoasPorMesa'], reserva['data'], reserva['horario'], reserva['restaurante'], reserva['email']])
            encontrado = True
    print(tabela)
    
    if not encontrado:
        print(f"{Cor.VERMELHO}😒 NENHUMA RESERVA CADASTRADA.{Cor.RESET}")

def listar_reservas():
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    if reservas:
        print("LISTA DE RESERVAS:")
        tabela = PrettyTable(['Nome', 'CPF', 'pessoasPorMesa', 'Data', 'Horário', 'Restaurante', 'Email'])
        for reserva in reservas:
            tabela.add_row([reserva['nome'], reserva['cpf'], reserva['pessoasPorMesa'], reserva['data'], reserva['horario'], reserva['restaurante'], reserva['email']])
        print(tabela)
    else:
        print("😒 NENHUMA RESERVA ENCONTRADA.")

def enviar_lembrete():
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    agora = datetime.now()
    para_lembrete = agora + timedelta(days=1)

    for reserva in reservas:
        data_reserva = datetime.strptime(reserva['data'], "%d/%m/%Y")
        if data_reserva.date() == para_lembrete.date():
            assunto = "Lembrete de Reserva"
            corpo = f"Olá {reserva['nome']},\n\nLembramos que você tem uma reserva para amanhã, dia {reserva['data']} às {reserva['horario']} no restaurante {reserva['restaurante']}.\n\nObrigado!"
            enviar_email(reserva['email'], assunto, corpo)
