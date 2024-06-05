from utils.json_util import carregar_arquivo, salvar_arquivo
from utils.email_util import enviar_email
from utils.colors import Cor
from datetime import datetime, timedelta
from prettytable import PrettyTable
from config.settings import ARQUIVO_RESERVAS

def adicionar_reserva(nome, data, horario, restaurante, email):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    nova_reserva = {'nome': nome, 'data': data, 'horario': horario, 'restaurante': restaurante, 'email': email}
    reservas.append(nova_reserva)

    salvar_arquivo(ARQUIVO_RESERVAS, reservas)

    print(f"{Cor.VERDE}😎 RESERVA ADICIONADA COM SUCESSO!{Cor.RESET}")

    assunto = "Confirmação de Reserva"
    corpo = f"Olá {nome},\n\nSua reserva foi confirmada para o dia {data} às {horario} no restaurante {restaurante}.\n\nObrigado!"
    enviar_email(email, assunto, corpo)

def atualizar_reserva(nome_antigo, novo_nome, nova_data, novo_horario, novo_restaurante, novo_email):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    for reserva in reservas:
        if reserva['nome'] == nome_antigo:
            reserva['nome'] = novo_nome
            reserva['data'] = nova_data
            reserva['horario'] = novo_horario
            reserva['restaurante'] = novo_restaurante
            reserva['email'] = novo_email
            salvar_arquivo(ARQUIVO_RESERVAS, reservas)
            print(f"{Cor.VERDE}😙 RESERVA ATUALIZADA COM SUCESSO!{Cor.RESET}")
            return

    print(f"{Cor.VERMELHO}😒 RESERVA NÃO ENCONTRADA.{Cor.RESET}")

def excluir_reserva(nome, data, horario, restaurante):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    reservas = [reserva for reserva in reservas if not (
        reserva['nome'] == nome and
        reserva['data'] == data and
        reserva['horario'] == horario and
        reserva['restaurante'] == restaurante
    )]

    salvar_arquivo(ARQUIVO_RESERVAS, reservas)
    print(f"{Cor.VERDE}😡 RESERVA EXCLUÍDA COM SUCESSO!{Cor.RESET}")

def buscar_reserva(nome, data, horario, restaurante):
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    encontrado = False

    for reserva in reservas:
        if (reserva['nome'] == nome and
            reserva['data'] == data and
            reserva['horario'] == horario and
            reserva['restaurante'] == restaurante):
            print(f"NOME: {reserva['nome']}, DATA: {reserva['data']}, HORÁRIO: {reserva['horario']}, RESTAURANTE: {reserva['restaurante']}")
            encontrado = True

    if not encontrado:
        print(f"{Cor.VERMELHO}😒 NENHUMA RESERVA CADASTRADA.{Cor.RESET}")

def listar_reservas():
    reservas = carregar_arquivo(ARQUIVO_RESERVAS)

    if reservas:
        print("=" * 50)
        print("LISTA DE RESERVAS:")
        print("-" * 50)
        tabela = PrettyTable(['Nome', 'Data', 'Horário', 'Restaurante', 'Email'])
        for reserva in reservas:
            tabela.add_row([reserva['nome'], reserva['data'], reserva['horario'], reserva['restaurante'], reserva['email']])
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
