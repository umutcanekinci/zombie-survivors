import pygame

def isMouseOver(rect, mousePosition: tuple) -> bool:

    return rect.collidepoint(mousePosition)

def isMouseButtonDown(rect, mousePosition: tuple, event: pygame.event.Event) -> bool:

    return isMouseOver(rect, mousePosition) and event.type == pygame.MOUSEBUTTONDOWN

def isMouseButtonUp(rect, mousePosition: tuple, event: pygame.event.Event) -> bool:

    return isMouseOver(rect, mousePosition) and event.type == pygame.MOUSEBUTTONUP

def isClicked(rect, mouseDownPosition: tuple, mousePosition: tuple, event: pygame.event.Event) -> bool:

    return mouseDownPosition != None and isMouseOver(rect, mouseDownPosition) and isMouseButtonUp(rect, mousePosition, event)

def GetImage(imagePath: str) -> pygame.Surface:

    pass

def Centerize(rect, parentRect, x=True, y=True) -> None:

    if x: rect.centerx = parentRect.width // 2
    if y: rect.centery = parentRect.height // 2
