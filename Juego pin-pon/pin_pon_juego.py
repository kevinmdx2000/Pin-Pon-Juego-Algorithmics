from pygame import *

#CLASE PRINCIPAL
class GameSprite(sprite.Sprite):
        #constructor de clase
        # FUNCIÓN QUE ME SIRVE PARA CARGAR LA IMAGEN DEL SPRITE CON SUS DIMENSIONES Y POSICIÓN
        def __init__(self,player _image,player_x, player_y, player_speed, width, height):
            self.image = transform.scale(image.load(player_image),(width,heigth))
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


