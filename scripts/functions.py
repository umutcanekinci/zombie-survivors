import pygame

def isMouseOver(object, mousePosition: tuple) -> bool:

    return object.rect.collidepoint(mousePosition)

def isMouseButtonDown(object, mousePosition: tuple, event: pygame.event.Event) -> bool:

    return isMouseOver(object, mousePosition) and event.type == pygame.MOUSEBUTTONDOWN

def isMouseButtonUp(object, mousePosition: tuple, event: pygame.event.Event) -> bool:

    return isMouseOver(object, mousePosition) and event.type == pygame.MOUSEBUTTONUP

def isClicked(object, mouseDownPosition: tuple, mousePosition: tuple, event: pygame.event.Event) -> bool:

    return mouseDownPosition and isMouseButtonDown(object, mouseDownPosition, pygame.event.Event) and isMouseButtonUp(object, mousePosition, event)

def GetImage(imagePath: str) -> pygame.Surface:

    pass

def Centerize(object, parentObject, x=True, y=True) -> None:

    if x:

        object.rect.centerx = parentObject.rect.width // 2

    if y:

        object.rect.centery = parentObject.rect.height // 2
