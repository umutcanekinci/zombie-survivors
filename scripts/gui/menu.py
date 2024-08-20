import pygame
from gui.button import Button, ColorButton, EllipseButton
from gui.input_box import InputBox
from functions import Centerize
from object import Object
from settings import BUTTON, TAB_ON_ESC

class Menu(Object):

    def __init__(self, tabs) -> None:

        super().__init__((0, 0))

        self.tab = None
        self.tabs = {}
        self.buttons = {}

        for tab in tabs:
                
            self.AddTab(tab)
        
    def SetTab(self, name: str) -> None:

        self.tab = name

    def AddTab(self, name: str) -> None:

        self.tabs[name] = pygame.sprite.Group()
        self.buttons[name] = []

    def AddButton(self, tab, button) -> None:

        self.tabs[tab].add(button)
        self.buttons[tab].append(button)
    
    def AddTextAuto(self, tab, text, space: int=BUTTON.SPACE) -> None:

        self.AddButton(tab, Button((0, 0)))
        self.buttons[tab][-1].rect.top = (self.buttons[tab][-2].rect.bottom if len(self.buttons[tab]) > 1 else 0) + space
        Centerize(self.buttons[tab][-1].rect, self.rect, y=False)
        self.buttons[tab][-1].SetText(text)

    def AddButtonAuto(self, tab, text, onClick=lambda: None, isEnabled=True, space: int=BUTTON.SPACE) -> None:
        
        self.AddButton(tab, EllipseButton((0, 0), onClick, isEnabled))
        self.buttons[tab][-1].rect.top = (self.buttons[tab][-2].rect.bottom if len(self.buttons[tab]) > 1 else 0) + space
        Centerize(self.buttons[tab][-1].rect, self.rect, y=False)
        self.buttons[tab][-1].SetText(text)

    def AddInputBoxAuto(self, tab, inactiveText='', space: int=BUTTON.SPACE) -> None:

        self.AddButton(tab, InputBox((0, 0), inactiveText))
        self.buttons[tab][-1].rect.top = (self.buttons[tab][-2].rect.bottom if len(self.buttons[tab]) > 1 else 0) + space
        Centerize(self.buttons[tab][-1].rect, self.rect, y=False)

    def HandleEvents(self, mousePosition, event: pygame.event.Event) -> None:

        if self.tab and self.tabs:
            
            for button in self.buttons[self.tab]:

                button.HandleEvents(mousePosition, event)

    def HandleExitEvents(self, event: pygame.event.Event) -> bool:

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):

            if self.tab in TAB_ON_ESC:
                
                if TAB_ON_ESC[self.tab] != 'exit': self.SetTab(TAB_ON_ESC[self.tab]) 
                else: return 1

            else:
                
                self.SetTab('main')

        return 0
    
    def Draw(self, surface: pygame.Surface) -> None:

        if self.tab and self.tabs and self.tab in self.tabs:

            for sprite in self.tabs[self.tab]: sprite.Draw(surface)