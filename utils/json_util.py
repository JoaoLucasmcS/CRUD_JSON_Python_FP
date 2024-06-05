import json
import os

def carregar_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        return []

def salvar_arquivo(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)
