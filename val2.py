import os
import signal
import threading
import time
from time import sleep
import keyboard

# salvando
testando = os.getpid()
print("valor", testando)

# print("dxa eu ve", testando)
# PROCURAR PELO NOME E MATAR TDO, INDEPENDENTE DO PID, N PRECISA SALVAR
# def main():
#     with open("comparando.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
#         for k in r:
#             vt = k


# while vt == vz:
#     os.system(
#         "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao*\" /FO CSV /NH') do @echo %~P >> comparando.txt")
#     os.system("start cmd /c S:/PM/ter/ets/Inter_Setor/COMPARTILHADO/APRENDIZES/MEIO_OFICIAIS/LETICIACAPOVILA/Projeto/bats/executa3v2.bat")
#
# with open("comparando.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
#     for y in r:
#         vt = y
#
# with open("valiteste.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
#     for x in r:
#         pp = x
#
# if vt != pp:
#     os.system(
#         "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao*\" /FO CSV /NH') do @echo %~P >> valiteste.txt")
#
# sleep(5)
# with open("comparando.txt", "w") as kv:  # Código para abrir o bloco de notas, e 'r' para read
#     kv.write("")

def tecla():
    while True:
        if keyboard.is_pressed('r'):
            while True:
                with open("comparando2.txt", "r") as r:
                    ktv = r.readline()
                    if ktv != "":
                        sleep(2)
                        try:
                            btk2 = int(ktv)
                            try:
                                print("Matando o valor:", btk2)
                                os.kill(btk2, signal.SIGTERM)
                                with open("comparando2.txt", "w") as wk:
                                    wk.write("")
                            except:
                                print("O programa já foi eliminado de outra forma, retirando-o da lista")
                                with open("comparando2.txt", "w") as wk:
                                    wk.write("")
                                os.system(
                                    "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                                sleep(2)

                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                            sleep(2)
                        except:
                            print("Entrou no except")
                            sleep(3)
                            with open("comparando2.txt", "w") as ww:
                                ww.write("")

                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                            sleep(3)

                            with open("comparando2.txt", "r") as vd:
                                vdt = vd.readline()
                                sleep(3)
                                if vdt == "" or vdt == btk2:  # Colocar se aqui for igual a vazio ou a asd
                                    print("Sem mais valores para matar, adeus")
                                    sleep(4)
                                    os.kill(testando, signal.SIGTERM)
                                if vdt != "":
                                    ads = int(vdt)
                                    print("matou pelo except")
                                    sleep(20)
                                    os.kill(ads, signal.SIGTERM)
                    else:
                        while True:
                            with open("comparando2.txt", "w") as ww:
                                ww.write("")

                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq Selecionar validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                            sleep(3)

                            with open("comparando2.txt", "r") as vd:
                                vdt = vd.readline()
                                sleep(3)
                                if vdt != "":
                                    ads = int(vdt)
                                    print("matou pelo except")
                                    sleep(3)
                                    os.kill(ads, signal.SIGTERM)
                                else:
                                    print("Sem mais valores para matar, adeus")
                                    sleep(2)
                                    os.kill(testando, signal.SIGTERM)

#Teste Selecionar validacao
    # while True:
    #     if keyboard.is_pressed('p'):
    #         while True:
    #             try:
    #                 with open("comparando.txt", "r") as r:
    #                     vt = r.readline()
    #                     if vt != "":
    #                         sleep(2)
    #                         btk = int(vt)
    #                         try:
    #                             print("Matando o valor:", btk)
    #                             os.kill(btk, signal.SIGTERM)
    #                             with open("comparando.txt", "w") as wk:
    #                                 wk.write("")
    #                         except:
    #                             print("O programa já foi eliminado de outra forma, retirando-o da lista")
    #                             with open("comparando.txt", "w") as wk:
    #                                 wk.write("")
    #
    #                         os.system("@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao*\" /FO CSV /NH') do @echo %~P >> comparando.txt")
    #                         sleep(2)
    #             except:
    #                 print("Entrou no except")
    #                 sleep(3)
    #                 with open("comparando.txt", "w") as ww:
    #                     ww.write("")
    #
    #                 os.system(
    #                     "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq Selecionar validacao*\" /FO CSV /NH') do @echo %~P >> comparando.txt")
    #                 sleep(3)
    #
    #                 with open("comparando.txt", "r") as vd:
    #                     vdt = vd.readline()
    #                     sleep(3)
    #                     if vdt != "":
    #                         sleep(2)
    #                         btkk = int(vdt)
    #                         try:
    #                             print("Matando o valor:", btkk)
    #                             os.kill(btkk, signal.SIGTERM)
    #                             with open("comparando.txt", "w") as wk:
    #                                 wk.write("")
    #                         except:
    #                             print("O programa já foi eliminado de outra forma, retirando-o da lista")
    #                             with open("comparando.txt", "w") as wk:
    #                                 wk.write("")
    #
    #                     else:
    #                         print("Sem mais valores para matar, adeus")
    #                         sleep(2)
    #                         os.kill(testando, signal.SIGTERM)




# def limpa_o_primeiro():
#     with open("comparando.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
#         for x in r:
#             kv = int(x)
#             print("qual o valor", kv)
#             os.kill(kv, signal.SIGTERM)

# with open("valiteste.txt", "w") as wk:
#     wk.write("")

# else:
#     os.kill(self.__pid32, signal.SIGTERM)

# dic_pids = {}
# pids = asd.split(',')
# pids.remove(pids[-1])
#
# for element in pids:
#     split_element = element.split(':')
#     dic_pids.update({split_element[0]: split_element[1]})

# if len(dic_pids) == 3:
#     os.kill(self.pid4, signal.SIGTERM)
#     self.__prog_len3(dic_pids)
#
# elif len(dic_pids) == 2:
#     os.kill(self.pid4, signal.SIGTERM)
#     self.__prog_len2(dic_pids)
#
# elif len(dic_pids) == 1:
#     os.kill(self.pid4, signal.SIGTERM)
#     self.__prog_len1(dic_pids)


# def __pararCmd(self):
#     listaPids = []
#     while True:
#         sleep(3)
#         for proc in psutil.process_iter():
#             listaPids.append(proc.pid)
#
#         try:
#             indice = listaPids.index(self.pid4)
#             print(indice)
#         except:
#             with open("saida.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
#                 for x in r:
#                     asd = x
#
#                     dic_pidss = {}
#                     pids = asd.split(',')
#                     pids.remove(pids[-1])
#
#                     for element in pids:
#                         split_element = element.split(':')
#                         dic_pidss.update({split_element[0]: split_element[1]})
#
#                 try:
#                     if len(dic_pidss) == 3:
#                         self.__prog_len3(dic_pidss)
#
#                     elif len(dic_pidss) == 2:
#                         self.__prog_len2(dic_pidss)
#
#                     elif len(dic_pidss) == 1:
#                         self.__prog_len1(dic_pidss)
#
#                 except:
#                     os.kill(self.__pid42, signal.SIGTERM)
#
#         listaPids.clear()


def funcoes():
    # t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=tecla)
    # t3 = threading.Thread(target=self.__pararCmd)
    # t3 = threading.Thread(target=limpa_o_primeiro())

    # t1.start()
    t2.start()
    # t3.start()

    # t1.join()
    t2.join()
    # t3.join()


if __name__ == "__main__":
    funcoes()
