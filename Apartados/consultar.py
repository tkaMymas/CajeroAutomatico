import time
from Apartados import depositar

def consultarSaldo():
    print("Se le mostrara su saldo en un momento...")
    time.sleep(0.5)
    print("Procesando...")
    time.sleep(0.5)
    print("Actulamente cuenta con", str(depositar.dineroTotal) + "$", "en su cuenta de banco.")