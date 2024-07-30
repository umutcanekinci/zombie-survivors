import pygame
from object import Object
from functions import isClicked, isMouseOver, Centerize
from settings import White, Blue, Yellow, PASSIVE_BUTTON_COLOR
from gui.text import Text
from path import FontPath

class Button(Object):

	def __init__(self, position: tuple = (0, 0), color= Blue, mouseOverColor: tuple = Yellow, image: pygame.Surface = None, spriteGroups: list = [], onClick = None, state = 'active', text: Text=None, mouseOverText: Text=None, passiveText: Text=None) -> None:

		super().__init__(position, spriteGroups)

		# Set the images of the button
		self.SetImage(image)
		self.mouseOverImage = self.image.copy()
		self.passiveImage = self.image.copy()
		
		# Set the color of the button
		self.SetColor(color)
		self.SetMouseOverColor(mouseOverColor)
		self.SetPassiveColor(PASSIVE_BUTTON_COLOR)

		# Set the text of the button
	
		if text:
			
			Centerize(text, self)
			text.Draw(self.image)
			
		if mouseOverText:
			
			Centerize(mouseOverText, self)
			mouseOverText.Draw(self.mouseOverImage)
		
		if passiveText:
			
			Centerize(passiveText, self)
			passiveText.Draw(self.passiveImage)

		self.state = state
		self.onClick = onClick

	def SetColor(self, color: tuple) -> None:

		self.image.fill(color)

	def SetMouseOverColor(self, color: tuple) -> None:

		self.mouseOverImage.fill(color)

	def SetPassiveColor(self, color: tuple) -> None:

		self.passiveImage.fill(color)

	def HandleEvents(self, mouseDownPosition, mousePosition, event: pygame.event.Event) -> None:
		
		if self.isMouseClick(mouseDownPosition, mousePosition, event):

			print('clicked')
			self.onClick()

		if self.state != 'passive':

			self.state = 'mouseOver' if isMouseOver(self, mousePosition) else 'active'
		
	def isMouseClick(self, mouseDownPosition, mousePosition, event: pygame.event.Event) -> bool:

		return isClicked(self, mouseDownPosition, mousePosition, event) and self.state != 'passive'
	
	def Draw(self, surface: pygame.Surface) -> None:
	
		if self.state == 'active':

			super().Draw(surface)

		elif self.state == 'mouseOver':

			surface.blit(self.mouseOverImage, self.rect)

		elif self.state == 'passive':

			surface.blit(self.passiveImage, self.rect)
