from dataclasses import dataclass
import wx

@dataclass
class ThemeColors:
    background: wx.Colour
    panel_background: wx.Colour
    foreground: wx.Colour
    tab: wx.Colour
    button_background: wx.Colour
    button_foreground: wx.Colour

class _ThemesLoader:
    """Lazy loader for themes"""
    def __init__(self):
        self._light = None
        self._dark = None
        self._color_list = None
    
    def _init_colors(self):
        """Initialize common colors from color database"""
        if self._color_list is None:
            self._color_list = {}
            self._color_list['WHITE'] = wx.ColourDatabase().Find('WHITE')
            self._color_list['BLACK'] = wx.ColourDatabase().Find('BLACK')
            self._color_list['DARK_GRAY'] = wx.ColourDatabase().Find('DARK GREY')
    
    @property
    def light(self):
        if self._light is None:
            self._init_colors()
            self._light = ThemeColors(

            )
        return self._light

    @property
    def dark(self):
        if self._dark is None:
            self._init_colors()
            self._dark = ThemeColors(
                background=self._color_list['BLACK'],
                panel_background=self._color_list['DARK_GRAY'],
                foreground=self._color_list['WHITE'],
                tab=self._color_list['BLACK'],
                button_background=self._color_list['DARK_GRAY'],
                button_foreground=self._color_list['WHITE']
            )
        return self._dark

Themes = _ThemesLoader()