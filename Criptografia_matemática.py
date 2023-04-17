#Importa a biblioteca numpy para fazer os calculos com matrizes 
import numpy as np
#Importa a biblioteca string do python e armazena o alfabeto em uma variavel
import string

#Função para encriptar a mensagem
def encriptografar(matriz):

    #encripta a mensagem multiplando a matriz pela chave
    mensagem_encriptografada = np.matmul(chave,matriz)

    #retorna a mensagem encriptada para o usuario
    return f'A Mensagem encriptada é:\n {mensagem_encriptografada}\n'

#Função para decodificar a mensagem
def decodificar(matriz):

    #Decodificação da mensagem
    mensagem = np.matmul(chave_inversa,matriz)
    #Variavel que vai armazenar a mensagem escrita em forma de string
    mensagem_decodificada = ''
    
    #Loop para escrever a mensagem usando o codigo decodificado
    for i in range(len(matriz)):
        for j in range(len(matriz)):
                #Se o valor for valido ele reproduz uma letra
                if 0 < int(mensagem[i][j]) < 26:
                    mensagem_decodificada += a[int(mensagem[i][j])]
                #Se o valor não for válido ele reproduz um espaço
                else:
                    mensagem_decodificada += ' '
            
    #Retorna apenas a mensagem escrita, já que a matriz decodificada não é mais útil        
    return f'A mensagem decodificada é:\n {mensagem_decodificada}\n'

# ------------------------------------------------------------------------------------------
#Arrumando as variaveis
#Armazena o alfabeto em letras maiusculas numa variavel
a = list(string.ascii_uppercase)

#Arruma retira o K e arruma a contagem para A = 1, B = 2...
a.remove('K')
a.insert(0,' ')

# chaves de teste 
chave = [[2,3],
         [1,2]]
chave_inversa = np.linalg.inv(chave)
# ------------------------------------------------------------------------------------------
#Chamando a função para encriptografar
print(encriptografar([[15,1],
                    [25,0]]))

#Chamando a função para decodificar
print(decodificar([[105,2],
                    [65,1]]))
