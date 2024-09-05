from Operaciones_basicas import *
import Operaciones_avanzadas
def main():
    invalido = True
    while invalido:
        print("\nBienvenido a su calculadora avanzada\nSeleccione su opcion:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division")
        opc = int(input("5. Potencia\n6. Radicacion\n7. Logaritmo\n8. Salir\nOPCION = "))
        if opc == 1:
            invalido = False
            print(suma_resta(1))
            main()
        elif opc == 2: 
            invalido = False
            print(suma_resta(-1))
            main()
        elif opc == 3:
            invalido = False
            print(multiplicacion())
            main()
        elif opc == 4:
            invalido = False
            print(division())
            main()
        elif opc == 5:
            invalido = False
            print(Operaciones_avanzadas.potencia())
            main()
        elif opc == 6:
            invalido = False
            print(Operaciones_avanzadas.raiz())
            main()
        elif opc == 7:
            invalido = False
            print(Operaciones_avanzadas.log())
            main()
        elif opc == 8:
            print("Cerrando el programa...")
            invalido = False
        else:
            print("ERROR!, Opcion no existente")

main()