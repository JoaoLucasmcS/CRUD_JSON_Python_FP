from utils.json_util import ler_json, escrever_json

CAMINHO_ARQUIVO = 'data/restaurantes.json'

def listar_restaurantes():
    return ler_json(CAMINHO_ARQUIVO)

def criar_restaurante(novo_restaurante):
    restaurantes = ler_json(CAMINHO_ARQUIVO)
    restaurantes.append(novo_restaurante)
    escrever_json(CAMINHO_ARQUIVO, restaurantes) 

def buscar_restaurante_por_nome(nome_restaurante):
    restaurantes = ler_json()
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            return restaurante
    return None        

def atualizar_restaurante (nome, dados_atualizados):
    restaurantes = ler_json(CAMINHO_ARQUIVO)
    for restaurante in restaurantes:
        if (restaurante['nome'].lower() == nome.lower()):
            restaurante.update(dados_atualizados)
            escrever_json(CAMINHO_ARQUIVO, restaurantes) 

def deletar_restaurante(nome):
    restaurantes = ler_json(CAMINHO_ARQUIVO)
    for restaurante in restaurantes:
        if(restaurante['nome'].lower() == nome.lower()):
            restaurante.remove(restaurante)
            escrever_json(CAMINHO_ARQUIVO, restaurantes)                  


