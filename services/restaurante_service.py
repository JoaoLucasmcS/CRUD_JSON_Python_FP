from utils.json_util import ler_json, escrever_json

CAMINHO_ARQUIVO = 'data/restaurantes.json'

def listar_restaurantes():
    return ler_json(CAMINHO_ARQUIVO)


