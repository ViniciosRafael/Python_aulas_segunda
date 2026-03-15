'''beecrowd | 1028
Figurinhas
Por Neilor Tonin, URI  Brasil

Timelimit: 1


Ricardo e Vicente são aficionados por figurinhas. Nas horas vagas, eles arrumam um jeito de jogar um “bafo” ou algum outro jogo que envolva tais figurinhas. Ambos também têm o hábito de trocarem as figuras repetidas com seus amigos e certo dia pensaram em uma brincadeira diferente. Chamaram todos os amigos e propuseram o seguinte: com as figurinhas em mãos, cada um tentava fazer uma troca com o amigo que estava mais perto seguindo a seguinte regra: cada um contava quantas figurinhas tinha. Em seguida, eles tinham que dividir as figurinhas de cada um em pilhas do mesmo tamanho, no maior tamanho que fosse possível para ambos. Então, cada um escolhia uma das pilhas de figurinhas do amigo para receber. Por exemplo, se Ricardo e Vicente fossem trocar as figurinhas e tivessem respectivamente 8 e 12 figuras, ambos dividiam todas as suas figuras em pilhas de 4 figuras (Ricardo teria 2 pilhas e Vicente teria 3 pilhas) e ambos escolhiam uma pilha do amigo para receber.
Entrada
A primeira linha da entrada contém um único inteiro N (1 ≤ N ≤ 3000), indicando o número de casos de teste. Cada caso de teste contém 2 inteiros F1 (1 ≤ F1 ≤ 1000) e F2 (1 ≤ F2 ≤ 1000) indicando, respectivamente, a quantidade de figurinhas que Ricardo e Vicente têm para trocar.

Saída
Para cada caso de teste de entrada haverá um valor na saída, representando o tamanho máximo da pilha de figurinhas que poderia ser trocada entre dois jogadores.'''

import math

def mdc(a, b):
    #se o resto for 0, é mds
    if b == 0:
        return a
    else:
        #chama recursivamente, passando o segundo número e o resto da divisão do primeiro pelo segundo
        return mdc(b, a % b)
    
def teste():
    # primeira linha: número de casos de teste
    n = int(input())

    for _ in range(n):
        # lê dois inteiros por linha
        f1, f2 = map(int, input().split())
        # calcula o mdc
        tamanho_max = mdc(f1, f2)
        print(tamanho_max)

if __name__ == "__main__":
    teste()
