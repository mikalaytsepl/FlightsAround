from Includes import flights_finder as ff
from Includes import screens
from Includes import popups as pop
import re
import dearpygui.dearpygui as dpg

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


def fill_table(fl_dict):
    with dpg.table_row(parent="main_tab"):
        for item in fl_dict.values():
            dpg.add_text(item)


def on_enter(sender, app_data):
    if dpg.is_key_pressed(dpg.mvKey_Return):
        if dpg.get_value("__area") and dpg.get_value("__rad"):
            if re.match(r'^[0-9]*\.?[0-9]*$', str(dpg.get_value("__rad"))):
                scanner = ff.Picker()
                scanner.get_by_bounds(int(dpg.get_value("__rad")), dpg.get_value("__area"))
                print(scanner.flight_detailed)  # start linking magic shit back up (4th time, huh?)
                clear_table()
                for meta in scanner.flight_detailed:
                    fill_table(meta)
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

    with dpg.handler_registry():
        dpg.add_key_press_handler(dpg.mvKey_Return, callback=on_enter)

    with dpg.child_window(width=600, height=30, border=False,
                          pos=(10, dpg.get_viewport_height() - 10)) as botLabs:
        with dpg.group(horizontal=True, horizontal_spacing=20):
            stat = dpg.add_text("scan status: NoScan")
    dpg.set_viewport_resize_callback(lambda: dpg.set_item_pos(botLabs, (10, dpg.get_viewport_height() - 60)))

dpg.set_primary_window("main_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# make invalid location popup
# make coloring and finding the Preferences
# find how to make interface bigger (set up a font maybe??)
# make viewport look cool maybe
# make exe file
