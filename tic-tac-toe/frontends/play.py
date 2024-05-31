import wx
import threading
from queue import Queue
from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark
from window.renderers import Window, WindowRenderer  # 确保路径正确
from window.players import WindowPlayer

def main():
    events = Queue()

    # 创建 wxPython 应用
    app = wx.App(False)

    # 创建窗口
    window = Window(events)

    # 创建玩家
    player1 = WindowPlayer(Mark("X"), events)
    player2 = RandomComputerPlayer(Mark("O"))

    # 创建渲染器
    renderer = WindowRenderer(window)

    # 创建游戏引擎
    game = TicTacToe(player1, player2, renderer)

    # 启动一个线程来处理游戏逻辑
    def game_loop():
        game.play()

    game_thread = threading.Thread(target=game_loop)
    game_thread.start()

    # 运行 wxPython 主循环
    app.MainLoop()

if __name__ == "__main__":
    main()
