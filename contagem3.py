import os
import threading
import keyboard
import signal
from time import sleep
import psutil


#Se ele não quiser igual da classe contagem2, essa está exatamente igual o que precisa estar na outra. Apenas muda o começo aqui do pid4, onde lá precisará colocar para proibir o pid do java.exe que não é possível fechar.
class Script3:
    __process_name = "node.exe"
    pid4 = None
    for __proc in psutil.process_iter():
        if __process_name in __proc.name():
            pid4 = __proc.pid
            break

    __pid4_l = [pid4]
    __pid42 = os.getpid()
    print("pid cmd", __pid42)
    print("pid programa js", pid4)

    def __init__(self):
        self.__funcoes()

    def __codigo_pid(self):
        with open('saida.txt', 'a') as f:
            for __passw in self.__pid4_l:
                __dicio3 = "3:{},".format(__passw)
                f.write(__dicio3)

    def __tecla(self):
        while True:
            if keyboard.is_pressed('p'):
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
                    os.kill(self.pid4, signal.SIGTERM)
                    self.__prog_len3(dic_pids)

                elif len(dic_pids) == 2:
                    os.kill(self.pid4, signal.SIGTERM)
                    self.__prog_len2(dic_pids)

                elif len(dic_pids) == 1:
                    os.kill(self.pid4, signal.SIGTERM)
                    self.__prog_len1(dic_pids)

    def __pararCmd(self):
        listaPids = []
        while True:
            sleep(3)
            for proc in psutil.process_iter():
                listaPids.append(proc.pid)

            try:
                indice = listaPids.index(self.pid4)
                print(indice)
            except:
                with open("saida.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
                    for x in r:
                        asd = x

                        dic_pidss = {}
                        pids = asd.split(',')
                        pids.remove(pids[-1])

                        for element in pids:
                            split_element = element.split(':')
                            dic_pidss.update({split_element[0]: split_element[1]})

                    try:
                        if len(dic_pidss) == 3:
                            self.__prog_len3(dic_pidss)

                        elif len(dic_pidss) == 2:
                            self.__prog_len2(dic_pidss)

                        elif len(dic_pidss) == 1:
                            self.__prog_len1(dic_pidss)

                    except:
                        os.kill(self.__pid42, signal.SIGTERM)

            listaPids.clear()

    def __prog_len1(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript3 = int(dic_pidss['3'])

        if self.pid4 == pidscript3:
            pf = str(3)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript3:
                    list_pids.remove(list_pids[val])
                val += 1
            with open("saida.txt", "w") as wk:
                wk.write("")

            os.kill(self.__pid42, signal.SIGTERM)
        else:
            os.kill(self.__pid42, signal.SIGTERM)

    def __prog_len2(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript3 = int(dic_pidss['3'])

        if self.pid4 == pidscript3:
            pf = str(3)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript3:
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

            os.kill(self.__pid42, signal.SIGTERM)
        else:
            os.kill(self.__pid42, signal.SIGTERM)

    def __prog_len3(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript3 = int(dic_pidss['3'])

        if self.pid4 == pidscript3:
            pf = str(3)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript3:
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

            os.kill(self.__pid42, signal.SIGTERM)
        else:
            os.kill(self.__pid42, signal.SIGTERM)

    def __funcoes(self):
        __t1 = threading.Thread(target=self.__codigo_pid)
        __t2 = threading.Thread(target=self.__tecla)
        __t3 = threading.Thread(target=self.__pararCmd)

        __t1.start()
        __t2.start()
        __t3.start()

        __t1.join()
        __t2.join()
        __t3.join()


programaNovo = Script3()
