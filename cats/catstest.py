"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 1000
screen_height= 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("For Quentin")

# load ressource images

background_image = pygame.image.load("res\\background_r.png").convert()
cat_content_image = pygame.image.load("res\\cat_content_r.png").convert()
cat_expecting_image = pygame.image.load("res\\cat_expecting_r.png").convert()
cat_meowing_image = pygame.image.load("res\\cat_meowing_r.png").convert()
cat_standing_image = pygame.image.load("res\\cat_standing_r.png").convert()
food_image = pygame.image.load("res\\food_r.png").convert()
hand_image = pygame.image.load("res\\hand_r.png").convert()
purr_sound = pygame.mixer.Sound("res\\purr.wav")


class Cat_Sprite(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
    def __init__(self):
        """ Graphic Sprite Constructor. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = cat_content_image

        # Set our transparent color
        self.image.set_colorkey(WHITE)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class Player_Sprite(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
    def __init__(self):
        """ Graphic Sprite Constructor. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = hand_image

        # Set our transparent color
        self.image.set_colorkey(WHITE)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

# Hide the mouse cursor
pygame.mouse.set_visible(0)


cat1 = Cat_Sprite()
def relocate_cat():
    cat1.rect.x = random.randrange(screen_width)
    cat1.rect.y = random.randrange(screen_height)



# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Create a RED player block
player = Player_Sprite()
all_sprites_list.add(player)

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
cat_list = pygame.sprite.Group()
cat_list.add(cat1)
all_sprites_list.add(cat1)


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background_image, [0, 0])

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]-50
    player.rect.y = pos[1]-50

    # See if the player block has collided with anything.
    cats_hit_list = pygame.sprite.spritecollide(player, cat_list, True)

    # Check the list of collisions.
    for cat in cats_hit_list:
        purr_sound.play()
        print("purr!")
        relocate_cat()
        cat_list.add(cat1)
        all_sprites_list.add(cat1)


    # Draw all the spites
    all_sprites_list.draw(screen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()