import numpy as np
import pygame
import time

'''
Welcome to my version of snake in python!
'''


background_color = (30,30,30)
(width, height) = (1020,612)
block_size = 50
head_color = (255,0,0)
grid_color =  (67,67,67)
y_loc = np.random.randint(0,height/block_size - 2)
x_loc = np.random.randint(0,(width/block_size - 2))
food_color = (0,255,0)
x_food = np.random.randint(0,((width/block_size) - 2))
y_food = np.random.randint(0,(height/block_size) - 2)
latest_input = 0
snake_tail_lix = []
snake_tail_liy= []
food_count = 0

class Screen:
	'''
	This class takes in parameters regarding displaying such as bg color,
	height and width in pixels and grid size. (block size)
	'''
	def __init__(self):
		self.background_color = (0,0,0)
		self.width = width
		self.height = height
		self.block_size = block_size

	def disp_screen():
		screen = pygame.display.set_mode((width,height))
		pygame.display.set_caption('Snake game')
		screen.fill(background_color)		
		return screen


	def grid_disp(screen):
		for y in range(height):
			for x in range(width):
				rect = pygame.Rect(x*(block_size+1),y*(block_size+1),block_size,block_size)
				pygame.draw.rect(screen, (grid_color), rect)
				

class Snake_head:
	'''
	Snae_head is the class were all changes regarding the 'head' of the snake. It takes in parameters such as which 
	position/location (x_loc, y_loc), event (keayboard inputs)
	'''
	def __init__(self,x_loc,y_loc,event):
		self.x_loc = x_loc
		self.y_loc = y_loc
		self.event = event
	


	def draw_head(x_loc,y_loc):
		rect = pygame.Rect(x_loc*(block_size+1), y_loc*(block_size+1), block_size, block_size)
		pygame.draw.rect(screen, head_color, rect)


	'''
	Moving the head is based on a point system whereas each block, which the game is made of, represents
	a point. For example the method right below, if key down is pushed then the head moves down a block
	and if it has reached the bottom of the screen it returns to the top. 
	'''
	def move_head_y(self):

		if self.event == pygame.K_DOWN:
			if y_loc < (height/block_size-2):
				return 1
			else:
				return -11

		if self.event == pygame.K_UP:
			if y_loc > 0:
				return (-1)
			else:
				return 11
		else:
			return 0


	def move_head_x(self):
		if self.event == pygame.K_LEFT:
			if x_loc > 0:	
				return -1
			else:
				return 19
		if self.event == pygame.K_RIGHT:
			if x_loc < (width/block_size-2):
				return 1
			else:
				return -19
		else:
			return 0

def snake_tail(addx,addy,foodx,foody):
	'''
	In the function snake_tail a 'memory' of past locations of the head is created (respectivly for y-
	and x-axis). 
	'''
	if len(snake_tail_lix) <= 241:
		snake_tail_lix.insert(0,addx)	
		snake_tail_liy.insert(0,addy)

	else:
		snake_tail_lix[-1] = []
		snake_tail_liy[-1] = []
		snake_tail_lix.insert(0,addx)	
		snake_tail_liy.insert(0,addy)

def disp_tail(snake_tail_lix,snake_tail_liy,food_count):
	'''
	The display_tail function is made up with a for-loop that pairs the x- and y-coordinates from the memory.
	Which values that is supposed to be called back is determined by the 'food-count' whis is the amount of 'food'
	the snake has eaten. The count is happening in the game loop.
	'''
	
	if len(snake_tail_lix[0:food_count]) >= 0:
		for num in range(food_count):
			rect = pygame.Rect(snake_tail_lix[num+1]*(block_size+1), snake_tail_liy[num+1]*(block_size+1), block_size, block_size)
			pygame.draw.rect(screen, head_color, rect)
		

def detect_tail():
	'''
	detect_tail is a function that detects if the head is any of the x- or y-positions of the tail.
	'''
	if len(snake_tail_lix[0:food_count]) >= 0:
		for num in range(food_count):
			if ((x_loc == snake_tail_lix[num+1]) and (y_loc == snake_tail_liy[num+1])) == True:
				print('You are dead')


class Food:
	def __init__(self):
		pass

	def spawn_food(x_food,y_food):
		rect = pygame.Rect(x_food*(block_size+1), y_food*(block_size+1), block_size, block_size)
		pygame.draw.rect(screen, food_color, rect)



screen = Screen.disp_screen()
screen

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:

			#latest input key is the direction the snake will move in and move in that direction each time the 
			#ticks uppdate.
			latest_input = event.key
			head = Snake_head(x_loc,y_loc,latest_input)	

	if (x_food == x_loc) and (y_food == y_loc):

		#The counting of how many 'food' the snake has eaten takes place here.
		food_count += 1
		if len(snake_tail_lix[0:food_count]) >= 0:
			'''
			This part of the code detects if the food is in the same location as the head or
			in the same place as the tail and relocate the food if it happens to be in the same location
			as eather the head or tail.
			'''
			for num in range(food_count):
				while ((x_food == x_loc) and (y_food == y_loc) or ((x_food == snake_tail_lix[num]) and (y_food == snake_tail_liy[num]))) == True:
					y_food = np.random.randint(0,(height/block_size - 2))
					x_food = np.random.randint(0,(width/block_size - 2))


	detect_tail()	
	head = Snake_head(x_loc,y_loc,latest_input)
	screen = Screen.disp_screen()
	Snake_head.draw_head(int(x_loc),int(y_loc))
	snake_tail(x_loc,y_loc,x_food,y_food)
	disp_tail(snake_tail_lix,snake_tail_liy,food_count)
	Food.spawn_food(x_food,y_food)
	pygame.display.flip()
	y_loc += int(head.move_head_y())
	x_loc += int(head.move_head_x())

	clock = pygame.time.Clock()
	clock.tick(6)


'''
I hope you have had a great time reading my first project, you may use the code how ever you see fit
and I´d be glad to help aswell as recieve constructive feedback about my code. 
'''
		