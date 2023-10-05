# Somatório de (1/n*n), onde o n varie de 1 até 100.

def soma_n2 (n):
    soma=0
    if 0 < n <= 100:
        while n > 0:
            soma = soma + (1/n**2)
            n = n - 1
        print(soma)
    else:
        print("Apenas valores de 1 a 100.")
        soma_n2(int(input('n= ')))
        
soma_n2(int(input('n= ')))
