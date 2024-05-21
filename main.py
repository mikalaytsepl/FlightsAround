from Includes import flights_finder as ff
from Includes import screens
from Includes import popups as pop
import re
import dearpygui.dearpygui as dpg
import uuid
import webbrowser

screen_width = screens.get_sizes("width")
screen_height = screens.get_sizes("heigth")

dpg.create_context()
dpg.create_viewport(title='FlightsAround', width=screen_width, height=screen_height - 30, decorated=True,
                    clear_color=[5, 5, 5])
dpg.toggle_viewport_fullscreen()


def clear_table():
    children = dpg.get_item_children("main_tab", 1)
    for item in children:
        dpg.delete_item(item=item)


def open_flihtradar():
    webbrowser.open("https://www.flightradar24.com/50.57,16.99/7")


class TableFiller:
    fl_dict = {}

    def __init__(self, fl_dict):
        self.fl_dict = fl_dict

    def _pref_checker(self, values):
        pref = dpg.get_value("__pref")
        if type(pref) != list:
            pref = pref.split("|")
            for preference in pref:
                if preference in values:
                    continue
                else:
                    return False
            return True
        else:
            if pref in values:
                return True
            else:
                return False

    def fill_table(self):
        pref = dpg.get_value("__pref")
        with dpg.table_row(parent="main_tab"):
            if pref:
                if self._pref_checker(self.fl_dict.values()):
                    for item in self.fl_dict.values():
                        temptag = f"button_{uuid.uuid4()}"
                        dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)
                        dpg.bind_item_theme(item=temptag, theme=button_theme)
                else:
                    for item in self.fl_dict.values():
                        temptag = f"button_{uuid.uuid4()}"
                        dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)
            else:
                for item in self.fl_dict.values():
                    temptag = f"button_{uuid.uuid4()}"
                    dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)


def on_table_button_clicked(sender, app_data):
    button_text = dpg.get_item_label(item=sender)
    dpg.set_clipboard_text(text=button_text)


def on_enter(sender, app_data):
    if dpg.is_key_pressed(dpg.mvKey_Return):
        if dpg.get_value("__area") and dpg.get_value("__rad"):
            if re.match(r'^[0-9]*\.?[0-9]*$', str(dpg.get_value("__rad"))):
                try:
                    scanner = ff.Picker()
                    scanner.get_by_bounds(int(dpg.get_value("__rad")), dpg.get_value("__area"))
                    print(scanner.flight_detailed)
                    clear_table()
                    for meta in scanner.flight_detailed:
                        tmp = TableFiller(meta)
                        tmp.fill_table()
                except AttributeError:
                    pop.loc_not_found()
            else:
                pop.invalid_radius()
        else:
            pop.mandatory_empty()


with dpg.window(label="Main", id='main_window', width=screen_width - 200, height=screen_height - 200,
                min_size=(int(screen_width / 2), int(screen_height / 2))):
    with dpg.group(horizontal=True, id="menu group", height=100):
        dpg.add_input_text(hint="Area (Mandatory)", width=screen_width / 3, height=-1, tag="__area")
        dpg.add_input_text(hint="Radius (Mandatory)", width=screen_width / 3, height=-1, tag="__rad")
        dpg.add_input_text(hint="Preferences (Optional)", width=screen_width / 3, height=-1, tag="__pref")

    with dpg.group(horizontal=True, id="flightbutton_group", width=screen_width):
        dpg.add_button(label="Click Here to open Flight Radar webpage in your default brouser", tag="browsebutton",
                       callback=open_flihtradar)

    with dpg.table(header_row=True, tag='main_tab', scrollY=True, scrollX=False) as tbl:
        dpg.add_table_column(label="Call-sign")
        dpg.add_table_column(label="Airline")
        dpg.add_table_column(label="ICAO")
        dpg.add_table_column(label="Model")
        dpg.add_table_column(label="Departure Name")
        dpg.add_table_column(label="Departure ICAO")
        dpg.add_table_column(label="Planned departure")
        dpg.add_table_column(label="Destination Name")
        dpg.add_table_column(label="Destination ICAO")
        dpg.add_table_column(label="Planned arrival")

    with dpg.theme() as button_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (23, 162, 184), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (40, 200, 220), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (10, 130, 150), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)

    with dpg.handler_registry():
        dpg.add_key_press_handler(dpg.mvKey_Return, callback=on_enter)

dpg.set_primary_window("main_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


