

lista_nomes = ['agosto', 'pedro', 'paulo']

nome1, nome2, nome3 = lista_nomes

print(nome2)

nome1, nome2, nome3 = ['agosto', 'lucas', 'paulo']

print(nome2)
''' para um unico valor e o resto da lista: '''

lista_nomes = ['agosto', 'lucas', 'paulo']

nome1, *_ = lista_nomes

print(nome1)
