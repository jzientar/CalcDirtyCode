#Refactorizado
def Calculadora(numero1,numero2, operacion):
    if operacion==1 :
        print(numero1+numero2)
    elif operacion==2 :
        print(numero1-numero2)
    elif operacion==3 :
        print(numero1*numero2)
    elif operacion==4 :
        print(numero1/numero2)
        
def Menu():
    opcion=0
    while True:
        print(" 1) Sumar 2) Restar 3) Multiplicar  4) Dividir")
        opcion = int(input("Elige una opción: "))
        primerNum = float(input("Introduce tu primer numero: "))
        segundoNum = float(input("Introduce tu segundo numero: "))
        Calculadora(primerNum, segundoNum, opcion)
Menu()