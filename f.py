import pygame as pg

win = pg.display.set_mode((300, 300))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False