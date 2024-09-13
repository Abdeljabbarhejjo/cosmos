import pygame

screenw ,screenh = 1280 ,720
screen = pygame.display.set_mode((screenw , screenh))

pause_menu = None
play_img_pause = None
play_img_pause_rect = None
exit_pause = None
setting_pause = None
exit_pause_rect = None
setting_pause_rect = None

background_settings = None
sound_bar = None
slide_bar = None

sound_bar_rect =None
slide_bar_rect =None

play_img = None
shop_img = None
setting_img = None
exit_img = None
youtube = None
instgram = None
X = None
bg = None

play_rect = None
shop_rect = None
setting_rect = None
exit_rect = None
youtube_rect = None
X_rect = None
instgram_rect = None

bg_levels_main = None
back_right_img = None
back_right_c_img = None
back_right_r_img = None
mars_img = None
jupiter_img = None
back_left_img = None

back_right_c_rect = None
back_right_r_rect = None
back_right_rect = None
back_left_rect = None
mars_rect = None
jupiter_rect = None



class STARS(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        self.image_size = (1080, 720)
        for num in range(1, 4):
            img = pygame.image.load(f"assets/STARS {num}.png")
            img = pygame.transform.scale(img, self.image_size)
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect(bottomleft=(0, 720))

    def update(self):
        self.counter += 1
        cooldown = 3
        if self.counter > cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)

# Create a global instance of STARS
stars = STARS()
def images_main():
    global play_img, shop_img, setting_img, youtube, instgram, X, bg, exit_img, exit_rect, back_left_img, back_right_img
    global play_rect, shop_rect, setting_rect, youtube_rect, X_rect, instgram_rect, back_left_rect, back_right_rect

    bg = pygame.image.load(r"assets/Game title.jpg")
    bg = pygame.transform.scale(bg, (screenw, screenh))

    play_img = pygame.image.load(r'assets/Play.png')
    play_rect = play_img.get_rect(center=(screenw // 2 - 430, screenh // 2 - 150))

    shop_img = pygame.image.load(r'assets/shop.png')
    shop_rect = shop_img.get_rect(center=(screenw // 2 - 430, screenh // 2 - 5))

    setting_img = pygame.image.load(r'assets/Settings2.png')
    setting_rect = setting_img.get_rect(center=(screenw // 2 - 425, screenh // 2 + 100))

    exit_img = pygame.image.load(r'assets/Exit 2.png')
    exit_rect = exit_img.get_rect(center=(screenw // 2 - 430, screenh // 2 + 210))

    youtube = pygame.image.load(r'assets/youtube.png')
    youtube_rect = youtube.get_rect(topright=(screenw // 2 + 600, screenh // 2 + 250))

    instgram = pygame.image.load(r'assets/Instagram.png')
    instgram_rect = instgram.get_rect(topright=(screenw // 2 + 500, screenh // 2 + 250))

    X = pygame.image.load(r'assets/X.png')
    X_rect = X.get_rect(topright=(screenw // 2 + 400, screenh // 2 + 250))

def draw_screen_main(screen):
    screen.blit(bg, (0, 0))
    screen.blit(play_img, play_rect)
    screen.blit(shop_img, shop_rect)
    screen.blit(setting_img, setting_rect)
    screen.blit(exit_img, exit_rect)
    screen.blit(youtube, youtube_rect)
    screen.blit(X, X_rect)
    screen.blit(instgram, instgram_rect)


def images_settings():
    global back_left_img, back_right_img ,background_settings
    global back_left_rect, back_right_rect

    back_right_img = pygame.image.load(r'assets/Arrow.png')
    back_right_rect = back_right_img.get_rect(center=(screenw // 2 - 450, screenh // 2 + 250))


    background_settings = pygame.image.load(r'assets/settings Background.jpg')
    background_settings = pygame.transform.scale(background_settings, (screenw, screenh))

def draw_background_settings(screen):
    screen.blit(background_settings, (0, 0))

def draw_settings(screen):
    #screen.blit(back_left_img, back_left_rect)
    screen.blit(back_right_img, back_right_rect)
    pygame.display.update()

def images_levels():
    global bg_levels_main, back_right_img, back_right_rect, back_right_c_img, back_right_c_rect
    global back_right_r_img, back_right_r_rect, mars_img, mars_rect, jupiter_img, jupiter_rect, back_left_img, back_left_rect

    bg_levels_main = pygame.image.load(r'assets/Level selection BG.jpg')

    back_right_img = pygame.image.load(r'assets/Back left Button.png')
    back_right_rect = back_right_img.get_rect(center=(screenw // 2 - 500, screenh // 2 + 250))

    back_right_c_img = pygame.image.load(r'assets/Right Arrow Button.png')
    back_right_c_img = pygame.transform.scale(back_right_c_img, (100, 50))
    back_right_c_rect = back_right_c_img.get_rect(center=(screenw // 2 + 450, screenh // 2 + 10))

    back_right_r_img = pygame.image.load(r'assets/Left Arrow Button.png')
    back_right_r_img = pygame.transform.scale(back_right_r_img, (100, 50))
    back_right_r_rect = back_right_r_img.get_rect(center=(screenw // 2 - 450, screenh // 2))

    mars_img = pygame.image.load(r'assets/Mars selection (1).png')
    mars_rect = mars_img.get_rect(center=(screenw // 2, screenh // 2))

    jupiter_img = pygame.image.load(r'assets/Coming soon Planet.png')
    jupiter_rect = jupiter_img.get_rect(center=(screenw // 2 + 1000, screenh // 2))


def draw_bg(screen):
    global bg_levels_main, back_right_img, back_right_rect, back_right_c_img, back_right_c_rect
    global back_right_r_img, back_right_r_rect, mars_img, jupiter_img, mars_rect, jupiter_rect, back_left_img, back_left_rect

    screen.blit(bg_levels_main, (0, 0))
    screen.blit(jupiter_img, jupiter_rect)
    screen.blit(mars_img, mars_rect)
    screen.blit(back_right_img, back_right_rect)
    screen.blit(back_right_c_img, back_right_c_rect)
    screen.blit(back_right_r_img, back_right_r_rect)

    stars.update()  # Update the STARS object
    screen.blit(stars.image, stars.rect)
