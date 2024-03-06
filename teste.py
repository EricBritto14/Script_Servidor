import psutil

__process_name = "Teste"
pid3 = []
for __proc in psutil.process_iter():
    if __process_name in __proc.name():
        # if __proc.pid != 8912:
        pid3 = __proc.pid
        break

print("teste", pid3)
