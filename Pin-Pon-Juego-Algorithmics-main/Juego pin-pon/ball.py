from pygame import *

#CLASE PRINCIPAL
class GameSprite(sprite.Sprite):
        #constructor de clase
        # FUNCIÓN QUE ME SIRVE PARA CARGAR LA IMAGEN DEL SPRITE CON SUS DIMENSIONES Y POSICIÓN
        def __init__(self,player_image,player_x, player_y, player_speed, width, height):
            super().__init__()
            self.image = transform.scale(image.load(player_image),(width,height))
            self.speed = player_speed

            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

        #Mostrar o dibujar el sprite en la pantalla
        def reset(self):
            window.blit((self.image),(self.rect,self.rect.y))


#MOVIMIENTO DE LAS BARRAS
class Player(GameSprite):
 def update_r(self):
          keys = key.get_pressed()
          if keys[K_UP] and self.rect.y > 5:
               self.rect.y -= self.speed
          if keys[K_DOWN] and self.rect.y < win_height - 80:
               self.rect.y += self.speed

        #MOVER PLAYER RAQUETA IZQUIERDA
def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_w] and self.rect.y < win_height - 80:
                self.rect.y += self.speed

    #Definir variables de pantalla

back=(200,255,255) #color de fondo
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

#Banderas responsables del estado del juego
game = True
finish = False
clock = time.Clock()
FPS = 60

#Creación  de la pelota y las paletas
racket1 = Player ('racket.png', 30, 200, 4, 50, 150)
racket2 = Player ('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('¡EL JUGADOR 1 PIERDE!' , True, (180,0,0))
lose2 = font.render('EL JUGADOR 2 PIERDE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
     for e in event.get():
        if e.type == QUIT:
            game = False

    
        if finish != True:
            window.fill(back)
            racket1.update_l()
            racket2.update_r()
            ball.rect.x += speed_x
            ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
                speed_x *=-1
                speed_y *=1

        #si la pelota alcanza los bordes de la pantalla cambiar de dirección
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
             speed_y *= -1

        #Sí la pelota va mas alla de la paleta , mostrar la condición de derrota al jugador1
        if ball.rect.x < 0:
             finish = True
             window.blit(lose1, (200, 200))
             game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

            racket1.reset()
            racket2.reset()
            ball.reset()





    
display.update()
clock.tick(FPS)









