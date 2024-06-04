from utils.json_util import ler_json, escrever_json

CAMINHO_ARQUIVO = 'data/reservas.json'

def listar_reservas():
    return ler_json(CAMINHO_ARQUIVO)

def criar_reserva(nova_reserva):
    reservas = ler_json(CAMINHO_ARQUIVO)
    reservas.append(nova_reserva)
    escrever_json(CAMINHO_ARQUIVO, reservas)

def buscar_reserva_por_nome(nome_reserva):
    reservas = ler_json()
    for reserva in reservas:
        if reserva['nome'].lower() == nome_reserva:
            return reserva
    return None    

def atualizar_reserva(nome, dados_atualizados):
    reservas = ler_json(CAMINHO_ARQUIVO)
    for reserva in reservas:
        if (reserva['nome'].lower() == nome):
            reserva.update(dados_atualizados)
            escrever_json(CAMINHO_ARQUIVO, reservas)
            return True
    return False    

def deletar_reserva(nome):
    reservas = ler_json(CAMINHO_ARQUIVO)
    for reserva in reservas:
        if(reserva['nome'].lower() == nome):
            reservas.remove(reserva)
            escrever_json(CAMINHO_ARQUIVO, reservas)
            return True
    return False    
