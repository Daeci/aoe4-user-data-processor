from utils import ThemeColors
import wx

class FFXIVPage(wx.Panel):
    def __init__(self, parent, theme: ThemeColors):
        super().__init__(parent)
        self.SetBackgroundColour(theme.panel_background)
        self.SetForegroundColour(theme.foreground)  