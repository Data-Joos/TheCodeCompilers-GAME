
#""" pygame.examples.aliens

#Shows a mini game where you have to defend against aliens.

#What does it show you about pygame?

#* pg.sprite, the difference between Sprite and Group.
#* dirty rectangle optimization for processing for speed.
#* music with pg.mixer.music, including fadeout
#* sound effects with pg.Sound
#* event processing, keyboard handling, QUIT handling.
#* a main loop frame limited with a game clock from pg.time.Clock
#* fullscreen switching.


#Controls
#--------

#* Left and right arrows to move.
#* Space bar to shoot
#* f key to toggle between fullscreen.

#"""

import random
import os

# import basic pygame modules
import pygame as pg

# see if we can load more than standard BMP
if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


# game constants
MAX_SHOTS = 3  # most player bullets onscreen
ALIEN_ODDS = 12  # chances a new alien appears
THANOS_ODDS = 12
DRAGON_ODDS = 12 
EDWARDBLOM_ODDS = 12
LEO_ODDS = 12
KALLE_ODDS = 12
ACADEMYAWARD_ODDS = 80
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 50  # frames between new aliens
THANOS_RELOAD = 50
DRAGON_RELOAD = 50
EDWARDBLOM_RELOAD = 50
LEO_RELOAD = 50
KALLE_RELOAD = 50
SCREENRECT = pg.Rect(0, 0, 640, 480)
SCORE = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]

# test-kommentar

def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()


def load_sound(file):
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


# Each type of game object gets an init and an update function.
# The update function is called once per frame, and it is when each object should
# change its current position and state.
#
# The Player object actually gets a "move" function instead of update,
# since it is passed extra information about the keyboard.


class Player(pg.sprite.Sprite):
    """Representing the player as a moon buggy type car."""

    speed = 50
    bounce = 24
    gun_offset = -11
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top


class Thanos(pg.sprite.Sprite):
    
    speed = 13
    animcycle = 12
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Thanos.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]


class Dragon(pg.sprite.Sprite):
    """An Dragon that slowly moves dwon the screen"""

    speed = 18
    animcycle = 12
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Dragon.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]        


class Edwardblom(pg.sprite.Sprite):
      
      speed = 33
      animcycle = 12
      images = []

      def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Edwardblom.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

      def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]     


class Leo(pg.sprite.Sprite):

    speed = 11
    animcycle = 12
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1,1)) * Leo.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right


    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom +1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame +1
        self.image = self.images[self.frame // self.animcycle % 3]

class Kalle(pg.sprite.Sprite):
    """An alien space ship. That slowly moves down the screen."""

    speed = 16
    animcycle = 12
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Kalle.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]

class Alien(pg.sprite.Sprite):
    """An alien space ship. That slowly moves down the screen."""

    speed = 13
    animcycle = 12
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]

class startKnapp(pg.sprite.Sprite):
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    
    def nedtryckt(self):
        self.image = self.images[1]
    
    def upptryckt(self):
        self.image = self.images[0]

class avslutaKnapp(startKnapp):

    def __init__(self, funktion_vid_tryck):
        super().__init__()
        self.funktion_vid_knapptryck = funktion_vid_tryck

    def knapptryck(self):
        self.funktion_vid_knapptryck()

class Explosion(pg.sprite.Sprite):
    """An explosion. Hopefully the Alien and not the player!"""

    defaultlife = 12
    animcycle = 3
    images = []

    def __init__(self, actor):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        """called every time around the game loop.

        Show the explosion surface for 'defaultlife'.
        Every game tick(update), we decrease the 'life'.

        Also we animate the explosion.
        """
        self.life = self.life - 1
        self.image = self.images[self.life // self.animcycle % 2]
        if self.life <= 0:
            self.kill()


class Shot(pg.sprite.Sprite):
    """a bullet the Player sprite fires."""

    speed = -27
    images = []

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        """called every time around the game loop.

        Every tick we move the shot upwards.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()

class Academyaward(pg.sprite.Sprite):
    """A bomb the aliens drop."""

    speed = 9
    images = []

    def __init__(self, leo):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=leo.rect.move(0, 5).midbottom)

    def update(self):
        """called every time around the game loop.

        Every frame we move the sprite 'rect' down.
        When it reaches the bottom we:

        - make an explosion.
        - remove the Bomb.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()

class Bomb(pg.sprite.Sprite):
    """A bomb the aliens drop."""

    speed = 9
    images = []

    def __init__(self, alien):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=alien.rect.move(0, 5).midbottom)

    def update(self):
        """called every time around the game loop.

        Every frame we move the sprite 'rect' down.
        When it reaches the bottom we:

        - make an explosion.
        - remove the Bomb.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()


class Score(pg.sprite.Sprite):
    """to keep track of the score."""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = "white"
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        """We only update the score in update() when it has changed."""
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)


def main(winstyle=0):
    # Initialize pygame
    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None

    fullscreen = False
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    img = load_image("player1.gif")
    Player.images = [img, pg.transform.flip(img, 1, 0)]
    img = load_image("explosion1.gif")
    Explosion.images = [img, pg.transform.flip(img, 1, 1)]
    Thanos.images = [load_image(im) for im in ("thanos.gif", "thanos.gif", "thanos.gif")]
    Edwardblom.images = [load_image(im) for im in ("edwardblom.png", "edwardblom.png","edwardblom.png")]
    Dragon.images = [load_image(im) for im in ("dragon.gif", "dragon.gif", "dragon.gif")]
    Leo.images = [load_image(im) for im in ("leoleft2.gif", "leoleft2.gif", "leoleft2.gif")]
    Kalle.images = [load_image(im) for im in ("kalle.gif", "kalle.gif", "kalle.gif")]
    Alien.images = [load_image(im) for im in ("alien1.gif", "alien2.gif", "alien3.gif")]
    Academyaward.images = [load_image("academyaward2.gif")]
    Bomb.images = [load_image("bomb.gif")]
    Shot.images = [load_image("falukorv.png")]

    startKnapp.images = [load_image("startKnapp.jpg"), load_image("startKnapp.jpg")]
    avslutaKnapp.images = [load_image("Exit.png"), load_image("Exit.png")]

    # decorate the game window
    icon = pg.transform.scale(Alien.images[0], (32, 32))
    pg.display.set_icon(icon)
    pg.display.set_caption("Pygame Aliens")
    pg.mouse.set_visible(0)

    # create the background, tile the bgd image
    bgdtile = load_image("background.gif")
    background = pg.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pg.display.flip()

    # load the sound effects
    boom_sound = load_sound("boom.wav")
    shoot_sound = load_sound("splurt.mp3")
    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    # Initialize Game Groups
    thanoss = pg.sprite.Group()
    dragons = pg.sprite.Group()
    edwards = pg.sprite.Group()
    leos = pg.sprite.Group()
    kalles = pg.sprite.Group()
    aliens = pg.sprite.Group()
    shots = pg.sprite.Group()
    academyawards = pg.sprite.Group()
    bombs = pg.sprite.Group()
    all = pg.sprite.RenderUpdates()
    lastkalle = pg.sprite.GroupSingle()
    lastleo = pg.sprite.GroupSingle()
    lastedward = pg.sprite.GroupSingle()
    lastdragon = pg.sprite.GroupSingle()
    lastthanos = pg.sprite.GroupSingle()
    lastalien = pg.sprite.GroupSingle()

    menu = pg.sprite.Group()

    # assign default groups to each sprite class
    Player.containers = all
    Thanos.containers = thanoss, all, lastthanos
    Leo.containers = leos, all, lastleo
    Kalle.containers = aliens, all, lastkalle
    Alien.containers = aliens, all, lastalien
    Dragon.containers = dragons, all, lastdragon
    Edwardblom.containers = edwards, all, lastedward
    Shot.containers = shots, all
    Academyaward.containers = academyawards, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all

    startKnapp.containers = menu
    avslutaKnapp.containers = menu

    # Create Some Starting Values
    global score
    thanosreload = THANOS_RELOAD
    dragonreload = DRAGON_RELOAD
    edwardblomreload = EDWARDBLOM_RELOAD
    leoreload = LEO_RELOAD
    kallereload = KALLE_RELOAD
    alienreload = ALIEN_RELOAD
    clock = pg.time.Clock()

    # initialize our starting sprites
    global SCORE
    player = Player()
    Thanos()
    if pg.font:
        all.add(Score())
    Dragon()
    if pg.font:
        all.add(Score())
    Edwardblom()
    if pg.font:
        all.add(Score())    
    Leo()
    if pg.font:
        all.add(Score())
    Kalle()
    if pg.font:
        all.add(Score())
    Alien()  # note, this 'lives' because it goes into a sprite group
    if pg.font:
        all.add(Score())

    # Addera startmeny
    def avslutaFunktion():
        pg.quit()

    start_knapp = startKnapp()
    avsluta_knapp = avslutaKnapp(avslutaFunktion)
    avsluta_knapp.rect.move_ip(0, 135)
    start_game = False
    menu.add()
    
    while not start_game:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                start_game = True
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if(start_knapp.rect.collidepoint(pg.mouse.get_pos())):
                    start_knapp.nedtryckt()
                if(avsluta_knapp.rect.collidepoint(pg.mouse.get_pos())):
                    avsluta_knapp.knapptryck()
                    # start game = true
            elif event.type == pg.MOUSEBUTTONUP:
                start_knapp.upptryckt()
                if(start_knapp.rect.collidepoint(pg.mouse.get_pos())):
                    start_game = True
        
            bgdtile = load_image("background.gif")
            background = pg.Surface(SCREENRECT.size)
            for x in range(0, SCREENRECT.width, bgdtile.get_width()):
                background.blit(bgdtile, (x, 0))
            screen.blit(background, (0, 0))
            pg.display.flip()
    
        pg.display.flip()
        dirty = menu.draw(screen)
        pg.display.update(dirty)

    # menu while-loop ends

    pg.mouse.set_visible(False)


    # Run our main loop whilst the player is alive.
    while player.alive():

        # get input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        print("Changing to FULLSCREEN")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle | pg.FULLSCREEN, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    else:
                        print("Changing to windowed mode")
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREENRECT.size, winstyle, bestdepth
                        )
                        screen.blit(screen_backup, (0, 0))
                    pg.display.flip()
                    fullscreen = not fullscreen

        keystate = pg.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # handle player input
        direction = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]
        player.move(direction)
        firing = keystate[pg.K_SPACE]
        if not player.reloading and firing and len(shots) < MAX_SHOTS:
            Shot(player.gunpos())
            if pg.mixer:
                shoot_sound.play()
        player.reloading = firing

        if thanosreload:
            thanosreload = thanosreload - 1
        elif not int(random.random() * THANOS_ODDS):
            Thanos()
            thanosreload = THANOS_RELOAD

        #Create new dragon
        if dragonreload:
            dragonreload = dragonreload - 1
        elif not int(random.random() * DRAGON_ODDS):
            Dragon()
            dragonreload = DRAGON_RELOAD

        #Create new edward
        if edwardblomreload:
            edwardblomreload = edwardblomreload - 1
        elif not int(random.random() * EDWARDBLOM_ODDS):
            Edwardblom()
            edwardblomreload = EDWARDBLOM_RELOAD   

        #L: Create new Leo
        if leoreload:
            leoreload = leoreload -1
        elif not int(random.random() * LEO_ODDS):
            Leo()
            leoreload = LEO_RELOAD

        #L: Create new Kalle
        if kallereload:
            kallereload = kallereload -1
        elif not int(random.random() * KALLE_ODDS):
            Kalle()
            kallereload = KALLE_RELOAD

        # Create new alien
        if alienreload:
            alienreload = alienreload - 1
        elif not int(random.random() * ALIEN_ODDS):
            Alien()
            alienreload = ALIEN_RELOAD

        # Drop bombs
        if lastthanos and not int(random.random() * BOMB_ODDS):
            Bomb(lastthanos.sprite)

        if lastdragon and not int(random.random() * BOMB_ODDS):
            Bomb(lastdragon.sprite)

        if lastedward and not int(random.random() * BOMB_ODDS):
            Bomb(lastedward.sprite)

        if lastalien and not int(random.random() * BOMB_ODDS):
            Bomb(lastalien.sprite)

        # Detect collisions between aliens and players.
        for thanos in pg.sprite.spritecollide(player, thanoss, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(thanos)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()


        for dragon in pg.sprite.spritecollide(player, dragons, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(dragon)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()


        for edwardblom in pg.sprite.spritecollide(player, edwards, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(edwardblom)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()   


        for alien in pg.sprite.spritecollide(player, aliens, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(alien)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()

        # Detect collisions between aliens and players.
        for kalle in pg.sprite.spritecollide(player, kalles, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(kalle)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()

        # Drop Academy awards
        if lastleo and not int(random.random() * ACADEMYAWARD_ODDS):
            Academyaward(lastleo.sprite)

                # Detect collisions between aliens and players.
        for leo in pg.sprite.spritecollide(player, leos, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(leo)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()

        # See if shots hit the aliens.
        for thanos in pg.sprite.groupcollide(thanoss, shots, 1, 1).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(thanos)
            SCORE = SCORE + 1  

        for dragon in pg.sprite.groupcollide(dragons, shots, 1, 1).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(dragon)
            SCORE = SCORE + 1

        for edwardblom in pg.sprite.groupcollide(edwards, shots, 1, 1).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(edwardblom)
            SCORE =SCORE + 1    

        for alien in pg.sprite.groupcollide(aliens, shots, 1, 1).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(alien)
            SCORE = SCORE + 1

        # See if shots hit the kalles.
        for kalle in pg.sprite.groupcollide(kalles, shots, 1, 1).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(kalle)
            SCORE = SCORE + 1

         # See if shots hit the leos.
        for leo in pg.sprite.groupcollide(leos, shots, 1, 1).keys():
            if pg.mixer:
                boom_sound.play()
            Explosion(leo)
            SCORE = SCORE + 1

     # See if leo academyawards hit the player.
        for academyaward in pg.sprite.spritecollide(player, academyawards, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(player)
            Explosion(academyaward)
            player.kill()

        # See if alien boms hit the player.
        for bomb in pg.sprite.spritecollide(player, bombs, 1):
            if pg.mixer:
                boom_sound.play()
            Explosion(player)
            Explosion(bomb)
            player.kill()

        # draw the scene
        dirty = all.draw(screen)
        pg.display.update(dirty)

        # cap the framerate at 40fps. Also called 40HZ or 40 times per second.
        clock.tick(5)

    if pg.mixer:
        pg.mixer.music.fadeout(1000)
    pg.time.wait(1000)


# call the "main" function if running this script
if __name__ == "__main__":
    main()
    pg.quit()