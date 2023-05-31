#Crie um programa que lê uma quantidade qualquer de números positivos e encerra quando um número negativo é digitado. Como resultado, ele apresenta o maior e o menor deles, a média e a mediana desses números.#

lista = []
soma = 0 

while True:
    numeros = int(input("Insira um número: "))
    if(numeros<0):
        break
    lista.append(numeros)
maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)
tamanho = len(lista)
if(tamanho % 2 == 0):
    mediana = (lista[tamanho // 2-1]+lista[tamanho //2])/2
else:
    mediana = lista[tamanho // 2]

print("O maior número é o:", maior)
print("O menor número é o:", menor)
print("O valor da média é de:", media)
print("A mediana número é:", mediana)
