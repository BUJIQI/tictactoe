import wx

class PlayerFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(PlayerFrame, self).__init__(*args, **kw)
        
        # 创建面板
        panel = wx.Panel(self)
        
        # 创建布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # 创建水平框架布局管理器用于单选按钮
        hbox_radio = wx.BoxSizer(wx.HORIZONTAL)
        
        # 创建单选按钮
        self.radio_basic_info = wx.RadioButton(panel, label='基本信息', style=wx.RB_GROUP)
        self.radio_win = wx.RadioButton(panel, label='胜局')
        self.radio_tie = wx.RadioButton(panel, label='平局')
        self.radio_lose = wx.RadioButton(panel, label='败局')
        
        # 添加单选按钮到水平框架布局管理器中
        hbox_radio.AddStretchSpacer(1)
        hbox_radio.Add(self.radio_basic_info, 0, wx.ALL, 5)
        hbox_radio.Add(self.radio_win, 0, wx.ALL, 5)
        hbox_radio.Add(self.radio_tie, 0, wx.ALL, 5)
        hbox_radio.Add(self.radio_lose, 0, wx.ALL, 5)
        hbox_radio.AddStretchSpacer(1)
        
        # 将单选按钮框架布局管理器添加到垂直框架布局管理器中
        vbox.Add(hbox_radio, 0, wx.EXPAND)
        
        # 创建列表框
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT)
        
        # 添加列表框到垂直框架布局管理器中
        vbox.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        
        # 创建水平框架布局管理器用于按钮
        hbox_btn = wx.BoxSizer(wx.HORIZONTAL)
        
        # 创建退出按钮
        self.btn_exit = wx.Button(panel, label='退出')
        
        # 添加退出按钮到水平框架布局管理器中
        hbox_btn.AddStretchSpacer(1)
        hbox_btn.Add(self.btn_exit, 0, wx.ALL, 5)
        hbox_btn.AddStretchSpacer(1)
        
        # 将按钮框架布局管理器添加到垂直框架布局管理器中
        vbox.Add(hbox_btn, 0, wx.ALIGN_CENTER)
        
        # 设置面板的布局管理器
        panel.SetSizer(vbox)
        
        # 初始化列表框显示内容
        self.init_list1()
        
        # 绑定单选按钮事件
        self.radio_basic_info.Bind(wx.EVT_RADIOBUTTON, self.on_radio_basic_info)
        self.radio_win.Bind(wx.EVT_RADIOBUTTON, self.on_radio_win)
        self.radio_tie.Bind(wx.EVT_RADIOBUTTON, self.on_radio_tie)
        self.radio_lose.Bind(wx.EVT_RADIOBUTTON, self.on_radio_lose)
        
        # 设置窗口属性
        self.SetTitle('玩家查看')
        self.SetSize((629, 400))
        self.Centre()
        
    def init_list1(self):
        # 初始化列表框显示内容 (编号、用户名、密码、胜局、平局、败局、得分)
        self.list_ctrl.ClearAll()
        self.list_ctrl.InsertColumn(0, '编号', width=80)
        self.list_ctrl.InsertColumn(1, '玩家名', width=100)
        self.list_ctrl.InsertColumn(2, '密码', width=100)
        self.list_ctrl.InsertColumn(3, '胜局', width=80)
        self.list_ctrl.InsertColumn(4, '平局', width=80)
        self.list_ctrl.InsertColumn(5, '败局', width=80)
        self.list_ctrl.InsertColumn(6, '得分', width=80)
    
    def init_list2(self):
        # 初始化列表框显示内容 (对局编号、对局详情、时长)
        self.list_ctrl.ClearAll()
        self.list_ctrl.InsertColumn(0, '游戏编号', width=100)
        self.list_ctrl.InsertColumn(1, '对局详情', width=350)
        self.list_ctrl.InsertColumn(2, '时长', width=150)
    
    def on_radio_basic_info(self, event):
        self.init_list1()
        
    def on_radio_win(self, event):
        self.init_list2()
        
    def on_radio_tie(self, event):
        self.init_list2()
        
    def on_radio_lose(self, event):
        self.init_list2()
        
    def on_exit(self, event):
        self.Close()
        
class MyApp(wx.App):
    def OnInit(self):
        frame = PlayerFrame(None)
        frame.Show(True)
        return True

# 运行应用
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()


