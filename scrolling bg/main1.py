import pygame
import os

pygame.init()
font = pygame.font.Font(None, 30)
direction = 'right'
direction1 = "right"
smash = 'smash'
lives = 5
x, y = 100, 300
def play():
    pygame.mixer.music.load(os.path.join("Mustard_ft_Roddy_Ricch_-_Ballin.mp3"))
    pygame.mixer.music.play(loops=0)

clock = pygame.time.Clock()
FPS = 60
black = (0,0,0)
white = (255, 255, 255)
red  = ( 255, 0, 0)
#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432
monkey = pygame.image.load("kong right.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monkey Mash")
jumping = False
Y_GRAVITY = 1
JUMP_HEIGHT = 25
Y_VELOCITY = JUMP_HEIGHT
JUMPING = pygame.image.load('kong smash.png')
STANDING = pygame.image.load('kong right.png')
kong_rect = STANDING.get_rect(center=(x, y))

#define game variables
scroll = 0
goomba_scroll = 900
enemy_scroll = 0


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y, direction, smash):
        
        self.bleh = 0
        self.animation_loop = 0
        
        self.direction = 'right'
        
        self.x = x
        self.y = y + 30
        self.lives = lives
          
        if self.direction == 'right':
          self.image = pygame.image.load(os.path.join('kong right.png')).convert()
        self.image = pygame.transform.scale(self.image, (150, 150))
        
        self.rect = self.image.get_rect()
        self.rect.center=(self.x, self.y)
        self.image.set_colorkey(black)
        self.enemy_count = 0

        

    def animation(self):
      self.left_amimation = [
        pygame.image.load("kong run left.png"),
        pygame.image.load('kong run left2.png')
      ]

      self.right_amimation = [
        pygame.image.load("kong run.png"),
        pygame.image.load('kong run2.png')
      ]

    def update(self):
   
      


      
      
      

      self.animation()

      if self.direction == 'left':
        self.bleh += 1
        if self.bleh % 5 == 0:
          self.image = self.left_amimation[self.animation_loop]
          self.animation_loop += 1

      if self.direction == 'right':
        self.bleh += 1
        if self.bleh % 5 == 0:
          self.image = self.right_amimation[self.animation_loop]
          self.animation_loop += 1
      if self.animation_loop >= 2:
        self.animation_loop = 0
      self.image = pygame.transform.scale(self.image, (200, 200))
      screen.blit(self.image, (self.x, self.y - 65))
    

      if self.enemy_count <= 500:
        self.enemy_count +=1
        goomba = Player1(300 + self.enemy_count*500, 360, direction1)
        goomba.rect.x -= enemy_scroll

        
        goomba_group.add(goomba)

      
        




class Player1(pygame.sprite.Sprite):
    def __init__(self, x1, y1, direction1):
        pygame.sprite.Sprite.__init__(self)

        self.enemy_count = 0
        self.lives = lives
        self.direction1 = direction1
        if direction1 == 'left':
          self.image = pygame.image.load(os.path.join('goomba left.png')).convert()
        if direction1 == 'right':
          self.image = pygame.image.load(os.path.join('goomba right.png')).convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.x1 = x1
        self.y1 = y1
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x1, self.y1)
        self.image.set_colorkey(black)

    def update(self):
      self.rect.x -= enemy_scroll
      if self.rect.x - 140 == player.rect.x and player.y >= 255:
        player.lives -= 1
ground_image = pygame.image.load("ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 4): 
  bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
  
  bg_image = pygame.transform.scale(bg_image, (800, 402))
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(800):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.2

def draw_ground():
  for x in range(4444):
    screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT + 20 - ground_height))

player = Player(x,y, direction, smash)

goomba_group = pygame.sprite.Group()


#game loop
run = True
while run:
  text = font.render('lives Left:' + str(player.lives), True,white)
  if player.lives == 0:
    pygame.quit()
  

  enemy_scroll = 5

  scroll += 20
  goomba_scroll -=10

  if scroll <= 0:
   scroll =0

  clock.tick(FPS)

  #draw world
  draw_bg()
  draw_ground()
  goomba_group.update()
  goomba_group.draw(screen)
  screen.blit(text, (300, 10))


  
  player.update()
  Player1(x,y,'left')

 
  

  #get keypresses
  key = pygame.key.get_pressed()
  if key[pygame.K_a] and scroll > 200:
    scroll -= 5
  if key[pygame.K_d] and scroll < 70000500:
    scroll += 5
  if key[pygame.K_a]:
    player.direction = 'left'
    scroll -= 5
  if key[pygame.K_d]: 
    player.direction = 'right'
    scroll += 5
  if key[pygame.K_SPACE]:
    smash = 'smash'
    player.direction = ''
  if key[pygame.K_q]:
    play()
   

  if key[pygame.K_w]:
    jumping = True

  if jumping:
    player.y -= Y_VELOCITY
    Y_VELOCITY -= Y_GRAVITY
    if Y_VELOCITY < - JUMP_HEIGHT:
      jumping = False
      Y_VELOCITY = JUMP_HEIGHT
    kong_rect = JUMPING.get_rect(center=(x, y))


    
  else:
    kong_rect = STANDING.get_rect(center=(x, y))

#event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    font = pygame.font.Font(None, 30)
    

  pygame.display.flip()
  clock.tick(FPS)

  pygame.display.update()

 
pygame.quit()