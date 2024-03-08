import os


class Guia:
    def __init__(self):
        ...

    def _executavel(self):  # __ dois significa private, e não pode puxar sem ser fora da própria classe... com um só, pode puxar pois só fica protected
        os.system("start \"validacao3\" cmd /c python C:/Users/abe4ca/Desktop/boschScript-main2/contagem.py")

        os.system(
            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao3\" /FO CSV /NH') do "
            "@echo %~P >> comparando3.txt")

        os.system("start \"validacao3\" cmd /c C:/Users/abe4ca/Desktop/boschScript-main2/bats/executa.bat")

    def _executavel2(self):  # __ dois significa private, e não pode puxar sem ser fora da própria classe... com um só, pode puxar pois só fica protected
        os.system("start \"validacao2\" cmd /c java C:/Users/abe4ca/Desktop/javaof/programa.java")

        os.system(
            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao2\" /FO CSV /NH') do "
            "@echo %~P >> comparando2.txt")

        os.system("start \"validacao2\" cmd /c C:/Users/abe4ca/Desktop/boschScript-main2/bats/executa2v2.bat")

    def _executavel3(self):  # __ dois significa private, e não pode puxar sem ser fora da própria classe... com um só, pode puxar pois só fica protected
        os.system("start \"validacao\" cmd /c node C:/Users/abe4ca/Desktop/js/newProgram.js")

        os.system(
            "@for /F \"tokens=2 delims=,\" %P in ('tasklist /SVC /FI \"WindowTitle eq validacao\" /FO CSV /NH') do "
            "@echo %~P >> comparando.txt")

        os.system("start \"validacao\" cmd /c C:/Users/abe4ca/Desktop/boschScript-main2/bats/executa3v2.bat")
