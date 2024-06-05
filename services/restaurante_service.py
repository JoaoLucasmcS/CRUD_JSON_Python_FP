from utils.json_util import (
    carregar_arquivo, salvar_arquivo
)
from prettytable import PrettyTable
from config.settings import ARQUIVO_RESTAURANTES
from utils.colors import Cor
import os

def listar_restaurantes():
    restaurantes = carregar_arquivo(ARQUIVO_RESTAURANTES)

    if restaurantes:
        print("=" * 50)
        print("LISTA DE RESTAURANTES:")
        print("-" * 50)
        tabela = PrettyTable(['Nome', 'Cozinha', 'Horário', 'Avaliação'])
        for restaurante in restaurantes:
            tabela.add_row([restaurante['nome'], restaurante['cozinha'], restaurante['horario'], restaurante['avaliacao']])
        print(tabela)
    else:
        print("😒 NENHUM RESTAURANTE ENCONTRADO.")

def adicionar_restaurante(nome, cozinha, horario, avaliacao):
    restaurantes = carregar_arquivo(ARQUIVO_RESTAURANTES)

    novo_restaurante = {'nome': nome, 'cozinha': cozinha, 'horario': horario, 'avaliacao': avaliacao}
    restaurantes.append(novo_restaurante)

    salvar_arquivo(ARQUIVO_RESTAURANTES, restaurantes)

    print(f"{Cor.VERDE}😎 RESTAURANTE ADICIONADO COM SUCESSO!{Cor.RESET}")


def atualizar_restaurante(nome_antigo, novo_nome, nova_cozinha, novo_horario, nova_avaliacao):
    restaurantes = carregar_arquivo(ARQUIVO_RESTAURANTES)

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_antigo:
            restaurante['nome'] = novo_nome
            restaurante['cozinha'] = nova_cozinha
            restaurante['horario'] = novo_horario
            restaurante['avaliacao'] = nova_avaliacao
           
            salvar_arquivo(ARQUIVO_RESTAURANTES, restaurantes)
            print(f"{Cor.VERDE}😙 RESTAURANTE ATUALIZADO COM SUCESSO!{Cor.RESET}")
            return

    print(f"{Cor.VERMELHO}😒 RESTAURANTE NÃO ENCONTRADO.{Cor.RESET}")

def excluir_restaurante(nome):
    restaurantes = carregar_arquivo(ARQUIVO_RESTAURANTES)

    restaurantes = [restaurante for restaurante in restaurantes if restaurante['nome'] != nome]

    salvar_arquivo(ARQUIVO_RESTAURANTES, restaurantes)
    print(f"{Cor.VERDE}😡 RESTAURANTE EXCLUÍDO COM SUCESSO!{Cor.RESET}")
