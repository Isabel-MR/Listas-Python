#Faça um programa que lê uma quantidade qualquer de frases, mostrando o tamanho delas após a digitação, e encerrando quando uma frase vazia é digitada. Ao final, repita a maior frase na tela.#

lista = []

while True:
    frase = input("Insira uma frase: ")
    if(frase == ""):
        break
    tamanho=len(frase)
    print(tamanho)
    lista.append(frase)
maior = max(lista)
    
print("A maior frase é: ", maior)