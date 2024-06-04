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
                               VALUES ('Computer', 'Computer', 0, 0, 0, 0);'''
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
                                    PLAYERID1 INTEGER NOT NULL,
                                    PLAYERNAME1 NVARCHAR(50) NOT NULL,
                                    PLAYERID2 INTEGER NOT NULL,                                    
                                    PLAYERNAME2 NVARCHAR(50) NOT NULL,
                                    DETAILTEXT NVARCHAR(150),
                                    TIME NVARCHAR(50),
                                    WINNER NVARCHAR(50) NOT NULL,
                                    FOREIGN KEY (PLAYERID1) REFERENCES Player(PLAYERID),
                                    FOREIGN KEY (PLAYERID2) REFERENCES Player(PLAYERID)
                                  );'''
        con.execute(sql_create_GameDetail)
        con.commit()
    return con

def insert_game_detail(playerid1, playername1, playerid2, playername2, detailtext, time, winner):
    try:
        con = get_or_create_db(DBFILE)
        sql = '''INSERT INTO GameDetail (PLAYERID1, PLAYERNAME1, PLAYERID2, PLAYERNAME2, DETAILTEXT, TIME, WINNER)
                 VALUES (?, ?, ?, ?, ?, ?, ?);'''
        con.execute(sql, (playerid1, playername1, playerid2, playername2, detailtext, time, winner))
        con.commit()
        print("Game detail inserted successfully.")
        return True
    except sqlite3.Error as e:
        print(f"插入游戏详情失败: {e}")
        return False
    finally:
        con.close()
