from pico2d import*
import os
import math

os.chdir('C:\Drill\Drill02\Lecture04_2D_Rendering')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
r = 0
while(1):
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.01)

    while(r < 720):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        r += 2
        x += 4 * math.cos(r / 360 * math.pi)
        y += 4 * math.sin(r / 360 * math.pi)
        delay(0.01)

    r = 0

    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.01)
    
    while(y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y += 2
        delay(0.01)

    while(x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= 2
        delay(0.01)

    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y -= 2
        delay(0.01)

    



close_canvas()

