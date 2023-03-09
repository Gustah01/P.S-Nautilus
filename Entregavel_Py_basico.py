### Questão 01:
### Média de um aluno

nota1 = input('Digite sua primeira nota: ')
nota2 = input('Digite sua segunda nota: ')
nota3 = input('Digite sua terceira nota: ')

media = ((float(nota1) + float(nota2) + float(nota3)) / 3)

if media >= 7.0:
    print('Aprovado') 
else:
    print('Reprovado')


### Questão 02:
### Média de 10 alunos

lista_nota1 = [10, 4.5, 7, 2.4, 6, 9.8, 1.3, 5, 8, 0]
lista_nota2 = [4, 5.5, 4.8, 6, 3, 7.2, 9, 1, 2.4, 10]
lista_nota3 = [0.4, 7, 10, 10, 5.4, 4, 6.9, 9.1, 10, 10]

for i in range(len(lista_nota1)):
    total = lista_nota1[i] + lista_nota2[i] + lista_nota3[i]
    media = (total) / 3
    if media >= 7.0:
        print('Aprovado')
    else:
        print('Reprovado')


### Questão 03:
### 1000 primeiros pares e ímpares

lista_mil = list(range(0,1000))
lista_par = list()
lista_impar = list()

for i in lista_mil:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(lista_par, lista_impar,sep='\n')


### Questão 04:
### Soma dos números primos

def primo(x):
    
    if x < 2:
        return False

    for i in range(2,x):
        if x % i == 0:
            return False
    return True

soma = 0
for i in range(0,1000):
    if primo(i) == True:
        soma += i
print(soma)