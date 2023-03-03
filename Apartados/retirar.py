import time
from Apartados import depositar

def retirarDinero():

    print("Ingrese la cantidad de dinero a retirar.")
    retirar = int(input())
    time.sleep(0.5)

    while True:
        if depositar.dineroTotal == 0:
            time.sleep(0.5)
            print("No cuenta con dinero en su cuenta de Banco.. \nPor favor primero ingrese dinero a su cuenta.")
            break
        if retirar != 0:
            depositar.dineroTotal -= retirar
            print("Procesando...")
            time.sleep(0.5)
            print("Transacción completada.. \nSe han retirado la cantidad de", str(retirar) + "$", "de tu cuenta bancaria.."
                  "\nSaldo total de la cuenta", str(depositar.dineroTotal) + "$")
            break
        else:
            print("Procesando...")
            time.sleep(0.5)
            print("Ingrese una cantidad valida.")
            print()
            return retirarDinero()