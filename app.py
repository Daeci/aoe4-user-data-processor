from panels import HomePage, AoC2025Page, BDOPage, FFXIVPage
from utils import Themes

import wx
import wx.lib.agw.aui as aui

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Playground', size=wx.Size(1280, 720))
        theme = Themes.dark
        if theme == Themes.dark:
            self._enable_system_dark_mode()
        self.Center()
        self.SetBackgroundColour(theme.background)
        navbar = aui.AuiNotebook(self, agwStyle=aui.AUI_NB_TOP)
        navbar.GetAuiManager().GetArtProvider().SetDefaultColours(base_colour=theme.tab)
        navbar.SetBackgroundColour(theme.background)
        navbar.SetForegroundColour(theme.foreground)

        # add all the pages to navbar
        home_panel = HomePage(navbar, theme)
        aoc2025_panel = AoC2025Page(navbar, theme)
        bdo_panel = BDOPage(navbar, theme)
        ffxiv_panel = FFXIVPage(navbar, theme)

        # add all added pages to notebook with labels
        navbar.AddPage(home_panel, "Home")
        navbar.AddPage(aoc2025_panel, "AoC 2025")
        navbar.AddPage(bdo_panel, "BDO Market Info")
        navbar.AddPage(ffxiv_panel, "FFXIV Market Info")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(navbar, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        self.Show()
    
    def _enable_system_dark_mode(self):
        """Enable dark mode for window title bar on Windows 10/11"""
        if wx.Platform == '__WXMSW__':
            try:
                import ctypes
                hwnd = self.GetHandle()
                DWMWA_USE_IMMERSIVE_DARK_MODE = 20 # (Windows 10 build 19041+)
                value = ctypes.c_int(1)  # 1 = dark mode, 0 = light mode
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, 
                    DWMWA_USE_IMMERSIVE_DARK_MODE,
                    ctypes.byref(value),
                    ctypes.sizeof(value)
                )
            except Exception:
                # maybe add an alert prompt to inform user to change dark mode val
                pass

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()