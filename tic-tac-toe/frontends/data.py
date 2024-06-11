"""井字棋管理系统：基于sqlite3"""
import os
import sqlite3

DBFILE = 'tictactoe.db'  # 井字棋sqlite3数据库，全局变量

def get_or_create_db(db_filename):
    """打开本地数据库文件db_filename，并返回数据库连接con
    如果本地数据库文件db_filename不存在，则创建数据库和相关表"""
    if os.path.exists(db_filename):
        con = sqlite3.connect(db_filename)
        con.execute('PRAGMA foreign_keys = ON;')
    else:
        con = sqlite3.connect(db_filename)
        con.execute('PRAGMA foreign_keys = ON;')
        # 创建玩家表
        sql_create_Player = '''CREATE TABLE Player (
                                PLAYERID INTEGER PRIMARY KEY AUTOINCREMENT,
                                PLAYERNAME NVARCHAR(50) NOT NULL,
                                PASSWORD VARCHAR(50) NOT NULL,
                                WIN INTEGER,
                                TIE INTEGER,
                                LOSE INTEGER,
                                POINT INTEGER
                              );'''
        con.execute(sql_create_Player)
        sql_insert_Player = '''INSERT INTO Player (PLAYERNAME, PASSWORD, WIN, TIE, LOSE, POINT) 
                               VALUES ('RandomComputer', 'RandomComputer', 0, 0, 0, 0),     
                                    ('MinimaxComputer', 'MinimaxComputer', 0, 0, 0, 0);'''
        con.execute(sql_insert_Player)

        # 创建管理员表
        sql_create_Admin = '''CREATE TABLE Admin (
                                ADMINID INTEGER PRIMARY KEY AUTOINCREMENT,
                                ADMINNAME NVARCHAR(50) NOT NULL,
                                PASSWORD NVARCHAR(50) NOT NULL
                              );'''
        con.execute(sql_create_Admin)

        # 创建游戏细节表
        sql_create_GameDetail = '''CREATE TABLE GameDetail (
                                    GAMEID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    PLAYERID1 INTEGER,
                                    PLAYERNAME1 NVARCHAR(50),
                                    PLAYERID2 INTEGER,                                    
                                    PLAYERNAME2 NVARCHAR(50),
                                    DETAILTEXT NVARCHAR(150),
                                    TIME NVARCHAR(50),
                                    WINNER INTEGER,
                                    LOSER INTEGER,
                                    FOREIGN KEY (PLAYERID1) REFERENCES Player(PLAYERID),
                                    FOREIGN KEY (PLAYERID2) REFERENCES Player(PLAYERID)
                                  );'''
        con.execute(sql_create_GameDetail)
        con.commit()
    return con

############用户注册#########################################################################
def register(username, password, UserType):
    try:
        con = get_or_create_db(DBFILE)
        if UserType == "玩家":
            sql = "INSERT INTO Player (PLAYERNAME, PASSWORD, WIN, TIE, LOSE, POINT) VALUES (?, ?, 0, 0, 0, 0);"
        elif UserType == "管理员":
            sql = "INSERT INTO Admin (ADMINNAME, PASSWORD) VALUES (?, ?);"
        else:
            raise ValueError(f"Invalid UserType: {UserType}")
        con.execute(sql, (username, password))
        con.commit()
        return True  # 注册成功返回 True
    except (ValueError, sqlite3.Error) as e:
        print(f"注册失败: {e}")
        return False  # 注册失败返回 False
    finally:
        con.close()

############用户登录#########################################################################
def login(username, password,UserType):  
    con = get_or_create_db(DBFILE)  
    try:  
        if UserType == "管理员":  
            sql_pattern = '''SELECT ADMINNAME, PASSWORD FROM Admin WHERE ADMINNAME=? AND PASSWORD=?'''  
            cur = con.execute(sql_pattern, (username, password))  
            row = cur.fetchone()  
            if row:  
                return True  
            else:  
                return False  
        elif UserType == "玩家":  
            sql_pattern = '''SELECT PLAYERNAME, PASSWORD FROM Player WHERE PLAYERNAME=? AND PASSWORD=?'''  
            cur = con.execute(sql_pattern, (username, password))  
            row = cur.fetchone()  
            if row:  
                return True  
            else:  
                return False  
    finally:  
        con.close()

def get_player_id_by_name(player_name):
    """根据玩家名称查询玩家ID"""
    con = get_or_create_db(DBFILE)
    try:
        sql = "SELECT PLAYERID FROM Player WHERE PLAYERNAME=?"
        cur = con.execute(sql, (player_name,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None
    finally:
        con.close()

############玩家查看#########################################################################
def get_player_game_records_basic(player_name):
    # 这里应该使用参数化查询来避免SQL注入
    con = get_or_create_db(DBFILE)
    try:
        # 假设Players表中有一个名为PlayerName的列来存储用户名
        # 首先，我们需要找到该玩家的PlayerID
        cur = con.cursor()
        cur.execute("SELECT PlayerID FROM Player WHERE PlayerName=?", (player_name,))
        player_id = cur.fetchone()
        if player_id:
            player_id = player_id[0]  # 提取PlayerID，它可能是一个元组
            # 然后，使用PlayerID查询游戏记录
            cur.execute("SELECT PLAYERID,PLAYERNAME,PASSWORD, Win, Tie, Lose, POINT FROM Player WHERE PlayerID=?", (player_id,))
            records = cur.fetchall()
            record_list = []
            for record in records:
                record_list.append(record)
            return record_list
        else:
            return []  # 如果没有找到玩家，返回一个空列表
    finally:
        con.close()

def get_player_game_records(player_name):
    # 这个函数返回特定玩家的胜局、平局、败局的游戏记录统计信息
    con = get_or_create_db(DBFILE)
    result = {
        'wins': [],
        'ties': [],
        'losses': []
    }

    try:
        cur = con.cursor()
        cur.execute("SELECT PlayerID FROM Player WHERE PlayerName=?", (player_name,))
        player_id = cur.fetchone()

        if player_id:
            player_id = player_id[0]  # 确保player_id是一个值

            # 查询胜局
            cur.execute("SELECT GAMEID, DETAILTEXT, TIME FROM GameDetail WHERE WINNER=?", (player_id,))
            result['wins'] = cur.fetchall()

            # 查询平局（胜者和败者都是NULL，且玩家参与了比赛）
            cur.execute("SELECT GAMEID, DETAILTEXT, TIME FROM GameDetail WHERE WINNER IS NULL AND LOSER IS NULL AND PlayerID1=?", (player_id,))
            result['ties'] = cur.fetchall()

            # 查询败局
            cur.execute("SELECT GAMEID, DETAILTEXT, TIME FROM GameDetail WHERE LOSER=?", (player_id,))
            result['losses'] = cur.fetchall()

    finally:
        con.close()

    return result

############管理员操作#########################################################################
def check_player_id(player_id):
    """检查Player表中是否存在player_id"""
    con = get_or_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT PLAYERNAME FROM Player WHERE PLAYERID="{0}"'''
        sql = sql_pattern.format(player_id)
        cur = con.execute(sql)
        row = cur.fetchone()
        if row:
            return row[0]
        else:
            return False
    finally:
        con.close()

def get_player_list():
    """查找数据库Player表，获取玩家信息列表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''SELECT * FROM Player'''
        results = con.execute(sql)
        players = results.fetchall()
        player_list = []
        for player in players:
            player_list.append(player)
        return player_list
    finally:
        con.close()

def get_admin_list():
    """查找数据库Admin表，获取管理员信息列表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''SELECT * FROM Admin'''
        results = con.execute(sql)
        admins = results.fetchall()
        admin_list = []
        for admin in admins:
            admin_list.append(admin)
        return admin_list
    finally:
        con.close()

def get_game_list():
    """查找数据库GameDetail表，获取游戏细节列表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''SELECT * FROM GameDetail'''
        results = con.execute(sql)
        games = results.fetchall()
        game_list = []
        for game in games:
            game_list.append(game)
        return game_list
    finally:
        con.close()

def insert_player(player_name, password, win, tie, lose, point):
    """插入一条记录到Player表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''INSERT INTO Player(PLAYERNAME, PASSWORD, WIN, TIE, LOSE, POINT)
                                      VALUES (?,?,?,?,?,?)'''
        con.execute(sql, (player_name, password, win, tie, lose, point))
        con.commit()
    finally:
        con.close()

def insert_admin(administrator_name, administrator_pw):
    """插入一条记录到Admin表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''INSERT INTO Admin(ADMINNAME, PASSWORD)
                                      VALUES (?,?)'''
        con.execute(sql, (administrator_name, administrator_pw))
        con.commit()
    finally:
        con.close()

def insert_game(player_id1, player_name1, player_id2, player_name2, location, duration, winner, loser):
    """插入一条记录到GameDetail表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''INSERT INTO GameDetail(PLAYERID1, PLAYERNAME1, PLAYERID2, PLAYERNAME2, DETAILTEXT, TIME, WINNER, LOSER)
                                      VALUES (?,?,?,?,?,?,?,?)'''
        con.execute(sql, (player_id1, player_name1, player_id2, player_name2, location, duration, winner, loser))
        con.commit()
        print("Game detail inserted successfully.")
    except sqlite3.Error as e:
        print(f"插入游戏详情失败: {e}")
        return False
    finally:
        con.close()

def update_player(player_id, player_name, password, win, tie, lose, point):
    """更新一条记录到Player表，同时更新GameDetail的相关记录"""
    con = get_or_create_db(DBFILE)
    try:
        sql_update_player = '''UPDATE Player
                                  SET PLAYERNAME = ?
                                      ,PASSWORD = ?
                                      ,WIN = ?
                                      ,TIE = ?
                                      ,LOSE = ?
                                      ,POINT = ?
                                  WHERE PLAYERID = ?'''
        con.execute(sql_update_player, (player_name, password, win, tie, lose, point, player_id))
        sql_update_game_detail = '''UPDATE GameDetail
                                       SET PLAYERNAME1 = ?
                                       WHERE PLAYERID1 = ?'''
        con.execute(sql_update_game_detail, (player_name, player_id))
        sql_update_game_detail2 = '''UPDATE GameDetail
                                       SET PLAYERNAME2 = ?
                                       WHERE PLAYERID2 = ?'''
        con.execute(sql_update_game_detail2, (player_name, player_id))
        con.commit()
    finally:
        con.close()

def update_admin(administrator_id, administrator_name, administrator_pw):
    """更新一条记录到Admin表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''UPDATE Admin
                    SET ADMINNAME = ?
                        ,PASSWORD = ?
                    WHERE ADMINID = ?'''
        con.execute(sql, (administrator_name, administrator_pw, administrator_id))
        con.commit()
    finally:
        con.close()

def update_game(game_id, player_id1, player_name1, player_id2, player_name2, location, duration, winner, loser):
    """更新一条记录到GameDetail表"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''UPDATE GameDetail
                    SET PLAYERID1 = ?
                        ,PLAYERNAME1 = ?                    
                        ,PLAYERID2 = ?
                        ,PLAYERNAME2 = ?
                        ,DETAILTEXT = ?
                        ,TIME = ?
                        ,WINNER = ?
                    WHERE GAMEID = ?'''
        con.execute(sql, (player_id1, player_name1, player_id2, player_name2, location, duration, winner, loser, game_id))
        con.commit()
    finally:
        con.close()

def delete_player(player_id):
    """从Player表中删除一条记录"""
    con = get_or_create_db(DBFILE)
    try:
        con.execute('PRAGMA foreign_keys = OFF;')
        sql_update_game_detail = '''UPDATE GameDetail
                                       SET PLAYERID1 = null
                                           ,PLAYERNAME1 = null
                                       WHERE PLAYERID1 = ?'''
        con.execute(sql_update_game_detail, (player_id,))

        sql_update_game_detail2 = '''UPDATE GameDetail
                                        SET PLAYERID2 = null
                                            ,PLAYERNAME2 = null
                                        WHERE PLAYERID2 = ?'''
        con.execute(sql_update_game_detail2, (player_id,))
        sql = '''DELETE FROM Player
                    WHERE PLAYERID = ?'''
        con.execute(sql, (player_id,))
        con.commit()
    finally:
        con.execute('PRAGMA foreign_keys = ON;')
        con.close()

def delete_admin(administrator_id):
    """从Admin表中删除一条记录"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''DELETE FROM Admin
                    WHERE ADMINID = ?'''
        con.execute(sql, (administrator_id,))
        con.commit()
    finally:
        con.close()

def delete_game(game_id):
    """从GameDetail表中删除一条记录"""
    con = get_or_create_db(DBFILE)
    try:
        sql = '''DELETE FROM GameDetail
                    WHERE GAMEID = ?'''
        con.execute(sql, (game_id,))
        con.commit()
    finally:
        con.close()

############游戏#########################################################################
def update_player_stats(winner_id, loser_id, is_tie, p1_id, p2_id):
    con = get_or_create_db(DBFILE)
    try:
        if is_tie:
            sql = '''UPDATE Player
                     SET TIE = TIE + 1
                     WHERE PLAYERID IN (?, ?)'''
            con.execute(sql, (p1_id, p2_id))
        else:
            sql_winner = '''UPDATE Player
                            SET WIN = WIN + 1, POINT = POINT + 1
                            WHERE PLAYERID = ?'''
            sql_loser = '''UPDATE Player
                           SET LOSE = LOSE + 1, POINT = POINT - 1
                           WHERE PLAYERID = ?'''
            con.execute(sql_winner, (winner_id,))
            con.execute(sql_loser, (loser_id,))
        con.commit()
    finally:
        con.close()
