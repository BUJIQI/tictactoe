import wx

class UserWindow(wx.Frame):
    def __init__(self, parent, title):
        super(UserWindow, self).__init__(parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)

        # 创建控件
        lblListAction = ['插入', '修改', '删除']
        self.rboxAction = wx.RadioBox(panel, label='操作', choices=lblListAction)
        lblListType = ['玩家信息', '管理员信息', '游戏历史记录']
        self.rboxUserType = wx.RadioBox(panel, label='表', choices=lblListType)



        self.listUser = wx.ListCtrl(panel, wx.ID_ANY, size=(400, 400), style=wx.LC_REPORT)

        self.labelUserID = wx.StaticText(panel, wx.ID_ANY, '用户编号:')
        self.inputTextUserID = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelUserName = wx.StaticText(panel, wx.ID_ANY, '用户名称:')
        self.inputTextUserName = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelPassword = wx.StaticText(panel, wx.ID_ANY, '用户密码:')
        self.inputTextPassword = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelWin = wx.StaticText(panel, wx.ID_ANY, '游戏胜局:')
        self.inputTextWin = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelDraw = wx.StaticText(panel, wx.ID_ANY, '游戏平局:')
        self.inputTextDraw = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelLose = wx.StaticText(panel, wx.ID_ANY, '游戏败局:')
        self.inputTextLose = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelLocation = wx.StaticText(panel, wx.ID_ANY, '位置顺序:')
        self.inputTextLocation = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelStartTime = wx.StaticText(panel, wx.ID_ANY, '开始时间:')
        self.inputTextStartTime = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelScore = wx.StaticText(panel, wx.ID_ANY, '游戏分数:')
        self.inputTextScore = wx.TextCtrl(panel, wx.ID_ANY, '')

        self.insertBtn = wx.Button(panel, wx.ID_ANY, '插入')
        self.updateBtn = wx.Button(panel, wx.ID_ANY, '更新')
        self.updateBtn.Disable()
        self.deleteBtn = wx.Button(panel, wx.ID_ANY, '删除')
        self.deleteBtn.Disable()
        exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        editSizer = wx.BoxSizer(wx.VERTICAL)
        useridSizer = wx.BoxSizer(wx.HORIZONTAL)
        usernameSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        winSizer = wx.BoxSizer(wx.HORIZONTAL)
        drawSizer = wx.BoxSizer(wx.HORIZONTAL)
        loseSizer = wx.BoxSizer(wx.HORIZONTAL)
        locationSizer = wx.BoxSizer(wx.HORIZONTAL)
        starttimeSizer = wx.BoxSizer(wx.HORIZONTAL)
        scoreSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)
        optionSizer.Add(self.rboxUserType, 0, wx.ALL, 5)

        listSizer.Add(self.listUser, 0, wx.ALL, 5)

        useridSizer.Add(self.labelUserID, 0, wx.ALL, 5)
        useridSizer.Add(self.inputTextUserID, 0, wx.ALL, 5)
        usernameSizer.Add(labelUserName, 0, wx.ALL, 5)
        usernameSizer.Add(self.inputTextUserName, 0, wx.ALL, 5)
        passwordSizer.Add(labelPassword, 0, wx.ALL, 5)
        passwordSizer.Add(self.inputTextPassword, 0, wx.ALL, 5)
        winSizer.Add(labelWin, 0, wx.ALL, 5)
        winSizer.Add(self.inputTextWin, 0, wx.ALL, 5)
        drawSizer.Add(labelDraw, 0, wx.ALL, 5)
        drawSizer.Add(self.inputTextDraw, 0, wx.ALL, 5)
        loseSizer.Add(labelLose, 0, wx.ALL, 5)
        loseSizer.Add(self.inputTextLose, 0, wx.ALL, 5)
        locationSizer.Add(labelLocation, 0, wx.ALL, 5)
        locationSizer.Add(self.inputTextLocation, 0, wx.ALL, 5)
        starttimeSizer.Add(labelStartTime, 0, wx.ALL, 5)
        starttimeSizer.Add(self.inputTextStartTime, 0, wx.ALL, 5)
        scoreSizer.Add(labelScore, 0, wx.ALL, 5)
        scoreSizer.Add(self.inputTextScore, 0, wx.ALL, 5)
        btnSizer.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(useridSizer, 0, wx.ALL, 5)
        editSizer.Add(usernameSizer, 0, wx.ALL, 5)
        editSizer.Add(passwordSizer, 0, wx.ALL, 5)
        editSizer.Add(winSizer, 0, wx.ALL, 5)
        editSizer.Add(drawSizer, 0, wx.ALL, 5)
        editSizer.Add(loseSizer, 0, wx.ALL, 5)
        editSizer.Add(locationSizer, 0, wx.ALL, 5)
        editSizer.Add(starttimeSizer, 0, wx.ALL, 5)
        editSizer.Add(scoreSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)

        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件
        self.Bind(wx.EVT_RADIOBOX, self.onAction, self.rboxAction)
        self.Bind(wx.EVT_RADIOBOX, self.onUserType, self.rboxUserType)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onUserList, self.listUser)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        # 查询用户信息并显示
        self.populate_user_list()
        self.Center()


    def onAction(self, e):
        """事件处理函数：根据操作类型（插入、更新、删除）设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "插入":
            self.rboxUserType.Enable()
            self.inputTextUserID.Enable()
            self.insertBtn.Enable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
        elif action == "修改":
            self.rboxUserType.Disable()
            self.inputTextUserID.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "删除":
            self.rboxUserType.Disable()
            self.inputTextUserID.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Enable()

    def onUserType(self, e):
        """事件处理函数：用户类别改变时，显示对应的用户信息列表"""
        self.populate_user_list()

    def onUserList(self, e):
        """事件处理函数：在列表中选择用户，内容显示在右侧"""
        index = e.GetIndex()  # 获得被激活表项的索引号
        user_type = self.rboxUserType.GetStringSelection()

        self.inputTextUserID.SetValue(self.listUser.GetItem(index, 0).GetText())
        self.inputTextUserName.SetValue(self.listUser.GetItem(index, 1).GetText())
        self.inputTextPassword.SetValue(self.listUser.GetItem(index, 2).GetText())

        if user_type == "玩家信息":
            self.inputTextWin.SetValue(self.listUser.GetItem(index, 3).GetText())
            self.inputTextDraw.SetValue(self.listUser.GetItem(index, 4).GetText())
            self.inputTextLose.SetValue(self.listUser.GetItem(index, 5).GetText())
            self.inputTextLocation.Disable()
            self.inputTextStartTime.Disable()
            self.inputTextScore.Disable()

            self.labelUserID.SetLabelText(label='1')

            self.inputTextWin.Disable()
            self.inputTextDraw.Disable()
            self.inputTextLose.Disable()
            self.inputTextLocation.Disable()
            self.inputTextStartTime.Disable()
            self.inputTextScore.Disable()
        elif user_type == "游戏历史记录":
            self.inputTextLocation.SetValue(self.listUser.GetItem(index, 3).GetText())
            self.inputTextStartTime.SetValue(self.listUser.GetItem(index, 4).GetText())
            self.inputTextScore.SetValue(self.listUser.GetItem(index, 5).GetText())
            self.inputTextWin.Disable()
            self.inputTextDraw.Disable()
            self.inputTextLose.Disable()

    def refresh_screen(self):
        """重新刷新界面"""
        self.inputTextUserID.SetValue('')
        self.inputTextUserName.SetValue('')
        self.inputTextPassword.SetValue('')
        self.inputTextWin.SetValue('')
        self.inputTextDraw.SetValue('')
        self.inputTextLose.SetValue('')
        self.inputTextLocation.SetValue('')
        self.inputTextStartTime.SetValue('')
        self.inputTextScore.SetValue('')
        # 查询用户信息并显示
        self.populate_user_list()

    def populate_user_list(self):
        """根据选择的表类型，显示对应的用户信息列表"""
        user_type = self.rboxUserType.GetStringSelection()
        self.listUser.ClearAll()

        if user_type == "玩家信息":
            self.listUser.InsertColumn(0, '编号', width=50)
            self.listUser.InsertColumn(1, '用户名', width=70)
            self.listUser.InsertColumn(2, '密码', width=130)
            self.listUser.InsertColumn(3, '胜局', width=50)
            self.listUser.InsertColumn(4, '平局', width=50)
            self.listUser.InsertColumn(5, '败局', width=50)
            self.labelUserID.SetLabelText('1')

            # 在这里添加玩家信息数据，实际应用中应从数据库或其他数据源获取
        elif user_type == "管理员信息":
            self.listUser.InsertColumn(0, '编号', width=130)
            self.listUser.InsertColumn(1, '用户名', width=130)
            self.listUser.InsertColumn(2, '密码', width=140)
            self.labelUserID.SetLabelText('2')
            self.labelUserID.Destroy()
            self.inputTextUserID.Destroy()
            # 在这里添加管理员信息数据，实际应用中应从数据库或其他数据源获取
        elif user_type == "游戏历史记录":
            self.listUser.InsertColumn(0, '编号', width=40)
            self.listUser.InsertColumn(1, '用户名', width=40)
            self.listUser.InsertColumn(2, '密码', width=40)
            self.listUser.InsertColumn(3, '位置', width=200)
            self.listUser.InsertColumn(4, '时间', width=40)
            self.listUser.InsertColumn(5, '分数', width=40)
            self.labelUserID.SetLabelText('3')
            # 在这里添加游戏历史记录数据，实际应用中应从数据库或其他数据源获取

    def onInsert(self, e):
        """插入新用户信息"""
        # 获取输入的用户信息
        user_id = self.inputTextUserID.GetValue()
        user_name = self.inputTextUserName.GetValue()
        password = self.inputTextPassword.GetValue()
        win = self.inputTextWin.GetValue()
        draw = self.inputTextDraw.GetValue()
        lose = self.inputTextLose.GetValue()
        location = self.inputTextLocation.GetValue()
        start_time = self.inputTextStartTime.GetValue()
        score = self.inputTextScore.GetValue()
        
        # 根据选择的表类型，执行相应的插入操作
        user_type = self.rboxUserType.GetStringSelection()
        if user_type == "玩家信息":
            # 插入玩家信息
            index = self.listUser.InsertItem(self.listUser.GetItemCount(), user_id)
            self.listUser.SetItem(index, 1, user_name)
            self.listUser.SetItem(index, 2, password)
            self.listUser.SetItem(index, 3, win)
            self.listUser.SetItem(index, 4, draw)
            self.listUser.SetItem(index, 5, lose)
        elif user_type == "管理员信息":
            # 插入管理员信息
            index = self.listUser.InsertItem(self.listUser.GetItemCount(), user_id)
            self.listUser.SetItem(index, 1, user_name)
            self.listUser.SetItem(index, 2, password)
        elif user_type == "游戏历史记录":
            # 插入游戏历史记录
            index = self.listUser.InsertItem(self.listUser.GetItemCount(), user_id)
            self.listUser.SetItem(index, 1, user_name)
            self.listUser.SetItem(index, 2, password)
            self.listUser.SetItem(index, 3, location)
            self.listUser.SetItem(index, 4, start_time)
            self.listUser.SetItem(index, 5, score)

        self.refresh_screen()

    def onUpdate(self, e):
        """更新选中的用户信息"""
        # 获取选中的用户信息
        index = self.listUser.GetFirstSelected()
        if index == -1:
            return

        user_id = self.inputTextUserID.GetValue()
        user_name = self.inputTextUserName.GetValue()
        password = self.inputTextPassword.GetValue()
        win = self.inputTextWin.GetValue()
        draw = self.inputTextDraw.GetValue()
        lose = self.inputTextLose.GetValue()
        location = self.inputTextLocation.GetValue()
        start_time = self.inputTextStartTime.GetValue()
        score = self.inputTextScore.GetValue()

        # 根据选择的表类型，执行相应的更新操作
        user_type = self.rboxUserType.GetStringSelection()
        if user_type == "玩家信息":
            self.listUser.SetItem(index, 0, user_id)
            self.listUser.SetItem(index, 1, user_name)
            self.listUser.SetItem(index, 2, password)
            self.listUser.SetItem(index, 3, win)
            self.listUser.SetItem(index, 4, draw)
            self.listUser.SetItem(index, 5, lose)
        elif user_type == "管理员信息":
            self.listUser.SetItem(index, 0, user_id)
            self.listUser.SetItem(index, 1, user_name)
            self.listUser.SetItem(index, 2, password)
        elif user_type == "游戏历史记录":
            self.listUser.SetItem(index, 0, user_id)
            self.listUser.SetItem(index, 1, user_name)
            self.listUser.SetItem(index, 2, password)
            self.listUser.SetItem(index, 3, location)
            self.listUser.SetItem(index, 4, start_time)
            self.listUser.SetItem(index, 5, score)

        self.refresh_screen()

    def onDelete(self, e):
        """删除选中的用户信息"""
        # 获取选中的用户信息
        index = self.listUser.GetFirstSelected()
        if index == -1:
            return

        self.listUser.DeleteItem(index)
        self.refresh_screen()

    def onExit(self, e):
        """退出程序"""
        self.Close(True)  # 关闭顶层框架窗口

if __name__ == '__main__':
    app = wx.App(False)
    frame = UserWindow(None, "管理员操作")
    frame.Show()
    app.MainLoop()


