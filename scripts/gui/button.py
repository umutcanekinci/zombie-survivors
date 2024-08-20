import pygame
from object import Object
from functions import isMouseOver, isHeld, Centerize, isMouseButtonUp
from settings import colors, BUTTON
from gui.text import Text
from path import FontPath

class Button(Object):

	def __init__(self, position: tuple = (0, 0), onClick = lambda: None, isEnabled=True, spriteGroups: list = []) -> None:

		super().__init__(position, spriteGroups)
		self.isEnabled = isEnabled
		self.state = 'normal'
		self.onClick = onClick

	def SetText(self, text: Text=None, mouseOverText: Text=None, heldText: Text=None):

		if text and hasattr(self, 'image') and self.image:
			
			Centerize(text.rect, self.rect)
			text.Draw(self.image)
			
		if mouseOverText and hasattr(self, 'mouseOverImage') and self.mouseOverImage:
			
			Centerize(mouseOverText.rect, self.rect)
			mouseOverText.Draw(self.mouseOverImage)
		
		if heldText and hasattr(self, 'heldImage') and self.heldImage:
			
			Centerize(heldText.rect, self.rect)
			heldText.Draw(self.heldImage)

		self.SetInactiveText(text, mouseOverText, heldText)

	def SetInactiveText(self, text: Text=None, mouseOverText: Text=None, inactiveText: Text=None):

		if text and hasattr(self, 'inactiveImage') and self.inactiveImage:
			
			Centerize(text.rect, self.rect)
			text.Draw(self.inactiveImage)
			
		if mouseOverText and hasattr(self, 'inactiveMouseOverImage') and self.inactiveMouseOverImage:
			
			Centerize(mouseOverText.rect, self.rect)
			mouseOverText.Draw(self.inactiveMouseOverImage)
		
		if inactiveText and hasattr(self, 'inactiveHeldImage') and self.inactiveHeldImage:
			
			Centerize(inactiveText.rect, self.rect)
			inactiveText.Draw(self.inactiveHeldImage)

	def SetImages(self, image: pygame.Surface = None, mouseOverImage: pygame.Surface= None, heldImage: pygame.Surface = None):

		self.image = image
		self.mouseOverImage = mouseOverImage if mouseOverImage else image
		self.heldImage = heldImage if heldImage else image

		self.rect = self.image.get_rect(center=self.rect.center)

	def SetInactiveImages(self, image: pygame.Surface = None, mouseOverImage: pygame.Surface= None, heldImage: pygame.Surface = None):

		self.inactiveImage = image
		self.inactiveMouseOverImage = mouseOverImage if mouseOverImage else image
		self.inactiveHeldImage = heldImage if heldImage else image

		self.rect = self.inactiveImage.get_rect(center=self.rect.center)

	def HandleEvents(self, mousePosition, event: pygame.event.Event) -> None:
		
		if self.state == 'held':
		
			if self.isEnabled:
					
				if event.type == pygame.MOUSEBUTTONUP:

					if isMouseOver(self.rect, mousePosition):

						self.state = 'mouseOver'
						self.onClick()

					else:

						self.state = 'normal'

				self.state == 'inactiveHeld'
	
			else:

				if event.type == pygame.MOUSEBUTTONUP:

					self.state = 'mouseOver' if isMouseOver(self.rect, mousePosition) else 'normal'

		else:

			if isHeld(self.rect, mousePosition, event): self.state = 'held'
			elif isMouseOver(self.rect, mousePosition): self.state = 'mouseOver'
			else: self.state = 'normal'

	def isClicked(self, mousePosition, event: pygame.event.Event) -> bool:
			
		return isMouseButtonUp(self.rect, mousePosition, event) and self.state=='held'
	
	def Draw(self, surface: pygame.Surface) -> None:
	
		if self.state == 'normal':

			super().Draw(surface) if self.isEnabled else surface.blit(self.inactiveImage, self.rect)

		elif self.state == 'mouseOver':

			surface.blit(self.mouseOverImage, self.rect) if self.isEnabled else surface.blit(self.inactiveMouseOverImage, self.rect)

		elif self.state == 'held':

			surface.blit(self.heldImage, self.rect) if self.isEnabled else surface.blit(self.inactiveHeldImage, self.rect)

class ColorButton(Button):

	def __init__(self, position: tuple = (0, 0), onClick=lambda: None, state='active', spriteGroups: list = [], size: tuple=BUTTON.SIZE, color: tuple=BUTTON.COLOR, mouseOverColor: tuple=BUTTON.MOUSE_OVER_COLOR, heldColor: tuple=BUTTON.HELD_COLOR) -> None:
	
		super().__init__(position, onClick, state, spriteGroups)

		self.SetImages(pygame.Surface(size), pygame.Surface(size), pygame.Surface(size))
		self.SetInactiveImages()

		self.image.fill(color)
		self.mouseOverImage.fill(mouseOverColor)
		self.heldImage.fill(heldColor)

	def SetInactiveImages(self, color: tuple=BUTTON.INACTIVE_COLOR, mouseOverColor: tuple=BUTTON.INACTIVE_MOUSE_OVER_COLOR, heldColor: tuple=BUTTON.INACTIVE_HELD_COLOR) -> None:

		super().SetInactiveImages(pygame.Surface(self.rect.size), pygame.Surface(self.rect.size), pygame.Surface(self.rect.size))

		self.inactiveImage.fill(color)
		self.inactiveMouseOverImage.fill(mouseOverColor)
		self.inactiveHeldImage.fill(heldColor)

	def SetText(self, text: Text = None, fontSize: int = BUTTON.TEXT_SIZE, antialias: bool = True, color: tuple = BUTTON.TEXT_COLOR, mouseOverColor: tuple=BUTTON.TEXT_MOUSE_OVER_COLOR, heldColor: tuple=BUTTON.TEXT_HELD_COLOR) -> None:
		
		super().SetText(
						Text((0, 0), text, fontSize, antialias, color),
						Text((0, 0), text, fontSize, antialias, mouseOverColor),
						Text((0, 0), text, fontSize, antialias, heldColor))

		self.SetInactiveText(text)

	def SetInactiveText(self, text: Text = None, fontSize: int = BUTTON.TEXT_SIZE, antialias: bool = True, color: tuple = BUTTON.TEXT_INACTIVE_COLOR, mouseOverColor: tuple=BUTTON.TEXT_INACTIVE_MOUSE_OVER_COLOR, heldColor: tuple=BUTTON.TEXT_INACTIVE_HELD_COLOR) -> None:
		
		return super().SetInactiveText(
						Text((0, 0), text, fontSize, antialias, color),
						Text((0, 0), text, fontSize, antialias, mouseOverColor),
						Text((0, 0), text, fontSize, antialias, heldColor))

class EllipseButton(Button):

	def __init__(self, position: tuple = (0, 0), onClick=lambda: None, state='active', spriteGroups: list = [], size: tuple=BUTTON.SIZE, color: tuple=BUTTON.COLOR, mouseOverColor: tuple=BUTTON.MOUSE_OVER_COLOR, heldColor: tuple=BUTTON.HELD_COLOR, heldSpace=BUTTON.HELD_SPACE, radius=BUTTON.RADIUS) -> None:
	
		super().__init__(position, onClick, state, spriteGroups)
		self.heldSpace = heldSpace
		self.radius = radius

		self.SetImages(pygame.Surface(size, pygame.SRCALPHA), pygame.Surface(size, pygame.SRCALPHA), pygame.Surface(size, pygame.SRCALPHA))
		self.SetInactiveImages()

		self.backgroundRect = pygame.Rect(0, 0, self.rect.width, self.rect.height)
		self.normalRect = pygame.Rect(0, 0, self.rect.width, self.rect.height - self.heldSpace)
		self.heldRect = pygame.Rect(0, self.heldSpace, self.rect.width, self.rect.height - self.heldSpace)
		
		pygame.draw.rect(self.image, colors.get('black'), self.backgroundRect, 0, self.radius)
		pygame.draw.rect(self.mouseOverImage, colors.get('black'), self.backgroundRect, 0, self.radius)
		
		pygame.draw.rect(self.image, color, self.normalRect, 0, self.radius)
		pygame.draw.rect(self.image, colors.get('black'), self.backgroundRect, 2, self.radius)
		
		pygame.draw.rect(self.mouseOverImage, mouseOverColor, self.normalRect, 0, self.radius)
		pygame.draw.rect(self.mouseOverImage, colors.get('black'), self.backgroundRect, 1, self.radius)

		pygame.draw.rect(self.heldImage, heldColor, self.heldRect, 0, self.radius)
		pygame.draw.rect(self.heldImage, colors.get('black'), self.heldRect, 1, self.radius)

	def SetInactiveImages(self, color=BUTTON.INACTIVE_COLOR, mouseOverColor=BUTTON.INACTIVE_MOUSE_OVER_COLOR, heldColor=BUTTON.INACTIVE_HELD_COLOR) -> None:

		super().SetInactiveImages(pygame.Surface(self.rect.size, pygame.SRCALPHA), pygame.Surface(self.rect.size, pygame.SRCALPHA), pygame.Surface(self.rect.size, pygame.SRCALPHA))
	
		self.backgroundRect = pygame.Rect(0, 0, self.rect.width, self.rect.height)
		self.normalRect = pygame.Rect(0, 0, self.rect.width, self.rect.height - self.heldSpace)
		self.heldRect = pygame.Rect(0, self.heldSpace, self.rect.width, self.rect.height - self.heldSpace)
		
		pygame.draw.rect(self.inactiveImage, colors.get('black'), self.backgroundRect, 0, self.radius)
		pygame.draw.rect(self.inactiveMouseOverImage, colors.get('black'), self.backgroundRect, 0, self.radius)
		
		pygame.draw.rect(self.inactiveImage, color, self.normalRect, 0, self.radius)
		pygame.draw.rect(self.inactiveImage, colors.get('black'), self.backgroundRect, 2, self.radius)
		
		pygame.draw.rect(self.inactiveMouseOverImage, mouseOverColor, self.normalRect, 0, self.radius)
		pygame.draw.rect(self.inactiveMouseOverImage, colors.get('black'), self.backgroundRect, 1, self.radius)

		pygame.draw.rect(self.inactiveHeldImage, heldColor, self.heldRect, 0, self.radius)
		pygame.draw.rect(self.inactiveHeldImage, colors.get('black'), self.heldRect, 1, self.radius)

	def SetText(self, text: Text = None, fontSize: int = BUTTON.TEXT_SIZE, antialias: bool = True, color: tuple = BUTTON.TEXT_COLOR, mouseOverColor: tuple=BUTTON.TEXT_MOUSE_OVER_COLOR, heldColor: tuple=BUTTON.TEXT_HELD_COLOR) -> None:
		
		normalText = Text((0, 0), text, fontSize, antialias, color)
		mouseOverText = Text((0, 0), text, fontSize, antialias, mouseOverColor)
		heldText = Text((0, 0), text, fontSize, antialias, heldColor)

		Centerize(normalText.rect, self.normalRect)
		normalText.Draw(self.image)
			
		Centerize(mouseOverText.rect, self.normalRect)
		mouseOverText.Draw(self.mouseOverImage)
		
		Centerize(heldText.rect, self.normalRect)
		heldText.rect.top += self.heldSpace
		heldText.Draw(self.heldImage)

		self.SetInactiveText(text)

	def SetInactiveText(self, text: Text = None, fontSize: int = BUTTON.TEXT_SIZE, antialias: bool = True, color: tuple = BUTTON.TEXT_INACTIVE_COLOR, mouseOverColor: tuple=BUTTON.TEXT_INACTIVE_MOUSE_OVER_COLOR, heldColor: tuple=BUTTON.TEXT_INACTIVE_HELD_COLOR) -> None:
		
		normalText = Text((0, 0), text, fontSize, antialias, color)
		mouseOverText = Text((0, 0), text, fontSize, antialias, mouseOverColor)
		heldText = Text((0, 0), text, fontSize, antialias, heldColor)

		Centerize(normalText.rect, self.normalRect)
		normalText.Draw(self.inactiveImage)
			
		Centerize(mouseOverText.rect, self.normalRect)
		mouseOverText.Draw(self.inactiveMouseOverImage)
		
		Centerize(heldText.rect, self.normalRect)
		heldText.rect.top += self.heldSpace
		heldText.Draw(self.inactiveHeldImage)
