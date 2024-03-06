import os
import time
from time import sleep

class Guia:
    def __init__(self):
        ...


    def _executavel(self):  # __ dois significa private, e não pode puxar sem ser fora da própria classe... com um só, pode puxar pois só fica protected
        os.system("start \"validacao3\" cmd /c python C:/Users/abe4ca/Desktop/boschScript-main2/contagem.py")
        # Background /b
        # os.system("start /wait cmd /c S:/PM/ter/ets/Inter_Setor/COMPARTILHADO/APRENDIZES/MEIO_OFICIAIS/LETICIACAPOVILA/Projeto/executa.bat")
        os.system(
            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao3\" /FO CSV /NH') do @echo %~P >> comparando3.txt")

        os.system("start \"validacao3\" cmd /c python C:/Users/abe4ca/Desktop/boschScript-main2/val3.py")

    def _executavel2(self):  # __ dois significa private, e não pode puxar sem ser fora da própria classe... com um só, pode puxar pois só fica protected
        os.system("start \"validacao2\" cmd /c java C:/Users/abe4ca/Desktop/javaof/programa.java")
        #/c java C:/Users/abe4ca/Desktop/javaof/programa.java

        #Trocar aqui o cmd para ir direto no programa não para ir no bat

        os.system(
            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do @echo %~P >> comparando2.txt")

        os.system("start \"validacao2\" cmd /c C:/Users/abe4ca/Desktop/boschScript-main2/bats/executa2v2.bat")

    def _executavel3(self):  # __ dois significa private, e não pode puxar sem ser fora da própria classe... com um só, pode puxar pois só fica protected
        os.system("start \"validacao\" cmd /c node C:/Users/abe4ca/Desktop/js/newProgram.js")

        # os.system("for /f \"tokens=2\" %F in ('tasklist /FI \"WindowTitle eq validacao*\"') do @echo %~F >> valiteste.txt")
        # os.system("@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao*\" /FO CSV /NH') do @echo %~P >> valiteste.txt")

        os.system(
            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao\" /FO CSV /NH') do @echo %~P >> comparando.txt")

        os.system("start \"validacao\" cmd /c C:/Users/abe4ca/Desktop/boschScript-main2/bats/executa3v2.bat")

        # with open("comparando.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
        #     for k in r:
        #         vz = k
        #         vt = k
        #
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
            # with open("comparando.txt", "w") as kv:  # Código para abrir o bloco de notas, e 'r' para read
            #     kv.write("")

        # && @echo off for /F \"delims=\" %%R in ('tasklist /FI \"WindowTitle eq validacao*\" /FI \"Status eq Running\" /FO CSV/NH') do (set \"FLAG1=\" & set \"FLAG2=\" for %%C in (%%R) do (if defined FLAG1 (if not defined FLAG2 (echo %% ~C) set \"FLAG2=#\") set \"FLAG1=#\")) >> valiteste.txt")
        # os.system("start cmd /c C:/Users/ct67ca/Desktop/teste.bat")
        #os.system("@echo off for /F \"delims=\" %%R in ('tasklist /FI \"ImageName eq cmd.exe\" /FI \"Status eq Running\" /FO CSV/NH') do (set \"FLAG1=\" & set \"FLAG2=\" for %%C in (%%R) do (if defined FLAG1 (if not defined FLAG2 (echo %% ~C) set \"FLAG2=#\") set \"FLAG1=#\"))")

        # for x in range(0, 5):
        # with open("valiteste.txt", "r") as r:  # Código para abrir o bloco de notas, e 'r' para read
        #     for x in r:
        #         vf = [x]

                # testando_dic = {}
                # pid_f = vf.split(',')
                # pid_f.remove(pid_f[-1])
                #
                # for element in pid_f:
                #     split_element = element.split(':')
                #     testando_dic.update({split_element[0]: split_element[1]})
            #
            # print("como fica no dic", testando_dic)

            # print("valor salvo na variável", vf)
            # pp = vf[0]
            # print("valor teste", pp)
    #     if os.system("for /f \"tokens=2\" %F in ('tasklist /FI \"WindowTitle eq validacao*\"') do @echo %~F") != vf:
    #         os.system("for /f \"tokens=2\" %F in ('tasklist /FI \"WindowTitle eq validacao*\"') do @echo %~F >> valiteste.txt")
    #     else:
    #         print("goddamn")

    # @echo off for /F "delims=" %%R in ('tasklist /FI "WindowTitle eq validacao*" /FI "Status eq Running" /FO CSV/NH') do (set "FLAG1=" & set "FLAG2=" for %%C in (%%R) do (if defined FLAG1 (if not defined FLAG2 (echo %% ~C) set "FLAG2=#") set "FLAG1=#"))



    # start "oii" cmd /c node S: / PM / ter / ets / Inter_Setor / COMPARTILHADO / APRENDIZES / MEIO_OFICIAIS / ERIC_APARECIDO_BRITTO_BARRETO / js / newProgram.js

    # os.system("start ""Programa cmd Py Teste"" cmd /c call python S:/PM/ter/ets/Inter_Setor/COMPARTILHADO/APRENDIZES"
    #             "/MEIO_OFICIAIS/LETICIACAPOVILA/Projeto/contagem3.py")
