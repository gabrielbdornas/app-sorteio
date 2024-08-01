from sorteio import sorteio

nomes = input('Quais nomes gostaria de incluir no sorteio (informe separando por virgula): ')
sorteado = sorteio(nomes.split(','))
print(sorteado)
