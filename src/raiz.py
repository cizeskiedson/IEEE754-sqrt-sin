##Primeira parte da implementação do trabalho de MC
##Autores: Edson Cizeski @ra107514 // Igor Picolo @ra105408
##Calculo da raiz quadrada
##Analisar as diferencas dos argumentos
import struct
import math 

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)

def binaryToFloat(value):
    hx = hex(int(value, 2))
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]

def bin_test(numeroZeros, string_binaria):
    teste = ''
    for i in range(numeroZeros):
        teste += '0'
    for i in string_binaria:
        teste += i
    return teste

S = 0
E = 0
M = 0
def printa_sinais(num):
    S = int(num[0])
    E = num[1:12]
    M = num[12:]
    print('S ', S)
    print('E ', E)
    print('M ', M)
    return S, E, M

def expoenteToDecimal(E):
    eResult = 0
    j = 0
    for i in range(10, -1, -1):
        eResult += int(E[j]) * pow(2, i)
        j += 1
    print('E em decimal', eResult)
    return eResult

def mantissaToDecimal(M):
    j = 0
    mResult = 0
    for i in range(51, -1, -1):
        mResult += int(M[j]) * pow(2, i)
        j += 1
    print('M em decimal', mResult)
    return mResult

def raiz_quadrada(e, y):
    if(e % 2 == 0):
        resultado = pow(2, (e/2)) * math.sqrt((1 + y))
    else:
        resultado = pow(2, ((e+1)/2)) * (math.sqrt((1+y)) / 1.41421356237309504880168872420969807856967187537694807317667973799)
    print('Resultado ', resultado)

def main():
   # num = input("Digite o valor de entrada:  ")
    string_binaria = floatToBinary64(1.9)
    print('Binario: ')
    print(string_binaria + '\n')
    print('Tamanho: ', len(string_binaria))
    numeroZeros = 64 - len(string_binaria)
    string_binaria = bin_test(numeroZeros, string_binaria)
    print('Binario Novo:', string_binaria)
    print('Tamanho:', len(string_binaria))
    S, E, M = printa_sinais(string_binaria)
    eResult = expoenteToDecimal(E)
    mResult = mantissaToDecimal(M)
    y = mResult / pow(2, 52)
    print('Y ', y)
    e = eResult - 1023
    resultado = 0
    raiz_quadrada(e, y)
main()