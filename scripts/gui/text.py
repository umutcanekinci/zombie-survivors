from settings import *
from object import Object
import pygame

class Text(Object):

	def __init__(self, position, text='', fontSize=25, antialias=True, color=colors.get('white'), backgroundColor=None, fontPath = None, spriteGroups: list=[]) -> None:

		super().__init__(position, spriteGroups)
		
		self.fontSize, self.antialias, self.color, self.backgroundColor, self.fontPath = fontSize, antialias, color, backgroundColor, fontPath
		self.SetText(text)
	
	def Render(self):

		_ = self.rect.left # Save the left position of the text
		self.SetImage(pygame.font.Font(self.fontPath, self.fontSize).render(self.text, self.antialias, self.color, self.backgroundColor))
		self.rect.left = _ # Set the left position of the text to the saved value
		
	def SetText(self, text: any) -> None:

		self.text = str(text)
		self.Render()

	def SetColor(self, color: tuple):

		self.color = color
		self.Render()