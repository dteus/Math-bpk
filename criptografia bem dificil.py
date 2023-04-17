#Importa a biblioteca numpy para fazer os calculos com matrizes 
import numpy as np
#Importa a biblioteca string do python
import string

#Arruma o alfabeto ascii nativo do python para ficar equivalente ao exercicio
a = list(string.ascii_uppercase)
a.remove('K')
a.insert(0,' ')
# ------------------------------------------------------------------------------------------
#Função para encriptar a mensagem
def encriptografar(chave):

    #encripta a mensagem multiplicando a matriz pela chave
    mensagem_encriptografada = np.matmul(chave,mensagem_matriz)
    
    #retorna a mensagem encriptada para o usuario
    return mensagem_encriptografada

#Função para decodificar a mensagem
def decodificar(mensagem):
    mensagem = np.asarray(mensagem, dtype='float64')
    #Decodificação da mensagem
    mensagem = np.matmul(chave_inversa,mensagem)
    #Variavel que vai armazenar a mensagem escrita em forma de string
    mensagem_decodificada = ''
    #Loop para escrever a mensagem usando o codigo decodificado
    for i in range(len(mensagem)):
        for j in range(len(mensagem)):
                #Se o valor for valido ele reproduz uma letra
                if 0 < int(mensagem[i][j]) < 26:
                    mensagem_decodificada += a[round(mensagem[i][j])]
                #Se o valor não for válido ele reproduz um espaço
                else:
                    mensagem_decodificada += ' '  

    #Retorna apenas a mensagem escrita, já que a matriz decodificada não é mais útil        
    return mensagem_decodificada
# ------------------------------------------------------------------------------------------
#Criando a chave
#Definindo dimensões
Linhas = Colunas = int(input("Numero de linhas e colunas da chave: \n"))
#Usuario insere todos os dados de uma só vez, separado por espaço
entries = list(map(float, input("Insira valores da chave em ordem: \n").split()))
#Cria a matrix chave
chave = np.array(entries).reshape(Linhas, Colunas)
#Checar se a matrix possuí inversa
while np.linalg.det(chave) == 0:
    entries = list(map(int, input("Matriz com determinante zero! Insira novos valores: \n").split()))
    chave = np.array(entries).reshape(Linhas, Colunas)
#Calculo da inversa
chave_inversa = np.linalg.inv(chave)

#Criar uma mensagem
mensagem_usuario = input("Informe a mensagiem que deseja enviar:\n").upper()

#Checa se a mensagem contem apenas letras
while mensagem_usuario.isalpha() == False:
    print("Porra, digita um bagulho certo ai karalho\n")
    mensagem_usuario = input("Informe a mensagem que deseja enviar: \n").upper()

#Transforma mensagem numa lista de numeros com index relacionados ao alfabeto
mensagem_matriz = []
for i in mensagem_usuario:
    mensagem_matriz.append(float(a.index(i)))

#Preenchendo valores vazios se necessário
while Linhas*Colunas > len(mensagem_matriz):
    mensagem_matriz.append(0)

#Cria a matrix da chave  
mensagem_matriz = np.array(mensagem_matriz).reshape(Linhas, Colunas)
# ------------------------------------------------------------------------------------------
#Chamando a função para encriptografar
print(encriptografar(chave))

#Chamando a função para decodificar
print(decodificar(encriptografar(chave)))