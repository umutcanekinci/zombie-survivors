import pygame

class Object(pygame.sprite.Sprite):

    def __init__(self, position: tuple = (0, 0), spriteGroups: list = []):

        super().__init__(spriteGroups)
        self.rect = pygame.Rect(position, (0, 0))

    def SetImage(self, image: pygame.Surface) -> None:
        
        self.image = image
        self.rect = self.image.get_rect(center=self.rect.center)

    def Draw(self, surface: pygame.Surface):

        surface.blit(self.image, self.rect)