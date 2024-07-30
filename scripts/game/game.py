from game.application import Application
from gui.menu import Menu
from gui.text import Text
from settings import *
from gui.button import Button
from functions import Centerize, isMouseButtonDown, isMouseButtonUp, isClicked

import pygame

class Game(Application):

    def __init__(self):
        
        super().__init__()
        pygame.init()
        self.InitGUI()

    def InitGUI(self) -> None:
        
        self.menu = Menu()
        self.menu.rect = self.rect
        
        self.menu.AddTab('main')
        self.menu.AddTab('player')
        self.menu.AddTab('upgrades')
        self.menu.AddTab('achievments')
        self.menu.AddTab('settings')
        self.menu.AddTab('credits')
        
        self.menu.AddTab('mode')
        self.menu.AddTab('connect')
        self.menu.AddTab('lobby')
        self.menu.AddTab('join')
        self.menu.AddTab('game')

        self.menu.SetTab('main')
        
        #-# Main Menu #-#
        image = pygame.Surface((400, 80))
        mouseOverImage = image.copy()
        clickImage = image.copy()
        passiveImage = image.copy()
        passiveMouseOverImage = image.copy()
        passiveClickImage = image.copy()

        image.fill(colors.get('blue'))
        mouseOverImage.fill(colors.get('red'))
        clickImage.fill(colors.get('green'))
        passiveImage.fill(colors.get('gray'))
        passiveMouseOverImage.fill(colors.get('black'))
        passiveClickImage.fill(colors.get('black'))

        text = Text((0, 0), 'New Game')
        mouseOverText = Text((0, 0), 'New Game', color=colors.get('black'))
        passiveText = Text((0, 0), '', color=colors.get('black'))

        button = Button((0, 150), lambda: self.menu.SetTab('player'))
        button.SetImages(image, mouseOverImage, clickImage)
        button.SetPassiveImages(passiveImage, passiveMouseOverImage, passiveClickImage)

        
        button.SetText(text, mouseOverText, passiveText)

        self.menu.AddButton('main', button)

    def NewGame(self) -> None:
        
        pass

    def ContinueGame(self) -> None:
        
        pass

    def HandleEvents(self, event: pygame.event.Event) -> None:
        
        self.menu.HandleEvents(self.mouseDownPosition, self.mousePosition, event)
        super().HandleEvents(event)

        self.DebugLog(4, f'Event Name: {pygame.event.event_name(event.type)}')
        self.DebugLog(5, f'Event Position: {event.dict.get("pos")}')
        self.DebugLog(6, f'---------------------------------------')
        self.DebugLog(7, f'Mouse Position: {self.mousePosition}')
        self.DebugLog(8, f'Mouse Down Position: {self.mouseDownPosition}')
    def Draw(self) -> None:

        self.window.fill(BACKGROUND_COLOR)

        if self.menu.tab == 'game':

            self.window.fill((255, 255, 255))

        else:

            self.menu.Draw(self.window)

        super().Draw()