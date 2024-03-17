from pygame import*
#фон
a = (112,181,255)
win_1 = 700
win_2 = 500
game = True
window = display.set_mode((700, 500))
display.set_caption("ping-pong")
window = display.set_mode((win_1, win_2))
window.fill(a)


while game:
    for a in event.get():
        if a.type == QUIT:
            game = False

    display.update()