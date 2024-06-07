import wx
import ui_play
import game_main
import player_check


class TicTacToePlayerFrame(wx.Frame):
    def __init__(self, parent, title, username):
        style = wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL
        super(TicTacToePlayerFrame, self).__init__(parent, title=title, size=(800, 600), style=style)
        self.CreateStatusBar()
        self.username = username

        # 创建菜单栏  
        menubar = wx.MenuBar()

        # 系统菜单  
        sysmenu = wx.Menu()
        menuExit = sysmenu.Append(wx.ID_EXIT, "退出", "退出游戏")
        menubar.Append(sysmenu, "&系统")
        menuReturnLogin = sysmenu.Append(wx.ID_ANY, "返回登录", "返回登录界面")
        self.Bind(wx.EVT_MENU, self.OnReturnLogin, menuReturnLogin)

        # 玩家菜单  
        playermenu = wx.Menu()
        menuGame = playermenu.Append(wx.ID_ANY, "开始新游戏", "开始一局新的井字棋游戏")
        menuView = playermenu.Append(wx.ID_ANY, "查看历史", "查看过去的游戏记录")
        menubar.Append(playermenu, "&玩家")

        # 关于菜单  
        helpmenu = wx.Menu()
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "关于", "关于井字棋游戏")
        menubar.Append(helpmenu, "&帮助")

        # 绑定事件  
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnReturnLogin, menuReturnLogin)
        self.Bind(wx.EVT_MENU, self.OnNewGame, menuGame)
        self.Bind(wx.EVT_MENU, self.OnViewHistory, menuView)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        # 设置菜单栏  
        self.SetMenuBar(menubar)
        self.Show()
        self.Center()

    def OnExit(self, e):
        self.Close()

    def OnReturnLogin(self, e):
        # 这里应该添加返回登录界面的逻辑  
        register_or_login_frame = game_main.MyFrame(None, title='井字棋')
        register_or_login_frame.Show()
        self.Close()

    def OnNewGame(self, e):
        # 这里可以添加开始新游戏的逻辑  
        ui_play_frame = ui_play.MyFrame(None, title='井字棋', username=self.username)
        ui_play_frame.Show()

    def OnViewHistory(self, e):
        # 这里可以添加查看历史游戏的逻辑  
        player_check_frame = player_check.PlayerFrame(None)
        player_check_frame.Show()
        self.Close()

    def OnAbout(self, e):
        description = '''
          本游戏基于传统井字棋玩法，同时拓展了玩家查询历史对局及积分功能。

           玩家部分：
           开始新游戏：玩家-开始新游戏。
           对手可选择简单难度或困难难度，同时支持添加人类玩家二。
           （可重复添加玩家一账号信息至玩家二，进行个人练习）。
           查看对局历史：玩家-查看历史。
           玩家可在此查看自己的基本信息（胜、败、平局数与总积分）。

           管理员部分：
           增删查改游戏信息：管理-查看游戏。
           可在此进行玩家信息，管理员信息，游戏对局细节的修改。

           其他：
           游戏细节：游戏细节描述为“标号与数字”的组合。
           例“X5”，代表X标记，位置第五格，九宫格位置序号从上到下从左至右分别为1~9。
           积分：一局游戏结束后，赢家积分+1，输家积分-1，平局时积分不变。
           '''

        dlg = wx.MessageDialog(self, description, "关于井字棋游戏", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


