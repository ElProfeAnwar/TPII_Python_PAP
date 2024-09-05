import math 

def suma_resta(inversor):
    res = 0
    if inversor == 1:
        n = int(input("Cuantos valores desea sumar?\nn = "))
        for i in range (n):
            sumando = float(input(f"Ingrese su valor {i + 1}: "))
            res += sumando
        return f"\nSu resultado es = {res}" 
    elif inversor == -1:
        n = int(input("Cuantos valores desea restar?\nn = "))
        for i in range (n):
            sumando = float(input(f"Ingrese su valor {i + 1}: "))
            if i == 0:
                res += sumando
            else:
                res += sumando * inversor
        return f"\nSu resultado es = {res}" 
        
def multiplicacion():
    n = int(input("Cuantos valores desea multiplicar?\nn = "))
    res = 1
    for i in range (n):
        multi = float(input(f"Iingrese su multiplo {i + 1} = "))
        res *= multi
    return f"\nSu resultado es = {res}"

def division():
    a = float(input("Ingrese el numerador de su fraccion: "))
    b = 0
    while b == 0:
        b = float(input("Ingrese el denominador de su fraccion: "))
        if b == 0:
            print("ERROR! division por 0\n")
    return f"\nEl resultado exacto de su division es {a // b} y su modulo es {a % b}"
