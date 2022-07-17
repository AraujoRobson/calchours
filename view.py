import dearpygui.dearpygui as dpg

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
    large_icon="docs/Logo_large.ico"
    )

with dpg.window(tag= "primary"):
    dpg.add_text("Defina a Carga horária:")
    get_carga = dpg.add_input_text(hint="CARGA HORÁRIA: 08:48")
    
    dpg.add_text("Defina o horário da ENTRADA 1:")
    get_horaEnt1 = dpg.add_input_text(hint="ENTRADA 1: 08:00")
    
    dpg.add_text("Defina o horária da SAÍDA 1:")
    get_horaSai1 = dpg.add_input_text(hint= "SAÍDA 1: 12:00")
    
    dpg.add_text("Defina o horário da ENTRADA 2:")
    get_horaEnt2 = dpg.add_input_text(hint="ENTRADA 2: 13:30")
    
    dpg.add_text("Defina o horária da SAÍDA 2:")
    get_horaSai2 = dpg.add_input_text(hint= "SAÍDA 2: 18:18")
    
    btn_result = dpg.add_button(label="Resultado")



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("primary", True)


dpg.start_dearpygui()

dpg.destroy_context()
