import math
def potencia():
    a = float(input("Ingrese la base de su potencia: "))
    b = float(input("Ingrese el exponente de su potencia: "))
    return f"El resultado de su potencia es: {math.pow(a,b)}"

def raiz():
    a = float(input("Ingrese su radicando: "))
    if a >= 0:
        return f"El resultado de su raiz es {round(math.sqrt(a),4)}"
    else:
        return f"El resultado de su raiz es {round(math.sqrt(a * -1),4)}i"

def log():
    print("Numero Euler = e\nNumero Pi = pi")
    verificador = True
    while verificador:
        base = input("Ingrese su base: ")
        if str(base) == 'pi':
            verificador = False
            base = math.pi
            return argumento(base)
        elif str(base) == 'e':
            verificador = False
            base = math.e
            return argumento(base)
        elif float(base) > 0:
            return argumento(base)
        else:
            print("ERROR!, base inexistente\n")
            
def argumento(base):
    verificador = True
    while verificador:
        argumento = input("Ingrese su argumento: ")
        if str(argumento) == 'pi':
            verificador = False
            argumento = math.pi
        elif str(argumento) == 'e':
            verificador = False
            argumento = math.e
        elif float(argumento) >= 0:
            verificador = False
            argumento = float(argumento)
        else:
            print("ERROR!, argumento inexistente\n")
            
    return f"El log en base {round(float(base), 4)} de {round(float(argumento), 4)} es: {round(math.log(float(argumento),float(base)), 4)}"