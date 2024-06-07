import wx
import data

class UserWindow(wx.Frame):
    def __init__(self, parent, title):
        super(UserWindow, self).__init__(parent, title=title, size=(800, 600))
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.list = []
        
        # 创建控件
        lblListAction = ['插入', '修改', '删除']
        self.rboxAction = wx.RadioBox(self.panel, label='操作', choices=lblListAction)
        lblListType = ['玩家信息', '管理员信息', '游戏细节']
        self.rboxTableType = wx.RadioBox(self.panel, label='表', choices=lblListType)

        self.listUser = wx.ListCtrl(self.panel, wx.ID_ANY, size=(400, 400), style=wx.LC_REPORT)

        self.labelPlayerID = wx.StaticText(self.panel, wx.ID_ANY, '玩家编号:')
        self.inputTextPlayerID = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        self.inputTextPlayerID.Disable()
        self.labelPlayerName = wx.StaticText(self.panel, wx.ID_ANY, '玩家名称:')
        self.inputTextPlayerName = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        self.labelPassword = wx.StaticText(self.panel, wx.ID_ANY, '玩家密码:')
        self.inputTextPassword = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        self.labelWin = wx.StaticText(self.panel, wx.ID_ANY, '游戏胜局:')
        self.inputTextWin = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        self.labelTie = wx.StaticText(self.panel, wx.ID_ANY, '游戏平局:')
        self.inputTextTie = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        self.labelLose = wx.StaticText(self.panel, wx.ID_ANY, '游戏败局:')
        self.inputTextLose = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        self.labelPoint = wx.StaticText(self.panel, wx.ID_ANY, '游戏得分:')
        self.inputTextPoint = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        self.list = [self.labelPlayerID, self.inputTextPlayerID, 
                     self.labelPlayerName, self.inputTextPlayerName, 
                     self.labelPassword, self.inputTextPassword,
                     self.labelWin, self.inputTextWin,
                     self.labelTie, self.inputTextTie,
                     self.labelLose, self.inputTextLose,
                     self.labelPoint, self.inputTextPoint]

        self.insertBtn = wx.Button(self.panel, wx.ID_ANY, '插入')
        self.updateBtn = wx.Button(self.panel, wx.ID_ANY, '更新')
        self.updateBtn.Disable()
        self.deleteBtn = wx.Button(self.panel, wx.ID_ANY, '删除')
        self.deleteBtn.Disable()
        self.exitBtn = wx.Button(self.panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        editSizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer6 = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer7 = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        bigSizer = wx.BoxSizer(wx.VERTICAL)

        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)
        optionSizer.Add(self.rboxTableType, 0, wx.ALL, 5)

        listSizer.Add(self.listUser, 0, wx.ALL, 5)

        self.Sizer1.Add(self.labelPlayerID, 0, wx.ALL, 5)
        self.Sizer1.Add(self.inputTextPlayerID, 0, wx.ALL, 5)
        self.Sizer2.Add(self.labelPlayerName, 0, wx.ALL, 5)
        self.Sizer2.Add(self.inputTextPlayerName, 0, wx.ALL, 5)
        self.Sizer3.Add(self.labelPassword, 0, wx.ALL, 5)
        self.Sizer3.Add(self.inputTextPassword, 0, wx.ALL, 5)
        self.Sizer4.Add(self.labelWin, 0, wx.ALL, 5)
        self.Sizer4.Add(self.inputTextWin, 0, wx.ALL, 5)
        self.Sizer5.Add(self.labelTie, 0, wx.ALL, 5)
        self.Sizer5.Add(self.inputTextTie, 0, wx.ALL, 5)
        self.Sizer6.Add(self.labelLose, 0, wx.ALL, 5)
        self.Sizer6.Add(self.inputTextLose, 0, wx.ALL, 5)
        self.Sizer7.Add(self.labelPoint, 0, wx.ALL, 5)
        self.Sizer7.Add(self.inputTextPoint, 0, wx.ALL, 5)
        btnSizer.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.exitBtn, 0, wx.ALL, 5)

        editSizer.Add(self.Sizer1, 0, wx.ALL, 5)
        editSizer.Add(self.Sizer2, 0, wx.ALL, 5)
        editSizer.Add(self.Sizer3, 0, wx.ALL, 5)
        editSizer.Add(self.Sizer4, 0, wx.ALL, 5)
        editSizer.Add(self.Sizer5, 0, wx.ALL, 5)
        editSizer.Add(self.Sizer6, 0, wx.ALL, 5)
        editSizer.Add(self.Sizer7, 0, wx.ALL, 5)

        bigSizer.Add(editSizer, 0, wx.ALL, 5)
        bigSizer.Add(btnSizer, 0, wx.ALL, 5)
        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(bigSizer, 0, wx.ALL, 5)

        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)

        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件
        self.Bind(wx.EVT_RADIOBOX, self.onAction, self.rboxAction)
        self.Bind(wx.EVT_RADIOBOX, self.onTableType, self.rboxTableType)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onTableList, self.listUser)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, self.exitBtn)

        # 查询用户信息并显示
        self.populate_table_list()
        self.Center()


    def onAction(self, e):
        """事件处理函数：根据操作类型（插入、更新、删除）设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "插入":
            self.rboxTableType.Enable()
            self.insertBtn.Enable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
        elif action == "修改":
            self.rboxTableType.Enable()
            self.insertBtn.Disable()
            self.updateBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "删除":
            self.rboxTableType.Enable()
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Enable()

    def onTableType(self, e):
        """事件处理函数：表类别改变时，更改对应的列表和控件"""
        self.populate_table_list()
        self.refactor_control()
        
    def populate_table_list(self):
        """根据选择的表类型，显示对应的用户信息列表"""
        self.listUser.ClearAll()        
        table_type = self.rboxTableType.GetStringSelection()

        if table_type == "玩家信息":
            self.listUser.InsertColumn(0, '玩家编号', width=50)
            self.listUser.InsertColumn(1, '玩家名', width=50)
            self.listUser.InsertColumn(2, '玩家密码', width=100)
            self.listUser.InsertColumn(3, '胜局', width=50)
            self.listUser.InsertColumn(4, '平局', width=50)
            self.listUser.InsertColumn(5, '败局', width=50)
            self.listUser.InsertColumn(6, '得分', width=50)    
            
            player_list = data.get_player_list()
            index = 0
            for player in player_list:
                self.listUser.InsertItem(index, str(player[0]))
                self.listUser.SetItem(index, 1, player[1])
                self.listUser.SetItem(index, 2, player[2])
                self.listUser.SetItem(index, 3, str(player[3]))
                self.listUser.SetItem(index, 4, str(player[4]))
                self.listUser.SetItem(index, 5, str(player[5]))
                self.listUser.SetItem(index, 6, str(player[6]))
                index += 1 

        elif table_type == "管理员信息":
            self.listUser.InsertColumn(0, '管理员编号', width=130)
            self.listUser.InsertColumn(1, '管理员名', width=130)
            self.listUser.InsertColumn(2, '管理员密码', width=140)
            
            admin_list = data.get_admin_list()
            index = 0
            for admin in admin_list:
                self.listUser.InsertItem(index, str(admin[0]))
                self.listUser.SetItem(index, 1, admin[1])
                self.listUser.SetItem(index, 2, admin[2])
                index += 1 

        elif table_type == "游戏细节":
            self.listUser.InsertColumn(0, '游戏编号', width=20)
            self.listUser.InsertColumn(1, '玩家编号1', width=20)
            self.listUser.InsertColumn(2, '玩家名1', width=40)            
            self.listUser.InsertColumn(3, '玩家编号2', width=20)
            self.listUser.InsertColumn(4, '玩家名2', width=40)
            self.listUser.InsertColumn(5, '对局详情', width=200)
            self.listUser.InsertColumn(6, '时长', width=20)
            self.listUser.InsertColumn(7, '胜者', width=20)
            self.listUser.InsertColumn(8, '败者', width=20)
            
            game_list = data.get_game_list()
            index = 0
            for game in game_list:
                self.listUser.InsertItem(index, str(game[0]))
                self.listUser.SetItem(index, 1, str(game[1]))
                self.listUser.SetItem(index, 2, str(game[2]))
                self.listUser.SetItem(index, 3, str(game[3]))
                self.listUser.SetItem(index, 4, str(game[4]))
                self.listUser.SetItem(index, 5, game[5])
                self.listUser.SetItem(index, 6, game[6])
                self.listUser.SetItem(index, 7, str(game[7]))
                self.listUser.SetItem(index, 8, str(game[8]))
                index += 1 
            
    def refactor_control(self):
        '''根据选择的表类型，重构输入框'''
        # 删除原有控件
        for control in self.list:
            control.Destroy()        
        
        table_type = self.rboxTableType.GetStringSelection()  
        
        if table_type == "玩家信息":                
            # 重新添加布局控件
            self.labelPlayerID = wx.StaticText(self.panel, wx.ID_ANY, '玩家编号:')
            self.inputTextPlayerID = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.inputTextPlayerID.Disable()
            self.labelPlayerName = wx.StaticText(self.panel, wx.ID_ANY, '玩家名称:')
            self.inputTextPlayerName = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelPassword = wx.StaticText(self.panel, wx.ID_ANY, '玩家密码:')
            self.inputTextPassword = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelWin = wx.StaticText(self.panel, wx.ID_ANY, '游戏胜局:')
            self.inputTextWin = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelTie = wx.StaticText(self.panel, wx.ID_ANY, '游戏平局:')
            self.inputTextTie = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelLose = wx.StaticText(self.panel, wx.ID_ANY, '游戏败局:')
            self.inputTextLose = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelPoint = wx.StaticText(self.panel, wx.ID_ANY, '游戏得分:')
            self.inputTextPoint = wx.TextCtrl(self.panel, wx.ID_ANY, '')           
    
            self.Sizer1.Add(self.labelPlayerID, 0, wx.ALL, 5)
            self.Sizer1.Add(self.inputTextPlayerID, 0, wx.ALL, 5)
            self.Sizer2.Add(self.labelPlayerName, 0, wx.ALL, 5)
            self.Sizer2.Add(self.inputTextPlayerName, 0, wx.ALL, 5)
            self.Sizer3.Add(self.labelPassword, 0, wx.ALL, 5)
            self.Sizer3.Add(self.inputTextPassword, 0, wx.ALL, 5)
            self.Sizer4.Add(self.labelWin, 0, wx.ALL, 5)
            self.Sizer4.Add(self.inputTextWin, 0, wx.ALL, 5)
            self.Sizer5.Add(self.labelTie, 0, wx.ALL, 5)
            self.Sizer5.Add(self.inputTextTie, 0, wx.ALL, 5)
            self.Sizer6.Add(self.labelLose, 0, wx.ALL, 5)
            self.Sizer6.Add(self.inputTextLose, 0, wx.ALL, 5)
            self.Sizer7.Add(self.labelPoint, 0, wx.ALL, 5)
            self.Sizer7.Add(self.inputTextPoint, 0, wx.ALL, 5)                       
            
            self.list = [self.labelPlayerID, self.inputTextPlayerID, 
                         self.labelPlayerName, self.inputTextPlayerName, 
                         self.labelPassword, self.inputTextPassword,
                         self.labelWin, self.inputTextWin,
                         self.labelTie, self.inputTextTie,
                         self.labelLose, self.inputTextLose,
                         self.labelPoint, self.inputTextPoint]
            
        elif table_type == "管理员信息":                
            # 重新添加布局控件
            self.labelAdministratorID = wx.StaticText(self.panel, wx.ID_ANY, '管理员编号:')
            self.inputTextAdministratorID = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.inputTextAdministratorID.Disable()
            self.labelAdministratorName = wx.StaticText(self.panel, wx.ID_ANY, '管理员名称:')
            self.inputTextAdministratorName = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelPassword = wx.StaticText(self.panel, wx.ID_ANY, '管理员密码:')
            self.inputTextPassword = wx.TextCtrl(self.panel, wx.ID_ANY, '')
    
            self.Sizer1.Add(self.labelAdministratorID, 0, wx.ALL, 5)
            self.Sizer1.Add(self.inputTextAdministratorID, 0, wx.ALL, 5)
            self.Sizer2.Add(self.labelAdministratorName, 0, wx.ALL, 5)
            self.Sizer2.Add(self.inputTextAdministratorName, 0, wx.ALL, 5)
            self.Sizer3.Add(self.labelPassword, 0, wx.ALL, 5)
            self.Sizer3.Add(self.inputTextPassword, 0, wx.ALL, 5)
            
            self.list = [self.labelAdministratorID, self.inputTextAdministratorID, 
                         self.labelAdministratorName, self.inputTextAdministratorName, 
                         self.labelPassword, self.inputTextPassword]
            
        elif table_type == "游戏细节":                
            # 重新添加布局控件
            self.labelGameID = wx.StaticText(self.panel, wx.ID_ANY, '游戏编号:')
            self.inputTextGameID = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.inputTextGameID.Disable()
            self.labelPlayer1 = wx.StaticText(self.panel, wx.ID_ANY, '玩家 1号:')
            self.inputTextPlayerID1 = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.inputTextPlayerName1 = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.inputTextPlayerName1.Disable()
            self.labelPlayer2 = wx.StaticText(self.panel, wx.ID_ANY, '玩家 2号:')
            self.inputTextPlayerID2 = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.inputTextPlayerName2 = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.inputTextPlayerName2.Disable()
            self.labelLocation = wx.StaticText(self.panel, wx.ID_ANY, '对局详情:')
            self.inputTextLocation = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelDuration = wx.StaticText(self.panel, wx.ID_ANY, '游戏时长:')
            self.inputTextDuration = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelWinner = wx.StaticText(self.panel, wx.ID_ANY, '游戏胜者:')
            self.inputTextWinner = wx.TextCtrl(self.panel, wx.ID_ANY, '')
            self.labelLoser = wx.StaticText(self.panel, wx.ID_ANY, '游戏败者:')
            self.inputTextLoser = wx.TextCtrl(self.panel, wx.ID_ANY, '')
    
            self.Sizer1.Add(self.labelGameID, 0, wx.ALL, 5)
            self.Sizer1.Add(self.inputTextGameID, 0, wx.ALL, 5)
            self.Sizer2.Add(self.labelPlayer1, 0, wx.ALL, 5)
            self.Sizer2.Add(self.inputTextPlayerID1, 0, wx.ALL, 5)
            self.Sizer2.Add(self.inputTextPlayerName1, 0, wx.ALL, 5)
            self.Sizer3.Add(self.labelPlayer2, 0, wx.ALL, 5)
            self.Sizer3.Add(self.inputTextPlayerID2, 0, wx.ALL, 5)
            self.Sizer3.Add(self.inputTextPlayerName2, 0, wx.ALL, 5)
            self.Sizer4.Add(self.labelLocation, 0, wx.ALL, 5)
            self.Sizer4.Add(self.inputTextLocation, 0, wx.ALL, 5)
            self.Sizer5.Add(self.labelDuration, 0, wx.ALL, 5)
            self.Sizer5.Add(self.inputTextDuration, 0, wx.ALL, 5)
            self.Sizer6.Add(self.labelWinner, 0, wx.ALL, 5)
            self.Sizer6.Add(self.inputTextWinner, 0, wx.ALL, 5)
            self.Sizer7.Add(self.labelLoser, 0, wx.ALL, 5)
            self.Sizer7.Add(self.inputTextLoser, 0, wx.ALL, 5)
            
            self.list = [self.labelGameID, self.inputTextGameID,
                         self.labelPlayer1, self.inputTextPlayerID1, self.inputTextPlayerName1,
                         self.labelPlayer2, self.inputTextPlayerID2, self.inputTextPlayerName2, 
                         self.labelLocation, self.inputTextLocation,
                         self.labelDuration, self.inputTextDuration,
                         self.labelWinner, self.inputTextWinner,
                         self.labelLoser, self.inputTextLoser] 

        self.panel.Layout()                 
            
    def onTableList(self, e):
        """事件处理函数：在列表中选择用户，内容显示在右侧"""
        self.refresh_screen()
        index = e.GetIndex()  # 获得被激活表项的索引号
        table_type = self.rboxTableType.GetStringSelection()

        if table_type == "玩家信息":
            self.inputTextPlayerID.SetValue(self.listUser.GetItem(index, 0).GetText())
            self.inputTextPlayerName.SetValue(self.listUser.GetItem(index, 1).GetText())
            self.inputTextPassword.SetValue(self.listUser.GetItem(index, 2).GetText())
            self.inputTextWin.SetValue(self.listUser.GetItem(index, 3).GetText())
            self.inputTextTie.SetValue(self.listUser.GetItem(index, 4).GetText())
            self.inputTextLose.SetValue(self.listUser.GetItem(index, 5).GetText())
            self.inputTextPoint.SetValue(self.listUser.GetItem(index, 6).GetText())
            
        elif table_type == "管理员信息":
            self.inputTextAdministratorID.SetValue(self.listUser.GetItem(index, 0).GetText())
            self.inputTextAdministratorName.SetValue(self.listUser.GetItem(index, 1).GetText())
            self.inputTextPassword.SetValue(self.listUser.GetItem(index, 2).GetText())

        elif table_type == "游戏细节":
            self.inputTextGameID.SetValue(self.listUser.GetItem(index, 0).GetText())
            self.inputTextPlayerID1.SetValue(self.listUser.GetItem(index, 1).GetText())
            self.inputTextPlayerName1.SetValue(self.listUser.GetItem(index, 2).GetText())            
            self.inputTextPlayerID2.SetValue(self.listUser.GetItem(index, 3).GetText())
            self.inputTextPlayerName2.SetValue(self.listUser.GetItem(index, 4).GetText())
            self.inputTextLocation.SetValue(self.listUser.GetItem(index, 5).GetText())
            self.inputTextDuration.SetValue(self.listUser.GetItem(index, 6).GetText())
            self.inputTextWinner.SetValue(self.listUser.GetItem(index, 7).GetText())
            self.inputTextLoser.SetValue(self.listUser.GetItem(index, 8).GetText())
            
    def refresh_screen(self):
        """重新刷新界面"""
        # 根据选择的表类型，清空输入框
        table_type = self.rboxTableType.GetStringSelection()
        
        if table_type == "玩家信息":
            self.inputTextPlayerID.SetValue('')
            self.inputTextPlayerName.SetValue('')
            self.inputTextPassword.SetValue('')
            self.inputTextWin.SetValue('')
            self.inputTextTie.SetValue('')
            self.inputTextLose.SetValue('')
            self.inputTextPoint.SetValue('')
            
        elif table_type == "管理员信息":
            self.inputTextAdministratorID.SetValue('')
            self.inputTextAdministratorName.SetValue('')
            self.inputTextPassword.SetValue('')
            
        elif table_type == "游戏细节":
            self.inputTextGameID.SetValue('')
            self.inputTextPlayerID1.SetValue('')
            self.inputTextPlayerName1.SetValue('')             
            self.inputTextPlayerID2.SetValue('') 
            self.inputTextPlayerName2.SetValue('')
            self.inputTextLocation.SetValue('')
            self.inputTextDuration.SetValue('')
            self.inputTextWinner.SetValue('') 
            self.inputTextLoser.SetValue('')
        
        # 查询用户信息并显示
        self.populate_table_list()

    def onInsert(self, e):
        """插入新信息"""       
        # 根据选择的表类型，执行相应的插入操作
        table_type = self.rboxTableType.GetStringSelection()
        
        if table_type == "玩家信息":
            # 获取输入的新信息
            player_name = self.inputTextPlayerName.GetValue()
            password = self.inputTextPassword.GetValue()
            win = self.inputTextWin.GetValue()
            tie = self.inputTextTie.GetValue()
            lose = self.inputTextLose.GetValue()
            point = self.inputTextPoint.GetValue()  
            
            if len(player_name.strip()) == 0:
                wx.MessageBox('请输入玩家姓名！')
                self.inputTextPlayerName.SetFocus()
                return None
            if len(password.strip()) == 0:
                wx.MessageBox('请输入密码！')
                self.inputTextPassword.SetFocus()
                return None 
            if win and not win.isdigit():
                wx.MessageBox('胜利次数必须是整数！')
                self.inputTextWin.SetFocus()
                return None
            
            if tie and not tie.isdigit():
                wx.MessageBox('平局次数必须是整数！')
                self.inputTextTie.SetFocus()
                return None
            
            if lose and not lose.isdigit():
                wx.MessageBox('败局次数必须是整数！')
                self.inputTextLose.SetFocus()
                return None
            
            if point and not point.isdigit():
                wx.MessageBox('积分必须是整数！')
                self.inputTextPoint.SetFocus()
                return None
            #插入记录
            data.insert_player(player_name, password, win, tie, lose, point)
            
        elif table_type == "管理员信息":
            # 获取输入的新信息
            administrator_name = self.inputTextAdministratorName.GetValue()
            administrator_pw = self.inputTextPassword.GetValue()     
            
            if len(administrator_name.strip()) == 0:
                wx.MessageBox('请输入管理员姓名！')
                self.inputTextAdministratorName.SetFocus()
                return None
            if len(administrator_pw.strip()) == 0:
                wx.MessageBox('请输入密码！')
                self.inputTextPassword.SetFocus()
                return None           
            #插入记录
            data.insert_admin(administrator_name, administrator_pw)
          
        elif table_type == "游戏细节":
            # 获取输入的新信息    
            player_id1 = self.inputTextPlayerID1.GetValue()            
            player_id2 = self.inputTextPlayerID2.GetValue()
            location = self.inputTextLocation.GetValue()
            duration = self.inputTextDuration.GetValue()
            winner = self.inputTextWinner.GetValue()
            loser = self.inputTextLoser.GetValue()

            if len(player_id1.strip()) == 0:
                wx.MessageBox('请输入玩家1编号！')
                self.inputTextPlayerID1.SetFocus()
                return None  
            
            if len(player_id2.strip()) == 0:
                wx.MessageBox('请输入玩家2编号！')
                self.inputTextPlayerID2.SetFocus()
                return None
            
            if not data.check_player_id(player_id1):
                wx.MessageBox("玩家1不存在！")
                self.inputTextPlayerID1.SetFocus()
                return None  
            else:
                player_name1 = data.check_player_id(player_id1)
                self.inputTextPlayerName1.SetValue(player_name1)
                
            if not data.check_player_id(player_id2):
                wx.MessageBox("玩家2不存在！")
                self.inputTextPlayerID2.SetFocus()
                return None 
            else:
                player_name2 = data.check_player_id(player_id2)
                self.inputTextPlayerName2.SetValue(player_name2)
                
            if winner != player_id1 and winner != player_id2 and len(winner) != 0:
                wx.MessageBox('胜者必须是玩家1和玩家2中的一个或者不填！')
                self.inputTextWinner.SetFocus()
                return None   

            if loser != player_id1 and loser != player_id2 and len(loser) != 0:
                wx.MessageBox('败者必须是玩家1和玩家2中的一个或者不填！')
                self.inputTextLoser.SetFocus()
                return None  

            if (not winner and loser) or (winner and not loser) or (winner == loser and winner and loser):
                wx.MessageBox('胜者和败者要求不相等或者都不填写！')
                if not winner:
                    self.inputTextWinner.SetFocus()
                else:
                    self.inputTextLoser.SetFocus()
                return None
            #插入记录
            data.insert_game(player_id1, player_name1, player_id2, player_name2, location, duration, winner, loser)              

        self.refresh_screen()

    def onUpdate(self, e):
        """更新选中的信息"""
        # 根据选择的表类型，执行相应的更新操作
        table_type = self.rboxTableType.GetStringSelection()
        
        if table_type == "玩家信息":
            # 获取选中的信息
            player_id = self.inputTextPlayerID.GetValue()
            player_name = self.inputTextPlayerName.GetValue()
            password = self.inputTextPassword.GetValue()
            win = self.inputTextWin.GetValue()
            tie = self.inputTextTie.GetValue()
            lose = self.inputTextLose.GetValue()
            point = self.inputTextPoint.GetValue()

            if len(player_name.strip()) == 0:
                wx.MessageBox('请输入玩家姓名！')
                self.inputTextPlayerName.SetFocus()
                return None
            if len(password.strip()) == 0:
                wx.MessageBox('请输入密码！')
                self.inputTextPassword.SetFocus()
                return None   
            if win and not win.isdigit():
                wx.MessageBox('胜利次数必须是整数！')
                self.inputTextWin.SetFocus()
                return None
            
            if tie and not tie.isdigit():
                wx.MessageBox('平局次数必须是整数！')
                self.inputTextTie.SetFocus()
                return None
            
            if lose and not lose.isdigit():
                wx.MessageBox('失败次数必须是整数！')
                self.inputTextLose.SetFocus()
                return None
            
            if point and not point.isdigit():
                wx.MessageBox('积分必须是整数！')
                self.inputTextPoint.SetFocus()
                return None
            # 更新记录
            data.update_player(player_id, player_name, password, win, tie, lose, point)
            
        elif table_type == "管理员信息":
            # 获取选中的信息
            administrator_id = self.inputTextAdministratorID.GetValue()
            administrator_name = self.inputTextAdministratorName.GetValue()
            administrator_pw = self.inputTextPassword.GetValue()    

            if len(administrator_name.strip()) == 0:
                wx.MessageBox('请输入管理员姓名！')
                self.inputTextAdministratorName.SetFocus()
                return None
            if len(administrator_pw.strip()) == 0:
                wx.MessageBox('请输入密码！')
                self.inputTextPassword.SetFocus()
                return None
            # 更新记录
            data.update_admin(administrator_id, administrator_name, administrator_pw)
            
        elif table_type == "游戏细节":
            # 获取选中的信息
            game_id = self.inputTextGameID.GetValue()      
            player_id1 = self.inputTextPlayerID1.GetValue()            
            player_id2 = self.inputTextPlayerID2.GetValue()
            location = self.inputTextLocation.GetValue()
            duration = self.inputTextDuration.GetValue()
            winner = self.inputTextWinner.GetValue()   
            loser = self.inputTextLoser.GetValue()

            if len(player_id1.strip()) == 0:
                wx.MessageBox('请输入玩家1编号！')
                self.inputTextPlayerID1.SetFocus()
                return None  
            
            if len(player_id2.strip()) == 0:
                wx.MessageBox('请输入玩家2编号！')
                self.inputTextPlayerID2.SetFocus()
                return None
            
            if not data.check_player_id(player_id1):
                wx.MessageBox("玩家1不存在！")
                self.inputTextPlayerID1.SetFocus()
                return None  
            else:
                player_name1 = data.check_player_id(player_id1)
                self.inputTextPlayerName1.SetValue(player_name1)
                
            if not data.check_player_id(player_id2):
                wx.MessageBox("玩家2不存在！")
                self.inputTextPlayerID2.SetFocus()
                return None 
            else:
                player_name2 = data.check_player_id(player_id2)
                self.inputTextPlayerName2.SetValue(player_name2)
                
            if winner != player_id1 and winner != player_id2 and len(winner) != 0:
                wx.MessageBox('胜者必须是玩家1和玩家2中的一个或者不填！')
                self.inputTextWinner.SetFocus()
                return None   

            if loser != player_id1 and loser != player_id2 and len(loser) != 0:
                wx.MessageBox('败者必须是玩家1和玩家2中的一个或者不填！')
                self.inputTextLoser.SetFocus()
                return None  

            if (not winner and loser) or (winner and not loser) or (winner == loser and winner and loser):
                wx.MessageBox('胜者和败者要求不相等或者都不填写！')
                if not winner:
                    self.inputTextWinner.SetFocus()
                else:
                    self.inputTextLoser.SetFocus()
                return None
            # 更新记录
            data.update_game(game_id, player_id1, player_name1, player_id2, player_name2, location, duration, winner, loser)            

        self.refresh_screen()

    def onDelete(self, e):
        """删除选中的用户信息"""
        # 根据选择的表类型，执行相应的更新操作
        table_type = self.rboxTableType.GetStringSelection()
        
        if table_type == "玩家信息":
            # 获取选中的信息  
            player_id = self.inputTextPlayerID.GetValue()
            # 删除记录
            data.delete_player(player_id)
            
        elif table_type == "管理员信息":
            # 获取选中的信息  
            administrator_id = self.inputTextAministratorID.GetValue()
            # 删除记录
            data.delete_admin(administrator_id)     
            
        elif table_type == "游戏细节":
            # 获取选中的信息  
            game_id = self.inputTextGameID.GetValue()
            # 删除记录
            data.delete_game(game_id)            

        self.refresh_screen()

    def onExit(self, e):
        """退出程序"""
        self.Close(True)  # 关闭顶层框架窗口

