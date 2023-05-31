#Faça um programa que peça a quantidade de números. Em seguida, lê os números e apresenta a média e mostre também os números digitados#

qtd = int(input("Insira uma quantidade de números: "))

numeros = []
acc = 0

for i in range(qtd):
    numero = float(input("Digite o número: "))
    numeros.append(numero)
    acc += numero

media = acc / qtd

print("Os números digitados são:", numeros)
print("E o valor da média é de:", media)
