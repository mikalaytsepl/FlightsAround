import dearpygui.dearpygui as dpg
import webbrowser


# popup functions for error handeling, each of them makes the window with the text inside it at the current position
# of the coursor

def mandatory_empty():
    with dpg.window(popup=True, no_resize=True, no_title_bar=True, no_move=True):
        dpg.add_text("Radius and/or Area fields are empty.\nThose fields are mandatory to fill.")


def invalid_radius():
    with dpg.window(popup=True, no_resize=True, no_title_bar=True, no_move=True):
        dpg.add_text("Radius format is invalid.\n Fileld can be filled only with numbers and one dot.")


def loc_not_found():
    with dpg.window(popup=True, no_resize=True, no_move=True, no_title_bar=True):
        dpg.add_text("Unable to found prowided location.\n Consider checking spelling.")


def open_flightradar(): # just opend fight radar file, may be done directly from controller, but it was moved here in
    # order to preserve MVC principles
    webbrowser.open("https://www.flightradar24.com/50.57,16.99/7")


def table_empty():
    with dpg.window(popup=True, no_resize=True, no_move=True, no_title_bar=True):
        dpg.add_text(
            "Tabel is empty, make a scan to then appy a filter \n or initialize a scan with a filter already \n"
            " set by filling all the textfields and pressing enter button.")
