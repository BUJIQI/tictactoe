import wx

class RegisterWindow(wx.Frame):
    def __init__(self, parent, title):
        style = wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL  
        super(RegisterWindow, self).__init__(parent, title=title, size=(800, 600), style=style)
        panel = wx.Panel(self, wx.ID_ANY)
        
        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        labelUser = wx.StaticText(panel, label="用户名:")
        self.inputTextUserID = wx.TextCtrl(panel)
        
        labelPassword = wx.StaticText(panel, label="密码:")
        self.inputTextPassword = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        
        lblList = ['管理员', '玩家']
        self.rboxUserType = wx.RadioBox(panel, label='角色', choices=lblList)
        self.rboxUserType.SetSelection(1) #默认选择玩家 
        
        okBtn = wx.Button(panel, label="注册")
        cancelBtn = wx.Button(panel, label="取消")
        
        topSizer = wx.BoxSizer(wx.VERTICAL)
        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        usertypeSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        userSizer.Add(labelUser, 0, wx.ALL, 5)
        userSizer.Add(self.inputTextUserID, 0, wx.ALL, 5)
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

        self.Bind(wx.EVT_BUTTON, self.onRegister, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)
        self.Center()
        
    def onRegister(self, e):
        userid = self.inputTextUserID.GetValue()
        password = self.inputTextPassword.GetValue()
        
        if len(userid.strip()) == 0:
            wx.MessageBox('请输入用户名！')
            self.inputTextUserID.SetFocus()
            return None
        if len(password.strip()) == 0:
            wx.MessageBox('请输入注册密码！')
            self.inputTextPassword.SetFocus()
            return None
        

        
    def onCancel(self, e):
        self.Close(True)
        

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = RegisterWindow(None, "注册")
    frame.CentreOnScreen() 
    frame.Show()
    app.MainLoop()
