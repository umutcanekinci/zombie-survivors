import pygame
from object import Object
from functions import isClicked, isMouseOver, Centerize
from settings import colors, PASSIVE_BUTTON_COLOR
from gui.text import Text
from path import FontPath

class Button(Object):

	def __init__(self, position: tuple = (0, 0), onClick = None, state = 'active', spriteGroups: list = []) -> None:

		super().__init__(position, spriteGroups)

		self.state = state
		self.onClick = onClick

	def SetText(self, text: Text=None, mouseOverText: Text=None, passiveText: Text=None):

		if text and self.image:
			
			Centerize(text.rect, self.rect)
			text.Draw(self.image)
			
		if mouseOverText and self.mouseOverImage:
			
			Centerize(mouseOverText.rect, self.rect)
			mouseOverText.Draw(self.mouseOverImage)
		
		if passiveText and self.passiveImage:
			
			Centerize(passiveText.rect, self.rect)
			passiveText.Draw(self.passiveImage)

	def SetImages(self, image: pygame.Surface = None, mouseOverImage: pygame.Surface= None, clickImage: pygame.Surface = None):

		self.image = image
		self.mouseOverImage = mouseOverImage
		self.clickImage = clickImage

		self.rect = self.image.get_rect(center=self.rect.center)

	def SetPassiveImages(self, image: pygame.Surface = None, mouseOverImage: pygame.Surface= None, clickImage: pygame.Surface = None):

		self.passiveImage = image
		self.passiveMouseOverImage = mouseOverImage
		self.passiveClickImage = clickImage

		self.rect = self.passiveImage.get_rect(center=self.rect.center)

	def HandleEvents(self, mouseDownPosition, mousePosition, event: pygame.event.Event) -> None:
		
		if self.isClicked(mouseDownPosition, mousePosition, event): self.onClick()

		#image
		#mouseOverImage
		#clickImage
		#passiveImage
		#passiveMouseOverImage
		#passiveClickImage

		if 'passive' in self.state:

			if isMouseOver(self.rect, mousePosition): self.state = 'passiveMouseOver'

			elif isClicked(self.rect, mouseDownPosition, mousePosition, event): self.state = 'passiveClick'

			else: self.state = 'passive'

		else:

			if isMouseOver(self.rect, mousePosition): self.state = 'mouseOver'

			elif isClicked(self.rect, mouseDownPosition, mousePosition, event): self.state = 'click'

			else: self.state = 'active'

	def isClicked(self, mouseDownPosition, mousePosition, event: pygame.event.Event) -> bool:
			
		return isClicked(self.rect, mouseDownPosition, mousePosition, event) and 'passive' not in self.state
	
	def Draw(self, surface: pygame.Surface) -> None:
	
		if self.state == 'active':

			super().Draw(surface)

		elif self.state == 'mouseOver':

			surface.blit(self.mouseOverImage, self.rect)

		elif self.state == 'click':

			surface.blit(self.clickImage, self.rect)

		elif self.state == 'passive':

			surface.blit(self.passiveImage, self.rect)

		elif self.state == 'passiveMouseOver':

			surface.blit(self.passiveMouseOverImage, self.rect)

		elif self.state == 'passiveClick':

			surface.blit(self.passiveClickImage, self.rect)

class EllipseButton(Button):

	def __init__(self, position: tuple = (0, 0), color=colors.get('blue'), mouseOverColor: tuple = colors.get('yellow'), image: pygame.Surface = None, spriteGroups: list = [], onClick=None, state='active', text: Text = None, mouseOverText: Text = None, passiveText: Text = None) -> None:
		
		super().__init__(position, color, mouseOverColor, image, spriteGroups, onClick, state, text, mouseOverText, passiveText)

		backgroundImage = self.image.copy()

		self.image
		self.mouseOverImage
		self.passiveImage

		self.clickedImage = self.image.copy()
		self.clickedMouseOverImage = self.mouseOverImage.copy()
		self.clickedPassiveImage = self.passiveImage.copy()
