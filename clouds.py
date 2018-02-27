import pygame
import random
import settings
from pygame.sprite import Sprite

class Cloud(Sprite):
	'''Облака, которые движутся на фоне,
		создавая иллюзию движения.'''
		
	def __init__(self, screen, settings):
		'''Инициализируем облака'''
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load(
						random.choice(settings.cloud_img))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.right
		self.rect.centery = random.randint(
						self.screen_rect.top, 
						self.screen_rect.bottom)
		
		# для дробных значений скорости
		self.centerx = float(self.rect.centerx)
						
	def update(self, settings):
		self.centerx -= settings.speed
		self.rect.centerx = self.centerx
						
	def blitme(self):
		''' рисуем облако в текущей локации '''
		self.screen.blit(self.image, self.rect)
