import os
import signal
import threading
import keyboard
from guia import Guia
import inquirer
import time
from time import sleep


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
                    with open("saida.txt", "w") as w:
                        w.write("")

                    with open("comparando.txt", "w") as ww:
                        ww.write("")
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
            with open("saida.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
                pp = r.readline()
                if pp == "":
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
                else:
                    with open("saida.txt", "r") as rr:
                        for x in rr:
                            asd = x

                        dic_pids = {}
                        pids = asd.split(',')
                        pids.remove(pids[-1])

                        for element in pids:
                            split_element = element.split(':')
                            dic_pids.update({split_element[0]: split_element[1]})

                    if len(dic_pids) == 3:
                        list_keys = []
                        list_pids = []
                        for key in dic_pids.keys():
                            list_pids.append(int(dic_pids[key]))
                            list_keys.append(key)

                        pidscript1 = int(dic_pids['1'])
                        pidscript2 = int(dic_pids['2'])
                        pidscript3 = int(dic_pids['3'])

                        if pidscript1 and pidscript2 and pidscript3 is not None:
                            print("Todos os softwares estão abertos!")

                    elif len(dic_pids) == 2:
                        list_keys = []
                        for key in dic_pids.keys():
                            list_keys.append(key)

                        script1 = int(list_keys[0])
                        script2 = int(list_keys[1])

                        if script1 == 1 and script2 == 2 or script1 == 2 and script2 == 1:
                            questionsIII = [
                                inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                              choices=["Contagem V3"])
                            ]
                            answersIII = inquirer.prompt(questionsIII)

                            if answersIII['iniciar'] == "Contagem V3":
                                guia._executavel3()
                            else:
                                print("Software não disponível")

                        elif script1 == 1 and script2 == 3 or script1 == 3 and script2 == 1:
                            questionsIV = [
                                inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                              choices=["Contagem V2"])
                            ]
                            answersIV = inquirer.prompt(questionsIV)

                            if answersIV['iniciar'] == "Contagem V2":
                                guia._executavel2()
                            else:
                                print("Software não disponível")

                        elif script1 == 2 and script2 == 3 or script1 == 3 and script2 == 2:
                            questionsV = [
                                inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                              choices=["Contagem V1"])
                            ]
                            answersV = inquirer.prompt(questionsV)

                            if answersV['iniciar'] == "Contagem V1":
                                guia._executavel()
                            else:
                                print("Software não disponível")

                    elif len(dic_pids) == 1:  # ao contrário 1 tem q ter todas as condições
                        list_keys = []
                        for key in dic_pids.keys():
                            list_keys.append(key)

                        script1 = int(list_keys[0])

                        if script1 == 1:
                            questionsVI = [
                                inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                              choices=["Contagem V2", "Contagem V3"])
                            ]
                            answersVI = inquirer.prompt(questionsVI)

                            if answersVI['iniciar'] == "Contagem V2":
                                guia._executavel2()

                            elif answersVI['iniciar'] == "Contagem V3":
                                guia._executavel3()

                            else:
                                print("Software não disponível")

                        elif script1 == 2:
                            questionsVII = [
                                inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                              choices=["Contagem V1", "Contagem V3"])
                            ]
                            answersVII = inquirer.prompt(questionsVII)

                            if answersVII['iniciar'] == "Contagem V1":
                                guia._executavel()

                            elif answersVII['iniciar'] == "Contagem V3":
                                guia._executavel3()

                            else:
                                print("Software não disponível")

                        elif script1 == 3:
                            questionsVIII = [
                                inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
                                              choices=["Contagem V1", "Contagem V2"])
                            ]
                            answersVIII = inquirer.prompt(questionsVIII)

                            if answersVIII['iniciar'] == "Contagem V1":
                                guia._executavel()

                            elif answersVIII['iniciar'] == "Contagem V2":
                                guia._executavel2()

                            else:
                                print("Software não disponível")
                        else:
                            print("Erro nas escolhas")
        except:
            print("Erro ao iniciar o programa")

    # def __iniciaProgramas(self):
    #     try:
    #         guia = Guia()
    #         with open("saida.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
    #             pp = r.readline()
    #             if pp == "":
    #                 questionsII = [
    #                     inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
    #                                   choices=["Contagem V1", "Contagem V2", "Contagem V3"])
    #                 ]
    #                 answersII = inquirer.prompt(questionsII)
    #
    #                 if answersII['iniciar'] == "Contagem V1":
    #                     guia._executavel()
    #                 elif answersII['iniciar'] == "Contagem V2":
    #                     guia._executavel2()
    #                 elif answersII['iniciar'] == "Contagem V3":
    #                     guia._executavel3()
    #                 else:
    #                     print("Software não disponível")
    #             else:
    #                 with open("saida.txt", "r") as rr:
    #                     for x in rr:
    #                         asd = x
    #
    #                     dic_pids = {}
    #                     pids = asd.split(',')
    #                     pids.remove(pids[-1])
    #
    #                     for element in pids:
    #                         split_element = element.split(':')
    #                         dic_pids.update({split_element[0]: split_element[1]})
    #
    #                 if len(dic_pids) == 3:
    #                     list_keys = []
    #                     list_pids = []
    #                     for key in dic_pids.keys():
    #                         list_pids.append(int(dic_pids[key]))
    #                         list_keys.append(key)
    #
    #                     pidscript1 = int(dic_pids['1'])
    #                     pidscript2 = int(dic_pids['2'])
    #                     pidscript3 = int(dic_pids['3'])
    #
    #                     if pidscript1 and pidscript2 and pidscript3 is not None:
    #                         print("Todos os softwares estão abertos!")
    #
    #                 elif len(dic_pids) == 2:
    #                     list_keys = []
    #                     for key in dic_pids.keys():
    #                         list_keys.append(key)
    #
    #                     script1 = int(list_keys[0])
    #                     script2 = int(list_keys[1])
    #
    #                     if script1 == 1 and script2 == 2 or script1 == 2 and script2 == 1:
    #                         questionsIII = [
    #                             inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
    #                                           choices=["Contagem V3"])
    #                         ]
    #                         answersIII = inquirer.prompt(questionsIII)
    #
    #                         if answersIII['iniciar'] == "Contagem V3":
    #                             guia._executavel3()
    #                         else:
    #                             print("Software não disponível")
    #
    #                     elif script1 == 1 and script2 == 3 or script1 == 3 and script2 == 1:
    #                         questionsIV = [
    #                             inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
    #                                           choices=["Contagem V2"])
    #                         ]
    #                         answersIV = inquirer.prompt(questionsIV)
    #
    #                         if answersIV['iniciar'] == "Contagem V2":
    #                             guia._executavel2()
    #                         else:
    #                             print("Software não disponível")
    #
    #                     elif script1 == 2 and script2 == 3 or script1 == 3 and script2 == 2:
    #                         questionsV = [
    #                             inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
    #                                           choices=["Contagem V1"])
    #                         ]
    #                         answersV = inquirer.prompt(questionsV)
    #
    #                         if answersV['iniciar'] == "Contagem V1":
    #                             guia._executavel()
    #                         else:
    #                             print("Software não disponível")
    #
    #                 elif len(dic_pids) == 1:  # ao contrário 1 tem q ter todas as condições
    #                     list_keys = []
    #                     for key in dic_pids.keys():
    #                         list_keys.append(key)
    #
    #                     script1 = int(list_keys[0])
    #
    #                     if script1 == 1:
    #                         questionsVI = [
    #                             inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
    #                                           choices=["Contagem V2", "Contagem V3"])
    #                         ]
    #                         answersVI = inquirer.prompt(questionsVI)
    #
    #                         if answersVI['iniciar'] == "Contagem V2":
    #                             guia._executavel2()
    #
    #                         elif answersVI['iniciar'] == "Contagem V3":
    #                             guia._executavel3()
    #
    #                         else:
    #                             print("Software não disponível")
    #
    #                     elif script1 == 2:
    #                         questionsVII = [
    #                             inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
    #                                           choices=["Contagem V1", "Contagem V3"])
    #                         ]
    #                         answersVII = inquirer.prompt(questionsVII)
    #
    #                         if answersVII['iniciar'] == "Contagem V1":
    #                             guia._executavel()
    #
    #                         elif answersVII['iniciar'] == "Contagem V3":
    #                             guia._executavel3()
    #
    #                         else:
    #                             print("Software não disponível")
    #
    #                     elif script1 == 3:
    #                         questionsVIII = [
    #                             inquirer.List("iniciar", message="Iniciar um Software - Qual software?",
    #                                           choices=["Contagem V1", "Contagem V2"])
    #                         ]
    #                         answersVIII = inquirer.prompt(questionsVIII)
    #
    #                         if answersVIII['iniciar'] == "Contagem V1":
    #                             guia._executavel()
    #
    #                         elif answersVIII['iniciar'] == "Contagem V2":
    #                             guia._executavel2()
    #
    #                         else:
    #                             print("Software não disponível")
    #                     else:
    #                         print("Erro nas escolhas")
    #     except:
    #         print("Erro ao iniciar o programa")


    def programa1(self):
        while True:
            with open("comparando3.txt", "r") as r:
                pp = r.readline()
                if pp != "":
                    sleep(2)
                    try:
                        print("Matando o valor:", pp)
                        btk3 = int(pp)
                        os.kill(btk3, signal.SIGTERM)
                        with open("comparando3.txt", "w") as wk:
                            wk.write("")

                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                        sleep(2)

                    except:
                        print("O programa já foi eliminado de outra forma, retirando-o da lista")
                        with open("comparando3.txt", "w") as wk:
                            wk.write("")
                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")
                        sleep(2)


                else:
                    print("Sem mais valores para matar, adeus \n")
                    with open("comparando3.txt", "w") as wk:
                        wk.write("")
                    break

    def programa2(self):
        while True:
            with open("comparando2.txt", "r") as r:
                pp = r.readline()
                if pp != "":
                    sleep(2)
                    try:
                        print("Matando o valor:", pp)
                        btk3 = int(pp)
                        os.kill(btk3, signal.SIGTERM)
                        with open("comparando2.txt", "w") as wk:
                            wk.write("")

                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                        sleep(2)

                    except:
                        print("O programa já foi eliminado de outra forma, retirando-o da lista")
                        with open("comparando2.txt", "w") as wk:
                            wk.write("")
                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")
                        sleep(2)

                else:
                    print("Sem mais valores para matar, adeus \n")
                    with open("comparando2.txt", "w") as wk:
                        wk.write("")
                    break

    def programa3(self):
        while True:
            with open("comparando.txt", "r") as r:
                ppp = r.readline()
                if ppp != "":
                    sleep(2)
                    try:
                        print("Matando o valor:", ppp)
                        btk3 = int(ppp)
                        os.kill(btk3, signal.SIGTERM)
                        with open("comparando.txt", "w") as wk:
                            wk.write("")

                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")
                        sleep(2)

                    except:
                        print("O programa já foi eliminado de outra forma, retirando-o da lista")
                        with open("comparando.txt", "w") as wk:
                            wk.write("")
                        os.system(
                            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")
                        sleep(2)

                else:
                    print("Sem mais valores para matar, adeus \n")
                    with open("comparando.txt", "w") as wk:
                        wk.write("")
                    break
    def __fechaProgramas(self):
        try:
            with open("comparando3.txt", "r") as r:
                p = r.readline()
            with open("comparando2.txt", "r") as rr:
                pp = rr.readline()
            with open("comparando.txt", "r") as rrr:
                ppp = rrr.readline()

            if p != "" and pp != "" and ppp != "":
                questionsI = [
                        inquirer.List("parar", message="Parada um Software - Qual software?",
                                      choices=["Contagem V1", "Contagem V2", "Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.programa1()

                elif answersI['parar'] == "Contagem V2":
                    self.programa2()

                elif answersI['parar'] == "Contagem V3":
                    self.programa3()
                else:
                    print("Escolha uma das três opções!")

            elif p != "" and pp != "" and ppp == "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V1", "Contagem V2"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.programa1()

                elif answersI['parar'] == "Contagem V2":
                    self.programa2()
                else:
                    print("Escolha uma das opções!")

            elif p != "" and pp == "" and ppp != "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V1", "Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.programa1()

                elif answersI['parar'] == "Contagem V3":
                    self.programa3()
                else:
                    print("Escolha uma das opções!")

            elif p == "" and pp != "" and ppp != "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V2", "Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V2":
                    self.programa2()

                elif answersI['parar'] == "Contagem V3":
                    self.programa3()
                else:
                    print("Escolha uma das opções!")

            elif p != "" and pp == "" and ppp == "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V1"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V1":
                    self.programa1()

                else:
                    print("Escolha a opção do modo certo!")

            elif p == "" and pp != "" and ppp == "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V2"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V2":
                    self.programa2()

                else:
                    print("Escolha a opção do modo certo!")

            elif p == "" and pp == "" and ppp != "":
                questionsI = [
                    inquirer.List("parar", message="Parada um Software - Qual software?",
                                  choices=["Contagem V3"])
                ]

                answersI = inquirer.prompt(questionsI)

                if answersI['parar'] == "Contagem V3":
                    self.programa3()

                else:
                    print("Escolha a opção do modo certo!")

            else:
                print("Erro nas escolhas")
        except:
            print("Inicie um programa antes de tentar fechar!")


            # with open("saida.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
            #     for x in r:
            #         asd = x
            #
            #         dic_pids = {}
            #         pids = asd.split(',')
            #         pids.remove(pids[-1])

                    # essa não chave_comparadora = ''
                    #essa não pid_salvo = ''

                    # for element in pids:
                    #     split_element = element.split(':')

                        # essa não if chave_comparadora == split_element[0]:
                        #    essa não dic_pids.update({'duplicata': pid_salvo})

                        # dic_pids.update({split_element[0]: split_element[1]})

                        # essa não chave_comparadora = split_element[0]
                        # essa não pid_salvo = split_element[1]

            # if len(dic_pids) == 3:
            #     list_keys = []
            #     list_pids = []
            #     for key in dic_pids.keys():
            #         list_pids.append(int(dic_pids[key]))
            #         list_keys.append(key)
            #
            #     pidscript1 = int(dic_pids['1'])
            #     pidscript2 = int(dic_pids['2'])
            #     pidscript3 = int(dic_pids['3'])
            #
            #     questionsI = [
            #         inquirer.List("parar", message="Parada um Software - Qual software?",
            #                       choices=["Contagem V1", "Contagem V2", "Contagem V3"])
            #     ]
            #     answersI = inquirer.prompt(questionsI)
            #
            #     if answersI['parar'] == "Contagem V1":
            #         try:
            #             os.kill(pidscript1, signal.SIGTERM)
            #             print("Programa Contagem V1 selecionado foi finalizado.\n")
            #             dic_pids.pop('1')  # Se zoar dnv, verificar esse pop
            #             for x in range(len(list_pids) - 1):
            #                 if pidscript1 == list_pids[x]:
            #                     del (list_pids[x])
            #             with open("saida.txt", "w") as wk:
            #                 wk.write("")
            #
            #             lista_nova = []
            #             lista_keys_nova = []
            #             for x in list_pids:
            #                 dsa = str(x)
            #                 lista_nova.append(dsa)
            #             for y in dic_pids.keys():
            #                 lista_keys_nova.append(y)
            #
            #             salvar = lista_nova[0]
            #             salvar2 = lista_nova[1]
            #             keyssalvar = lista_keys_nova[0]
            #             keyssalvar2 = lista_keys_nova[1]
            #
            #             with open("saida.txt", "a") as ww:
            #                 ww.write(keyssalvar + ":" + salvar + ",")
            #                 ww.write(keyssalvar2 + ":" + salvar2 + ",")
            #         except:
            #             print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #             dic_pids.pop('1')  # Se zoar dnv, verificar esse pop
            #             for x in range(len(list_pids) - 1):
            #                 if pidscript1 == list_pids[x]:
            #                     del (list_pids[x])
            #             with open("saida.txt", "w") as wk:
            #                 wk.write("")
            #
            #             lista_nova = []
            #             lista_keys_nova = []
            #             for x in list_pids:
            #                 dsa = str(x)
            #                 lista_nova.append(dsa)
            #             for y in dic_pids.keys():
            #                 lista_keys_nova.append(y)
            #
            #             salvar = lista_nova[0]
            #             salvar2 = lista_nova[1]
            #             keyssalvar = lista_keys_nova[0]
            #             keyssalvar2 = lista_keys_nova[1]
            #
            #             with open("saida.txt", "a") as ww:
            #                 ww.write(keyssalvar + ":" + salvar + ",")
            #                 ww.write(keyssalvar2 + ":" + salvar2 + ",")
            #
            #     elif answersI['parar'] == "Contagem V2":
            #         try:
            #             os.kill(pidscript2, signal.SIGTERM)
            #             print("Programa Contagem V2 selecionado foi finalizado.\n")
            #             dic_pids.pop('2')
            #             for x in range(len(list_pids) - 1):
            #                 if pidscript2 == list_pids[x]:
            #                     del (list_pids[x])
            #             with open("saida.txt", "w") as wk:
            #                 wk.write("")
            #
            #             lista_nova = []
            #             lista_keys_nova = []
            #             for x in list_pids:
            #                 dsa = str(x)
            #                 lista_nova.append(dsa)
            #             for y in dic_pids.keys():
            #                 lista_keys_nova.append(y)
            #
            #             salvar = lista_nova[0]
            #             salvar2 = lista_nova[1]
            #             keyssalvar = lista_keys_nova[0]
            #             keyssalvar2 = lista_keys_nova[1]
            #
            #             with open("saida.txt", "a") as ww:
            #                 ww.write(keyssalvar + ":" + salvar + ",")
            #                 ww.write(keyssalvar2 + ":" + salvar2 + ",")
            #         except:
            #             print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #             dic_pids.pop('2')
            #             for x in range(len(list_pids) - 1):
            #                 if pidscript2 == list_pids[x]:
            #                     del (list_pids[x])
            #             with open("saida.txt", "w") as wk:
            #                 wk.write("")
            #
            #             lista_nova = []
            #             lista_keys_nova = []
            #             for x in list_pids:
            #                 dsa = str(x)
            #                 lista_nova.append(dsa)
            #             for y in dic_pids.keys():
            #                 lista_keys_nova.append(y)
            #
            #             salvar = lista_nova[0]
            #             salvar2 = lista_nova[1]
            #             keyssalvar = lista_keys_nova[0]
            #             keyssalvar2 = lista_keys_nova[1]
            #
            #             with open("saida.txt", "a") as ww:
            #                 ww.write(keyssalvar + ":" + salvar + ",")
            #                 ww.write(keyssalvar2 + ":" + salvar2 + ",")
            #
            #     elif answersI['parar'] == "Contagem V3":
            #         try:
            #             os.kill(pidscript3, signal.SIGTERM)
            #             print("Programa Contagem V3 selecionado foi finalizado.\n")
            #             dic_pids.pop('3')
            #             for x in range(len(list_pids) - 1):
            #                 if pidscript3 == list_pids[x]:
            #                     del (list_pids[x])
            #             with open("saida.txt", "w") as wk:
            #                 wk.write("")
            #
            #             lista_nova = []
            #             lista_keys_nova = []
            #             for x in list_pids:
            #                 dsa = str(x)
            #                 lista_nova.append(dsa)
            #             for y in dic_pids.keys():
            #                 lista_keys_nova.append(y)
            #
            #             salvar = lista_nova[0]
            #             salvar2 = lista_nova[1]
            #             keyssalvar = lista_keys_nova[0]
            #             keyssalvar2 = lista_keys_nova[1]
            #
            #             with open("saida.txt", "a") as ww:
            #                 ww.write(keyssalvar + ":" + salvar + ",")
            #                 ww.write(keyssalvar2 + ":" + salvar2 + ",")
            #         except:
            #             print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #             dic_pids.pop('3')
            #             for x in range(len(list_pids) - 1):
            #                 if pidscript3 == list_pids[x]:
            #                     del (list_pids[x])
            #             with open("saida.txt", "w") as wk:
            #                 wk.write("")
            #
            #             lista_nova = []
            #             lista_keys_nova = []
            #             for x in list_pids:
            #                 dsa = str(x)
            #                 lista_nova.append(dsa)
            #             for y in dic_pids.keys():
            #                 lista_keys_nova.append(y)
            #
            #             salvar = lista_nova[0]
            #             salvar2 = lista_nova[1]
            #             keyssalvar = lista_keys_nova[0]
            #             keyssalvar2 = lista_keys_nova[1]
            #
            #             with open("saida.txt", "a") as ww:
            #                 ww.write(keyssalvar + ":" + salvar + ",")
            #                 ww.write(keyssalvar2 + ":" + salvar2 + ",")
            #     else:
            #         print("Selecione de acordo com as 3 opções!")
            #
            # elif len(dic_pids) == 2:
            #     list_pids = []
            #     list_keys = []
            #     for key in dic_pids.keys():
            #         list_pids.append(int(dic_pids[key]))
            #         list_keys.append(key)
            #
            #     pidscript1 = list_pids[0]
            #     pidscript2 = list_pids[1]
            #
            #     script1 = int(list_keys[0])
            #     script2 = int(list_keys[1])
            #
            #     if script1 == 1 and script2 == 2:
            #         questionsII = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V1", "Contagem V2"])
            #         ]
            #         answersII = inquirer.prompt(questionsII)
            #
            #         if answersII['parar'] == "Contagem V1":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V1 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('1')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 dic_pids.pop('1')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #
            #         elif answersII['parar'] == "Contagem V2":
            #             try:
            #                 print("Programa Contagem V2 selecionado, foi finalizado.\n")
            #                 os.kill(pidscript2, signal.SIGTERM)
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #
            #     elif script1 == 2 and script2 == 1:
            #         questionsIII = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V2", "Contagem V1"])
            #         ]
            #         answersIII = inquirer.prompt(questionsIII)
            #
            #         if answersIII['parar'] == "Contagem V2":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V2 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #
            #         elif answersIII['parar'] == "Contagem V1":
            #             try:
            #                 os.kill(pidscript2, signal.SIGTERM)
            #                 print("Programa Contagem V1 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('1')
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 dic_pids.pop('1')
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #         else:
            #             print("Selecione de acordo com as duas opções!")
            #
            #     elif script1 == 2 and script2 == 3:
            #         questionsIV = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V2", "Contagem V3"])
            #         ]
            #         answersIV = inquirer.prompt(questionsIV)
            #
            #         if answersIV['parar'] == "Contagem V2":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V2 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #         elif answersIV['parar'] == "Contagem V3":
            #             try:
            #                 os.kill(pidscript2, signal.SIGTERM)
            #                 print("Programa Contagem V3 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('3')
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 dic_pids.pop('3')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #         else:
            #             print("Selecione de acordo com as duas opções!")
            #
            #     elif script1 == 3 and script2 == 2:
            #         questionsV = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V3", "Contagem V2"])
            #         ]
            #         answersV = inquirer.prompt(questionsV)
            #
            #         if answersV['parar'] == "Contagem V3":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V3 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('3')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 dic_pids.pop('3')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #         elif answersV['parar'] == "Contagem V2":
            #             try:
            #                 os.kill(pidscript2, signal.SIGTERM)
            #                 print("Programa Contagem V2 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 dic_pids.pop('2')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #         else:
            #             print("Selecione de acordo com as duas opções!")
            #
            #     elif script1 == 3 and script2 == 1:
            #         questionsVI = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V3", "Contagem V1"])
            #         ]
            #         answersVI = inquirer.prompt(questionsVI)
            #
            #         if answersVI['parar'] == "Contagem V3":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V3 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('3')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 dic_pids.pop('3')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #         elif answersVI['parar'] == "Contagem V1":
            #             try:
            #                 os.kill(pidscript2, signal.SIGTERM)
            #                 print("Programa Contagem V1 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('1')
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 dic_pids.pop('1')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #         else:
            #             print("Selecione de acordo com as duas opções!")
            #
            #     elif script1 == 1 and script2 == 3:
            #         questionsVII = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V1", "Contagem V3"])
            #         ]
            #         answersVII = inquirer.prompt(questionsVII)
            #
            #         if answersVII['parar'] == "Contagem V1":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V1 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('1')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 dic_pids.pop('1')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #         elif answersVII['parar'] == "Contagem V3":
            #             try:
            #                 os.kill(pidscript2, signal.SIGTERM)
            #                 print("Programa Contagem V3 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('3')
            #                 print(
            #                     "O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #             except:
            #                 dic_pids.pop('3')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[1])
            #                 with open("saida.txt", "w") as wk:
            #                     wk.write("")
            #
            #                 lista_nova = []
            #                 lista_keys_nova = []
            #                 for x in list_pids:
            #                     dsa = str(x)
            #                     lista_nova.append(dsa)
            #                 for y in dic_pids.keys():
            #                     lista_keys_nova.append(y)
            #
            #                 salvar = lista_nova[0]
            #                 keyssalvar = lista_keys_nova[0]
            #
            #                 with open("saida.txt", "a") as ww:
            #                     ww.write(keyssalvar + ":" + salvar + ",")
            #
            #         else:
            #             print("Selecione de acordo com as duas opções!")
            #
            # elif len(dic_pids) == 1:
            #     list_pids = []
            #     list_keys = []
            #     for key in dic_pids.keys():
            #         list_pids.append(int(dic_pids[key]))
            #         list_keys.append(key)
            #
            #     pidscript1 = list_pids[0]
            #     script1 = int(list_keys[0])
            #
            #     if script1 == 1:
            #         questionsVIII = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V1"])
            #         ]
            #         answersVIII = inquirer.prompt(questionsVIII)
            #         if answersVIII['parar'] == "Contagem V1":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa {} Contagem selecionado, foi finalizado.\n".format(script1))
            #                 dic_pids.pop('1')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as ww:
            #                     ww.write("")
            #             except:
            #                 dic_pids.pop('1')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as ww:
            #                     ww.write("")
            #         else:
            #             print("Selecione de acordo com as duas opções!")
            #
            #     elif script1 == 2:
            #         questionsIX = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V2"])
            #         ]
            #         answersIX = inquirer.prompt(questionsIX)
            #         if answersIX['parar'] == "Contagem V2":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V2 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as ww:
            #                     ww.write("")
            #             except:
            #                 dic_pids.pop('2')
            #                 list_pids.remove(list_pids[-0])
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 with open("saida.txt", "w") as ww:
            #                     ww.write("")
            #         else:
            #             print("Selecione de acordo com as duas opções!")
            #
            #     elif script1 == 3:
            #         questionsX = [
            #             inquirer.List("parar", message="Parada um Software - Qual software?",
            #                           choices=["Contagem V3"])
            #         ]
            #         answersX = inquirer.prompt(questionsX)
            #         if answersX['parar'] == "Contagem V3":
            #             try:
            #                 os.kill(pidscript1, signal.SIGTERM)
            #                 print("Programa Contagem V3 selecionado, foi finalizado.\n")
            #                 dic_pids.pop('3')
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as ww:
            #                     ww.write("")
            #             except:
            #                 dic_pids.pop('3')
            #                 print("O programa anterior foi encerrado por outro método fora do script, retirando-o da lista.\n")
            #                 list_pids.remove(list_pids[-0])
            #                 with open("saida.txt", "w") as ww:
            #                     ww.write("")
            #         else:
            #             print("Selecione de acordo com as duas opções!")
        # except:
        #     print("Inicie um programa antes de tentar fechar!")
    #
    def __funcoes(self):
        __t1 = threading.Thread(target=self.__menu)
        __t2 = threading.Thread(target=self.__tecla)
        __t1.start()
        __t2.start()
        __t1.join()
        __t2.join()


menu = Programa()
