from datetime import datetime as dt

carga = input(str('(HH:MM) Carga horária diária: ')) #recebe carga horaria
hora_1 = input(str('(HH:MM) Entrada 1: ')) #recebe primeira hora
hora_2 = input(str('(HH:MM) Saída   1: ')) #recebe segunda hora
hora_3 = input(str('(HH:MM) Entrada 2: ')) #recebe segunda hora
hora_4 = input(str('(HH:MM) Saída   2: ')) #recebe segunda hora

carga1 = dt.strptime(carga,"%H:%M") #formata a carga horária
time_1 = dt.strptime(hora_1,"%H:%M") #formata a primeira hora
time_2 = dt.strptime(hora_2,"%H:%M") #formata a segunda hora
time_3 = dt.strptime(hora_3,"%H:%M") #formata a primeira hora
time_4 = dt.strptime(hora_4,"%H:%M") #formata a segunda hora

time_interval1 = time_2 - time_1 #calcula período 1
time_interval2 = time_4 - time_3 #calcula período 2

horas_trab = time_interval1 + time_interval2 #soma entre os 2 períodos




print("Período 1 trabalhado: ",time_interval1)
print("Período 2 trabalhado: ",time_interval2)
print("Horas Trabalhandas  : ", horas_trab)

