import os
import signal
import threading
import keyboard

testando = os.getpid()


def __tecla():
    while True:
        if keyboard.is_pressed('p'):
            while True:
                with open("comparando.txt", "r") as r:
                    vt = r.readline()
                    if vt != "":
                        # sleep(2)
                        try:
                            btk = int(vt)
                            try:
                                if btk == testando:
                                    try:
                                        with open("comparando.txt", "w") as wk:
                                            wk.write("")
                                        os.system(
                                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                            "Selecionar validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")

                                        with open("comparando.txt", "r") as pm:
                                            vtt = pm.readline()

                                        if vtt == "":
                                            print("Sem mais valores para matar, adeus")
                                            os.kill(btk, signal.SIGTERM)
                                        else:
                                            vmt = int(vtt)
                                            print("Matando o valor:", vmt)
                                            os.kill(vmt, signal.SIGTERM)
                                            with open("comparando.txt", "w") as wk:
                                                wk.write("")

                                            os.system(
                                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                                "Selecionar validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")
                                    except:
                                        print("erro doido")
                                else:
                                    print("Matando o valor:", btk)
                                    os.kill(btk, signal.SIGTERM)
                                    with open("comparando.txt", "w") as wk:
                                        wk.write("")

                                os.system(
                                    "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                    "validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")
                                # sleep(2)
                            except:
                                print("O programa já foi eliminado de outra forma, retirando-o da lista")
                                with open("comparando.txt", "w") as wk:
                                    wk.write("")
                                os.system(
                                    "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                    "validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")
                                # sleep(2)

                        except:
                            print("Erro ao converter o valor")
                            # print("Entrou no except")
                            # with open("comparando.txt", "w") as ww:
                            #     ww.write("")
                            #
                            # os.system(
                            #     "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao\" "
                            #     "/FO CSV /NH') do @echo %~P >> comparando.txt")
                            # # sleep(3)
                            #
                            # with open("comparando.txt", "r") as vd:
                            #     vdt = vd.readline()
                            #     # sleep(3)
                            #     if vdt == "" or vdt == btk:  # Colocar se aqui for igual a vazio ou a asd
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
                        with open("comparando.txt", "w") as ww2:
                            ww2.write("")
                        # sleep(2)
                        os.kill(testando, signal.SIGTERM)


def __funcoes():
    __t1 = threading.Thread(target=__tecla)
    __t1.start()
    __t1.join()


if __name__ == "__main__":
    __funcoes()
