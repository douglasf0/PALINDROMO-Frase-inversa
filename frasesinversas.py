#lendo palindromos
    #retirando espaços do começo e fim e colocando em maiusculas
frase = str(input('Digite uma frase: ')).strip().upper()
    #separando a frase em palavras
palavras = frase.split()
    #juntando as palavras
juntar = ''.join(palavras)

#Usando FOR
inverso = ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]

'''
#Forma simplificada PYTHON
    #começa no inicio e termina no fim, so que de tras para frente
inverso = juntar[:: -1]
'''

print(f'O inverso de {frase} é {inverso}.')
if juntar == inverso:
    print('Temos um PALIDROMO!')
else:
    print('Não temos um PALIDROMO!')
