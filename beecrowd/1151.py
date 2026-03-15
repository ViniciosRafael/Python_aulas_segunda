'''beecrowd | 1151
Fibonacci Fácil
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.'''

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    # primeiros n-1 numeros
    serie = fibonacci(n -1)

    #calcula o proximo numero somando os dois ultimos
    proximo_numero = serie[-1] + serie[-2]

    # adiciona o novo numero a serie
    serie.append(proximo_numero)
    return serie

def main():
    print("Digite o número de termos da série de Fibonacci:")
    n = int(input())
    resultado = fibonacci(n)
    print(resultado)

if __name__ == "__main__":    main()
