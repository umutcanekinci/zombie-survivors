import sys, pygame
from settings import WINDOW, FPS, DEBUG_MODE, DEBUG_MODE_COLOR
from gui.text import Text

class Application:

	def __init__(self) -> None:
		
		super().__init__()
		self.InitPygame()
		self.InitClock()
		self.InitMixer()
		self.InitDebugLog()
		self.SetTitle(WINDOW.TITLE)
		self.SetSize(WINDOW.SIZE)
		self.SetFPS(FPS)
		self.SetDebugMode(DEBUG_MODE)
		self.InitWindow()

	def InitPygame(self) -> None:
		
		pygame.init()

	def InitMixer(self) -> None:

		pygame.mixer.init()

	def InitDebugLog(self) -> None:

		self.debugMode = DEBUG_MODE
		self.debugModeLog = []

	def AddDebugLog(self, text: str) -> None:

		self.debugModeLog.append(Text((0, 0), text, 25, True, DEBUG_MODE_COLOR))
		self.debugModeLog[-1].rect.topleft = (0, 25 * len(self.debugModeLog) - 25)

	def DebugLog(self, row: int, text: str) -> None:

		if row < len(self.debugModeLog):

			self.debugModeLog[row].SetText(text)

		else:

			self.AddDebugLog(text)

	def InitClock(self) -> None:

		self.clock = pygame.time.Clock()

	def SetTitle(self, title: str) -> None:
		
		self.title = title
		pygame.display.set_caption(self.title)

	def SetSize(self, size: tuple) -> None:

		self.rect = pygame.Rect((0, 0), size)

	def SetFPS(self, FPS: int) -> None:
		
		self.FPS = FPS

	def SetDebugMode(self, value: bool) -> None:

		self.debugMode = value

	def InitWindow(self) -> None:

		self.window = pygame.display.set_mode(self.rect.size)

	def Run(self) -> None:
		
		self.mouseDownPosition = None

		#-# Starting App #-#
		self.isRunning = True

		#-# Main Loop #-#
		while self.isRunning:

			#-# FPS #-#
			self.deltaTime = self.clock.tick(self.FPS) * .001 * self.FPS

			#-# Getting Mouse Position #-#
			self.mousePosition = pygame.mouse.get_pos()

			#-# etting Pressed Keys #-#
			self.keys = pygame.key.get_pressed()

			#-# Handling Events #-#
			for event in pygame.event.get():
					
				self.HandleEvents(event)

			self.Update()

			#-# Draw Objects #-#
			self.Draw()
	
	def UpdateDebugLog(self, event) -> None:

		self.DebugLog(0, 'Debug Mode: ON, Press F3 to toggle')
		self.DebugLog(1, f'Python Version: {sys.version}')
		self.DebugLog(2, f'Pygame Version: {pygame.version.ver}')
		self.DebugLog(3, f'---------------------------------------')
		self.DebugLog(4, f'FPS: {round(self.clock.get_fps())}')
		self.DebugLog(5, f'Event Name: {pygame.event.event_name(event.type)}')
		self.DebugLog(6, f'Event Position: {event.dict.get("pos")}')
		self.DebugLog(7, f'Mouse Position: {self.mousePosition}')
		self.DebugLog(8, f'---------------------------------------')

	def HandleEvents(self, event: pygame.event.Event) -> None:
		
		keys = pygame.key.get_pressed()

		if keys[pygame.K_F3]:

			self.debugMode = not self.debugMode

		self.UpdateDebugLog(event)
		self.HandleExitEvents(event)

	def HandleExitEvents(self, event: pygame.event.Event) -> None:

		if event.type == pygame.QUIT:

			self.Exit()

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_ESCAPE:

				self.Exit()
	
	def Update(self) -> None:
			
		pass

	def Draw(self):

		if self.debugMode:
				
			for text in self.debugModeLog:
				
				text.Draw(self.window)

		pygame.display.update()

	def Exit(self) -> None:

		self.isRunning = False
		sys.exit()

"""

	FullScreen
	CenterWindow
	SetCursorVisible
	SetCursorImage
	PlaySound
	SetVolume

	infoObject = pygame.display.Info()
	infoObject.current_w, infoObject.current_h

	@staticmethod
	def PlaySound(channel: int, soundPath: SoundPath, volume: float, loops=0) -> None:

		mixer.Channel(channel).play(mixer.Sound(soundPath), loops)
		Application.SetVolume(channel, volume)

	@staticmethod
	def SetVolume(channel: int, volume: float):

		if volume < 0:

			volume = 0

		if volume > 1:

			volume = 1

		mixer.Channel(channel).set_volume(volume)

	def CenterWindow(self) -> None:

		os.environ['SDL_VIDEO_CENTERED'] = '1'

	def SetBackgorundColor(self, colors: list = {}) -> None:

		self.backgroundColors = colors

	def SetCursorVisible(self, value=True) -> None:

		pygame.mouse.set_visible(value)

	def SetCursorImage(self, image: Object) -> None:

		self.cursor = image


"""