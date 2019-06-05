def steruj(event):
    global x
    global y


if event.type == pygame.KEYUP and event.key == pygame.K_w:
    if y - 10 > 0:
        y = y - 25
if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
    if y + 10 < 590:
        y = y + 25
if event.type == pygame.KEYUP and event.key == pygame.K_a:
    if x - 10 > 0:
        x = x - 25
if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
    if x + 10 < 560:
        x = x + 25

steruj()
