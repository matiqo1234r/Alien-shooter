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


class Level():

    def rysuj(self):



    def wczytajzpliku(self):


class Tło():

    def rysuj(self):
        pass

class Duszek():

    def rysuj(self):



    def ustawpozycję(self):




    def pokaż(self):




    def ukruj(self):




    def zniszcz(self):




    def pozycja(self):




    def rozmiar(self):



rocket = def __int__():
    pygame.image.load(os.path.join('data', 'minecrtafte.png'))




steruj()