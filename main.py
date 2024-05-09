from Includes import flights_finder as ff
from Includes import screens
import dearpygui.dearpygui as dpg

screen_wigth = screens.get_sizes("width")
screen_heigth = screens.get_sizes("heigth")

dpg.create_context()
dpg.create_viewport(title='FlightsAround', width=screen_wigth, height=screen_heigth - 30, decorated=True,
                    clear_color=[5, 5, 5])
dpg.toggle_viewport_fullscreen()

with dpg.window(label="Main", id='main_window', width=screen_wigth - 200, height=screen_heigth - 200,
                min_size=(int(screen_wigth / 2), int(screen_heigth / 2))):
    with dpg.group(horizontal=True, id="menu group", width=-1, height=100):
        dpg.add_input_text(hint="Area (Mandatory)", width=screen_wigth / 3, height=-1)
        dpg.add_input_text(hint="Raius (Mandatory)", width=screen_wigth / 3)
        dpg.add_input_text(hint="Preferences (Optional)", width=screen_wigth / 3)

    with dpg.table(header_row=True, tag='tag', scrollY=True, scrollX=False) as tbl:
        dpg.add_table_column(label="Callsign")
        dpg.add_table_column(label="Airline")
        dpg.add_table_column(label="ICAO")
        dpg.add_table_column(label="Model")
        dpg.add_table_column(label="Departure Name")
        dpg.add_table_column(label="Departure ICAO")
        dpg.add_table_column(label="Planned departure")
        dpg.add_table_column(label="Destination Name")
        dpg.add_table_column(label="Destination ICAO")
        dpg.add_table_column(label="Planed arrival")

    with dpg.child_window(width=600, height=30, border=False,
                          pos=(10, dpg.get_viewport_height() - 75)) as botLabs:
        with dpg.group(horizontal=True, horizontal_spacing=20):
            stat = dpg.add_text("scan status: NoScan")
            sc = dpg.add_text("scanned: 0")
    dpg.set_viewport_resize_callback(lambda: dpg.set_item_pos(botLabs, (10, dpg.get_viewport_height() - 100)))

dpg.set_primary_window("main_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


# get stuff working
# make popups
# make coloring and finding the Preferences
# make viewport look cool maybe
# make exe file
