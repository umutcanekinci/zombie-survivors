import pygame
from game.application import Application
from gui.menu import Menu
from settings import TABS, BACKGROUND_COLOR
from network import Network


class Game(Application):

	def __init__(self):
		
		super().__init__()
		pygame.init()
		self.InitGUI()
		self.network = Network(self.OnRecieveData)

	def InitGUI(self) -> None:
		
		self.menu = Menu(TABS)
		self.menu.rect = self.rect
		self.menu.SetTab('connect')

		# Main Menu Buttons
		self.menu.AddButtonAuto('main', 'New Game', lambda: self.menu.SetTab('player'))
		self.menu.AddButtonAuto('main', 'Continue Game', self.ContinueGame, 'inactive')
		self.menu.AddButtonAuto('main', 'Upgrades', lambda: self.menu.SetTab('upgrades'), False)
		self.menu.AddButtonAuto('main', 'Achievements', lambda: self.menu.SetTab('achievements'), False)
		self.menu.AddButtonAuto('main', 'Settings', lambda: self.menu.SetTab('settings'), False)
		self.menu.AddButtonAuto('main', 'Credits', lambda: self.menu.SetTab('credits'), False)
		self.menu.AddButtonAuto('main', 'Exit', self.Exit)

		# Player Menu Buttons
		self.menu.AddInputBoxAuto('player', 'Enter your name')
		self.menu.AddButtonAuto('player', 'Confirm', lambda: self.menu.SetTab('mode'), False)
		self.menu.AddButtonAuto('player', 'Back', lambda: self.menu.SetTab('main'))

		# Mode Menu Buttons
		self.menu.AddButtonAuto('mode', 'Singleplayer', self.Singleplayer)
		self.menu.AddButtonAuto('mode', 'Multiplayer', lambda: self.menu.SetTab('connect'))
		self.menu.AddButtonAuto('mode', 'Back', lambda: self.menu.SetTab('player'))

		# Connect Menu Buttons
		self.menu.AddButtonAuto('connect', 'Join via IP', lambda: self.menu.SetTab('join'))
		self.menu.AddButtonAuto('connect', 'Host & Play', self.Host)
		self.menu.AddButtonAuto('connect', 'Back', lambda: self.menu.SetTab('mode'))

		# Join Menu Buttons
		self.menu.AddInputBoxAuto('join', 'Enter the IP')
		self.menu.AddInputBoxAuto('join', 'Enter the Port')
		self.menu.AddButtonAuto('join', 'Join', self.JoinLobby, False)
		self.menu.AddButtonAuto('join', 'Back', lambda: self.menu.SetTab('connect'))

		# Lobby Menu Buttons
		self.menu.AddButtonAuto('lobby', 'Start Game', lambda: self.menu.SetTab('game'), False)
		self.menu.AddButtonAuto('lobby', 'Back', lambda: self.menu.SetTab('connect'))

		
		pass
	def Singleplayer(self) -> None:
		
		# Database should be added
		pass

	def JoinLobby(self) -> None:

		if self.network.Connect(self.menu.buttons['join'][0].text, int(self.menu.buttons['join'][1].text)):

			self.menu.SetTab('lobby')

		else:

			self.menu.SetTab('connect')

	def Host(self) -> None:

		self.network.Host()

	def OnRecieveData(self, data) -> None:

		command, data = data

		if command == '':

			pass

	def ContinueGame(self) -> None:
		
		# Database should be added
		pass

	








	def UpdateDebugLog(self, event) -> None:
		
		self.DebugLog(9, f'Mouse Down Position: {self.mouseDownPosition}')
		self.DebugLog(10, f'Network Status: {self.network.status}')

		return super().UpdateDebugLog(event)

	def HandleEvents(self, event: pygame.event.Event) -> None:
		
		# Activate confirm buttons when text is entered
		if self.menu.tab == 'player':

			self.menu.buttons[self.menu.tab][1].isEnabled = self.menu.buttons[self.menu.tab][0].text    
		
		elif self.menu.tab == 'join':

			self.menu.buttons[self.menu.tab][2].isEnabled = self.menu.buttons[self.menu.tab][0].text and self.menu.buttons[self.menu.tab][1].text        

		self.menu.HandleEvents(self.mousePosition, event)
		super().HandleEvents(event)       

	def HandleExitEvents(self, event: pygame.event.Event) -> None:
		
		if self.menu.HandleExitEvents(event): self.Exit()
	
	def Draw(self) -> None:

		self.window.fill(BACKGROUND_COLOR)
		self.menu.Draw(self.window)

		super().Draw()

	def Exit(self) -> None:

		self.network.Close()
		return super().Exit()