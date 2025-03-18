import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')  # Para Windows
    else:
        _ = system('clear')  # Para Mac ou Linux

# Função que desenha a forca na tela
def display_hangman():
    # Cada índice da lista 'board' representa um estágio do desenho da forca
    board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
    return board  # Retorna a lista com os desenhos da forca

# Classe para o jogo da forca
class Hangman:
    # Método Construtor
    def __init__(self, palavra, tentativas=6):
        self.palavra = palavra  # A palavra a ser adivinhada
        self.palavra_errada = []  # Lista para armazenar as letras erradas
        self.palavra_certa = ['_' for _ in palavra]  # Inicializa as letras descobertas com '_'
        self.attempts = 0  # Contador de tentativas erradas
        self.tentativas = tentativas  # Número máximo de tentativas erradas antes de perder

    # Método para adivinhar a letra
    def adivinhar_letra(self, letra):
        # Verifica se a letra já foi tentada antes
        if letra in self.palavra_certa or letra in self.palavra_errada:
            print("Você já tentou essa letra antes!")
            input("Pressione Enter para continuar...")  # Pausa até o jogador pressionar Enter
            return  # Não faz nada e não conta como tentativa

        # Se a letra estiver na palavra
        if letra in self.palavra:
            # Atualiza a palavra certa com a letra descoberta
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.palavra_certa[i] = letra
        else:
            # Se a letra não estiver na palavra, adiciona na lista de erradas
            self.palavra_errada.append(letra)
            self.attempts += 1  # Incrementa o número de tentativas erradas

    # Método para verificar se o jogo terminou
    def verificar_jogo(self):
        # Se todas as letras foram descobertas, o jogador ganhou
        if '_' not in self.palavra_certa:
            return "Você ganhou!!!"
        # Se o número de tentativas erradas atingiu o limite, o jogador perdeu
        elif self.attempts >= self.tentativas:
            return f"Você perdeu!!! A palavra era: {self.palavra}"
        return ""  # Se o jogo ainda não acabou, retorna uma string vazia

    # Método para exibir o status atual do jogo
    def status_jogo(self):
        # Exibe a palavra com as letras descobertas e o número de tentativas restantes
        print(f"Palavra: {' '.join(self.palavra_certa)}")
        print(f"Letras erradas: {', '.join(self.palavra_errada)}")
        print(f"Tentativas restantes: {self.tentativas - self.attempts}")
        print(display_hangman()[self.attempts])  # Exibe o desenho da forca com base no número de tentativas erradas

# Função principal para jogar
def jogar():
    palavras = ['python', 'java', 'javascript', 'ruby', 'html', 'css']  # Lista de palavras possíveis
    palavra = random.choice(palavras)  # Escolhe uma palavra aleatória da lista
    jogo = Hangman(palavra)  # Cria um novo objeto da classe Hangman com a palavra escolhida

    # Loop principal do jogo
    while True:
        limpa_tela()  # Limpa a tela a cada rodada
        jogo.status_jogo()  # Exibe o status atual do jogo

        letra = input("Digite uma letra: ").lower()  # Solicita uma letra ao jogador e converte para minúscula
        # Verifica se o input é uma letra válida
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida!")
            continue  # Se não for válida, pede para o jogador tentar novamente

        jogo.adivinhar_letra(letra)  # Chama o método para adivinhar a letra
        resultado = jogo.verificar_jogo()  # Verifica o estado do jogo
        if resultado:
            limpa_tela()  # Limpa a tela
            jogo.status_jogo()  # Exibe o status final do jogo
            print(resultado)  # Exibe a mensagem de vitória ou derrota
            break  # Finaliza o jogo

# Inicia o jogo
if __name__ == "__main__":
    jogar()
