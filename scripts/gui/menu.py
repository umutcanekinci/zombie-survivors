import pygame
from gui.button import Button
from functions import Centerize
from object import Object
class Menu(Object):

    def __init__(self) -> None:

        super().__init__((0, 0))

        self.tab = None
        self.tabs = {}
        self.buttons = {}
        
    def SetTab(self, name: str) -> None:

        self.tab = name

    def AddTab(self, name: str) -> None:

        self.tabs[name] = pygame.sprite.Group()
        self.buttons[name] = []

    def AddButton(self, tab, button) -> None:

        Centerize(button.rect, self.rect, y=False)

        self.tabs[tab].add(button)
        self.buttons[tab].append(button)
    
    def HandleEvents(self, mouseDownPosition, mousePosition, event: pygame.event.Event) -> None:

        if self.tab and self.tabs:
            
            for button in self.buttons[self.tab]:

                button.HandleEvents(mouseDownPosition, mousePosition, event)

    def Draw(self, surface: pygame.Surface) -> None:

        if self.tab:

            for sprite in self.tabs[self.tab]:

                sprite.Draw(surface)