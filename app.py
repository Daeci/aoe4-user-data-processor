import wx
from aoc2025 import Day1, Day2, Day3, Day4

#globals
X_BORDER_PX = 5
Y_BORDER_PX = 5

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='App')
        panel = wx.Panel(self)

        #region AoC
        day1part1_btn = wx.Button(panel, label='Day 1 Part 1')
        day1part1_btn.Bind(wx.EVT_BUTTON, self.on_day1part2_clicked)
        day1part2_btn = wx.Button(panel, label='Day 1 Part 2')
        day1part2_btn.Bind(wx.EVT_BUTTON, self.on_day1part2_clicked)
        day2part1_btn = wx.Button(panel, label='Day 2 Part 1')
        day2part1_btn.Bind(wx.EVT_BUTTON, self.on_day2part1_clicked)
        day2part2_btn = wx.Button(panel, label='Day 2 Part 2')
        day2part2_btn.Bind(wx.EVT_BUTTON, self.on_day2part2_clicked)
        day3part1_btn = wx.Button(panel, label='Day 3 Part 1')
        day3part1_btn.Bind(wx.EVT_BUTTON, self.on_day3part1_clicked)
        day3part2_btn = wx.Button(panel, label='Day 3 Part 2')
        day3part2_btn.Bind(wx.EVT_BUTTON, self.on_day3part2_clicked)
        day4part1_btn = wx.Button(panel, label='Day 4 Part 1')
        day4part1_btn.Bind(wx.EVT_BUTTON, self.on_day4part1_clicked)
        day4part2_btn = wx.Button(panel, label='Day 4 Part 2')
        day4part2_btn.Bind(wx.EVT_BUTTON, self.on_day4part2_clicked)

        btn_sizer = wx.BoxSizer(wx.VERTICAL)
        btn_sizer.Add(day1part1_btn, 0, wx.ALL, 5)
        btn_sizer.Add(day1part2_btn, 0, wx.ALL, 5)
        btn_sizer.Add(day2part1_btn, 0, wx.ALL, 5)
        btn_sizer.Add(day2part2_btn, 0, wx.ALL, 5)
        btn_sizer.Add(day3part1_btn, 0, wx.ALL, 5)
        btn_sizer.Add(day3part2_btn, 0, wx.ALL, 5)
        btn_sizer.Add(day4part1_btn, 0, wx.ALL, 5)
        btn_sizer.Add(day4part2_btn, 0, wx.ALL, 5)

        panel.SetSizer(btn_sizer)
        #endregion
        
        self.Show()
    
    def on_day1part1_clicked(self, event):
        wx.MessageBox(message=f"{Day1.Part1()}", caption="Day 1 Part 1", style=wx.OK)
    
    def on_day1part2_clicked(self, event):
        wx.MessageBox(message=f"{Day1.Part2()}", caption="Day 1 Part 2", style=wx.OK)

    def on_day2part1_clicked(self, event):
        wx.MessageBox(message=f"{Day2.Part1()}", caption="Day 2 Part 1", style=wx.OK)

    def on_day2part2_clicked(self, event):
        wx.MessageBox(message=f"{Day2.Part2()}", caption="Day 2 Part 2", style=wx.OK)

    def on_day3part1_clicked(self, event):
        wx.MessageBox(message=f"{Day3.Part1()}", caption="Day 3 Part 1", style=wx.OK)

    def on_day3part2_clicked(self, event):
        wx.MessageBox(message=f"{Day3.Part2()}", caption="Day 3 Part 2", style=wx.OK)

    def on_day4part1_clicked(self, event):
        wx.MessageBox(message=f"{Day4.Part1()}", caption="Day 4 Part 1", style=wx.OK)

    def on_day4part2_clicked(self, event):
        wx.MessageBox(message=f"{Day4.Part2()}", caption="Day 4 Part 2", style=wx.OK)

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()