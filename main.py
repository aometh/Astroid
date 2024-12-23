import pygame
from constants import *
from player import *
def main():
	pygame.init()
	gameTime = pygame.time.Clock()
	dt = gameTime.tick(60) / 1000.0 
	framerate = 60

	black = (0,0,0)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)


	while 1 == 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(black)
		player.draw(screen)
		player.update(dt)
		pygame.display.flip()
		gameTime.tick(60)
		
		
		
		
	

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__== "__main__":
	main()