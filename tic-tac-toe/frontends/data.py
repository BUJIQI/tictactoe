"""井字棋管理系统：基于sqlite3"""
import os
import sqlite3

DBFILE = 'tictactoe6.db'  # 井字棋sqlite3数据库，全局变量

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
