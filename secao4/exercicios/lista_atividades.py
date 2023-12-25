# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
""" from os import system

def listar(tarefas):
    if not tarefas:
        print('\nSem tarefas!')
        return
    print('tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_desfazer):
    if not tarefas:
        print('Não possui nenhuma tarefa para desfazer!')
        return
    tarefa = tarefas.pop()
    tarefas_desfazer.append(tarefa)
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa!')
    tarefas.append(tarefa)
def limpar():
    system('cls')


tarefas = []
tarefas_refazer = []
while True:
    print('comandos: [listar, desfazer, refazer, limpar, sair]')
    comando_atividade = input('Digite o comando ou atividade: ').upper()
    if comando_atividade == 'LIMPAR':
        limpar()
        continue
    elif comando_atividade == 'LISTAR':
        listar(tarefas)
        continue
    elif comando_atividade == 'REFAZER':
        refazer(tarefas, tarefas_refazer)
    elif comando_atividade == 'DESFAZER':
        desfazer(tarefas, tarefas_refazer)
    elif comando_atividade == 'SAIR':
        break
    else:
        adicionar(comando_atividade, tarefas)
        continue
     """
     
     
""" import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
 """

from os import system


tarefas = []
tarefas_refazer = []
def limpar():
    system('cls')

def listar(tarefas):
    if not tarefas:
        print('Você não possui tarefas na lista!!')
        return
    for tarefa in tarefas:
        print(f'{tarefa}\t')
def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Você não possui tarefas para desfazer!!')
        return
    try:
        tarefa = tarefas.pop()
        tarefas_refazer.append(tarefa)
    except:
        ...
def refazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('você não possui tarefas para refazer!!')
        return
    tarefa =  tarefas_refazer.pop()
    tarefas.append(tarefa)
def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('você não digitou uma tarefa')
        return
    tarefas.append(tarefa)
    print(tarefas)
def sair(tarefas):
    print('programa finalizado!!')
    if not tarefas:
        print('você finalizou o programa sem ter atividadeos na lista')
        return True
    print('sua lista final foi: ')
    for tarefa in tarefas:
        print(f'{tarefa}\t')
        return True
    

comandos = {
    'limpar': lambda: limpar(),
    'listar': lambda: listar(tarefas),
    'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
    'refazer': lambda: refazer(tarefas, tarefas_refazer),
    'adicionar': lambda: adicionar(tarefa, tarefas),
    'sair': lambda:  sair(tarefas),
}

while True:
    print('comandos: limpar, listar, desfazer, rafazer, adicionar e sair.')
    tarefa = input('informe uma tarefa ou um comando: ').lower()
    comando = (comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']   
            )
    if comando():
        break
    
'''
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'clear':
    #     os.system('clear')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue
'''
        
 
 
 
 
 