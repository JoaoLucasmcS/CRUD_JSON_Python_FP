from time import sleep
from utils.colors import Cor

def enviar_email(destinatario, assunto, corpo):
    print(f"{Cor.CIANO}Enviando email de confirmação para {destinatario}...{Cor.RESET}")
    print(f"Assunto: {assunto}")
    print(f"Corpo:\n{corpo}")
    sleep(2)
    print(f"{Cor.VERDE}Email de confirmação enviado com sucesso!{Cor.RESET}")
