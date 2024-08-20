from pygame.color import THECOLORS as colors
from pygame import Rect

FPS = 60
DEBUG_MODE = True
DEBUG_MODE_COLOR = colors.get('red')
BACKGROUND_COLOR = (72, 218, 233)

# NETWORK
PORT = 5050
MAX_CONNECTIONS = 4
HEADER = 4

# MENU
TABS = ['main', 'player', 'upgrades', 'achievements', 'settings', 'credits', 'mode', 'connect', 'lobby', 'join', 'game']
TAB_ON_ESC = {
    'main': 'exit',
    'player': 'main',
    'upgrades': 'main',
    'achievements': 'main',
    'settings': 'main',
    'credits': 'main',
    'mode': 'player',
    'connect': 'mode',
    'join': 'mode',
    'lobby': 'connect',
    'game': 'main'
}

class WINDOW:
    
    TITLE = "Zombie Survivors"
    SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (1920, 1080)
    RECT = Rect((0, 0), SIZE)

class BUTTON:

    # Sizes
    SIZE = (400, 80)
    TEXT_SIZE = 25

    # Borders
    BORDER_WIDTH = 2
    HELD_BORDER_WIDTH = 1
    
    # Colors
    COLOR = colors.get('red')
    MOUSE_OVER_COLOR = colors.get('pink')
    HELD_COLOR = colors.get('darkblue')
    INACTIVE_COLOR = colors.get('grey')
    INACTIVE_MOUSE_OVER_COLOR = colors.get('lightgrey')
    INACTIVE_HELD_COLOR = colors.get('darkgrey')

    # Text Colors
    TEXT_COLOR = colors.get('white')
    TEXT_MOUSE_OVER_COLOR = colors.get('black')
    TEXT_HELD_COLOR = colors.get('black')
    TEXT_INACTIVE_COLOR = colors.get('black')
    TEXT_INACTIVE_MOUSE_OVER_COLOR = colors.get('black')
    TEXT_INACTIVE_HELD_COLOR = colors.get('black')

    SPACE = 30 # Space between buttons when added automatically
    HELD_SPACE = 5 # Space between button and text when held
    RADIUS = 25 # Radius of the button corners
    
class INPUT_BOX:

    COLOR = colors.get('dodgerblue2')
    INACTIVE_COLOR = colors.get('gray')

    SIZE = (380, 80)