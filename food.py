import pygame
import random
from pygame.sprite import Sprite

class Food(Sprite):
	'''Вкусняшки. Дают Пушину очки, но уменьшают энергию'''
	
	def __init__(self, screen, settings, coordinates):
		'''Инициализируем вкусняшку'''
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.image = pygame.image.load(random.choice(settings.food_img))
		
		self.rect = self.image.get_rect()
		
		# создаем вкусняшку по заданным координатам
		self.rect.center = coordinates
		
		# задаем пищевую ценность
		self.calories = 50
	
	# для дробных значений скорости
		self.centerx = float(self.rect.centerx)
	
	def update(self, settings):
		self.centerx -= settings.speed
		self.rect.centerx = self.centerx
		
	def blitme(self):
		'''Рисуем вкусняшку в ее текущей локации.'''
		self.screen.blit(self.image, self.rect)	
	# вкусняшки исчезают, после того как их съел пушин
	
		
