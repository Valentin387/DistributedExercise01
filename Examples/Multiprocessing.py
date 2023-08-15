import multiprocessing

def tarea1():
    # realizar alguna operación
    pass

def tarea2():
    # realizar alguna operación
    pass

proceso1 = multiprocessing.Process(target=tarea1)
proceso2 = multiprocessing.Process(target=tarea2)

proceso1.start()
proceso2.start()

proceso1.join()
proceso2.join()