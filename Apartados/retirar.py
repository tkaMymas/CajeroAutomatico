import time

def retirarDinero():
    print("Ingrese la cantidad de dinero a retirar.")
    retirar = int(input())
    time.sleep(0.5)

    while True:
        if retirar != 0:
            print("Procesando...")
            time.sleep(0.5)
            print("Transacción completada.. \nSe han retirado la cantidad de", str(retirar) + "$", "de tu cuenta bancaria.")
            break
        else:
            print("Procesando...")
            time.sleep(0.5)
            print("Ingrese una cantidad valida.")
            print()
            return retirarDinero()