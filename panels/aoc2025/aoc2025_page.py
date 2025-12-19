import wx
from .aoc2025 import Day1, Day2, Day3, Day4

class AoC2025Page(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        day1part1_btn = wx.Button(self, label='Day 1 Part 1')
        day1part1_btn.Bind(wx.EVT_BUTTON, self.on_day1part2_clicked)
        day1part2_btn = wx.Button(self, label='Day 1 Part 2')
        day1part2_btn.Bind(wx.EVT_BUTTON, self.on_day1part2_clicked)
        day2part1_btn = wx.Button(self, label='Day 2 Part 1')
        day2part1_btn.Bind(wx.EVT_BUTTON, self.on_day2part1_clicked)
        day2part2_btn = wx.Button(self, label='Day 2 Part 2')
        day2part2_btn.Bind(wx.EVT_BUTTON, self.on_day2part2_clicked)
        day3part1_btn = wx.Button(self, label='Day 3 Part 1')
        day3part1_btn.Bind(wx.EVT_BUTTON, self.on_day3part1_clicked)
        day3part2_btn = wx.Button(self, label='Day 3 Part 2')
        day3part2_btn.Bind(wx.EVT_BUTTON, self.on_day3part2_clicked)
        day4part1_btn = wx.Button(self, label='Day 4 Part 1')
        day4part1_btn.Bind(wx.EVT_BUTTON, self.on_day4part1_clicked)
        day4part2_btn = wx.Button(self, label='Day 4 Part 2')
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

        self.SetSizer(btn_sizer)

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