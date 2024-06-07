# coding=utf-8
import wx
import wx.lib.newevent
import time
import threading
from datetime import datetime, timedelta
from queue import Queue
from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer, MinimaxComputerPlayer
from tic_tac_toe.logic.models import Mark, GameState
from tic_tac_toe.game.renderers import Renderer
from window.renderers import Window, WindowRenderer
from window.players import WindowPlayer
import re
import data as db
import json


# 创建一个事件，用于更新时间
UpdateTimeEvent, EVT_UPDATE_TIME = wx.lib.newevent.NewEvent()
global conn
conn = db.get_or_create_db('tictactoe.db')

class MyFrame(wx.Frame):
    def __init__(self, parent, title, username):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 250))

        # 设置窗口标题和大小
        self.SetSize((600, 400))
        self.Center()
        self.username = username
        self.p2_name = ''

        # 创建面板
        panel = wx.Panel(self)

        # 使用GridBagSizer布局管理器
        grid_sizer = wx.GridBagSizer(6, 6)

        # 左侧布局
        left_panel = wx.Panel(panel)
        vbox_left = wx.BoxSizer(wx.VERTICAL)
        text_inf = wx.StaticText(left_panel, label="我的信息")
        text_id = wx.StaticText(left_panel, label=f"玩家1：{self.username}")
        vbox_left.Add(text_inf, 0, wx.ALL, 5)
        vbox_left.Add(text_id, 0, wx.ALL, 5)
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

        self.result_text = wx.StaticText(middle_panel, label="")
        vbox_middle.Add(self.result_text, 0, wx.ALL, 5)

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
        self.p2_inf = wx.StaticText(right_panel, label=" ")
        vbox_right.Add(self.p2_inf, 0, wx.ALL, 5)
        right_panel.SetSizer(vbox_right)
        grid_sizer.Add(right_panel, pos=(0, 6), span=(1, 1), flag=wx.EXPAND | wx.ALL, border=15)




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
        self.player1 = player1
        if self.radio1.GetValue():
            player2 = RandomComputerPlayer(Mark("O"))
            self.p2_name = 'RandomComputer'
        elif self.radio2.GetValue():
            player2 = MinimaxComputerPlayer(Mark("O"))
            self.p2_name = 'MinimaxComputer'
        else:
            player2 = WindowPlayer(Mark("O"), self.events)
        self.player2 = player2
        renderer = WindowRenderer(self)
        self.game = TicTacToe(player1, player2, renderer)
        self.game_started = True

        global click_record
        click_record = []

        # 启动一个线程来处理游戏逻辑
        def game_loop():
            movelist, game_state = self.game.play()
            self.OnGameEnd(movelist, game_state)

        self.game_thread = threading.Thread(target=game_loop)
        self.game_thread.start()

    def UpdateTime(self, event):
        if self.start_time:
            global elapsed_time
            elapsed_time = datetime.now() - self.start_time
            wx.PostEvent(self, UpdateTimeEvent(elapsed_time=elapsed_time))
            elapsed_time = str(elapsed_time)


    def OnUpdateTime(self, event):
        elapsed_time = event.elapsed_time
        self.time_text.SetLabel(f"time：{str(elapsed_time).split('.')[0]}")


    def OnGameEnd(self, movelist, game_state):
        # 停止计时器
        wx.CallAfter(self.timer.Stop)
        self.player1_id = db.get_player_id_by_name(self.username)
        self.player2_id = db.get_player_id_by_name(self.p2_name)
        winner = None
        loser = None
        is_tie = False
        if not game_state.tie:
            if self.player1.mark == game_state.winner.value:
                winner = self.player1_id
                loser = self.player2_id
                self.result_text.SetLabelText(f"Player 1 wins!")
            else:
                winner = self.player2_id
                loser = self.player1_id
                self.result_text.SetLabelText(f"Player 2 wins!")

        else:
            self.result_text.SetLabelText("Ties!")
            is_tie = True

        print(f'p1_id:{self.player1_id}')
        print(f'p1_name:{self.username}')
        print(f'p2_id:{self.player2_id}')
        print(f'p2_name:{self.p2_name}')
        print(f'winner:{winner}')
        print(f'loser:{loser}')
        print(f'time:{str(elapsed_time)}')
        regex = r"Move\(mark=<([A-Za-z.]+): '([XO])'>, cell_index=(\d+)"
        matches = re.findall(regex, str(movelist))
        mark_log = ''
        for match in matches:
            mark = match[1]
            cell_index = int(match[2])
            mark_log += mark + str(cell_index+1) + ','
        print(f'对局细节：{mark_log}')
        db.insert_game(self.player1_id, self.username, self.player2_id, self.p2_name, mark_log, str(elapsed_time), winner, loser)
        db.update_player_stats(winner, loser, is_tie, self.player1_id, self.player2_id)
        game_data = {
            'p1_id': self.player1_id,
            'p1_name': self.username,
            'p2_id': self.player2_id,
            'p2_name': self.p2_name,
            'winner': winner,
            'loser': loser,
            'time': str(elapsed_time),
            '对局细节': mark_log.rstrip(',')
        }

        self.write_game_data_to_json(game_data)

    def write_game_data_to_json(self, game_data):
        try:
            with open('game_data.json', 'a', encoding='utf-8') as json_file:
                json.dump(game_data, json_file, ensure_ascii=False, indent=4)
                json_file.write('\n')
        except IOError as e:
            print(f"Failed to write game data to JSON file: {e}")

    # 添加玩家键
    def add_player(self, event):
        self.radio1.SetValue(False)
        self.radio2.SetValue(False)

        import login
        class Login(login.LoginWindow):
            def __init__(self, parent, title, button, p2_inf, callback):
                super(Login, self).__init__(parent, title=title)
                self.button = button
                self.p2_inf = p2_inf
                self.callback = callback  # 保存回调函数

            def onLogin(self, e):
                self.p2_name = self.inputTextUserName.GetValue()
                self.password = self.inputTextPassword.GetValue()
                self.Close()
                self.button.Destroy()
                self.p2_inf.SetLabelText(f'玩家2：{self.p2_name}')
                self.callback(self.p2_name)  # 调用回调函数并传递p2_name

        def set_p2_name(p2_name):
            self.p2_name = p2_name

        login_frame = Login(None, title='登录', button=self.button, p2_inf=self.p2_inf, callback=set_p2_name)
        login_frame.Show()



class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        return True


