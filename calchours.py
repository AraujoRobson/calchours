from datetime import datetime as dt
from tkinter import *
from turtle import width
import dearpygui.dearpygui as dpg

def calc_hours():

    #carga = input('(HH:MM) Carga horária diária: ') #recebe carga horaria
    #hora_1 = input('(HH:MM) Entrada 1: ') #recebe primeira hora
    #hora_2 = input('(HH:MM) Saída   1: ') #recebe segunda hora
    #hora_3 = input('(HH:MM) Entrada 2: ') #recebe segunda hora
    #hora_4 = input('(HH:MM) Saída   2: ') #recebe segunda hora


    carga = "08:48"
    hora_1 = "08:00"
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
        Carga horária:        {carga}
        Horas Trabalhadas:  {horas_trab}
        {msg1}   {exft}'''
    elif msg1 == "EXISTE FALTA DE:":
        texto = f'''
        Carga horária:        {carga}
        Horas Trabalhadas:  {horas_trab}
        {msg1}   {exft}'''
    else:
        texto = f'''
        Carga horária:        {carga}
        Horas Trabalhadas:  {horas_trab}
        {msg1}'''

    texto_resultado["text"] = texto


#config window
WINDOW_TITLE = "AMMES | CALCULADORA DE HORAS"
WINDOW_HEIGHT = 550
WINDOW_WIDTH = 380
SPACING = 5
SHORT_INPUT_WIDTH = 150

dpg.create_context()

vp = dpg.create_viewport(
    title=WINDOW_TITLE,
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    small_icon="docs/Logo.ico",
    large_icon="docs/Logo.ico"
    )
# dpg.create_viewport(title= "AMMES | CALCULADORA DE HORAS", width=380 , height=550)

with dpg.window(tag= "primary"):
    dpg.add_text("Defina a Carga horária:")
    dpg.add_input_text(default_value= "08:48")
    dpg.add_text("Defina o horário da ENTRADA 1:")
    dpg.add_input_text(default_value= "08:00")
    dpg.add_text("Defina o horária da SAÍDA 1:")
    dpg.add_input_text(default_value= "12:00")
    dpg.add_text("Defina o horário da ENTRADA 2:")
    dpg.add_input_text(default_value= "13:30")
    dpg.add_text("Defina o horária da SAÍDA 2:")
    dpg.add_input_text(default_value= "18:18")
    btn_result = dpg.add_button(label="Resultado")



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("primary", True)


dpg.start_dearpygui()

dpg.destroy_context()