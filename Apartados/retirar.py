import time
from Apartados import depositar

dineroRetirado = 0

def retirarDinero():
    global dineroRetirado
    print("Ingrese la cantidad de dinero a retirar.")
    retirar = int(input())
    time.sleep(0.5)

    while True:
        if depositar.dineroEnBanco == 0:
            time.sleep(0.5)
            print("No cuenta con dinero en su cuenta de Banco.. \nPor favor primero ingrese dinero a su cuenta.")
            break
        if retirar != 0:
            dineroRetirado = depositar.dineroEnBanco - retirar
            print("Procesando...")
            time.sleep(0.5)
            print("Transacción completada.. \nSe han retirado la cantidad de", str(retirar) + "$", "de tu cuenta bancaria.."
                  "\nSaldo total de la cuenta", str(dineroRetirado) + "$")
            break
        else:
            print("Procesando...")
            time.sleep(0.5)
            print("Ingrese una cantidad valida.")
            print()
            return retirarDinero()