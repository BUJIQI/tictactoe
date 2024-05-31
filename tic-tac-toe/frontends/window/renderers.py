import wx
from queue import Queue
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState

class Window(wx.Frame):
    def __init__(self, events: Queue) -> None:
        super().__init__(None, title="Tic-Tac-Toe", size=(300, 300))
        self.events = events

        panel = wx.Panel(self)
        grid = wx.GridSizer(3, 3, 5, 5)  # 3x3 grid with 5px gaps

        self.buttons = []
        for row in range(3):
            for col in range(3):
                button = wx.Button(panel, label="", size=(50, 50))
                self.buttons.append(button)
                button.Bind(wx.EVT_BUTTON, self.on_button_click)
                grid.Add(button, 0, wx.EXPAND)

        panel.SetSizer(grid)
        self.Centre()
        self.Show()

    def on_button_click(self, event):
        clicked_button = event.GetEventObject()
        self.events.put(self.buttons.index(clicked_button))

class WindowRenderer(Renderer):
    def __init__(self, window: Window) -> None:
        self.window = window

    def render(self, game_state: GameState) -> None:
        default_font = wx.Font(wx.FontInfo(9))
        for button in self.window.buttons:
            button.SetFont(default_font)
        for label, button in zip(game_state.grid.cells, self.window.buttons):
            button.SetLabel(label)
        if game_state.winner:
            for i in game_state.winning_cells:
                self.window.buttons[i].SetFont(wx.Font(wx.FontInfo(9).Bold()))


