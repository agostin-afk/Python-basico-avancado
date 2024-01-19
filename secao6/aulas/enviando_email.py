import os
import pathlib
from string_ import MyTemplate
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


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

with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo:
    texto_arquivo = arquivo.read()
    template = MyTemplate(texto_arquivo)
    texto_email = template.substitute(nome ='Agosto', escritor='Agosto')

mime_multpart = MIMEMultipart()
mime_multpart['from'] = remetente
mime_multpart['to'] = destinatario
mime_multpart['subject'] = 'Este é o assunto do Email'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multpart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multpart)
    print('Email enviado')