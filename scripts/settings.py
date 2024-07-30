from pygame.color import THECOLORS as colors
from pygame import Rect

FPS = 60
DEBUG_MODE = True

PASSIVE_BUTTON_COLOR = colors.get('grey')
BACKGROUND_COLOR = (72, 218, 233)

# Window
WINDOW_TITLE = "Zombie Survivors"
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (1920, 1080)
WINDOW_RECT = Rect((0, 0), WINDOW_SIZE)