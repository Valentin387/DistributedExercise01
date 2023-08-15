import multiprocessing

def tarea1():
    print("Executing tarea1")

def tarea2():
    print("Executing tarea2")

proceso1 = multiprocessing.Process(target=tarea1)
proceso2 = multiprocessing.Process(target=tarea2)

proceso1.start()
proceso2.start()

proceso1.join()
proceso2.join()
