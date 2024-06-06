import re
from datetime import datetime
from utils.colors import Cor

def validar_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def validar_data(data):
    try:
        data_reserva = datetime.strptime(data, '%d/%m/%Y')
        if data_reserva.date() >= datetime.now().date():
            return True
        else:
            return False
    except ValueError:
        return False

def validar_cpf(cpf):
    regex = r'^\d{9}$'
    return re.match(regex, cpf)

def validar_horario(horario):
    try:
        datetime.strptime(horario, '%H:%M')
        return True
    except ValueError:
        return False

def obter_input(validacao_func, mensagem, mensagem_erro):
    while True:
        valor = input(mensagem)
        if validacao_func(valor):
            return valor
        else:
            print(f"{Cor.VERMELHO}{mensagem_erro}{Cor.RESET}")
