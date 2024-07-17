# adding modules from model -> API and GUI manager

from model.APImanager import flights_finder as ff
from model.GUImanager import interactive as inter, screens
from model.GUImanager import colortext
import re
import dearpygui.dearpygui as dpg
import uuid


# --------------------- controller part, where model action toggleing functions are stored -----------------------------
#        (because of a chosen GUI framework, view and controller cant be truelly separated into different modules)
#    (no matter of that, program is working accoarding the MVC principle and model and view parts are not owerlaping)
#    (therefore, MVC architectural pattern's benefits (such as for ex. modularity and reusability) are still provided)


# ---------------- gets main screen width and heigth to then create a "false full size" window ---------------------

screen_width = screens.get_sizes("width")
screen_height = screens.get_sizes("heigth")

# wiewport -- smth like window inside window, cause this framework allwos to make multiple windows inside the system one
# therefore, one window is made and "strached" to fit the system window
dpg.create_context()
dpg.create_viewport(title='FlightsAround', width=screen_width, height=screen_height - 30, decorated=True,
                    clear_color=[5, 5, 5])
dpg.toggle_viewport_fullscreen()

scan_results: bool  # flag for filter functions to "understand"  wether scan has been initialized or not


# clears all table contents  by rows, getting tabel's chidlren id
def clear_table():
    children = dpg.get_item_children("main_tab", 1)
    for item in children:
        dpg.delete_item(item=item)


# filter manager class, which is made mostly for fillers with preferences, since they share common methods like
# reset default and static metho like pref checker
class FilterManager:
    def __init__(self):
        self._children = dpg.get_item_children("main_tab", 1)

    # function to reset all the table rows to default theme (discard coloring)
    def _reset_defaults(self):

        for row in self._children:
            dpg.bind_item_theme(theme=default_theme, item=row)

    @staticmethod  # because it does not need to have access to a self instance but needs to be private
    def _pref_checker(values):  # private method because this will newer used outsde of the class or its children
        pref = dpg.get_value("__pref")
        if type(pref) != list:  # checks if there is more than 1 preference, and depending on the answer
            # splits and checks if all the preferences are in table row and returns false if not
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

    # overloaded str operator to fill table with print(), not necessary nor effective, cause exception is raised,
    # but it is made for educational purposes
    def __str__(self):
        try:
            self._reset_defaults()  # reset default teams at the start
            if not scan_results:  # if scan flag is not true, which means that scan was not initialized yet
                # exception popup is being rased
                inter.table_empty()
            elif not dpg.get_value(
                    "__pref").strip():  # if scan is applied without preference, all the coloring is reset
                self._reset_defaults()
            else:
                self._reset_defaults()
                for row in self._children:
                    if self._pref_checker([dpg.get_item_configuration(child_of_the_row)["label"] for child_of_the_row in
                                           dpg.get_item_children(row, 1)]):
                        dpg.bind_item_theme(item=row, theme=button_theme)
        except NameError:
            inter.table_empty()  # popup from interaction module sayind that scan is empty


# function for apply button's callback to apply a filter wihout initializing a new scan
def assemble_filter() -> None:
    tmp = FilterManager()
    try:
        print(tmp)
    except TypeError:
        pass


# class to fill a clear table

class TableFillerNoPref:
    def __init__(self, fl_dict: dict):
        self._fl_dict = fl_dict

    def fill_tabel(self):
        with dpg.table_row(parent="main_tab"):
            for item in self._fl_dict.values():
                temptag = f"button_{uuid.uuid4()}"  # makes shure that there will be no same tags no matter how many
                # buttons are in table and all of them are sharing hte same "copy to clipboard" callback
                dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)


# class which is a child of  TableFillerNoPref and FilterManager
# in order to be able to use preference checkers ect.

class TableFillerPref(TableFillerNoPref, FilterManager):

    def fill_table(self):  # this function is bein owerdriven

        with dpg.table_row(parent="main_tab"):
            if self._pref_checker(self._fl_dict.values()):
                for item in self._fl_dict.values():
                    temptag = f"button_{uuid.uuid4()}"
                    dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)
                    dpg.bind_item_theme(item=temptag, theme=button_theme)
            else:  # this part fills without coloring
                for item in self._fl_dict.values():
                    temptag = f"button_{uuid.uuid4()}"
                    dpg.add_button(label=item, tag=temptag, callback=on_table_button_clicked)


def on_table_button_clicked(sender):  # copies text written on button
    # to a clipboard (is a callback of each button in table)
    button_text = dpg.get_item_label(item=sender)
    dpg.set_clipboard_text(text=button_text)


# function which initializes scanning process by the press of an enter key
def on_enter():
    if dpg.is_key_pressed(
            dpg.mvKey_Return):  # prewens from errors of calling a function without enter key beind pressed
        if dpg.get_value("__area") and dpg.get_value("__rad"):  # checks if mandatory fields are empty and if yes,
            # exceptin popup is being shown
            if re.match(r'^[0-9]*\.?[0-9]*$', str(dpg.get_value("__rad"))): # checks if radius format is propper
                try: # starts scann asssembly, but if location prowided in the area field cant be found,
                    # the AttributeError is being raised, therefore, location not found exception popup window is
                    # being shown, and program can continiue

                    colortext.RedText("status_text")() # colors status text in red and changes it to scan pocessing
                    # this syntax is possible because of overriden __call__ method, which is really helpful in a
                    # situation with the abstract class and RedText beind it's instance and serving he only one
                    # purpose
                    dpg.set_value(item="status_text", value="Scan processing.")

                    global scan_results

                    # scanner object is made and scanner is being initialized using the data gathered from the
                    # mandatory fields

                    scanner = ff.Picker()
                    scanner.get_by_bounds(int(dpg.get_value("__rad")), dpg.get_value("__area"))
                    scan_results = True

                    clear_table()# table gets cleared, just in case

                    # this part makes checkes which tabel filling method should be used based on wether there is
                    # something in preferences field or not
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
                finally: # fnally condition in try except construction makes shure that the code inside it will be
                    # excecuted no matter of wether code was excecuted wiht or without an exception being raised

                    # those two commands are changeing the status scan text to scan finished positiond and accordingly
                    # the color of the font
                    colortext.GreenText("status_text")()
                    dpg.set_value(item="status_text", value="Scan finished.")

            else:
                inter.invalid_radius()
        else:
            inter.mandatory_empty()


# ----------------------------------------------------------------------------------------------------------------------

# -------- GUI (View) setting up part, where all the callbacks, elemetns, ect. are being initialized -------------------

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
        scan_status = dpg.add_text("No scan initialized", tag="status_text")

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

    default_theme = dpg.get_item_theme("browsebutton") # gets default theme (actually does not matter from what element)
    # which is used to restore the "untouched" look to table elements while clearing it with the empty scan preference
    # or to refresh table's look when annother preferences are applied

# ----------------------------------------------------------------------------------------------------------------------

    # ------------------------------Sets up new theme for selected table elements ------------------------------------

    with dpg.theme() as button_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (23, 162, 184), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (40, 200, 220), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (10, 130, 150), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)

    # ----------------------------------------------------------------------------------------------------------------

    # enter press handler
    with dpg.handler_registry():
        dpg.add_key_press_handler(dpg.mvKey_Return, callback=on_enter)

dpg.set_primary_window("main_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
