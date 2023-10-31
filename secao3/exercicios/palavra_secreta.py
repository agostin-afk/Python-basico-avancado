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
palavra_secreta = "Agostinho"
palavra_censura = ""
while True:
    chute = input('Tente acertar uma letra: ').upper()
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
    try:
       for i in palavra_secreta:
           palavra_censura +="*"
           if chute == palavra_secreta[i].upper():
               palavra_censura[i].replace(chute)
       else:
           print(f'Sua palavra secreta é: {palavra_censura}')
        
    
    except:
        ...

