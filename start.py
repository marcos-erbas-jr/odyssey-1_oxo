import pygame

pygame.init()
screen = pygame.display.set_mode((310,310))
clock = pygame.time.Clock()
running = True
list_cross = []
list_circle = []
list_positions = []
list_positionsX = []
list_positionsO = []
coordenadas = [(45.0, 45.0),(145.0, 45.0),(245.0, 45.0),(45.0, 145.0),(145.0, 145.0),(245.0, 145.0),(45.0, 245.0),(145.0, 245.0),(245.0, 245.0)]
player = "cross"
play = 0

dt = 0
x = (screen.get_width()/2)-10
y = (screen.get_height()/2)-10
def backgroung():
    screen.fill((0, 0, 0))  # RGB - BLACK 0,0,0

    # game's Background containment
    pygame.draw.line(screen, "white", (10, 10), (300, 10), 5)
    pygame.draw.line(screen, "white", (10, 10), (10, 300), 5)
    pygame.draw.line(screen, "white", (10, 300), (300, 300), 5)
    pygame.draw.line(screen, "white", (300, 10), (300, 300), 5)

    # game's Background lines
    pygame.draw.line(screen, "white", (10, 100), (300, 100), 5)
    pygame.draw.line(screen, "white", (10, 200), (300, 200), 5)
    pygame.draw.line(screen, "white", (100, 10), (100, 300), 5)
    pygame.draw.line(screen, "white", (200, 10), (200, 300), 5)
    

def crossdraw(posx, posy, list, list_positions):
    if (posx, posy) in list_positions:
        return
    else:
        lista = []
        list_positions.append((posx, posy))
        for coordenada in coordenadas:
            if coordenada == (posx, posy):
                lista = list.copy()
                list.append(coordenadas.index(coordenada))
                lista.sort()
                list = lista.copy()
                lista.clear()

        posy += 5
        posx += 5
        list_cross.append((posx-20, posy-20, posx+20, posy+20, posx+20,
                            posy-20, posx-20, posy+20))
        print("coordenadas cross:",list_positionsX)

def circledraw(posx, posy, list, list_positions):
    if (posx, posy) in list_positions:
        #print('circle não feito')
        return
    else:
        lista = []
        list_positions.append((posx, posy))
        for coordenada in coordenadas:
            if coordenada == (posx, posy):
                lista = list.copy()
                list.append(coordenadas.index(coordenada))
                lista.sort()
                list = lista.copy()
                lista.clear()
        posy += 5
        posx += 5
        list_circle.append((posx, posy))
        print("coordenadas circulo:", list_positionsO)
def winner(player):
    if player == "cross":
        lista = list_positionsX.copy()
    else:
        lista = list_positionsO.copy()
    if (0 in lista and 1 in lista and 2 in lista
            or 0 in lista and 3 in lista and 6 in lista
            or 0 in lista and 4 in lista and 8 in lista
            or 3 in lista and 4 in lista and 5 in lista
            or 1 in lista and 4 in lista and 7 in lista
            or 2 in lista and 4 in lista and 6 in lista
            or 6 in lista and 7 in lista and 8 in lista
            or 2 in lista and 5 in lista and 8 in lista):
        print(f"{player.capitalize()} WIN!!")
        return 1
    else:
        lista.clear()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        backgroung()

        pygame.draw.rect(surface=screen, color="white", rect=(x,y,10,10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if y == 45:
                continue
            else:
                y -= 100
        if keys[pygame.K_DOWN]:
            if y == 245:
                continue
            else:
                y += 100
        if keys[pygame.K_LEFT]:
            if x == 45:
                continue
            else:
                x -= 100
        if keys[pygame.K_RIGHT]:
            if x == 245:
                continue
            else:
                x += 100
        if keys[pygame.K_SPACE]:
            if player == "cross":
                crossdraw(x, y, list_positionsX,list_positions)
                play = winner(player)
                player = "circle"
                break

            else:
                circledraw(posx=x, posy=y, list=list_positionsO,
                           list_positions=list_positions)
                winner(player)
                play = winner(player)
                player = "cross"
                break
        if len(list_cross) > 0:
            for cross in list_cross:
                pygame.draw.line(screen, "white", (cross[0], cross[1]),
                                 (cross[2], cross[3]), 5)
                pygame.draw.line(screen, "white", (cross[4], cross[5]),
                                 (cross[6], cross[7]), 5)
        if len(list_circle) > 0:
            for circle in list_circle:
                pygame.draw.circle(screen, (255, 255, 255), (circle[0],circle[1]),30, 5)

        if play == 1:
           running = False

        pygame.display.flip()
        clock.tick(60)

pygame.quit()