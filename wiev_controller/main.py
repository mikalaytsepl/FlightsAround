from model.APImanager import flights_finder as ff
from model.GUImanager import interactive as inter, screens
import re
import dearpygui.dearpygui as dpg
import uuid

screen_width = screens.get_sizes("width")
screen_height = screens.get_sizes("heigth")

dpg.create_context()
dpg.create_viewport(title='FlightsAround', width=screen_width, height=screen_height - 30, decorated=True,
                    clear_color=[5, 5, 5])
dpg.toggle_viewport_fullscreen()

scan_results: bool


def clear_table():
    children = dpg.get_item_children("main_tab", 1)
    for item in children:
        dpg.delete_item(item=item)


class FilterManager:
    def __init__(self):
        self._children = dpg.get_item_children("main_tab", 1)

    def _reset_defaults(self):

        for row in self._children:
            dpg.bind_item_theme(theme=default_theme, item=row)

    @staticmethod  # because it does not need to have access to a self instance but needs to be private
    def _pref_checker(values):
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

    def __str__(self):
        try:
            self._reset_defaults()
            if not scan_results:
                inter.table_empty()
            elif not dpg.get_value("__pref").strip():
                self._reset_defaults()
            else:
                self._reset_defaults()
                for row in self._children:
                    if self._pref_checker([dpg.get_item_configuration(child_of_the_row)["label"] for child_of_the_row in dpg.get_item_children(row, 1)]):
                        dpg.bind_item_theme(item=row, theme=button_theme)
        except NameError:
            inter.table_empty()


def assemble_filter() -> None:
    tmp = FilterManager()
    try:
        print(tmp)
    except TypeError:
        pass


class TableFillerNoPref:
    def __init__(self, fl_dict: dict):
        self._fl_dict = fl_dict

    def fill_tabel(self):
        with dpg.table_row(parent="main_tab"):
            for item in self._fl_dict.values():
                temptag = f"button_{uuid.uuid4()}"
                dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)


class TableFillerPref(TableFillerNoPref, FilterManager):

    def fill_table(self):

        with dpg.table_row(parent="main_tab"):
            if self._pref_checker(self._fl_dict.values()):
                for item in self._fl_dict.values():
                    temptag = f"button_{uuid.uuid4()}"
                    dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)
                    dpg.bind_item_theme(item=temptag, theme=button_theme)
            else:
                for item in self._fl_dict.values():
                    temptag = f"button_{uuid.uuid4()}"
                    dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)


def on_table_button_clicked(sender):
    button_text = dpg.get_item_label(item=sender)
    dpg.set_clipboard_text(text=button_text)


def on_enter():
    if dpg.is_key_pressed(dpg.mvKey_Return):
        if dpg.get_value("__area") and dpg.get_value("__rad"):
            if re.match(r'^[0-9]*\.?[0-9]*$', str(dpg.get_value("__rad"))):
                try:
                    global scan_results

                    scanner = ff.Picker()
                    scanner.get_by_bounds(int(dpg.get_value("__rad")), dpg.get_value("__area"))
                    scan_results = True

                    clear_table()
                    pref = dpg.get_value("__pref")
                    if pref:
                        for meta in scanner.flight_detailed:
                            filler = TableFillerPref(meta)
                            filler.fill_table()
                    else:
                        for meta in scanner.flight_detailed:
                            filler = TableFillerNoPref(meta)
                            filler.fill_tabel()
                except AttributeError:
                    inter.loc_not_found()
            else:
                inter.invalid_radius()
        else:
            inter.mandatory_empty()


with dpg.window(label="Main", id='main_window', width=screen_width - 200, height=screen_height - 200,
                min_size=(int(screen_width / 2), int(screen_height / 2))):
    with dpg.group(horizontal=True, id="menu group", height=20):
        dpg.add_input_text(hint="Area (Mandatory)", width=screen_width / 3, height=-1, tag="__area")
        dpg.add_input_text(hint="Radius (Mandatory)", width=screen_width / 3, height=-1, tag="__rad")
        dpg.add_input_text(hint="Preferences (Optional)", width=screen_width / 4, height=-1, tag="__pref")
        dpg.add_button(label="Apply", width=screen_width / 15, height=-1, tag="__filter",
                       callback=assemble_filter)

    with dpg.group(horizontal=True, id="flightbutton_group", width=screen_width):
        dpg.add_button(label="Click Here to open Flight Radar webpage in your default brouser", tag="browsebutton",
                       callback=inter.open_flightradar)

    with dpg.group(horizontal=True, id="scan_status_window", width=screen_width):
        dpg.add_text(label="No scan initialized", tag="status_text")

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

    default_theme = dpg.get_item_theme("browsebutton")

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

#  make a loading icon  when scan
