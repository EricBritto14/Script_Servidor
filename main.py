import os
import signal
import threading
import keyboard
from guia import Guia
import inquirer


class Programa:
    def __init__(self):
        self.__funcoes()

    def __menu(self):
        pid = os.getpid()
        while True:
            try:
                questions = [
                    inquirer.List("fazer", message="O que você gostaria de fazer?",
                                  choices=["Iniciar um Software", "Parar um Software", "Sair", "Limpar"]),
                ]
                answers = inquirer.prompt(questions)

                if answers['fazer'] == 'Iniciar um Software':
                    os.system('cls')
                    self.__iniciaProgramas()
                elif answers['fazer'] == "Parar um Software":
                    os.system('cls')
                    self.__fechaProgramas()
                elif answers['fazer'] == "Sair":
                    print("Adeus")
                    os.system('cls')
                    os.kill(pid, signal.SIGTERM)

                elif answers['fazer'] == "Limpar":
                    print("Limpo!")
                    with open("comparando.txt", "w") as w, \
                            open("comparando2.txt", "w") as ww, \
                            open("comparando3.txt", "w") as www:
                        w.write("")
                        ww.write("")
                        www.write("")
            except:
                print("Erro no menu!")

    @staticmethod
    def __tecla():
        while True:
            if keyboard.is_pressed('k'):
                os._exit(0)

    def __iniciaProgramas(self):
        try:
            guia = Guia()
            with open("comparando.txt", "r") as r, \
                    open("comparando2.txt", "r") as rr, \
                    open("comparando3.txt", "r") as rrr:  # Código para abrir o bloco de notas, e 'r' para read
                ppp = r.readline()  # Programa val3 (validação3)
                pp = rr.readline()  # Programa val2 (validacao2)
                p = rrr.readline()  # Programa val1 (validacao)
                try:
                    if p == "" and pp == "" and ppp == "":
                        questionsII = [
                            inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                          choices=["Contagem V1", "Contagem V2", "Contagem V3"])
                        ]
                        answersII = inquirer.prompt(questionsII)

                        if answersII['iniciar'] == "Contagem V1":
                            guia._executavel()
                        elif answersII['iniciar'] == "Contagem V2":
                            guia._executavel2()
                        elif answersII['iniciar'] == "Contagem V3":
                            guia._executavel3()
                        else:
                            print("Software não disponível")
                    elif p == "" and pp == "" and ppp != "":
                        questionsII = [
                            inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                          choices=["Contagem V1", "Contagem V2"])
                        ]
                        answersII = inquirer.prompt(questionsII)

                        if answersII['iniciar'] == "Contagem V1":
                            guia._executavel()
                        elif answersII['iniciar'] == "Contagem V2":
                            guia._executavel2()
                        else:
                            print("Software não disponível")
                    elif p == "" and pp != "" and ppp == "":
                        questionsII = [
                            inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                          choices=["Contagem V1", "Contagem V3"])
                        ]
                        answersII = inquirer.prompt(questionsII)

                        if answersII['iniciar'] == "Contagem V1":
                            guia._executavel()
                        elif answersII['iniciar'] == "Contagem V3":
                            guia._executavel3()
                        else:
                            print("Software não disponível")
                    elif p == "" and pp != "" and ppp != "":
                        questionsII = [
                            inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                          choices=["Contagem V1"])
                        ]
                        answersII = inquirer.prompt(questionsII)

                        if answersII['iniciar'] == "Contagem V1":
                            guia._executavel()
                        else:
                            print("Software não disponível")

                    elif p != "" and pp == "" and ppp == "":
                        questionsII = [
                            inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                          choices=["Contagem V2", "Contagem V3"])
                        ]
                        answersII = inquirer.prompt(questionsII)

                        if answersII['iniciar'] == "Contagem V2":
                            guia._executavel2()
                        elif answersII['iniciar'] == "Contagem V3":
                            guia._executavel3()
                        else:
                            print("Software não disponível")
                    elif p != "" and pp == "" and ppp != "":
                        questionsII = [
                            inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                          choices=["Contagem V2"])
                        ]
                        answersII = inquirer.prompt(questionsII)

                        if answersII['iniciar'] == "Contagem V2":
                            guia._executavel2()
                        else:
                            print("Software não disponível")
                    elif p != "" and pp != "" and ppp == "":
                        questionsII = [
                            inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                          choices=["Contagem V3"])
                        ]
                        answersII = inquirer.prompt(questionsII)

                        if answersII['iniciar'] == "Contagem V3":
                            guia._executavel3()
                        else:
                            print("Software não disponível")
                    else:
                        print("Erro nas escolhas")
                except:
                    print("Erro ao iniciar o programa")
        except:
            print("Erro ao escolher o programa")

    def __programa1(self):
        while True:
            with open("comparando3.txt", "r") as r:
                pp = r.readline()
                if pp != "":
                    # sleep(2)
                    try:
                        print("Matando o valor:", pp)
                        btk3 = int(pp)
                        os.kill(btk3, signal.SIGTERM)
                        with open("comparando3.txt", "w") as wk:
                            wk.write("")

                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                        # sleep(2)
                        with open("comparando3.txt", "r") as mma:
                            asdwr = mma.readline()

                        if asdwr == "":
                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                "Selecionar validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")

                    except:
                        print("O programa já foi eliminado de outra forma, retirando-o da lista")
                        with open("comparando3.txt", "w") as wk:
                            wk.write("")
                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                        # sleep(2)
                        with open("comparando3.txt", "r") as r:
                            vd = r.readline()

                        if vd == "":
                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                "Selecionar validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")


                else:
                    print("Sem mais valores para matar, adeus \n")
                    with open("comparando3.txt", "w") as wk:
                        wk.write("")
                    break

    def __programa2(self):
        while True:
            with open("comparando2.txt", "r") as rm:
                pp = rm.readline()
                if pp != "":
                    # sleep(2)
                    try:
                        print("Matando o valor:", pp)
                        btk33 = int(pp)
                        os.kill(btk33, signal.SIGTERM)
                        with open("comparando2.txt", "w") as wkl:
                            wkl.write("")

                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                        with open("comparando2.txt", "r") as mmaw:
                            mam = mmaw.readline()

                        if mam == "":
                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                "Selecionar validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")

                    except:
                        print("O programa já foi eliminado de outra forma, retirando-o da lista")
                        with open("comparando2.txt", "w") as wkv:
                            wkv.write("")
                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                        ##sleep(2)
                        with open("comparando2.txt", "r") as r:
                            vd = r.readline()

                        if vd == "":
                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                "Selecionar validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")

                else:
                    print("Sem mais valores para matar, adeus \n")
                    with open("comparando2.txt", "w") as wk:
                        wk.write("")
                    break

    def __programa3(self):
        while True:
            with open("comparando.txt", "r") as r:
                ppp = r.readline()
                if ppp != "":
                    # sleep(2)
                    try:
                        print("Matando o valor:", ppp)
                        btk3 = int(ppp)
                        os.kill(btk3, signal.SIGTERM)
                        with open("comparando.txt", "w") as wk:
                            wk.write("")

                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")
                        with open("comparando.txt", "r") as rswas:
                            mom = rswas.readline()

                        if mom == "":
                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                "Selecionar validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")

                    except:
                        print("O programa já foi eliminado de outra forma, retirando-o da lista")
                        with open("comparando.txt", "w") as wk:
                            wk.write("")
                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")
                        # sleep(2)
                        with open("comparando.txt", "r") as r:
                            vd = r.readline()

                        if vd == "":
                            os.system(
                                "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq "
                                "Selecionar validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")

                else:
                    print("Sem mais valores para matar, adeus \n")
                    with open("comparando.txt", "w") as wk:
                        wk.write("")
                    break

    def __fechaProgramas(self):
        try:
            with open("comparando3.txt", "r") as r, \
                    open("comparando2.txt", "r") as rr, \
                    open("comparando.txt", "r") as rrr:
                p = r.readline()
                pp = rr.readline()
                ppp = rrr.readline()

            if p != "" and pp != "" and ppp != "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V1", "Contagem V2", "Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.__programa1()

                elif answersI['parar'] == "Contagem V2":
                    self.__programa2()

                elif answersI['parar'] == "Contagem V3":
                    self.__programa3()
                else:
                    print("Escolha uma das três opções!")

            elif p != "" and pp != "" and ppp == "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V1", "Contagem V2"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.__programa1()

                elif answersI['parar'] == "Contagem V2":
                    self.__programa2()
                else:
                    print("Escolha uma das opções!")

            elif p != "" and pp == "" and ppp != "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V1", "Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.__programa1()

                elif answersI['parar'] == "Contagem V3":
                    self.__programa3()
                else:
                    print("Escolha uma das opções!")

            elif p == "" and pp != "" and ppp != "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V2", "Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V2":
                    self.__programa2()

                elif answersI['parar'] == "Contagem V3":
                    self.__programa3()
                else:
                    print("Escolha uma das opções!")

            elif p != "" and pp == "" and ppp == "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V1"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.__programa1()

                else:
                    print("Escolha a opção do modo certo!")

            elif p == "" and pp != "" and ppp == "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V2"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V2":
                    self.__programa2()

                else:
                    print("Escolha a opção do modo certo!")

            elif p == "" and pp == "" and ppp != "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V3":
                    self.__programa3()

                else:
                    print("Escolha a opção do modo certo!")

            else:
                print("Inicie um programa antes de tentar fechar!")
        except:
            print("Inicie um programa antes de tentar fechar!")

    def __funcoes(self):
        __t1 = threading.Thread(target=self.__menu)
        __t2 = threading.Thread(target=self.__tecla)
        __t1.start()
        __t2.start()
        __t1.join()
        __t2.join()


menu = Programa()
