# Somatório de 1/n, onde o n varie de 1 até 100.

def soma_n (n):
    soma=0
    if 0 < n <= 100:
        for i in range(1,n+1):
            soma = soma + (1/i)
            i = i - 1
        print (soma)
    else:
        print("Apenas valores de 1 a 100.")
        soma_n(int(input('n= ')))
        
soma_n(int(input('n= ')))
