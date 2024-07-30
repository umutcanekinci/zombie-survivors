from settings import *
from object import Object
import pygame

class Text(Object):

	def __init__(self, position, text='', textSize=25, antialias=True, color=White, backgroundColor=None, fontPath = None, spriteGroups: list=[]) -> None:

		super().__init__(position, spriteGroups)
		
		self.textSize, self.antialias, self.color, self.backgroundColor, self.fontPath = textSize, antialias, color, backgroundColor, fontPath
		self.SetText(text)
	
	def Render(self):

		_ = self.rect.left # Save the left position of the text
		self.SetImage(pygame.font.Font(self.fontPath, self.textSize).render(self.text, self.antialias, self.color, self.backgroundColor))
		self.rect.left = _ # Set the left position of the text to the saved value
		
	def SetText(self, text: any) -> None:

		self.text = str(text)
		self.Render()

	def SetColor(self, color: tuple):

		self.color = color
		self.Render()