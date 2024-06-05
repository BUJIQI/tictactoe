import wx
import data as db

class PlayerFrame(wx.Frame):  
    def __init__(self, parent,player_name,title="Player Information"):    
        # 确保 parent 作为位置参数传递，title 作为关键字参数传递  
        super(PlayerFrame, self).__init__(parent, title=title)  # 这里不需要修改，已经是正确的  
        self.player_name = player_name  
    
        # 例如，在状态栏中显示用户名  
        self.CreateStatusBar()  
        self.SetStatusText('查看用户: {}'.format(self.player_name))  
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
    
        # 绑定按钮事件
        self.radio_basic_info.Bind(wx.EVT_RADIOBUTTON, self.on_radio_basic_info)
        self.radio_win.Bind(wx.EVT_RADIOBUTTON, self.on_radio_win)
        self.radio_tie.Bind(wx.EVT_RADIOBUTTON, self.on_radio_tie)
        self.radio_lose.Bind(wx.EVT_RADIOBUTTON, self.on_radio_lose)
        self.Bind(wx.EVT_BUTTON, self.on_exit, self.btn_exit)
        
        # 设置窗口属性
        self.SetTitle('玩家查看')
        self.SetSize((629, 400))
        
        # 初始化basic
        self.init_list1() 
        game_records =db.get_player_game_records_basic(self.player_name)
        index = 0
        for record in game_records:
            self.list_ctrl.InsertItem(index, str(record[0]))
            self.list_ctrl.SetItem(index, 1, record[1])
            self.list_ctrl.SetItem(index, 2, record[2])
            self.list_ctrl.SetItem(index, 3, str(record[3]))
            self.list_ctrl.SetItem(index, 4, str(record[4]))
            self.list_ctrl.SetItem(index, 5, str(record[5]))
            self.list_ctrl.SetItem(index, 6, str(record[6]))
            index += 1
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
         game_records =db.get_player_game_records_basic(self.player_name)
         self.list_ctrl.DeleteAllItems()
         index = 0
         for record in game_records:
             self.list_ctrl.InsertItem(index, str(record[0]))
             self.list_ctrl.SetItem(index, 1, record[1])
             self.list_ctrl.SetItem(index, 2, record[2])
             self.list_ctrl.SetItem(index, 3, str(record[3]))
             self.list_ctrl.SetItem(index, 4, str(record[4]))
             self.list_ctrl.SetItem(index, 5, str(record[5]))
             self.list_ctrl.SetItem(index, 6, str(record[6]))
             index += 1
  
    def on_radio_win(self, event):  
        self.init_list2()  
        game_records =db.get_player_game_records(self.player_name)  
        self.update_list_ctrl(game_records['wins'], '胜局')  
  
    def on_radio_tie(self, event):
        self.init_list2()
        game_records =db.get_player_game_records(self.player_name)  
        self.update_list_ctrl(game_records['ties'], '平局')  
  
    def on_radio_lose(self, event):
        self.init_list2()
        game_records =db.get_player_game_records(self.player_name)  
        self.update_list_ctrl(game_records['losses'], '败局')  
  
    def update_list_ctrl(self, result, category):    
        index = 0  
        for game_id, detail_text, time in result:  
            # 更新列表控件的列，这里需要根据实际情况调整列的数量和内容  
            self.list_ctrl.InsertItem(index, str(game_id))  # 游戏编号  
            self.list_ctrl.SetItem(index, 1, detail_text)   # 对局详情  
            self.list_ctrl.SetItem(index, 2, time)         # 时长        
            index += 1  
            
    def on_exit(self, event):
        self.Close(True)
   
  
# 示例用法   
class MyApp(wx.App):
    def OnInit(self):
        frame = PlayerFrame(None, ' ', title='玩家查看')  
        frame.Show(True)  
        return True  
