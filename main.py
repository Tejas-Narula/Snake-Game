import pygame
from pygame.locals import *
import button
import game
import options

BACKGROUND_COLOR = (136,217,247)
fullscreen = False

if fullscreen == True:
  screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
else:
  SCREEN_HEIGHT = 800
  SCREEN_WIDTH = 1000
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
SCREEN_WIDTH,SCREEN_HEIGHT = pygame.display.get_window_size()
#print(str(SCREEN_WIDTH)+" "+str(SCREEN_HEIGHT))

pygame.display.set_caption('Snake Game')
screen.fill((BACKGROUND_COLOR))

class Menu:
  def __init__(self,menu_screen_width,menu_screen_height):
    self.SCREEN_WIDTH,self.SCREEN_HEIGHT = menu_screen_width,menu_screen_height
    self.main_menu_running = True

    #load title image
    self.title_img = pygame.image.load('resources/snake-game-poster2.png').convert_alpha()

    #load button images
    self.start_img = pygame.image.load('resources/start_btn.png').convert_alpha()
    self.options_img = pygame.image.load('resources/option_button.png').convert_alpha()
    self.exit_img = pygame.image.load('resources/exit_button.png').convert_alpha()

    #create button instances
    self.start_button = button.Button(SCREEN_WIDTH/2-139, SCREEN_HEIGHT/2-120, self.start_img, 0.8)
    self.options_button = button.Button(SCREEN_WIDTH/2-139, SCREEN_HEIGHT/2+0, self.options_img, 0.8)
    self.exit_button = button.Button(SCREEN_WIDTH/2-139, SCREEN_HEIGHT/2+120, self.exit_img, 0.8)
  
  def displayText(self, font_name, font_size, message, color,Textposition):
        font =  pygame.font.Font(font_name, font_size)
        message_to_display = font.render(str(message),True,color)
        screen.blit(message_to_display,Textposition)

  def main_menu(self):
    while self.main_menu_running:

      screen.fill((BACKGROUND_COLOR))
      screen.blit(self.title_img,(self.SCREEN_WIDTH/2-391,70))
      
      #button functionality
      if self.start_button.draw(screen):
        screen.fill((255,255,255))
        Game.run()
      elif self.options_button.draw(screen):
        #print("Opening options menu!")
        Options.run()
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = pygame.display.get_window_size()
      elif self.exit_button.draw(screen):
        self.main_menu_running = False

      if game.quitPressed == True or options.quitPressed == True:
        self.main_menu_running = False

      #event handler
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            self.main_menu_running = False
        if event.type == pygame.QUIT:
          self.main_menu_running = False
      
      self.start_button = button.Button(self.SCREEN_WIDTH/2-139, self.SCREEN_HEIGHT/2-120, self.start_img, 0.8)
      self.options_button = button.Button(self.SCREEN_WIDTH/2-139, self.SCREEN_HEIGHT/2+0, self.options_img, 0.8)
      self.exit_button = button.Button(self.SCREEN_WIDTH/2-139, self.SCREEN_HEIGHT/2+120, self.exit_img, 0.8)

      self.displayText("RoadRage.ttf",30,"@Tejas Narula", (255,255,255),(self.SCREEN_WIDTH-130, self.SCREEN_HEIGHT-30))
      pygame.display.update()


if __name__ == "__main__":
  Game = game.play_game(screen)
  Bot = None
  Options = options.menu(screen,fullscreen)
  Menu(SCREEN_WIDTH,SCREEN_HEIGHT).main_menu()