##Segunda parte da implementação do trabalho de MC
##Autores: Edson Cizeski @ra107514 // Igor Picolo @ra105408
##Calculo do seno
##Analisar as diferencas dos argumentos

import math
import decimal


#fatoriais pre-calculados pra otimizar tempo
fat2 = math.factorial(2)
fat3 = math.factorial(3)
fat4 = math.factorial(4)
fat5 = math.factorial(5)
fat6 = math.factorial(6)
fat7 = math.factorial(7)
fat8 = math.factorial(8)
fat9 = math.factorial(9)
fat10 = math.factorial(10)
fat11 = math.factorial(11)
fat12 = math.factorial(12)

#rad pre-calculados pra otimizar tempo
rad0 = math.radians(0)
rad45 = math.radians(45)
rad90 = math.radians(90)
rad180 = math.radians(180)
rad270 = math.radians(270)
rad360 = math.radians(360)

#funcao que implementa o primeiro caso da serie de taylor
def primeiraFormula(x):
    return (x-(pow(x,3)/fat3) + (pow(x,5)/fat5) - 
    (pow(x, 7)/fat7) + (pow(x, 9)/fat9) - (pow(x, 11)/fat11))

#funcao que implementa o segundo caso da serie de taylor
def segundaFormula(x):
    x_linha = rad90 - x
    return cosseno(x_linha)

#funcao q calcula o cosseno baseado na serie de taylor
def cosseno(x):
    return (1-(pow(x,2)/fat2)+(pow(x,4)/fat4) - (pow(x,6)/fat6) +  (pow(x, 8)/fat8) -
    (pow(x, 10)/fat10) + (pow(x, 12)/fat12))

#funcao que transforma um angulo de outros quadrantes pro primeiro quadrante
def Q2toQ1(x):
        return rad180 - x

def Q34toQ1(x):
    if rad180 < x <= rad270:
        return x - rad180
    else:
        return rad360 - x

#funcao que calcula o seno do angulo X
def seno(x):
    #3 casos
    if rad0 <= x <= rad45:
        return primeiraFormula(x)
    elif rad45 < x <= rad90:
        return segundaFormula(x)
    elif rad90 < x <= rad180:
        x_linha = Q2toQ1(x)
        return seno(x_linha)
    else:
        x_linha = Q34toQ1(x)
        return -(seno(x_linha))

#funcao principal
def main():
    erroMax = 0 #variavel que armazena o valor do maior Erro encontrado
    anguloMaxErro = 0 #variavel que armazena o angulo que gerou o maior erro
    for x in range(0, 370, 10):
        print("angulo ", x)
        y = seno(math.radians(x))
        print("seno %.16f" %y)
        z = math.sin(math.radians(x))
        print("sin %.16f" %z)
        erro = abs(y - z)
        print("erro %.16f" %erro)
        if erro > erroMax:
            erroMax = erro
            anguloMaxErro = x
    print("Maior erro encontrado no argumento: %.16f" %erroMax)
    print("Angulo do max erro: %.16f" %anguloMaxErro)
#inicio
main()
