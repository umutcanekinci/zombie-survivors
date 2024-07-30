import pygame
from gui.button import Button

class Menu:

    def __init__(self):

        self.tab = None
        self.tabs = {}
        self.buttons = {}

    def SetTab(self, name: str) -> None:

        self.tab = name

    def AddTab(self, name: str) -> None:

        self.tabs[name] = pygame.sprite.Group()
        self.buttons[name] = []

    def AddButton(self, tab, button) -> None:
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