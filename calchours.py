from datetime import datetime as dt
from tkinter import *
from typing import TextIO

def calc_hours():
    #carga = input('(HH:MM) Carga horária diária: ') #recebe carga horaria
    #hora_1 = input('(HH:MM) Entrada 1: ') #recebe primeira hora
    #hora_2 = input('(HH:MM) Saída   1: ') #recebe segunda hora
    #hora_3 = input('(HH:MM) Entrada 2: ') #recebe segunda hora
    #hora_4 = input('(HH:MM) Saída   2: ') #recebe segunda hora

    carga = "08:48"
    hora_1 = "08:10"
    hora_2 = "12:00"
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
        msg1 = "EXISTE EXTRA DE:"
    elif horas_trab == carga:
        msg1 = "Funcionário(a) fez a carga horária corretamente."
    else:
        msg1 = "EXISTE FALTA DE:"

    if horas_trab >= carga:
        exft = str(horas_trab - carga)
    else:
        exft = str(carga - horas_trab)

    exft = dt.strptime(exft, "%H:%M:%S")


    carga = carga.strftime("%H:%M") #formata exibição
    horas_trab = horas_trab.strftime("%H:%M") #formata exibição
    exft = exft.strftime("%H:%M") #formata exibição

    if msg1 == "EXISTE EXTRA DE:":
        texto = f'''
        Carga horária:    {carga}
        Horas Trbalhadas: {horas_trab}
        {msg1}  {exft}'''
    elif msg1 == "EXISTE FALTA DE:":
        texto = f'''
        Carga horária:    {carga}
        Horas Trbalhadas: {horas_trab}
        {msg1}  {exft}'''
    else:
        texto = f'''
        Carga horária:    {carga}
        Horas Trbalhadas: {horas_trab}
        {msg1}'''

    texto_resultado["text"] = texto




janela = Tk()
janela.title("AMMES | CALCULADORA DE HORAS")
janela.geometry('450x550')

btn_result = Button(janela, text= "RESULTADO", command=calc_hours)
btn_result.grid(column=0, row=0)

texto_resultado = Label(janela, text="Informe as entradas e saídas para obter o resultado!")
texto_resultado.grid(column=0, row=2)


janela.mainloop()