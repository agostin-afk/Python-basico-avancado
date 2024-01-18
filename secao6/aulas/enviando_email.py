import os
import pathlib
from dotenv import load_dotenv



load_dotenv()

CAMINHO_HTML = pathlib.Path(__file__).parent / 'mensagem.html' 
print(CAMINHO_HTML)

remetente = os.getenv('FROM_EMAIL', '')
password = os.getenv('FROM_PASSWORD', '')

destinatario = remetente

smtp_server = os.getenv('smtp_server', '')
smtp_port = os.getenv('smtp_port', '')
smtp_username = os.getenv('smtp_username', '')
smtp_password = os.getenv('smtp_password', '')

with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
