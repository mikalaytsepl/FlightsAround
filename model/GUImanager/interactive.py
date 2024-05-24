import dearpygui.dearpygui as dpg
import webbrowser


def mandatory_empty():
    with dpg.window(popup=True, no_resize=True, no_title_bar=True, no_move=True):
        dpg.add_text("Radius and/or Area fields are empty.\nThose fields are mandatory to fill.")


def invalid_radius():
    with dpg.window(popup=True, no_resize=True, no_title_bar=True, no_move=True):
        dpg.add_text("Radius format is invalid.\n Fileld can be filled only with numbers and one dot.")


def loc_not_found():
    with dpg.window(popup=True, no_resize=True, no_move=True, no_title_bar=True):
        dpg.add_text("Unable to found prowided location.\n Consider checking spelling.")


def open_flightradar():
    webbrowser.open("https://www.flightradar24.com/50.57,16.99/7")
