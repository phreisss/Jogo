import random
from os import system, name

def limpar_tela():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def game():

    limpar_tela()

    print("Seja bem-vindo ao nosso jogo da forca!")
    print("Adivinhe a palavra abaixo \n")
    palavras = ['banana','uva','morango','abacaxi','laranja']

    palavra = random.choice(palavras)
    lista_forca = ['_' for letra in palavra]

    chances = 6
    respostas_erradas = []

    while chances > 0:
        print(" ".join(lista_forca))
        print("\n Chances descobertas", chances)
        print("Letras erradas: "," ".join(respostas_erradas))
        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    lista_forca[index] = letra
                index += 1 
        else:
            chances -= 1
            respostas_erradas.append(tentativa)
        
        if "_" not in lista_forca:
            print("\n Você venceu, a palavra é ",palavra)
            break

if __name__ == '__main__':
    game()
    
