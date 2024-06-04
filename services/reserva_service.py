from utils.json_util import ler_json, escrever_json
from datetime import datetime, timedelta

CAMINHO_ARQUIVO = 'data/reservas.json'

def listar_reservas():
    return ler_json(CAMINHO_ARQUIVO)

