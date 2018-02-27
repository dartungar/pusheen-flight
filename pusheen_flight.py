import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from pusheen import Pusheen
from clouds import Cloud
from food import Food

def run_game():
	'''запускаем игру.
		инициализируем пушина, постельку и вкусняшки.
		запускаем главный процесс'''
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(
		(settings.screen_width, settings.screen_height)
		)
	pygame.display.set_caption('Pusheen Defence!')	
	
	# создаем Пушина!
	pusheen = Pusheen(screen, settings)
	
	# создаем вкусняшку
	foods = Group(gf.create_random_food(screen, settings))
	
	# создаем облака
	clouds = Group(Cloud(screen, settings))
	
	# задаем цвет фона
	bg_color = settings.bg_color
	
	
	#начинаем главный процесс игры.
	timer = 0
	while True:
		# считаем секунды. сделай нормальный таймер!
		timer += 1
		if timer % (1500 / settings.speed) == 0:
			cloud = Cloud(screen, settings)
		if timer % (1500 / settings.speed) == 0:
			food = gf.create_random_food(screen, settings)
					
		gf.check_events(pusheen)
		#gf.check_for_food(screen, pusheen, food)
		#if pusheen.is_fed:
			#food = gf.create_random_food(screen, settings)
			#pusheen.is_fed = False
		for cloud in clouds:
			cloud.update(settings)
		for food in foods:
			food.update(settings)
		pusheen.update(settings)
		gf.update_screen(settings, screen, pusheen, foods, clouds)
		
run_game()
