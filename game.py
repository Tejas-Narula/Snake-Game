import pygame
from pygame.locals import *
import time
import random

import highscore

quitPressed = False
size = 40
clock = pygame.time.Clock()
fps = 10


SCREEN_WIDTH = 1
SCREEN_HEIGHT = 1

#apple class
class Apple:
  def __init__(self, parent_screen):
    self.apple = pygame.image.load("resources/apple.png")
    self.parent_screen = parent_screen
    self.move()
  def draw(self):
    self.parent_screen.blit(self.apple,(self.x,self.y))

  def move(self):
    self.x = random.randint(0,int(SCREEN_WIDTH/size)-1)*size
    self.y = random.randint(0,int(SCREEN_HEIGHT/size)-1)*size
    

class Snake:
  def __init__(self, parent_screen, length):
    #snakeBody Graphics
    self.head_down_img = pygame.image.load("resources\snakeBody\head_down.png")
    self.head_up_img = pygame.image.load("resources\snakeBody\head_up.png")
    self.head_left_img = pygame.image.load("resources\snakeBody\head_left.png")
    self.head_right_img = pygame.image.load("resources\snakeBody\head_right.png")

    self.tail_down_img = pygame.image.load("resources\snakeBody\\tail_down.png")
    self.tail_up_img = pygame.image.load("resources\snakeBody\\tail_up.png")
    self.tail_left_img = pygame.image.load("resources\snakeBody\\tail_left.png")
    self.tail_right_img = pygame.image.load("resources\snakeBody\\tail_right.png")

    self.body_horizontal_img = pygame.image.load("resources\snakeBody\\body_horizontal.png")
    self.body_vartical_img = pygame.image.load("resources\snakeBody\\body_vertical.png")

    self.body_turn1_img = pygame.image.load("resources\snakeBody\\body_bl.png")
    self.body_turn2_img = pygame.image.load("resources\snakeBody\\body_br.png")
    self.body_turn3_img = pygame.image.load("resources\snakeBody\\body_tl.png")
    self.body_turn4_img = pygame.image.load("resources\snakeBody\\body_tr.png")

    self.snake_img = pygame.image.load("resources\\block.jpg")

    self.length = length
    self.parent_screen = parent_screen
    self.image = pygame.image.load("resources/block.jpg").convert()
    self.x = [size] * self.length
    for i in range(self.length):
      self.x[i] = self.x[i] + (i * 40)
    self.y = [size] * self.length
    self.direction = []
    for i in range (self.length):
      self.direction.append("down")
    self.block = self.image
    self.moved = False

  def increase_length(self):
    self.length += 1
    self.x.append(-1)
    self.y.append(-1)
    self.direction.append(self.direction[-1])

  def draw(self):
    #draw body
    for i in range(self.length):
      if i == 0:
        #draw head
        if self.direction[0] == "down":
          self.parent_screen.blit(self.head_down_img,(self.x[0],self.y[0]))
        elif self.direction[0] == "up":
          self.parent_screen.blit(self.head_up_img,(self.x[0],self.y[0]))
        elif self.direction[0] == "left":
          self.parent_screen.blit(self.head_left_img,(self.x[0],self.y[0]))
        elif self.direction[0] == "right":
          self.parent_screen.blit(self.head_right_img,(self.x[0],self.y[0]))
        else:
          pass
      elif i == self.length - 1:

        #draw tail
        if self.direction[-1] == "down":
          self.parent_screen.blit(self.tail_down_img,(self.x[-1],self.y[-1]))
        elif self.direction[-1] == "up":
          self.parent_screen.blit(self.tail_up_img,(self.x[-1],self.y[-1]))
        elif self.direction[-1] == "left":
          self.parent_screen.blit(self.tail_left_img,(self.x[-1],self.y[-1]))
        elif self.direction[-1] == "right":
          self.parent_screen.blit(self.tail_right_img,(self.x[-1],self.y[-1]))
        else:
          pass
      else:
        #draw rest of the body
        if self.direction[i] == "down" or self.direction[i] == "up":
          self.parent_screen.blit(self.body_vartical_img,(self.x[i],self.y[i]))
        elif self.direction[i] == "right" or self.direction[i] == "left":
          self.parent_screen.blit(self.body_horizontal_img,(self.x[i],self.y[i]))
  
  def drawbasic(self):
    for i in range(self.length):
      self.parent_screen.blit(self.snake_img,(self.x[i],self.y[i]))
    
  def move_left(self):
    if self.direction[0] != "right":
      self.direction[0] = 'left'
  
  def move_right(self):
    if self.direction[0] != "left":
      self.direction[0] = 'right'
  
  def move_up(self):
    if self.direction[0] != "down":
      self.direction[0] = 'up'
  
  def move_down(self):
    if self.direction[0] != "up":
      self.direction[0] = 'down'
  
  def walk(self):
    #print(self.direction)

    for i in range(self.length-1,0,-1):
      self.x[i] = self.x[i - 1]
      self.y[i] = self.y[i - 1]
      self.direction[i] = self.direction[i - 1]

    if self.direction[0] == 'left':
      self.x[0] -= size
    elif self.direction[0] == 'right':
      self.x[0] += size
    elif self.direction[0] == 'up':
      self.y[0] -= size
    elif self.direction[0] == 'down':
      self.y[0] += size
    # checking if snake goes outside the screen taking it to other side of screen.

    if self.x[0] >= SCREEN_WIDTH:
      self.x[0] = 0
    elif self.x[0] < 0:
      self.x[0] = SCREEN_WIDTH
    elif self.y[0] >= SCREEN_HEIGHT:
      self.y[0] = 0
    elif self.y[0] < 0:
      self.y[0] = SCREEN_HEIGHT
    
    #self.draw()
    self.drawbasic()

class play_game:
  def __init__(self,surface):
    global SCREEN_WIDTH,SCREEN_HEIGHT
    SCREEN_WIDTH,SCREEN_HEIGHT = pygame.display.get_window_size()
    
    pygame.init()
    pygame.mixer.init()

    self.surface = surface
    self.surface.fill((110,110,5))
    
    self.apple = Apple(self.surface)
    self.apple.draw()
    
    # set snake starting size and draw
    self.snake = Snake(self.surface, 3)
    self.snake.draw()
    self.moved = False

    #getting the previous best score
    self.high_score = highscore.Highscore(self.snake.length).current_HighScore

  def is_collision(self,x1,y1,x2,y2):
    if x1 >= x2 and x1 < x2 + size:
      if y1 >= y2 and y1 < y2 + size:
        return True
    return False

  def play(self):
    self.render_background()
    self.apple.draw()
    self.snake.walk()
    self.display_score()
    pygame.display.flip()

  def play_background_music(self):
    pygame.mixer.music.load("resources/bg_music.mp3")
    pygame.mixer.music.play(-1)

  def play_sound(self,sound):
    sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
    pygame.mixer.Sound.play(sound)

  def create_background(self):
    #only need to run to create s surface "background" and blit that to use it
    backGround_color = (175,215,70)
    grass_color = (167 , 209 , 61)
    
    self.background = pygame.surface.Surface(self.surface.get_size())
    self.background.fill(backGround_color)
    for row in range((int(SCREEN_HEIGHT/size)-1)*size):
      if row % 2 == 0:
        for col in range((int(SCREEN_WIDTH/size)-1)*size):
          if col % 2 == 0:
            grass_rect = pygame.Rect(col*size,row*size,size,size)
            pygame.draw.rect(self.background,grass_color,grass_rect)
      else:
        for col in range((int(SCREEN_WIDTH/size)-1)*size):
          if col % 2 != 0:
            grass_rect = pygame.Rect(col*size,row*size,size,size)
            pygame.draw.rect(self.background,grass_color,grass_rect)


  def render_background(self):
    self.surface.blit(self.background, (0,0))
  
  def display_score(self):
    font = pygame.font.Font('RoadRage.ttf', 40)
    score = self.snake.length - 3
    score_to_display = font.render(f"Score: {score} | " + f"HighScore: {self.high_score}",True,(255,255,255))
    self.surface.blit(score_to_display, (SCREEN_HEIGHT/2-50,3))

    #Snake colliding with apple
    if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
      self.play_sound('ding')
      self.snake.increase_length()
      #updating highscore ; +1 is beacuse we just ate the apple and score isnt updated yet!
      self.high_score = highscore.Highscore(score + 1).checkAndUpdateScore()
      self.apple.move()
    
    #snake colliding with itself
    for i in range(1,self.snake.length):
      if self.is_collision(self.snake.x[0], self.snake.y[0],self.snake.x[i],self.snake.y[i]):
        self.play_sound('crash')
        raise "Game Over!"
  
  def show_game_over(self):
    self.render_background()
    font = pygame.font.Font('RoadRage.ttf',30)
    line1 = font.render(f"Game is over! Your score is {self.snake.length}", True,(0,0,0))
    self.surface.blit(line1, (100,100))
    line2 = font.render(f"To play again press enter, To exit press escape!", True,(0,0,0))
    self.surface.blit(line2, (100,150))
    pygame.display.flip()

    pygame.mixer.music.pause()
  
  def reset(self):
    self.snake = Snake(self.surface, 3)
    self.apple = Apple(self.surface)
  
  def run(self):
    self.play_background_music()
    self.create_background()
    global SCREEN_WIDTH,SCREEN_HEIGHT
    global quitPressed
    running = True
    pause = False
    SCREEN_WIDTH,SCREEN_HEIGHT = pygame.display.get_window_size()
    global fps
    #print(pygame.display.get_window_size())

    while running:
      for event in pygame.event.get():
        #self.bot()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            pygame.mixer.music.pause()
            running = False
          
          if event.key ==K_RETURN:
            pygame.mixer.music.unpause()
            pause = False
          
          if not pause:
            if self.moved == False:
              if event.key == K_UP or event.key == K_w:
                self.snake.move_up()
                self.moved = True
              if event.key == K_DOWN or event.key == K_s:
                self.snake.move_down()
                self.moved = True
              if event.key == K_LEFT or event.key == K_a:
                self.snake.move_left()
                self.moved = True
              if event.key == K_RIGHT or event.key == K_d:
                self.snake.move_right()
                self.moved = True
        elif event.type == QUIT:
          running = False
          quitPressed = True
      try:
        if not pause: 
          self.play()
          self.moved = False
          clock.tick(fps)
      except Exception as e:
        self.show_game_over()
        pause = True
        self.reset()
      