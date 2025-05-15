import pygame
from pygame.locals import *
import time
import button

quitPressed = False


class menu():
    def __init__(self, surface, fullscreen):
        self.surface = surface
        self.fullscreen = fullscreen

        self.checkbox_unticked_img = pygame.image.load('resources/checkbox_unTicked.png').convert_alpha()
        self.checkbox_ticked_img = pygame.image.load('resources/checkbox_ticked.png').convert_alpha()

        if self.fullscreen == True:
            self.full_screen_checkBox = button.Button(120,150, self.checkbox_ticked_img, 0.3)
        else:
            self.full_screen_checkBox = button.Button(120,150, self.checkbox_unticked_img, 0.3)

        self.screenWidth,self.screenHeight = pygame.display.get_window_size()
        
    
    def displayText(self, font_name, font_size, message, color, posX, posY):
        font =  pygame.font.Font(font_name, font_size)
        message_to_display = font.render(str(message),True,color)
        self.surface.blit(message_to_display,(posX,posY))

    def run(self):
        running = True
        global quitPressed

        while running:
            self.surface.fill((255,255,255))

            #drawing buttons from button class and checking if clicked
            if self.full_screen_checkBox.draw(self.surface):
                if self.fullscreen == False:
                    self.fullscreen = True
                    self.full_screen_checkBox = button.Button(120,150, self.checkbox_ticked_img, 0.3)
                    #print("full screen pos "+str(pygame.mouse.get_pos()))
                    pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                    pygame.mouse.set_pos(0,0)
                elif self.fullscreen == True:
                    self.fullscreen = False
                    self.full_screen_checkBox = button.Button(120,150, self.checkbox_unticked_img, 0.3)
                    #print("small screen pos "+str(pygame.mouse.get_pos()))
                    pygame.display.set_mode((self.screenWidth,self.screenHeight))
                    pygame.mouse.set_pos(0,0)
                time.sleep(0.1)

            

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        #print("exiting options menu")
                        running = False
                    
                elif event.type == QUIT:
                    running = False
                    quitPressed = True

            self.displayText("RoadRage.ttf",20,"*Note: This menu is in beta and options mayn not work as intended!", (0,0,0), 0, 20)
            self.displayText("RoadRage.ttf", 25, "Full Screen: ", (18, 156, 16),30, 150)

            pygame.display.update()