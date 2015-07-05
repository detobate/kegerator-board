import wiiboard
import pygame
import time
import os
import sys

os.environ["SDL_VIDEODRIVER"] = "dummy"

# Keg calibration in kg
CORNIE_EMPTY = 1.78
CORNIE_FULL = 21.8

def main():
	board = wiiboard.Wiiboard()

	pygame.init()
	
	address = board.discover()
	board.connect(address) #The wii board must be in sync mode at this time

	time.sleep(0.2)
	board.setLight(True)
	done = False

	while (not done):
		time.sleep(0.05)
		for event in pygame.event.get():
			if event.type == wiiboard.WIIBOARD_MASS:
				if (event.mass.totalWeight > 1):   
					print "Total weight: " + `event.mass.totalWeight` + ". Top left: " + `event.mass.topLeft` + ". Top Right: " + `event.mass.topRight`
					print "Total weight: " + `event.mass.totalWeight` + ". Bottom left: " + `event.mass.bottomLeft` + ". Bottom Right: " + `event.mass.bottomRight`

	board.disconnect()
	pygame.quit()

#Run the script if executed
if __name__ == "__main__":
	main()
