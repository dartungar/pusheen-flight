import sys
import pygame
import random
from food import Food
from clouds import Cloud

def check_move_events(event, pusheen, flag):
	'''Ставим флаги движения 
		в соответствии с нажатием\отпущением кнопок'''
	if event.key == pygame.K_UP:
		pusheen.moving_up = flag
	if event.key == pygame.K_DOWN:
		pusheen.moving_down = flag
		

def check_events(pusheen):
	'''Реагируем на нажатия клавиш и движения мышкой.'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()		
		elif event.type == pygame.KEYDOWN:
			check_move_events(event, pusheen, True)				
		elif event.type == pygame.KEYUP:
			check_move_events(event, pusheen, False)
			
			
def get_random_y_coordinates(screen):
	'''случайные координаты в границе экрана (но не слишком близко)'''
	screen_rect = screen.get_rect()
	border = 20
	x = screen_rect.right + 200
	y = random.randint(border, screen_rect.bottom - border)
	coordinates = (x, y)
	return coordinates
	
			
def create_random_food(screen, settings):
	'''Создаем вкусняшку в случайном месте на экране'''
	coordinates = get_random_y_coordinates(screen)
	food = Food(screen, settings, coordinates)
	return food
	
def check_for_food(screen, pusheen, food):
	'''Проверяем на коллизию с вкусняшкой'''
	if pusheen.rect.colliderect(food):
		pusheen.eat_food(food)

def update_screen(settings, screen, pusheen, foods, clouds):
	'''Перерисовываем экран и делаем его видимым'''
	# перерисовываем экран заново на каждой итерации цикла
	screen.fill(settings.bg_color)
	for food in foods.sprites():
		food.blitme()
	for cloud in clouds.sprites():
		cloud.blitme()	
	
	pusheen.blitme()					
	# делаем новейший нарисованный экран видимым 
	#(обновляем картинку)
	pygame.display.flip()
