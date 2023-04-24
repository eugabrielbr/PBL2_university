#Autor: Gabriel Silva dos Santos
#Componente curricular: Algoritmos I
#Concluido em: 14/11/2022
#Declaro que este código foi elaborado somente por mim de forma individual
#sem conter nenhum trecho de código de colega ou de outros autores, tais como
#provindos de de livros e apostilas, páginas ou documentos eletrônicos da
#internet. Qualquer trecho de código de outra autoria que não é minha será desta-
#cada com sua fonte, estando eu, ciente, que estes trechos não serão considerados
#para fins de avaliação.

from random import *
from PBL_2_funcoes import matrizfake,ger,linhas,colunas,mostrarfake,verificando_valores,n_repetir

print('+=' * 50)
print ('                          Bem vindo ao Jogo das Somas 2.0!\n')

#nesta parte do codigo pega o nome dos jogadores, escolhe a fase do jogo e decide quem começa jogando

a = 's'
#nome dos jogadores e escolha de fase
while a == 's': #este loop é reponsável por reiniciar o jogo (ou nao) no final

    jogador1 = input('Insira o nome do Player 1: ')
    jogador2 = input('Insira o nome do Player 2: ')


    while True:
        
        try:

            sorteio1 = int(input(f'\nEscolha um numero de 1 a 10, {jogador1}: '))
            sorteio2 = int(input(f'Escolha um numero de 1 a 10, {jogador2}: '))    
            print('\n1 - 4x4')
            print('2 - 9x9')
            fase = int(input('\nEscolham a fase do jogo: '))
            if 10 >= sorteio1 >= 0 and 10 >= sorteio2 >= 0 and 2 >= fase > 0:
                break
            else:
                print('\nNumero inválido!')

        except:

            print('\nDigite um valor válido!')

    #verificando quem vai começar jogando

    numero_sorteado = randint(1,10)

    diferenca1 = sorteio1 - numero_sorteado
    diferenca2 = sorteio2 - numero_sorteado

    if diferenca1 < 0:
        diferenca1 = diferenca1 * -1
    if diferenca2 < 0:
        diferenca2 = diferenca2 * -1

    print(f'\nNumero sorteado pelo sistema: {numero_sorteado}')

    if diferenca1 < diferenca2:
        print(f'\nO numero mais proximo do sorteado é o de {jogador1}. Ele é o jogador 1 e começa jogando!')
    else:
        print(f'\nO numero mais proximo do sorteado é o de {jogador2}. Ele é o jogador 1 e começa jogando!')

    #nesta parte do codigo acontece todo o jogo 4x4, desde a revelação dos números até as pontuações
    if fase == 1:

        print('+=' * 50)
        print('\nO jogo começou! uma matriz misteriosa foi gerada...')
        print()

        #criando a matriz 4x4

        n = 4
        f = 2
        #gerando as seções
        secao_1 = ger(n,f)
        secao_2 = ger(n,f)
        secao_3 = ger(n,f)
        secao_4 = ger(n,f)
        
        #colocando as 4 seções em uma matriz maior  
        matriz = [[secao_1,secao_2],[secao_3,secao_4]]
        matrizf = matrizfake(n+1) #a matriz fake é criada através de uma função

        for zeros in range(4):
            matrizf[zeros][4] = 0

        valor_bonus = 0

        #nesta parte do codigo, é armazenado as somas na matriz representativa (matriz fake)
        
        for y in range(2):
            #somas de cada linha das 4 seções
            
            for k in matriz[0][y][0]:
                matrizf[0][4]+= k
            for k in matriz[0][y][1]:
                matrizf[1][4] += k
            
            for k in matriz[1][y][0]:
                matrizf[2][4] += k
            for k in matriz[1][y][1]:
                matrizf[3][4] += k

            #somas diagonal principal

            valor_bonus += matriz[0][0][y][y] #k ele é 00 e dps fica 11
            valor_bonus += matriz[1][1][y][y]


            #somas coluna
        for zeross in range(4):
            matrizf[4][zeross] = 0 #aqui é substituidos os x em zeros (para ter uma interação int-int, e nao int-str)
    

        for coluna in range(2):

            matrizf[4][3] += matriz[0][1][coluna][1]
            matrizf[4][3] += matriz[1][1][coluna][1]

            matrizf[4][2] += matriz[0][1][coluna][0]
            matrizf[4][2] += matriz[1][1][coluna][0]
            
            matrizf[4][1] += matriz[0][0][coluna][1]
            matrizf[4][1] += matriz[1][0][coluna][1]

            matrizf[4][0] += matriz[0][0][coluna][0]
            matrizf[4][0] += matriz[1][0][coluna][0]

        #IMPRIMINDO para o usuário dar uma olhada na matriz fake antes de começar a jogar
        mostrarfake(matrizf,4,2,26)

        #jogadas
        contador_de_jogadas4 = 0
        
        cont04 = 0
        cont14 = 0
        cont24 = 0  
        cont34 = 0
        
        cont00 = 0
        cont10 = 0
        cont20 = 0
        cont30 = 0
        cont40 = 0
        contbonus = 0
        
        listabonus = []
        
        pontuacao1 = 0 
        pontuacao2 = 0
        
        lista1 = []
        lista2 = []
        lista3 = []
        lista4 = []

        #inicio do jogo 4x4

        while contador_de_jogadas4 < 16: 
            
            #nesta parte se encontra todos os mecanismos de jogadas para o jogador 1

            print()
            numero1,secao1 = verificando_valores('Jogador 1','[1 - 4]',4)
            
            #função para nao repetir os numeros nas seções
            numero1,secao1 = n_repetir(numero1,secao1,lista1,'Jogador 1',1,4,'[1 - 4]')
            numero1,secao1 = n_repetir(numero1,secao1,lista2,'Jogador 1',2,4,'[1 - 4]')
            numero1,secao1 = n_repetir(numero1,secao1,lista3,'Jogador 1',3,4,'[1 - 4]')
            numero1,secao1 = n_repetir(numero1,secao1,lista4,'Jogador 1',4,4,'[1 - 4]')

            #revelando os valores das seções
            if secao1 == 1:
                
                for i in range(2):
                    for y in range(2):
                        if numero1 == matriz[0][0][i][y] and secao1 == 1:
                            lista1.append(numero1)
                            matrizf[i][y] = matriz[0][0][i][y]                  
            elif secao1 == 2:
      
                for i in range(2):
                    for y in range(2):
                        if numero1 == matriz[0][1][i][y] and secao1 == 2:
                            matrizf[i][y+2] = matriz[0][1][i][y]
                            lista2.append(numero1)                          
            elif secao1 == 3:
             
                for i in range(2):
                    for y in range(2):
                        if numero1 == matriz[1][0][i][y] and secao1 == 3:
                            matrizf[i+2][y] = matriz[1][0][i][y]
                            lista3.append(numero1)          
            elif secao1 == 4:

                for i in range(2):
                    for y in range(2):
                        if numero1 == matriz[1][1][i][y] and secao1 == 4:
                            matrizf[i+2][y+2] = matriz[1][1][i][y]
                            lista4.append(numero1)
                           
            #pontuação das linhas 

            pontuacao1 += linhas(cont04,0,matrizf,4)
            if linhas(cont04,0,matrizf,4) != 0:
                cont04=1
            pontuacao1 += linhas(cont14,1,matrizf,4)
            if linhas(cont14,1,matrizf,4) != 0:
                cont14=1
            pontuacao1 += linhas(cont24,2,matrizf,4)
            if linhas(cont24,2,matrizf,4) != 0:
                cont24=1
            pontuacao1 += linhas(cont34,3,matrizf,4)
            if linhas(cont34,3,matrizf,4) != 0:
                cont34=1
            
            #pontuação cada coluna 
            
            pontuacao1 += colunas(0,cont00,matrizf,4)
            if colunas(0,cont00,matrizf,4) != 0:
                cont00 = 1 
            pontuacao1 += colunas(1,cont10,matrizf,4)
            if colunas(1,cont10,matrizf,4) != 0:
                cont10 = 1
            pontuacao1 += colunas(2,cont20,matrizf,4)
            if colunas(2,cont20,matrizf,4) != 0:
                cont20 = 1
            pontuacao1 += colunas(3,cont30,matrizf,4)
            if colunas(3,cont30,matrizf,4) != 0:
                cont30 = 1
            
            #pontuacao bonus

            for j in range(4):
                listabonus.append(matrizf[j][j])
            if 'x' in listabonus:
                listabonus = []
            else:
                if contbonus == 0:
                    pontuacao1 += valor_bonus
                    matrizf[4][4] = valor_bonus
                    contbonus = 1
                    print('\nO jogador 1 encontrou o valor escondido!')
            
            mostrarfake(matrizf,4,2,26) #mostrando a matriz fake logo após o jogador 1 jogar     
            
            print()
            print('Pontuação de cada jogador') #mostrando, em tempo real, a pontuação de cada jogador 
            print(f'Jogador 1: {pontuacao1} \nJogador 2: {pontuacao2}') 
            
            #nesta parte se encontra todos os mecanismos de jogadas para o jogador 2
            print()
            numero2,secao2 = verificando_valores('Jogador 2','[1 - 4]',4) #aqui, o jogador insere o numero&seção que quer revelar
            
            #função para nao repetir os numeros nas seções
            numero2,secao2 = n_repetir(numero2,secao2,lista1,'Jogador 2',1,4,'[1 - 4]')
            numero2,secao2 = n_repetir(numero2,secao2,lista2,'Jogador 2',2,4,'[1 - 4]')
            numero2,secao2 = n_repetir(numero2,secao2,lista3,'Jogador 2',3,4,'[1 - 4]')
            numero2,secao2 = n_repetir(numero2,secao2,lista4,'Jogador 2',4,4,'[1 - 4]')

            #revelando os valores das seções
            if secao2 == 1:
        
                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz[0][0][i][y] and secao2 == 1:
                            matrizf[i][y] = matriz[0][0][i][y]
                            lista1.append(numero2)                        
            elif secao2 == 2:
                
                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz[0][1][i][y] and secao2 == 2:
                            matrizf[i][y+2] = matriz[0][1][i][y]
                            lista2.append(numero2)                        
            elif secao2 == 3:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz[1][0][i][y] and secao2 == 3:
                            matrizf[i+2][y] = matriz[1][0][i][y]
                            lista3.append(numero2)                 
            elif secao2 == 4:
        
                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz[1][1][i][y] and secao2 == 4:
                            matrizf[i+2][y+2] = matriz[1][1][i][y]
                            lista4.append(numero2)
                            
            contador_de_jogadas4 += 2 #ao inves de contar mais 1 a cada jogada de cada jogador, somei mais 2 aos dois jogarem
            
            #pontuação das linhas 
            pontuacao2 += linhas(cont04,0,matrizf,4)
            if linhas(cont04,0,matrizf,4) != 0:
                cont04=1
            pontuacao2 += linhas(cont14,1,matrizf,4)
            if linhas(cont14,1,matrizf,4) != 0:
                cont14=1
            pontuacao2 += linhas(cont24,2,matrizf,4)
            if linhas(cont24,2,matrizf,4) != 0:
                cont24=1
            pontuacao2 += linhas(cont34,3,matrizf,4)
            if linhas(cont34,3,matrizf,4) != 0:
                cont34=1
            
            #pontuacao de cada coluna
            pontuacao2 += colunas(0,cont00,matrizf,4)
            if colunas(0,cont00,matrizf,4) != 0:
                cont00 = 1 
            pontuacao2 += colunas(1,cont10,matrizf,4)
            if colunas(1,cont10,matrizf,4) != 0:
                cont10 = 1
            pontuacao2 += colunas(2,cont20,matrizf,4)
            if colunas(2,cont20,matrizf,4) != 0:
                cont20 = 1
            pontuacao2 += colunas(3,cont30,matrizf,4)
            if colunas(3,cont30,matrizf,4) != 0:
                cont30 = 1

            #valor bonus

            for j in range(4):
                listabonus.append(matrizf[j][j])
            if 'x' in listabonus:
                listabonus = []
            else:
                if contbonus == 0:
                    pontuacao2 += valor_bonus
                    matrizf[4][4] = valor_bonus
                    contbonus = 1
                    print('\nO jogador 2 encontrou o valor escondido!')
            
            mostrarfake(matrizf,4,2,26)
        #pontuação cada jogador
            print()
            print('Pontuação de cada jogador')
            print(f'Jogador 1: {pontuacao1} \nJogador 2: {pontuacao2}')

    #inicio do jogo 9x9

    elif fase == 2:

    #gerando a matriz 9x9
        n = 9
        f = 3
        
        secao1 = ger(n,f) #gerando as seções através de uma função
        secao2 = ger(n,f)
        secao3 = ger(n,f)
        secao4 = ger(n,f)
        secao5 = ger(n,f)
        secao6 = ger(n,f)
        secao7 = ger(n,f)
        secao8 = ger(n,f)
        secao9 = ger(n,f)
        #colocando as 9 seções em uma matriz maior 
        matriz9 = [[secao1,secao2,secao3],[secao4,secao5,secao6],[secao7,secao8,secao9]]
        
        matriz9f = matrizfake(n+1)

        print('+=' * 50)
        print('\nO jogo começou! uma matriz misteriosa foi gerada...')
        print()
        
        #somas das linhas

        for zeros in range(9):
            matriz9f[zeros][9] = 0

        #algumas variaveis
        contador_de_jogadas = 0
        
        valor_bonus = 0

        cont09 = 0
        cont19 = 0
        cont29 = 0
        cont39 = 0
        cont49 = 0
        cont59 = 0
        cont69 = 0
        cont79 = 0
        cont89 = 0

        listabonus = []
        contbonus = 0

        cont80 = 0
        cont81 = 0
        cont82 = 0
        cont83 = 0
        cont84 = 0
        cont85 = 0
        cont86 = 0
        cont87 = 0
        cont88 = 0

        pontuacao1 = 0
        pontuacao2 = 0

        lista1 = []
        lista2 = []
        lista3 = []
        lista4 = []
        lista5 = []
        lista6 = []
        lista7 = []
        lista8 = []
        lista9 = []

        for y in range(3):
            #somas de cada linha das 9 seções
            
            for k in matriz9[0][y][0]:
                matriz9f[0][9]+= k
            for k in matriz9[0][y][1]:
                matriz9f[1][9] += k
            for k in matriz9[0][y][2]:
                matriz9f[2][9] += k
            
            for k in matriz9[1][y][0]:
                matriz9f[3][9]+= k
            for k in matriz9[1][y][1]:
                matriz9f[4][9] += k
            for k in matriz9[1][y][2]:
                matriz9f[5][9] += k

            for k in matriz9[2][y][0]:
                matriz9f[6][9]+= k
            for k in matriz9[2][y][1]:
                matriz9f[7][9] += k
            for k in matriz9[2][y][2]:
                matriz9f[8][9] += k

            for x in range(3):
                valor_bonus += matriz9[x][x][y][y] #k ele é 00 e dps fica 11

        #soma de cada coluna
        
        for zeros in range(9):
            matriz9f[9][zeros] = 0
        
        for coluna in range(3):
            for i in range(3):
                
                matriz9f[9][0] += matriz9[i][0][coluna][0]
                matriz9f[9][1] += matriz9[i][0][coluna][1]
                matriz9f[9][2] += matriz9[i][0][coluna][2]

                matriz9f[9][3] += matriz9[i][1][coluna][0]
                matriz9f[9][4] += matriz9[i][1][coluna][1]
                matriz9f[9][5] += matriz9[i][1][coluna][2]

                matriz9f[9][6] += matriz9[i][2][coluna][0]
                matriz9f[9][7] += matriz9[i][2][coluna][1]
                matriz9f[9][8] += matriz9[i][2][coluna][2]

        #mostrando a matriz fake ao iniciar o game
        mostrarfake(matriz9f,9,3,57)

        while contador_de_jogadas < 81:
            
            #nesta parte se encontra todos os mecanismos de jogadas para o jogador 1
            print()
            numero1,secao1 = verificando_valores('jogador 1','[1 - 9]',9)
            
            #funcao pra nao se repetir
            numero1,secao1 = n_repetir(numero1,secao1,lista1,'jogador 1',1,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista2,'jogador 1',2,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista3,'jogador 1',3,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista4,'jogador 1',4,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista5,'jogador 1',5,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista6,'jogador 1',6,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista7,'jogador 1',7,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista8,'jogador 1',8,9,'[1 - 9]')
            numero1,secao1 = n_repetir(numero1,secao1,lista9,'jogador 1',9,9,'[1 - 9]')
    

            #preenchendo as secoes
            if secao1 == 1:

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[0][0][i][y]:
                            matriz9f[i][y] = matriz9[0][0][i][y]
                            lista1.append(numero1)
            elif secao1 == 2:

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[0][1][i][y]:
                            matriz9f[i][y+3] = matriz9[0][1][i][y]
                            lista2.append(numero1)
            elif secao1 == 3:

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[0][2][i][y]:
                            matriz9f[i][y+6] = matriz9[0][2][i][y]
                            lista3.append(numero1)
            elif secao1 == 4:

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[1][0][i][y]:
                            matriz9f[i+3][y] = matriz9[1][0][i][y]
                            lista4.append(numero1)
            elif secao1 == 5:

                for i in range(f):
                        for y in range(f):
                            if numero1 == matriz9[1][1][i][y]:
                                matriz9f[i+3][y+3] = matriz9[1][1][i][y]
                                lista5.append(numero1)
            elif secao1 == 6:

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[1][2][i][y]:
                            matriz9f[i+3][y+6] = matriz9[1][2][i][y]
                            lista6.append(numero1)
            elif secao1 == 7:

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[2][0][i][y]:
                            matriz9f[i+6][y] = matriz9[2][0][i][y]
                            lista7.append(numero1)
            elif secao1 == 8: 

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[2][1][i][y]:
                            matriz9f[i+6][y+3] = matriz9[2][1][i][y]
                            lista8.append(numero1)
            elif secao1 == 9: 

                for i in range(f):
                    for y in range(f):
                        if numero1 == matriz9[2][2][i][y]:
                            matriz9f[i+6][y+6] = matriz9[2][2][i][y]
                            lista9.append(numero1)
            
            contador_de_jogadas += 1
           #somando a pontuacao do jogador 1 

            pontuacao1 += linhas(cont09,0,matriz9f,9)
            if linhas(cont09,0,matriz9f,9) != 0:
                cont09=1
            pontuacao1 += linhas(cont19,1,matriz9f,9)
            if linhas(cont19,1,matriz9f,9) != 0:
                cont19=1
            pontuacao1 += linhas(cont29,2,matriz9f,9)
            if linhas(cont29,2,matriz9f,9) != 0:
                cont29=1
            pontuacao1 += linhas(cont39,3,matriz9f,9)
            if linhas(cont39,3,matriz9f,9) != 0:
                cont39=1 
            pontuacao1 += linhas(cont49,4,matriz9f,9)
            if linhas(cont49,4,matriz9f,9) != 0:
                cont49=1
            pontuacao1 += linhas(cont59,5,matriz9f,9)
            if linhas(cont59,5,matriz9f,9) != 0:
                cont59=1
            pontuacao1 += linhas(cont69,6,matriz9f,9)
            if linhas(cont69,6,matriz9f,9) != 0:
                cont69=1
            pontuacao1 += linhas(cont79,7,matriz9f,9)
            if linhas(cont79,7,matriz9f,9) != 0:
                cont79=1
            pontuacao1 += linhas(cont89,8,matriz9f,9)
            if linhas(cont89,8,matriz9f,9) != 0:
                cont89=1
            
            #coluna

            pontuacao1 += colunas(0,cont80,matriz9f,9)
            if colunas(0,cont80,matriz9f,9) != 0:
                cont80 = 1
            pontuacao1 += colunas(1,cont81,matriz9f,9)
            if colunas(1,cont81,matriz9f,9) != 0:
                cont81 = 1
            pontuacao1 += colunas(2,cont82,matriz9f,9)
            if colunas(2,cont82,matriz9f,9) != 0:
                cont82 = 1
            pontuacao1 += colunas(3,cont83,matriz9f,9)
            if colunas(3,cont83,matriz9f,9) != 0:
                cont83 = 1
            pontuacao1 += colunas(4,cont84,matriz9f,9)
            if colunas(4,cont84,matriz9f,9) != 0:
                cont84 = 1
            pontuacao1 += colunas(5,cont85,matriz9f,9)
            if colunas(5,cont85,matriz9f,9) != 0:
                cont85 = 1
            pontuacao1 += colunas(6,cont86,matriz9f,9)
            if colunas(6,cont86,matriz9f,9) != 0:
                cont86 = 1
            pontuacao1 += colunas(7,cont87,matriz9f,9)
            if colunas(7,cont87,matriz9f,9) != 0:
                cont87 = 1
            pontuacao1 += colunas(8,cont88,matriz9f,9)
            if colunas(8,cont88,matriz9f,9) != 0:
                cont88 = 1

            #valor bonus

            for j in range(9):
                listabonus.append(matriz9f[j][j])
            if 'x' in listabonus:
                listabonus = []
            else:
                if contbonus == 0:
                    pontuacao1 += valor_bonus
                    matriz9f[9][9] = valor_bonus
                    contbonus = 1
                    print('\nO jogador 1 encontrou o valor escondido!')
            
            #mostrando a matriz fake a cada rodada
            
            mostrarfake(matriz9f,9,3,57)
            
            print()
            print('Pontuação de cada jogador')
            print(f'Jogador 1: {pontuacao1} \nJogador 2: {pontuacao2}')
            print()
            
            #nesta parte se encontra todos os mecanismos de jogadas para o jogador 2
            numero2,secao2 = verificando_valores('jogador 2','[1 - 9]',9)
            
            #funcao para n repetir
            numero2,secao2 = n_repetir(numero2,secao2,lista1,'jogador 2',1,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista2,'jogador 2',2,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista3,'jogador 2',3,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista4,'jogador 2',4,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista5,'jogador 2',5,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista6,'jogador 2',6,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista7,'jogador 2',7,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista8,'jogador 2',8,9,'[1 - 9]')
            numero2,secao2 = n_repetir(numero2,secao2,lista9,'jogador 2',9,9,'[1 - 9]')
            
            #preenchendo as secoes
            if secao2 == 1:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[0][0][i][y]:
                            matriz9f[i][y] = matriz9[0][0][i][y]
                            lista1.append(numero2)
            elif secao2 == 2:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[0][1][i][y]:
                            matriz9f[i][y+3] = matriz9[0][1][i][y]
                            lista2.append(numero2)
            elif secao2 == 3:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[0][2][i][y]:
                            matriz9f[i][y+6] = matriz9[0][2][i][y]
                            lista3.append(numero2)
            elif secao2 == 4:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[1][0][i][y]:
                            matriz9f[i+3][y] = matriz9[1][0][i][y]
                            lista4.append(numero2)
            elif secao2 == 5:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[1][1][i][y]:
                            matriz9f[i+3][y+3] = matriz9[1][1][i][y]
                            lista5.append(numero2)   
            elif secao2 == 6:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[1][2][i][y]:
                            matriz9f[i+3][y+6] = matriz9[1][2][i][y]
                            lista6.append(numero2)
            elif secao2 == 7:

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[2][0][i][y]:
                            matriz9f[i+6][y] = matriz9[2][0][i][y]
                            lista7.append(numero2)
            elif secao2 == 8: 

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[2][1][i][y]:
                            matriz9f[i+6][y+3] = matriz9[2][1][i][y]
                            lista8.append(numero2)
            elif secao2 == 9: 

                for i in range(f):
                    for y in range(f):
                        if numero2 == matriz9[2][2][i][y]:
                            matriz9f[i+6][y+6] = matriz9[2][2][i][y]
                            lista9.append(numero2)
           
            contador_de_jogadas += 1 # no 9x9, decidi contar mais 1 a cada valor revelado, ja que sao 81 jogadas (impar)
          
           #somando a pontuacao das linhas do jogador 2

            pontuacao2 += linhas(cont09,0,matriz9f,9)
            if linhas(cont09,0,matriz9f,9) != 0:
                cont09=1
            pontuacao2 += linhas(cont19,1,matriz9f,9)
            if linhas(cont19,1,matriz9f,9) != 0:
                cont19=1
            pontuacao2 += linhas(cont29,2,matriz9f,9)
            if linhas(cont29,2,matriz9f,9) != 0:
                cont29=1
            pontuacao2 += linhas(cont39,3,matriz9f,9)
            if linhas(cont39,3,matriz9f,9) != 0:
                cont39=1 
            pontuacao2 += linhas(cont49,4,matriz9f,9)
            if linhas(cont49,4,matriz9f,9) != 0:
                cont49=1
            pontuacao2 += linhas(cont59,5,matriz9f,9)
            if linhas(cont59,5,matriz9f,9) != 0:
                cont59=1
            pontuacao2 += linhas(cont69,6,matriz9f,9)
            if linhas(cont69,6,matriz9f,9) != 0:
                cont69=1
            pontuacao2 += linhas(cont79,7,matriz9f,9)
            if linhas(cont79,7,matriz9f,9) != 0:
                cont79=1
            pontuacao2 += linhas(cont89,8,matriz9f,9)
            if linhas(cont89,8,matriz9f,9) != 0:
                cont89=1
            
            #coluna

            pontuacao2 += colunas(0,cont80,matriz9f,9)
            if colunas(0,cont80,matriz9f,9) != 0:
                cont80 = 1
            pontuacao2 += colunas(1,cont81,matriz9f,9)
            if colunas(1,cont81,matriz9f,9) != 0:
                cont81 = 1
            pontuacao2 += colunas(2,cont82,matriz9f,9)
            if colunas(2,cont82,matriz9f,9) != 0:
                cont82 = 1
            pontuacao2 += colunas(3,cont83,matriz9f,9)
            if colunas(3,cont83,matriz9f,9) != 0:
                cont83 = 1
            pontuacao2 += colunas(4,cont84,matriz9f,9)
            if colunas(4,cont84,matriz9f,9) != 0:
                cont84 = 1
            pontuacao2 += colunas(5,cont85,matriz9f,9)
            if colunas(5,cont85,matriz9f,9) != 0:
                cont85 = 1
            pontuacao2 += colunas(6,cont86,matriz9f,9)
            if colunas(6,cont86,matriz9f,9) != 0:
                cont86 = 1
            pontuacao2 += colunas(7,cont87,matriz9f,9)
            if colunas(7,cont87,matriz9f,9) != 0:
                cont87 = 1
            pontuacao2 += colunas(8,cont88,matriz9f,9)
            if colunas(8,cont88,matriz9f,9) != 0:
                cont88 = 1

            #valor bonus

            for j in range(9):
                listabonus.append(matriz9f[j][j])
            if 'x' in listabonus:
                listabonus = []
            else:
                if contbonus == 0:
                    pontuacao1 += valor_bonus
                    matriz9f[9][9] = valor_bonus
                    contbonus = 1
                    print('\nO jogador 2 encontrou o valor escondido!')

            
            mostrarfake(matriz9f,9,3,57)    
            print()
            print('Pontuação de cada jogador')
            print(f'Jogador 1: {pontuacao1} \nJogador 2: {pontuacao2}')
          
    #aqui, tanto pra 4x4, ou 9x9, decide quem ganhou (quem tem maior pontuação)
    if pontuacao1 > pontuacao2:
        print('\nParabens jogador 1, você ganhou!')
    elif pontuacao2 > pontuacao1:
        print('\nParabens jogador 2, você ganhou!')
    
    #pergunta se quer reiniciar o jogo de acordo com o primeiro loop (while)
    a = input('\nDeseja reiniciar o jogo? [s/n]: ').upper().lower()
    print()