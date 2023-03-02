import time
from Apartados import depositar, retirar, consultar

time.sleep(1)
print("Bienvenido a Central Bank")
def menuCajero():
    time.sleep(1)
    print("Ingrese una operación a realizar.")
    print("Depositar(1)    -    Retirar(2)   -   Consultar Historial(3)")
    operacion = int(input())

    if operacion == 1:
        time.sleep(0.5)
        print("Procesando...")
        time.sleep(1)
        depositar.depositarDinero()
        time.sleep(1)
        print("Procesando...")
        print()
        return menuCajero()

    elif operacion == 2:
        time.sleep(0.5)
        print("Procesando...")
        time.sleep(0.5)
        retirar.retirarDinero()
        time.sleep(1)
        print("Procesando...")
        print()
        return menuCajero()

    elif operacion == 3:
        time.sleep(0.5)
        print("Procesando...")
        time.sleep(1)
        consultar.consultarHistorial()
        time.sleep(1)
        print("Procesando...")
        print()
        return menuCajero()

    else:
        time.sleep(0.5)
        print("Procesando...")
        time.sleep(1)
        print("Ingrese una operación valida...")
        print()
        return menuCajero()

menuCajero()