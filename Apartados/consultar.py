import time
from Apartados import depositar, retirar

dineroCuentaBancaria = 0

def consultarHistorial():
    print("Se le mostrara su historial bancario")
    time.sleep(0.5)
    print("Procesando...")
    time.sleep(0.5)

    print("Su cuenta de banco cuenta con..", str(dineroCuentaBancaria) + "$")