import os
import threading
from time import sleep


class Script1:
    __pid2 = os.getpid()
    __pid2_l = [__pid2]
    print("Pid contagem I {}".format(__pid2))

    def __init__(self):
        self.__funcoes()

    def __programa(self):
        __numero = 1
        while __numero < 200:
            __numero += 1
            sleep(1)
            print(__numero)

    def __funcoes(self):
        __t1 = threading.Thread(target=self.__programa)
        __t1.start()
        __t1.join()


contagem1 = Script1()
