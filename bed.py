import pygame

class Bed():
	'''Постелька. Восстанавливает котучую энергию'''
	
	def __init__(self, screen, settings):
		'''Инициализируем постельку'''
		self.screen = screen
		self.image = pygame.image.load(settings.bed_img)
		
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# создаем кроватку в верхнем правом углу
		self.rect.right= self.screen_rect.right
		self.rect.top = self.screen_rect.top
		
		
	def blitme(self):
		'''Рисуем Кроватку в его текущей локации.'''
		self.screen.blit(self.image, self.rect)
	
		
