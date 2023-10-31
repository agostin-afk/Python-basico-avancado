"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = "agostinho"
palavra_censura = ""
letras_acerto = ""
while True:
    chute = input('Tente acertar uma letra: ').lower()
    if len(chute) > 1:
        print('informe apenas uma letra.')
        continue
    elif len(chute) < 1:
        print('você não informou uma letra, tente novamente.')
        continue
    chute_teste = chute.isalpha()
    if chute_teste:
        pass
    else:
        print("informe uma letra, não numero ou caractere especial.")
        continue
    if chute in palavra_secreta:
        letras_acerto += chute
    palavra_censura = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acerto:
            palavra_censura += letra_secreta
        else:
            palavra_censura += '*'
    print(palavra_censura)

