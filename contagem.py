import os
import threading
import keyboard
import signal
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

    def __codigo_pid2(self):
        with open('saida.txt', 'a') as f:
            for passw in self.__pid2_l:
                __dicio2 = "1:{},".format(passw)
                f.write(__dicio2)

    def __tecla(self):
        while True:
            if keyboard.is_pressed('i'):
                with open("saida.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
                    for x in r:
                        asd = x

                        dic_pids = {}
                        pids = asd.split(',')
                        pids.remove(pids[-1])

                        for element in pids:
                            split_element = element.split(':')
                            dic_pids.update({split_element[0]: split_element[1]})

                if len(dic_pids) == 3:
                    self.__prog_len3(dic_pids)

                elif len(dic_pids) == 2:
                    self.__prog_len2(dic_pids)

                elif len(dic_pids) == 1:
                    self.__prog_len1(dic_pids)

    def __prog_len2(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript1 = int(dic_pidss['1'])

        if self.__pid2 == pidscript1:
            pf = str(1)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript1:
                    list_pids.remove(list_pids[val])
                val += 1
            with open("saida.txt", "w") as wk:
                wk.write("")
            lista_nova = []
            lista_keys_nova = []
            for x in list_pids:
                dsa = str(x)
                lista_nova.append(dsa)
            for y in dic_pidss.keys():
                lista_keys_nova.append(y)

            salvar = lista_nova[0]
            keyssalvar = lista_keys_nova[0]

            with open("saida.txt", "a") as ww:
                ww.write(keyssalvar + ":" + salvar + ",")

            os.kill(self.__pid2, signal.SIGTERM)
        else:
            os.kill(self.__pid2, signal.SIGTERM)

    def __prog_len3(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript1 = int(dic_pidss['1'])

        if self.__pid2 == pidscript1:
            pf = str(1)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript1:
                    list_pids.remove(list_pids[val])
                val += 1
            with open("saida.txt", "w") as wk:
                wk.write("")
            lista_nova = []
            lista_keys_nova = []
            for x in list_pids:
                dsa = str(x)
                lista_nova.append(dsa)
            for y in dic_pidss.keys():
                lista_keys_nova.append(y)

            salvar = lista_nova[0]
            salvar2 = lista_nova[1]
            keyssalvar = lista_keys_nova[0]
            keyssalvar2 = lista_keys_nova[1]

            with open("saida.txt", "a") as ww:
                ww.write(keyssalvar + ":" + salvar + ",")
                ww.write(keyssalvar2 + ":" + salvar2 + ",")

            os.kill(self.__pid2, signal.SIGTERM)
        else:
            os.kill(self.__pid2, signal.SIGTERM)

    def __prog_len1(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript1 = int(dic_pidss['1'])

        if self.__pid2 == pidscript1:
            pf = str(1)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript1:
                    list_pids.remove(list_pids[val])
                val += 1
            with open("saida.txt", "w") as wk:
                wk.write("")

            os.kill(self.__pid2, signal.SIGTERM)
        else:
            os.kill(self.__pid2, signal.SIGTERM)

    def __funcoes(self):
        __t1 = threading.Thread(target=self.__codigo_pid2)
        __t2 = threading.Thread(target=self.__programa)
        __t3 = threading.Thread(target=self.__tecla)

        __t1.start()
        __t2.start()
        __t3.start()

        __t1.join()
        __t2.join()
        __t3.join()


contagem1 = Script1()
