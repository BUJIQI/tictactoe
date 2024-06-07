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
        register_or_login_frame = register_or_login.MyFrame(None, title='井字棋')
        register_or_login_frame.Show()
        self.Close()
  
    def OnViewGames(self, e):  
        # 这里可以添加查看所有游戏记录的逻辑  
        administrator_check_frame = administrator_check.UserWindow(None, title='登录')
        administrator_check_frame.Show()
        self.Close()
  
    def OnAbout(self, e):  
        # 这里可以添加关于对话框的逻辑  
        print("关于井字棋游戏")  
  

