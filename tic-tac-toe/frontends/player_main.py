import wx
import ui_play
import register_or_login
import player_check
  
class TicTacToePlayerFrame(wx.Frame):  
    def __init__(self, parent, title, username):
        style = wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL  
        super(TicTacToePlayerFrame, self).__init__(parent, title=title, size=(800, 600), style=style)  
        self.CreateStatusBar()  
        self.username = username  
        self.SetStatusText('已登录用户: {}'.format(self.username))

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
        register_or_login_frame = register_or_login.MyFrame(None, title='井字棋')
        register_or_login_frame.Show()
        self.Close()

    def OnNewGame(self, e):  
        # 这里可以添加开始新游戏的逻辑  
        ui_play_frame = ui_play.MyFrame(None, title='井字棋', username=self.username)
        ui_play_frame.Show()

  
    def OnViewHistory(self, e):  
        # 这里可以添加查看历史游戏的逻辑  
        player_check_frame = player_check.PlayerFrame(self, 'PlayerNameExample', title='玩家查看')
        player_check_frame.Show()
  
    def OnAbout(self, e):  
        # 这里可以添加关于对话框的逻辑  
        print("关于井字棋游戏")
  

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = TicTacToePlayerFrame(None, '井字棋游戏 - 玩家', 'PlayerName')
    frame.CentreOnScreen() 
    frame.Show()
    app.MainLoop()
