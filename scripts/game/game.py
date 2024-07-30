from game.application import Application
from gui.menu import Menu
from gui.text import Text
from settings import *
from gui.button import Button
from functions import Centerize

import pygame

class Game(Application):

    def __init__(self):
        
        super().__init__()
        pygame.init()
        self.InitGUI()

    def InitGUI(self) -> None:
        
        self.menu = Menu()
        self.menu.AddTab('main')
        self.menu.AddTab('player')
        self.menu.AddTab('mode')
        self.menu.AddTab('connect')
        self.menu.AddTab('lobby')
        self.menu.AddTab('join')
        self.menu.AddTab('game')
        self.menu.SetTab('main')
        
        
        self.menu.AddButton('main', Button((0, 150), image=pygame.Surface((400, 80)), onClick= lambda: self.menu.SetTab('player'), text=Text((0, 0), 'New Game', 25, True, White), mouseOverText=Text((0, 0), 'Main Menu', 25, True, Black), passiveText=Text((0, 0), 'Main Menu', 25, True, Black)))
        self.menu.AddButton('main', Button((0, 300), image=pygame.Surface((400, 80)), onClick= lambda: self.menu.SetTab('player'), text=Text((0, 0), 'Continue', 25, True, White), mouseOverText=Text((0, 0), 'Main Menu', 25, True, Black), passiveText=Text((0, 0), 'Main Menu', 25, True, Black)))
        self.menu.AddButton('main', Button((0, 450), image=pygame.Surface((400, 80)), onClick= lambda: self.menu.SetTab('player'), text=Text((0, 0), 'Upgrades', 25, True, White), mouseOverText=Text((0, 0), 'Main Menu', 25, True, Black), passiveText=Text((0, 0), 'Main Menu', 25, True, Black)))
        self.menu.AddButton('main', Button((0, 600), image=pygame.Surface((400, 80)), onClick= lambda: self.menu.SetTab('player'), text=Text((0, 0), 'Achievments', 25, True, White), mouseOverText=Text((0, 0), 'Main Menu', 25, True, Black), passiveText=Text((0, 0), 'Main Menu', 25, True, Black)))
        self.menu.AddButton('main', Button((0, 750), image=pygame.Surface((400, 80)), onClick= lambda: self.menu.SetTab('player'), text=Text((0, 0), 'Settings', 25, True, White), mouseOverText=Text((0, 0), 'Main Menu', 25, True, Black), passiveText=Text((0, 0), 'Main Menu', 25, True, Black)))
        self.menu.AddButton('main', Button((0, 900), image=pygame.Surface((400, 80)), onClick= lambda: self.menu.SetTab('player'), text=Text((0, 0), 'Credits', 25, True, White), mouseOverText=Text((0, 0), 'Main Menu', 25, True, Black), passiveText=Text((0, 0), 'Main Menu', 25, True, Black)))
        self.menu.AddButton('main', Button((0, 900), image=pygame.Surface((400, 80)), onClick= self.Exit, text=Text((0, 0), 'Exit', 25, True, White), mouseOverText=Text((0, 0), 'Main Menu', 25, True, Black), passiveText=Text((0, 0), 'Main Menu', 25, True, Black)))
        for button in self.menu.buttons['main']:
            
            Centerize(button, self, y=False)

    def HandleEvents(self, event: pygame.event.Event) -> None:
        
        self.menu.HandleEvents(self.mouseDownPosition, self.mousePosition, event)
        super().HandleEvents(event)

        self.DebugLog(4, f'Event: {event}')

    def Draw(self) -> None:

        self.window.fill((0, 0, 0))

        if self.menu.tab == 'game':

            self.window.fill((255, 255, 255))

        else:

            self.menu.Draw(self.window)

        super().Draw()