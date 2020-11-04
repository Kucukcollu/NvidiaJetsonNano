import pygame

pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

# Prints the joystick's name
JoyName = pygame.joystick.Joystick(0).get_name()
print("Name of the joystick: ")
print(JoyName)

# Gets the number of axes
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print("Number of axis:")
print(JoyAx)

JoyAy = pygame.joystick.Joystick(0).get_numaxes()
print("Number of axis:")
print(JoyAy)

# Prints the values for axis0
while True:
	pygame.event.pump()
	answer = pygame.joystick.Joystick(0).get_axis(0)
	print(answer)
	if answer < 0:
		print("SOLA DÖN!")
	if answer > 0:
		print("SAĞA DÖN!")
