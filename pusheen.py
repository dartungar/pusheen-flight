import pygame
import settings
import game_functions as gf

class Pusheen():

	
	def __init__(self, screen, settings):
		'''Инициализируем Пушина и задаем его стартовую позицию
			и другие атрибуты'''
		self.screen = screen
		
		# загружаем картинку-Пушина и получаем его габариты (rect)
		
		self.image = pygame.image.load(settings.pusheen_img_left)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# создаем пушина внизу экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# сохраняем дробные значения для координатов, 
		# чтобы работали дробные параметры для скорости
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		# задаем уровень котучести
		self.energy_level = 100
		self.hunger_level = 1
		self.is_fed = False
		self.is_sleeping = False
		self.velocity = 0.3
		
		
		# флаги движения
		self.moving_up = False
		self.moving_down = False
		self.floating_up = False
		self.floating_down = False
		self.floating_altitude = 0
		self.float_direction = 0
		
	def eat_food(self, food):
		self.hunger_level = 1
		# потом сделать увязку с калориями
		self.is_fed = True
		del food
		
	def update(self, settings):
		'''мастер-обновление всего.'''
		self.update_floating(settings)
		self.update_position()
		self.update_image(settings)
		
	def update_floating(self, settings):
		'''заставляем Пушина немного парить в воздухе'''
		
		if self.floating_altitude == 0:
			self.floating_up = True
			self.floating_down = False
			self.float_direction = 1
		if self.floating_altitude == settings.ambient_floating_range:
			self.floating_up = False
			self.floating_down = True
			self.float_direction = -1
		self.floating_altitude += self.float_direction

		
	def update_position(self):
		'''обновляем координаты и позицию на их основе'''
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.velocity
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.velocity
		if self.floating_up:
			self.centery -= self.velocity / 5
		if self.floating_down:
			self.centery += self.velocity / 5
			
		# обновляем позицию на основе координат
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def update_image(self, settings):
		'''разворачиваем пушина в зависимости от направления.'''
		# обновляем картинку. TODO
		
	def blitme(self):
		'''Рисуем Пушина в его текущей локации.'''
		self.screen.blit(self.image, self.rect)
		
		
