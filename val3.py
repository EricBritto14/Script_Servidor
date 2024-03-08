import os
import signal
import threading
import keyboard

testando = os.getpid()
print("valor", testando)


def __tecla():
    while True:
        if keyboard.is_pressed('u'):
            while True:
                with open("comparando3.txt", "r") as r:
                    ktv = r.readline()
                    if ktv != "":
                        # sleep(2)
                        try:
                            btk2 = int(ktv)
                            try:
                                if btk2 == testando:
                                    try:
                                        with open("comparando3.txt", "w") as wk:
                                            wk.write("")
                                        os.system(
                                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                            "Selecionar validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")

                                        with open("comparando3.txt", "r") as pm:
                                            vtt = pm.readline()

                                        if vtt == "":
                                            print("Sem mais valores para matar, adeus")
                                            os.kill(btk2, signal.SIGTERM)
                                        else:
                                            vmt = int(vtt)
                                            print("Matando o valor:", vmt)
                                            os.kill(vmt, signal.SIGTERM)
                                            with open("comparando3.txt", "w") as wk:
                                                wk.write("")

                                            os.system(
                                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                                "Selecionar validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                                    except:
                                        print("erro doido")
                                else:
                                    print("Matando o valor:", btk2)
                                    os.kill(btk2, signal.SIGTERM)
                                    with open("comparando3.txt", "w") as wk:
                                        wk.write("")

                                        os.system(
                                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                            "validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                                        # sleep(2)

                            except:
                                print("O programa já foi eliminado de outra forma, retirando-o da lista")
                                with open("comparando3.txt", "w") as wk:
                                    wk.write("")
                                os.system(
                                    "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                    "validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                                # sleep(2)
                        except:
                            print("Erro ao converter o valor")
                            # sleep(3)
                            # with open("comparando3.txt", "w") as ww:
                            #     ww.write("")
                            #
                            # os.system(
                            #     "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                            #     "validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                            # # sleep(3)
                            #
                            # with open("comparando3.txt", "r") as vd:
                            #     vdt = vd.readline()
                            #     # sleep(3)
                            #     if vdt == "" or vdt == btk2:  # Colocar se aqui for igual a vazio ou a asd
                            #         print("Sem mais valores para matar, adeus")
                            #         # sleep(4)
                            #         os.kill(testando, signal.SIGTERM)
                            #     if vdt != "":
                            #         ads = int(vdt)
                            #         print("matou pelo except")
                            #         # sleep(20)
                            #         os.kill(ads, signal.SIGTERM)
                    else:
                        print("Sem mais valores para matar, adeus \n")
                        with open("comparando3.txt", "w") as ww2:
                            ww2.write("")
                        # sleep(2)
                        os.kill(testando, signal.SIGTERM)


def __funcoes():
    __t1 = threading.Thread(target=__tecla)
    __t1.start()
    __t1.join()


if __name__ == "__main__":
    __funcoes()
