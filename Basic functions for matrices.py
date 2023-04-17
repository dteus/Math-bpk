# Construção de uma matriz
# for i in range(X):
#     for j in range(Y):
#         list.append[value_row][value_collumn]
import numpy as np
np.set_printoptions(threshold=np.inf)
# # ------------------------------------------------------------------    
# # Indique explicitamente os elementos da matriz A = (a[i][j])3x3 tal que a[i][j] = i - j
# l = 3
# c = 3
# matrix = np.arange(9).reshape(3,3)
# value = 0
# for i in range(l):
#     for j in range(c):
#         value = i - j
#         matrix[i][j] = value
# print(matrix)
# # ------------------------------------------------------------------
# # Construa as seguintes matrizes:
# # A = a[i][j]3x3 tal que 1 se i =j e 0 se i!=j
# l = 3
# c = 3
# matrix = np.arange(9).reshape(3,3)
# value = 0
# for i in range(l):
#     for j in range(c):
#         if i == j:
#             value = 1
#         else: 
#             value = 0
#         matrix[i][j] = value
# print(matrix)

# matrixb = np.arange(9).reshape(3,3)
# value = 0
# for i in range(l):
#     for j in range(c):
#         if i+j == 2:
#             value = 1
#         else: 
#             value = 0
#         matrixb[i][j] = value
# print(matrixb)
# # ------------------------------------------------------------------
# # Construa a matriz A de ordem 3 por 2 definida pela lei a ij = 1 se  i=j e i**2  se i !=j
# matrix = np.arange(6).reshape(3,2)
# value = 0 
# l = 3
# c = 2
# for i in range(l):
#     for j in range(c):
#         if i == j:
#             value = 1
#         else: 
#             value = (i+1) **2 
#         matrix[i][j] = value
# print(matrix)
# # ------------------------------------------------------------------
# # Dada uma matriz A m x n e as operações:
# # a. A_2, que transforma a matriz A numa outra matriz A’ m x 1 em que cada elemento da única
# # coluna de A’ é obtido somando-se os elementos da linha correspondente de A.
# # b. + A_3, que transforma a matriz A m x n numa outra matriz A” 1 x n em que cada elemento da
# # única linha de A” é obtido somando-se os elementos da coluna correspondente de A.
# # Nessas condições, se A for a matriz identidade de ordem p, calcule a expressão +A_1(+ A_2).

# # Criando as variáveis 
# coluna = int(input("Qual o numero de colunas"))
# linhas = int(input("Qual o numero de linhas"))
# total = coluna * linhas
# matrix = np.arange(total).reshape(linhas,coluna)
# matrix_A_2 = []
# matrix_A_3 = []

# # Construindo a matriz
# for i in range(linhas):
#     for j in range(coluna): 
#         matrix[i][j] = i+j
# print(f'A matriz A é:\n {matrix}\n')

# # Calculo de uma matrix com uma coluna só
# def A_2(matrix):
#     matrix_A_2 = np.arange(linhas).reshape(linhas,1)
#     for i in range(linhas):
#         value = 0
#         for j in range(coluna):
#              value += matrix[i][j]
#         matrix_A_2[i] = value
#     return f'+/A da matriz A é igual a:\n {matrix_A_2}\n' 
# print(A_2(matrix))

# # Calculo da matrix com uma linha só 
# def A_3(matrix):
#     matrix_A_3 = np.arange(coluna)
#     for j in range(coluna):
#         value = 0
#         for i in range(linhas):
#             value += matrix[j][i]
#         matrix_A_3[j] = value
#     return f'+|A da matriz A é igual a:\n{matrix_A_3}\n'
# print(A_3(matrix))
# # ------------------------------------------------------------------
# # Seja A = [[1,3,6],[2,-5,8],[4,2,7]] determinar o traço de A
# A = [[1,3,6],[2,-5,8],[4,2,7]]

# def traco_matriz(matriz):
#     traco = []
#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if i == j:
#                 traco.append(matriz[i][j])
#     return f'O traco é a soma de {traco} que é igual a: {sum(traco)}'
# print(traco_matriz(A))
# # ------------------------------------------------------------------

# # Escreva a transposta da matriz A = [[3,-1],[2,4],[5,0]] 
# # Matriz original
# A = np.array([[3,-1],[2,4],[5,0]])

# def transposta_matriz(matriz):
#     #Definir o numero de valores na matrix
#     qnt_valores = len(matriz)*(len(matriz[0]))
#     #Criar uma matrix com as dimensões desejadas
#     transposta = np.arange(qnt_valores).reshape(len(matriz[0]),len(matriz))
#     #Modificar a matrix com os valores desejados
#     for j in range(len(matriz[0])):
#         for i in range(len(matriz)):
#             transposta[j][i] = matriz[i][j]
#     return f'A transposta da matriz é igual a:\n{transposta}'
# print(transposta_matriz(A))

# # ------------------------------------------------------------------

# # # Determine o traço da matriz A de ordem 3 definida por a[i][j] = i+j+2.

# #Função da transposta    
# def traco_matriz(matriz):
#     for i in range(linhas):
#         for j in range(coluna):
#             if i == j:
#                 traco.append(matriz[i][j])
#     return f'O traço da matriz:\n {matriz}\n é a soma dos valores {traco}:\n {sum(traco)}'

# #Variáveis 
# coluna = 3
# linhas = 3
# total = coluna * linhas
# matriz = np.arange(total).reshape(linhas,coluna)
# traco = []

# #Construindo a matriz
# for i in range(linhas):
#     for j in range(coluna):
#         matriz[i][j] = i+j+2

# #chamando a função
# print(traco_matriz(matriz))

# ------------------------------------------------------------------
# matriz_1 = [[1,0],[1,1],[2,3]]
# matriz_2 = [[2,0,1,2],[1,1,1,2]]
# resultante = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# print(np.array(matriz_1),'\n\n')
# print(np.array(matriz_2),'\n\n')
# print(np.array(resultante),'\n\n')
# for i in range(len(resultante)):
#     for k in range(len(resultante[0])):
#         value = 0
#         for j in range(len(matriz_1[0])):
#             value += matriz_1[i][j] * matriz_2[j][k] 
#         resultante[i][k] = value

# print(np.array(resultante))
# print(np.matmul(matriz_1,matriz_2))

# ------------------------------------------------------------------
# homens = [[80,120]]
# mulheres = [[100,200]]
# adultos = [[20,20,20],[10,20,30]]
# homens_total = np.matmul(homens, adultos)
# mulheres_total = np.matmul(mulheres, adultos)
# print(f'A quantidade total de proteinas consumidas por homens adultos e crianças é de {homens_total[0][0]}')
# print(f'A quantidade total de gorduras consumidas por mulheres adultas e crianças é de {mulheres_total[0][1]}')


#Importa a biblioteca string do python e armazena o alfabeto em uma variavel
import string
a = list(string.ascii_uppercase)
#chave de teste 
chave = [[2,3],
         [1,2]]
#Se necessário podemos criar qualquer outra chave inserindo o comando
# chave = input("Qual a chave encriptadora?")

#Arruma o alfabeto ascii nativo do python para ficar equivalente ao exercicio
a.remove('K')
a.append(' ')
#Função para encriptar a mensagem
def encriptografar(matriz):

    #encripta a mensagem multiplando a matriz pela chave
    mensagem_encriptografada = np.matmul(matriz,chave)

    #retorna a mensagem encriptada para o usuario
    return f'A Mensagem encriptada é:\n {mensagem_encriptografada}\n'

#Função para decodificar a mensagem
def criptografia(matriz):

    #Decodificação da mensagem
    mensagem = np.matmul(matriz,np.linalg.inv(chave))

    #Variavel que vai armazenar a mensagem escrita em forma de string
    mensagem_codificada = ''
    
    #Loop para escrever a mensagem usando o codigo decodificado
    for i in range(2):
        for j in range(2):
            mensagem_codificada += a[int(mensagem[i][j])-1]

    #Retorna apenas a mensagem escrita, já que a matriz decodificada não é mais útil        
    return f'A mensagem decodificada é : {mensagem_codificada}\n'


#Chamando a função para encriptografar
print(encriptografar([[15,1],
                    [25,0]]))

#Chamando a função para decodificar
print(criptografia([[31,47],
                    [50,75]]))
