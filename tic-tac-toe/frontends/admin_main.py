import wx
import game_main
import administrator_check
  
class TicTacToeAdminFrame(wx.Frame):  
    def __init__(self, parent, title, username):  
        style = wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL  
        super(TicTacToeAdminFrame, self).__init__(parent, title=title, size=(800, 600), style=style)   
        self.CreateStatusBar()  
        self.username = username  
          
        # 创建菜单栏  
        menubar = wx.MenuBar()  
          
        # 系统菜单  
        sysmenu = wx.Menu()  
        menuExit = sysmenu.Append(wx.ID_EXIT, "退出", "退出系统")  
        menubar.Append(sysmenu, "&系统")  
        menuReturnLogin = sysmenu.Append(wx.ID_ANY, "返回登录", "返回登录界面")  
        # 管理者菜单（只有查看）  
        adminmenu = wx.Menu()  
        menuView = adminmenu.Append(wx.ID_ANY, "查看游戏", "查看所有游戏记录")  
        menubar.Append(adminmenu, "&管理")  
          
        # 关于菜单  
        helpmenu = wx.Menu()  
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "关于", "关于井字棋游戏")  
        menubar.Append(helpmenu, "&帮助")  
          
        # 绑定事件  
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)  
        self.Bind(wx.EVT_MENU, self.OnViewGames, menuView)  
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnReturnLogin, menuReturnLogin)

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
  
    def OnViewGames(self, e):  
        # 这里可以添加查看所有游戏记录的逻辑  
        administrator_check_frame = administrator_check.UserWindow(None, title='管理员查看')
        administrator_check_frame.Show()

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
  


  

