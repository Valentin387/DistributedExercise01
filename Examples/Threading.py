import threading
import time

def imprimir_numeros():
    for i in range(1, 11):
        print(threading.current_thread().name, i)
        time.sleep(1)

for _ in range(3):
    thread = threading.Thread(target=imprimir_numeros)
    thread.start()

for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()