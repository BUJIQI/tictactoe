本游戏基于传统井字棋玩法，同时拓展了玩家查询历史对局及积分功能。

# 玩家部分：
开始新游戏：玩家-开始新游戏。
对手可选择简单难度或困难难度，同时支持添加人类玩家二。
（可重复添加玩家一账号信息至玩家二，进行个人练习）。
查看对局历史：玩家-查看历史。
玩家可在此查看自己的基本信息（胜、败、平局数与总积分）。

# 管理员部分：
增删查改游戏信息：管理-查看游戏。
可在此进行玩家信息，管理员信息，游戏对局细节的修改。

# 其他：
游戏细节：游戏细节描述为“标号与数字”的组合。
例“X5”，代表X标记，位置第五格，九宫格位置序号从上到下从左至右分别为1~9。
积分：一局游戏结束后，赢家积分+1，输家积分-1，平局时积分不变。

项目结构如下：
```python

tree.txt
│  
└─tic-tac-toe
    ├─frontends
    │  │  administrator_check.py
    │  │  admin_main.py
    │  │  data.py
    │  │  game_data.json
    │  │  game_main.py
    │  │  login.py
    │  │  play.py
    │  │  player_check.py
    │  │  player_main.py
    │  │  register.py
    │  │  tictactoe.db
    │  │  ui_play.py
    │  │  
    │  ├─window
    │  │  │  cli.py
    │  │  │  players.py
    │  │  │  renderers.py
    │  │  │  __init__.py
    │  │  │  __main__.py
    │  │  │  
    │  │  └─__pycache__
    │  │          players.cpython-312.pyc
    │  │          renderers.cpython-312.pyc
    │  │          __init__.cpython-312.pyc
    │  │          
    │  └─__pycache__
    │          administrator_check.cpython-312.pyc
    │          admin_main.cpython-312.pyc
    │          data.cpython-312.pyc
    │          game_main.cpython-312.pyc
    │          login.cpython-312.pyc
    │          play.cpython-312.pyc
    │          player_check.cpython-312.pyc
    │          player_main.cpython-312.pyc
    │          register.cpython-312.pyc
    │          register_or_login.cpython-312.pyc
    │          ui_play.cpython-312.pyc
    │          
    └─library
        │  LICENSE
        │  MANIFEST.in
        │  pyproject.toml
        │  README.md
        │  
        └─src
            └─tic_tac_toe
                │  __init__.py
                │  
                ├─game
                │  │  engine.py
                │  │  engine_async.py
                │  │  players.py
                │  │  players_async.py
                │  │  renderers.py
                │  │  __init__.py
                │  │  
                │  └─__pycache__
                │          engine.cpython-312.pyc
                │          players.cpython-312.pyc
                │          renderers.cpython-312.pyc
                │          __init__.cpython-312.pyc
                │          
                ├─logic
                │  │  exceptions.py
                │  │  minimax.json
                │  │  minimax.py
                │  │  models.py
                │  │  validators.py
                │  │  __init__.py
                │  │  
                │  └─__pycache__
                │          exceptions.cpython-312.pyc
                │          minimax.cpython-312.pyc
                │          models.cpython-312.pyc
                │          validators.cpython-312.pyc
                │          __init__.cpython-312.pyc
                │          
                └─__pycache__
                        __init__.cpython-312.pyc
                        
