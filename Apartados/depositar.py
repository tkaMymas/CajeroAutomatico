import time

def depositarDinero():
    print("Ingrese la cantidad de dinero a depositar.")
    print("10$", "25$", "50$", "100$")
    deposito = int(input())
    print("Procesando...")
    time.sleep(0.5)

    while True:
        if deposito == 10 or deposito == 25 or deposito == 50 or deposito == 100:
            print("Ingrese la cantidad de montos de dinero depositara.")
            depositoMonto = int(input())
            print("Procesando...")
            time.sleep(0.5)

            def ingresarDinero():
                totalIngreso = deposito * depositoMonto
                time.sleep(1)
                print("Transacción completada.. \nSe han ingresado la cantidad de", str(totalIngreso) + "$",
                      "a tu cuenta bancaria.")
            ingresarDinero()
            break
        else:
            time.sleep(0.5)
            print("Ingrese una cantidad valida.")
            print()
            time.sleep(0.5)
            return depositarDinero()