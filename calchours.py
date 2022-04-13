from datetime import datetime as dt


#carga = input('(HH:MM) Carga horária diária: ') #recebe carga horaria
#hora_1 = input('(HH:MM) Entrada 1: ') #recebe primeira hora
#hora_2 = input('(HH:MM) Saída   1: ') #recebe segunda hora
#hora_3 = input('(HH:MM) Entrada 2: ') #recebe segunda hora
#hora_4 = input('(HH:MM) Saída   2: ') #recebe segunda hora

carga = "08:48"
hora_1 = "08:00"
hora_2 = "12:10"
hora_3 = "13:30"
hora_4 = "18:18"

carga = dt.strptime(carga,"%H:%M") #formata a carga horária
hora_1 = dt.strptime(hora_1,"%H:%M") #formata a primeira hora
hora_2 = dt.strptime(hora_2,"%H:%M") #formata a segunda hora
hora_3 = dt.strptime(hora_3,"%H:%M") #formata a primeira hora
hora_4 = dt.strptime(hora_4,"%H:%M") #formata a segunda hora

periodo1 = hora_2 - hora_1 #calcula período 1
periodo2 = hora_4 - hora_3 #calcula período 2

horas_trab = str(periodo1 + periodo2) #soma entre os 2 períodos
horas_trab = dt.strptime(horas_trab,"%H:%M:%S") #formata a horas trabalhadas

if horas_trab > carga:
    extra = "EXISTE EXTRA"
elif horas_trab == carga:
    extra = "NÃO TEM EXTRA NEM FALTA"
else:
    extra = "EXISTE FALTA"



carga = carga.strftime("%H:%M") #formata exibição
horas_trab = horas_trab.strftime("%H:%M") #formata exibição
#time_1 = hora_1.strftime("%H:%M") #formata exibição
#time_2 = hora_2.strftime("%H:%M") #formata exibição
#time_3 = hora_3.strftime("%H:%M") #formata exibição
#time_4 = hora_4.strftime("%H:%M") #formata exibição

print("\nCarga horária: ", carga, "\nHoras Trbalhadas: ", horas_trab, "\n", extra)


