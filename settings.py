class Settings():
	'''Класс со всеми настройками Pusheen Flight'''
	
	def __init__(self):
		'''Инициализируем настройки игры'''
		# настройки экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (160, 226, 255)
		
		# скорость движения экрана
		self.speed = 0.2
		
		# радиус парения и скорость
		self.ambient_floating_range = 3000
		self.ambient_floating_speed = 0.2
		
		
		# картинки для пушина
		self.pusheen_img_left = 'resources\\pusheens.png'
		
		# картинки для облаков
		self.cloud_img = [
						'resources\\cloud01.png',
						'resources\\cloud02.png',
						'resources\\cloud03.png',
						'resources\\cloud04.png',
						]
		
		# картинки для вкусняшек
		self.food_img = [
						'resources\\cupcake1.png',
						'resources\\cupcake2.png',
						'resources\\cake1.png',
						'resources\\cake2.png',
						]
