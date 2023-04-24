
from random import *

#esta funcao sorteia os numeros sem repetir
def g(n):
    return sample(range(1,n+1),n)


#cria a matriz fake (ou qualquer outra matriz "normal")
def matrizfake(valor):
    matrizfake = []

    for i in range(valor):
        linha = []
        for l in range(valor):
            linha.append('x')
        matrizfake.append(linha)
    return matrizfake

#joga os valores sorteados nas suas respectivas seções
def ger(n,f): 
    secao = []
    simple = g(n)
    for i in range(f):
        linha = [] 
        for j in range(f):
            linha.append(simple.pop())
        secao.append(linha)
    return secao

#faz a soma das linhas
def linhas(cont,n,matrizf,n2):
    pontuacao = 0

    if 'x' in matrizf[n]:
            ()               
    else:
        if cont == 0:
            pontuacao += matrizf[n][n2]
    return pontuacao

#faz a soma das colunas
def colunas(n,cont,matriz,n2):
    pontuacao = 0
    lista = []
    for y in range(n2):
        lista.append(matriz[y][n])
    if 'x' in lista:
        lista = []
    else:
        if cont == 0:
            pontuacao += matriz[n2][n]
    return pontuacao

#mostra a matriz fake
cont2 = 0
def mostrarfake(matriz,n,n2,n3):
    
    print()
    cont2 = 0

    for m in range (n+1): #printando a matriz fake
        cont = 0
        for k in range(n+1):
            print (f'{matriz[m][k]:^6}', end ='')
            cont += 1
            if cont != [0,1] and cont % n2 == 0:
                print('|', end ='')
        print ()
        cont2 +=1
        if cont2 == n2:
            print('-'*n3)
            cont2 = 0

#recebe os valores que serão revelados
def verificando_valores(jogador,txt,n):
    while True:
                
        try:

            numero = int(input(f'Escolha o numero a ser revelado, {jogador} {txt}: '))
            secao = int(input(f'Escolha a seção, {jogador} {txt}: '))

            if 0 < secao <= n and 0 < numero <= n:
                break 
            else:
                print('\nValor inválido! Escolha a seção e número novamente!')

        except:
            print('\nDigite um número inteiro!')

    return numero,secao

#verifica se o valor ja foi revelado
def n_repetir(numero,secao,lista,jogador,n,n2,txt):
        
    try:
        while numero in lista and secao == n:
            print('\nValor ja revelado! Tente novamente!')
            print()
            numero,secao = verificando_valores(jogador,txt,n2)
    except:
        ()    
    return numero,secao
