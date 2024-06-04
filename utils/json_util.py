import json

def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def escrever_json(caminho_arquivo, dados):
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
