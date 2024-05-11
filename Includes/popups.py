import dearpygui.dearpygui as dpg


def mandatory_empty():
    with dpg.window(popup=True, no_resize=True, no_title_bar=True, no_move=True):
        dpg.add_text("Radius and/or Area fields are empty.\nThose fields are mandatory to fill.")


def invalid_radius():
    with dpg.window(popup=True, no_resize=True, no_title_bar=True, no_move=True):
        dpg.add_text("Radius format is invalid.\n Fileld can be filled only with numbers and one dot.")
