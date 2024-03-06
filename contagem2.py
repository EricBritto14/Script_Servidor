import os
import threading
import keyboard
import signal
import psutil
from time import sleep



#1°Opção mas ruim, colocar #if __proc.pid != 8912: pra cada pid que não quer que salve
#2°Opção, tentar cada projeto, por exemplo .js salvar o pid em um bloco de notas, e depois tentar fazer um programa para ler o pid dentro do txt
#3°Opção, tentar procurar o cmd exato pelo TITLE diferente, ou algo assim.
#4°Opção, pelo proprio cmd sem ser pelo python
class Script2:
    __process_name = "java.exe"
    pid3 = []
    for __proc in psutil.process_iter():
        if __process_name in __proc.name():
            #if __proc.pid != 8912:
            pid3 = __proc.pid
            break

    __pid3l = [pid3]
    __pid32 = os.getpid()
    print("Segundo pid {}".format(__pid32))
    print("Pid programa java", pid3)

    def __init__(self):
        self.__funcoes()

    def __codigo_pid2(self):
        with open('saida.txt', 'a') as f:
            for __passw in self.__pid3l:
                __dicio2 = "2:{},".format(__passw)
                f.write(__dicio2)

    def __tecla(self):
        while True:
            if keyboard.is_pressed('o'):
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
                    os.kill(self.pid3, signal.SIGTERM)
                    self.__prog_len3(dic_pids)

                elif len(dic_pids) == 2:
                    os.kill(self.pid3, signal.SIGTERM)
                    self.__prog_len2(dic_pids)

                elif len(dic_pids) == 1:
                    #os.kill(self.pid3, signal.SIGTERM)
                    self.__prog_len1(dic_pids, self.__process_name)

    def __pararCMD(self):
        listaPids = []
        while True:
            sleep(3)
            for proc in psutil.process_iter():
                listaPids.append(proc.pid)

            try:
                indice = listaPids.index(self.pid3)
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
                            self.__prog_len1(dic_pidss, self.__process_name)
                    except:
                        os.kill(self.__pid32, signal.SIGTERM)

            listaPids.clear()

    def __prog_len2(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript2 = int(dic_pidss['2'])

        if self.pid3 == pidscript2:
            pf = str(2)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript2:
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

            os.kill(self.__pid32, signal.SIGTERM)
        else:
            os.kill(self.__pid32, signal.SIGTERM)

    def __prog_len3(self, dic_pidss):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript2 = int(dic_pidss['2'])

        if self.pid3 == pidscript2:
            pf = str(2)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript2:
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

            os.kill(self.__pid32, signal.SIGTERM)
        else:
            os.kill(self.__pid32, signal.SIGTERM)

    def __prog_len1(self, dic_pidss, __prog):
        list_pids = []
        list_keys = []
        for key in dic_pidss.keys():
            list_pids.append(int(dic_pidss[key]))
            list_keys.append(key)

        pidscript2 = int(dic_pidss['2'])

        if self.pid3 == pidscript2:
            pf = str(2)
            dic_pidss.pop(pf)
            val = 0
            for x in list_pids:
                if x == pidscript2:
                    list_pids.remove(list_pids[val])
                val += 1
            with open("saida.txt", "w") as wk:
                wk.write("")

            self.mata_o_programa(__prog)

        else:
            os.kill(self.__pid32, signal.SIGTERM)

    def mata_o_programa(self, __prog_name):
        #Se o Cleber garantir que é só 1 programa que terá o mesmo nome, não tem necessidade dessa função
        #Ou se ele quiser apenas que proíba 1 programa que terá o mesmo nome, da pra fazer a gambiarra do != e o pid
        #Essa função pega todos os java.exe e mata, e se não conseguir matar algum, pula pro próximo. Assim lá no começo também não tem necessidade de saber qual é o pid certo dos vários javas abertos, já que vai fechar todos.
        pid4r = None
        try:
            for __proc in psutil.process_iter():
                if __prog_name in __proc.name():
                    pid4r = __proc.pid
                    os.kill(pid4r, signal.SIGTERM)
                    print("matando")
        except:
            print("Pegou algum programa que precisa de permissão para matar, pulando o programa {}".format(pid4r))
            for __proc in psutil.process_iter():
                if __prog_name in __proc.name():
                    if __proc.pid != pid4r:
                        pid4r2 = __proc.pid
                        os.kill(pid4r2, signal.SIGTERM)
                        print("matando")
        finally:
            os.kill(self.__pid32, signal.SIGTERM)

    def __funcoes(self):
        __t1 = threading.Thread(target=self.__codigo_pid2)
        __t2 = threading.Thread(target=self.__tecla)
        __t3 = threading.Thread(target=self.__pararCMD)

        __t1.start()
        __t2.start()
        __t3.start()

        __t1.join()
        __t2.join()
        __t3.join()


contagem2 = Script2()
