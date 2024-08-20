import pygame
from settings import *
from object import Object
from functions import isMouseOver, Centerize
from settings import colors, INPUT_BOX
from gui.text import Text

class InputBox(Object):

	def __init__(self, position, placeholder = '', spriteGroups: list=[], text='', size=INPUT_BOX.SIZE, color=INPUT_BOX.COLOR):

		super().__init__(position, spriteGroups=spriteGroups)
		self.size = size
		self.color = color
		self.text, self.placeholder = text, placeholder
		self.active = True
		
		self.Rerender()

	def HandleEvents(self, mousePosition, event):

		if event.type == pygame.MOUSEBUTTONDOWN:

			# If the user clicked on the input_box rect.
			self.active = True if isMouseOver(self.rect, mousePosition) else False
			self.color = INPUT_BOX.COLOR if self.active else INPUT_BOX.INACTIVE_COLOR
			self.Rerender()

		elif event.type == pygame.KEYDOWN and self.active:

			if event.key == pygame.K_BACKSPACE:

				self.text = self.text[:-1]

			elif self.textSurface.image.get_width() < self.rect.width - 25:

				self.text += event.unicode

			self.Rerender()

	def Rerender(self):
		
		super().SetImage(pygame.Surface(self.size, pygame.SRCALPHA))

		self.textSurface = Text((0, 0), self.text if self.text else self.placeholder, 32, color=self.color)
		Centerize(self.textSurface.rect, self.rect)
		self.textSurface.Draw(self.image)

		pygame.draw.rect(self.image, self.color, pygame.Rect((0, 0), self.rect.size), 2)