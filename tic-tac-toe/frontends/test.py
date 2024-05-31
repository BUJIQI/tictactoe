import wx
import wx.lib.newevent
import time
import threading
from datetime import datetime, timedelta
from queue import Queue
from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer, MinimaxComputerPlayer
from tic_tac_toe.logic.models import Mark
from tic_tac_toe.game.renderers import Renderer
from window.renderers import Window, WindowRenderer  # 确保路径正确
from window.players import WindowPlayer

# 创建一个事件，用于更新时间
UpdateTimeEvent, EVT_UPDATE_TIME = wx.lib.newevent.NewEvent()


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # 设置窗口标题和大小
        self.SetTitle("Play")
        self.SetSize((600, 400))
        self.Center()

        # 创建面板
        panel = wx.Panel(self)

        # 使用GridBagSizer布局管理器
        grid_sizer = wx.GridBagSizer(6, 6)

        # 左侧布局
        left_panel = wx.Panel(panel)
        vbox_left = wx.BoxSizer(wx.VERTICAL)
        text_inf = wx.StaticText(left_panel, label="我的信息")
        text_id = wx.StaticText(left_panel, label="id:")
        text_score = wx.StaticText(left_panel, label="score:")
        vbox_left.Add(text_inf, 0, wx.ALL, 5)
        vbox_left.Add(text_id, 0, wx.ALL, 5)
        vbox_left.Add(text_score, 0, wx.ALL, 5)
        left_panel.SetSizer(vbox_left)
        grid_sizer.Add(left_panel, pos=(0, 0), span=(2, 2), flag=wx.EXPAND | wx.ALL, border=15)

        # 中间布局
        middle_panel = wx.Panel(panel)
        vbox_middle = wx.BoxSizer(wx.VERTICAL)
        self.time_text = wx.StaticText(middle_panel, label="time：")
        vbox_middle.Add(self.time_text, 0, wx.ALL, 5)

        # 插入Tic-Tac-Toe游戏
        self.events = Queue()
        self.buttons = []
        grid = wx.GridSizer(3, 3, 5, 5)  # 3x3 grid with 5px gaps
        for _ in range(3):
            for _ in range(3):
                button = wx.Button(middle_panel, label="", size=(50, 50))
                self.buttons.append(button)
                button.Bind(wx.EVT_BUTTON, self.on_button_click)
                grid.Add(button, 0, wx.EXPAND)
        vbox_middle.Add(grid, 1, wx.EXPAND | wx.ALL, 20)


        self.start_button = wx.Button(middle_panel, label='开始')
        self.start_button.Bind(wx.EVT_BUTTON, self.OnStartGame)
        vbox_middle.Add(self.start_button, 0, wx.ALL | wx.ALIGN_RIGHT, 20)
        middle_panel.SetSizer(vbox_middle)
        grid_sizer.Add(middle_panel, pos=(0, 3), span=(2, 3), flag=wx.EXPAND | wx.ALL, border=15)

        # 右侧布局
        right_panel = wx.Panel(panel)
        vbox_right = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(right_panel, label="选择你的对手")
        vbox_right.Add(text, 0, wx.ALL, 5)
        self.radio1 = wx.RadioButton(right_panel, label="简单", style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(right_panel, label="困难")
        vbox_right.Add(self.radio1, 0, wx.ALL, 5)
        vbox_right.Add(self.radio2, 0, wx.ALL, 5)
        self.button = wx.Button(right_panel, label='添加玩家')
        vbox_right.Add(self.button, 0, wx.ALL, 5)
        right_panel.SetSizer(vbox_right)
        grid_sizer.Add(right_panel, pos=(0, 6), span=(1, 1), flag=wx.EXPAND | wx.ALL, border=15)

        # 游戏结果文本
        self.result_text = wx.StaticText(panel, label="")
        grid_sizer.Add(self.result_text, pos=(3, 0), span=(1, 7), flag=wx.EXPAND | wx.ALL, border=15)

        # 设置主面板布局
        panel.SetSizer(grid_sizer)

        # 绑定按钮事件
        self.button.Bind(wx.EVT_BUTTON, self.add_player)

        # 定时器与线程
        self.Bind(EVT_UPDATE_TIME, self.OnUpdateTime)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.UpdateTime, self.timer)

        self.start_time = None
        self.game = None

    def on_button_click(self, event):
        if self.game_started:
            clicked_button = event.GetEventObject()
            self.events.put(self.buttons.index(clicked_button))

    # 开始键
    def OnStartGame(self, event):
        self.start_time = datetime.now()
        self.timer.Start(1000)

        # 根据单选按钮的选择创建玩家
        player1 = WindowPlayer(Mark("X"), self.events)
        if self.radio1.GetValue():
            player2 = RandomComputerPlayer(Mark("O"))
        elif self.radio2.GetValue():
            player2 = MinimaxComputerPlayer(Mark("O"))
        else:
            player2 = WindowPlayer(Mark("O"), self.events)

        renderer = WindowRenderer(self)
        self.game = TicTacToe(player1, player2, renderer)
        self.game_started = True

        # 启动一个线程来处理游戏逻辑
        def game_loop():
            winner = self.game.play()
            self.OnGameEnd(winner)

        self.game_thread = threading.Thread(target=game_loop)
        self.game_thread.start()

    def UpdateTime(self, event):
        if self.start_time:
            elapsed_time = datetime.now() - self.start_time
            wx.PostEvent(self, UpdateTimeEvent(elapsed_time=elapsed_time))

    def OnUpdateTime(self, event):
        elapsed_time = event.elapsed_time
        self.time_text.SetLabel(f"time：{str(elapsed_time).split('.')[0]}")

    def OnGameEnd(self, winner):
        # 停止计时器
        wx.CallAfter(self.timer.Stop)
        if winner:
            self.result_text.SetLabel(f"{winner} wins")
        else:
            self.result_text.SetLabel("Ties")

    # 添加玩家键
    def add_player(self, event):
        self.radio1
