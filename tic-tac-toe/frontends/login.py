import wx
import player_main
import admin_main
import data as db


class LoginWindow(wx.Frame):
    def __init__(self, parent, title):
        style = wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL
        super(LoginWindow, self).__init__(parent, title=title, size=(800, 600), style=style)
        panel = wx.Panel(self, wx.ID_ANY)

        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        labelUser = wx.StaticText(panel, label="用户名:")
        self.inputTextUserName = wx.TextCtrl(panel)

        labelPassword = wx.StaticText(panel, label="密码:")
        self.inputTextPassword = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        lblList = ['管理员', '玩家']
        self.rboxUserType = wx.RadioBox(panel, label='角色', choices=lblList)
        self.rboxUserType.SetSelection(1)  # 默认选择玩家

        okBtn = wx.Button(panel, label="登录")
        cancelBtn = wx.Button(panel, label="取消")

        topSizer = wx.BoxSizer(wx.VERTICAL)
        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        usertypeSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        userSizer.Add(labelUser, 0, wx.ALL, 5)
        userSizer.Add(self.inputTextUserName, 0, wx.ALL, 5)
        passwordSizer.Add(labelPassword, 0, wx.ALL, 5)
        passwordSizer.Add(self.inputTextPassword, 0, wx.ALL, 5)
        usertypeSizer.Add(self.rboxUserType)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        topSizer.Add(userSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(passwordSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(usertypeSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        self.Bind(wx.EVT_BUTTON, self.onLogin, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)
        self.Center()

    def onLogin(self, e):
        username = self.inputTextUserName.GetValue()
        password = self.inputTextPassword.GetValue()
        UserType = self.rboxUserType.GetStringSelection()

        if len(username.strip()) == 0:
            wx.MessageBox('请输入用户名！')
            self.inputTextUserName.SetFocus()
            return None
        if len(password.strip()) == 0:
            wx.MessageBox('请输入登录密码！')
            self.inputTextPassword.SetFocus()
            return None


        if db.login(username, password,UserType):
            wx.MessageBox('登录成功！')
            if self.rboxUserType.GetSelection() == 0:
                if username and password:
                    admin_main_frame = admin_main.TicTacToeAdminFrame(None, title='井字棋', username=username)
                    admin_main_frame.Show()
                    self.Close()

            if self.rboxUserType.GetSelection() == 1:
                if username and password:
                    player_main_frame = player_main.TicTacToePlayerFrame(None, title='井字棋', username=username)
                    player_main_frame.Show()
                    self.Close()  # 这里可以跳转到游戏主界面或其他逻辑
        else:
            wx.MessageBox('登录失败，请检查您的用户名和密码！')

    def onCancel(self, e):
        self.Close(True)



