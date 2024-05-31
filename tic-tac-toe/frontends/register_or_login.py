import wx
import register  # 导入注册窗口模块
import login  # 导入登录窗口模块


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # 创建面板
        panel = wx.Panel(self)

        # 创建垂直框架布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建占位空间，用于垂直居中
        vbox.AddStretchSpacer()

        # 创建水平框架布局管理器，用于按钮水平居中
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # 创建按钮
        self.register_button = wx.Button(panel, label='注册')
        self.login_button = wx.Button(panel, label='登录')

        # 在水平框架布局管理器中添加占位空间
        hbox.AddStretchSpacer()
        hbox.Add(self.register_button, 0, wx.ALL, 10)
        hbox.Add(self.login_button, 0, wx.ALL, 10)
        hbox.AddStretchSpacer()

        # 将水平框架布局管理器添加到垂直框架布局管理器中
        vbox.Add(hbox, 0, wx.ALIGN_CENTER_HORIZONTAL)

        # 创建占位空间，用于垂直居中
        vbox.AddStretchSpacer()

        # 设置面板的布局管理器
        panel.SetSizer(vbox)

        # 设置窗口的属性
        self.SetTitle('井字棋')
        self.Centre()

        # 绑定按钮事件
        self.register_button.Bind(wx.EVT_BUTTON, self.on_register)
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)

    def on_register(self, event):
        # 创建并显示注册窗口
        register_frame = register.RegisterWindow(None, title='注册')
        register_frame.Show()
        self.Close()

    def on_login(self, event):
        # 创建并显示登录窗口
        login_frame = login.LoginWindow(None, title='登录')
        login_frame.Show()
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title='井字棋', size=(300, 150), style=wx.CAPTION | wx.CLOSE_BOX)
        frame.Show(True)
        return True


# 运行应用
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
