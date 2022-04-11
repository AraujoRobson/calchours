import datetime as dt

hora_1 = input(str('(HH:MM:SS) Hora 1: ')) #recebe primeira hora
hora_2 = input(str('(HH:MM:SS) Hora 2: ')) #recebe segunda hora
time_1 = dt.datetime.strptime(hora_1,"%H:%M:%S") #formata a primeira hora
time_2 = dt.datetime.strptime(hora_2,"%H:%M:%S") #formata a segunda hora

time_interval = time_1 - time_2

print(time_interval)