import dearpygui.dearpygui as dpg
from abc import ABC, abstractmethod


#  ---- abstract class for a text style with abstract owerride for __call__ and non abscract __init__, because
#       all instances have it jst the same -----------------------------------------------------------------------------

class TextStyle(ABC):
    def __init__(self, tag: str):
        self._tag = tag

    @abstractmethod
    def __call__(self):
        pass


# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------instances with owerriden __call__ --------------------------------------------------------
class GreenText(TextStyle, ABC):
    def __call__(self):
        with dpg.theme() as text_theme:
            with dpg.theme_component(dpg.mvText):
                dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 0), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme(self._tag, text_theme)


class RedText(TextStyle, ABC):
    def __call__(self):
        with dpg.theme() as text_theme:
            with dpg.theme_component(dpg.mvText):
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme(self._tag, text_theme)


class WhiteText(TextStyle, ABC):
    def __call__(self):
        with dpg.theme() as text_theme:
            with dpg.theme_component(dpg.mvText):
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme(self._tag, text_theme)

# ----------------------------------------------------------------------------------------------------------------------
