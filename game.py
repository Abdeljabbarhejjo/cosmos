import pygame
import random
import sys
import webbrowser


pygame.init()

def main():
    bg = pygame.image.load(r"C:\Users\noohy\Desktop\Final legislator\solar\img\pg.png")
    sasuki = pygame .image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\sasuki.png')
    bg = pygame.transform.scale(bg, (1280, 720))
    screenw = 1280  # عرض الشاشة
    screenh = 720   # ارتفاع الشاشة
    screen = pygame.display.set_mode((screenw, screenh))
    pygame.display.set_caption('main menu')

    play_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\play.png')
    play_img = pygame.transform.scale(play_img, (250, 250))
    play_rect = play_img.get_rect()
    play_rect=pygame.Rect(play_rect.y, play_rect.x, 200, 120)
    play_rect.center = (screenw // 2 - 360, screenh // 2 - 150)

    shop_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\sho.png')
    shop_img = pygame.transform.scale(shop_img, (300, 100))
    shop_rect = shop_img.get_rect()
    shop_rect=pygame.Rect(shop_rect.y, shop_rect.x, 300, 100)
    shop_rect.center =(screenw // 2 - 480, screenh // 2 + 80)

    setting_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\sho.png')
    setting_img = pygame.transform.scale(setting_img, (300, 100))
    setting_rect = setting_img.get_rect()
    setting_rect=pygame.Rect(setting_rect.y, setting_rect.x, 300, 100)
    setting_rect.center = (screenw // 2 - 160, screenh // 2 + 80)

    youtube = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\youtyube.png')
    youtube = pygame.transform.scale(youtube, (60, 40))
    youtube_rect = youtube.get_rect()
    youtube_rect=pygame.Rect(youtube_rect.y, youtube_rect.x, 60, 40)
    youtube_rect.topright = (screenw // 2 + 580, screenh // 2 + 280)

    instgram = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\instgram.png')
    instgram = pygame.transform.scale(instgram, (50, 50))
    instgram_rect = instgram.get_rect()
    instgram_rect=pygame.Rect(instgram_rect.y, instgram_rect.x, 50, 50)
    instgram_rect.topright = (screenw // 2 + 510 , screenh // 2 +280)

    facebook = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\fasboke.png')
    facebook = pygame.transform.scale(facebook, (50, 50))
    facebook_rect = facebook.get_rect()
    facebook_rect=pygame.Rect(facebook_rect.y, facebook_rect.x, 50, 50)
    facebook_rect.topright =(screenw // 2 + 430, screenh // 2 + 280)

    def draw_screen():
        screen.blit(bg, (0, 0))
        screen.blit(sasuki ,(700 , 0))
        screen.blit(youtube, youtube_rect)
        screen.blit(facebook, facebook_rect)
        screen.blit(instgram, instgram_rect)
        screen.blit(setting_img ,setting_rect)
        screen.blit(play_img, play_rect)
        screen.blit(shop_img, shop_rect)


    run = True
    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    level()
                    run = False
                elif shop_rect.collidepoint(event.pos):
                    pass
                elif setting_rect.collidepoint(event.pos):
                    settings()
                    run = False
                if youtube_rect.collidepoint(event.pos):
                    webbrowser.open("https://www.youtube.com/@fninjaf1875")
                elif facebook_rect.collidepoint(event.pos):
                    webbrowser.open("https://www.facebook.com/profile.php?id=100036843253331&mibextid=ZbWKwL")
                elif instgram_rect.collidepoint(event.pos):
                    webbrowser.open("https://www.instagram.com/x7_a?igsh=azhxNjE3MnB3OGww")

        draw_screen()
        pygame.display.update()

def game():

    screenh = 720
    screenw = 1280
    screen = pygame.display.set_mode((screenw, screenh))
    font = pygame.font.Font(None, 36)
    surface = pygame.Surface((screenw, screenh), pygame.SRCALPHA)

    # إعدادات اللاعب
    setting_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\Settings.png')
    setting_rect = setting_img.get_rect()
    setting_rect.center = (screenw // 2 , screenh // 2 + 5 )

    exit_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\Exit.png')
    exit_rect = exit_img.get_rect()
    exit_rect.center =(screenw // 2, screenh // 2 + 180)

    play_img = pygame.image.load('C:\\Users\\noohy\\Desktop\\Final legislator\\solar\\img\\Play button.png')
    play_rect = play_img.get_rect()
    play_rect.center = (screenw // 2 , screenh // 2 -180)

    def draw_pause():
        pygame.draw.rect(surface, (100, 100, 250, 150), [360, 50, 600, 600])
        screen.blit(surface, (0, 0))
        screen.blit(play_img, play_rect)
        screen.blit(setting_img, setting_rect)
        screen.blit(exit_img, exit_rect)
    # إعدادات الشاشة

    x, y = 70, 250
    speed = 10

    pause = False
    options_img=pygame.image.load(f'C:\\Users\\noohy\\Desktop\\Final legislator\\solar\\img\\setting img.png')
    options_rect = options_img.get_rect()
    options_img = pygame.transform.scale(options_img, (100 , 100))
    options_rect.topleft  = ( screenw - options_rect.height + 650,0)
    # تعديل مسار الصور واستخدام f-string بشكل صحيح
    image_paths = [f"C:\\Users\\noohy\\Desktop\\Final legislator\\solar\\img,herro\\{i}.jpg" for i in range(1, 25)]
    images = [pygame.transform.scale(pygame.image.load(img), (100, 100)) for img in image_paths]
    move = 0
    right = False

    jumping = False
    jump_speed = 15
    gravity = 1
    jump_height = jump_speed

    dash = False

    # إعداد شريط الصحة
    class HealthBar:
        def __init__(self, x, y, w, h, max_hp):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.hp = max_hp
            self.max_hp = max_hp

        def draw(self, surface):
            ratio = self.hp / self.max_hp
            pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.w, self.h))
            pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, self.w * ratio, self.h))

    health_bar = HealthBar(20, 20, 200, 30, 200)
    collision_cooldown = 0

    # إعداد العوائق
    class Obstacle:
        def __init__(self, x, y, w, h):
            self.rect = pygame.Rect(x, y, w, h)

        def draw(self, surface):
            pygame.draw.rect(surface, (255, 0, 0), self.rect)

        def move(self, speed):
            self.rect.x -= speed

        def respawn(self):
            if self.rect.x < -50:
                self.rect.x = screenw + 1000
                self.rect.y = random.randint(100, 200)

    # إنشاء العوائق
    obstacles = [
        Obstacle(screenw + 1000, random.randint(100, 200), 50, 50),
        Obstacle(screenw + 1000, random.randint(100, 200) + 150, 50, 50),
        Obstacle(screenw + 1000, random.randint(100, 200) + 300, 50, 50),
        Obstacle(screenw + 1000, random.randint(100, 200) + 450, 50, 50)
    ]

    # إعداد عنصر الجائزة (jocker)
    v = random.randint(1000, 5000)
    b = random.randint(50, 550)

    def draw_jocker():

        nonlocal v, b
        if v < -30:
            v = random.randint(1000, 5000)
            b = random.randint(50, 550)
        jocker = pygame.Rect(v, b, 30, 30)
        pygame.draw.rect(screen, (255, 255, 255), jocker)
        v -= speed
        return jocker

    # الألوان
    WHITE = (255, 255, 255)

    # شاشة اللعبة
    def gscreen():

        nonlocal x, y, move, right
        screen.fill(WHITE)
        if right:
            screen.blit(images[move], (x, y))
            move += 1
            if move == 23:
                move = 0
        else:
            screen.blit(images[12], (x, y))

        screen.blit( options_img, options_rect)
        text = font.render(f"Health: {health_bar.hp}", True, (100, 100, 100))
        screen.blit(text, (375, 10))
        health_bar.draw(screen)


    # إنشاء ساعة لتحديد الإطار
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(24)  # تحديد معدل الإطارات إلى 24 إطار في الثانية
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_rect.collidepoint(event.pos):
                    pause = not pause
                if pause:
                    if play_rect.collidepoint(event.pos):
                        pause = False
                    elif setting_rect.collidepoint(event.pos):
                        settings()
                    elif exit_rect.collidepoint(event.pos):
                        main()

        # التعامل مع حركة اللاعب
        keys = pygame.key.get_pressed()
        if pause:
            draw_pause()
        else:
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 0:
                x -= speed
                right = False

            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < screenw - 100:
                x += speed
                right = True

            if keys[pygame.K_x]:
                dash = True

            if dash:
                x += 30
                dash = False

            if not jumping:
                if (keys[pygame.K_w] or keys[pygame.K_UP]) and y > 0:
                    y -= speed
                if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y < screenh - 100:
                    y += speed

            if not jumping and keys[pygame.K_SPACE]:
                jumping = True

            if jumping:
                y -= jump_height
                jump_height -= gravity
                if jump_height < -jump_speed:
                    jumping = False
                    jump_height = jump_speed

            if y >= screenh - 50:
                y = screenh - 50
                jumping = False

            player = pygame.Rect(x, y, 100, 100)

            if collision_cooldown > 0:
                collision_cooldown -= 1

            for obstacle in obstacles:
                obstacle.move(speed)
                obstacle.respawn()
                if obstacle.rect.colliderect(player) and collision_cooldown == 0:
                    health_bar.hp -= 20
                    collision_cooldown = 60  # إعادة تعيين فترة التبريد بعد الاصطدام

            jocker = draw_jocker()
            if player.colliderect(jocker) and health_bar.hp < health_bar.max_hp:
                health_bar.hp += 10
                if health_bar.hp > health_bar.max_hp:
                    health_bar.hp = health_bar.max_hp

            gscreen()

            for obstacle in obstacles:
                obstacle.draw(screen)

        pygame.display.update()

def settings():
    screenw = 1280
    screenh = 720
    screen = pygame.display.set_mode((screenw, screenh))
    BLUE = (100, 10, 200)



    back_left_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\left back.png')
    back_left_rect = back_left_img.get_rect()
    back_left_img = pygame.transform.scale(back_left_img, (200 , 200))
    back_left_rect = pygame.Rect(back_left_rect.x, back_left_rect.y, 200, 200)
    back_left_rect.center = (screenw//2 - 550 , screenh//2 + 250)

    back_right_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\right back.png')
    back_right_rect = back_right_img.get_rect()
    back_right_img = pygame.transform.scale(back_right_img, (200 , 200))
    back_right_rect = pygame.Rect(back_right_rect.x, back_right_rect.y, 200, 200)
    back_right_rect.center = (screenw//2 + 550 , screenh//2 + 250)


    def draw_buttons ():
        screen.blit(back_left_img, back_left_rect)
        screen.blit(back_right_img, back_right_rect)
    run =  True
    while run :


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_left_rect.collidepoint(event.pos):
                    return
                if back_right_rect.collidepoint(event.pos):
                    main()
                    pygame.quit()
                    sys.exit()

        screen.fill(BLUE)
        draw_buttons()
        pygame.display.update()


def level():
    screenw = 1280
    screenh = 720
    screen = pygame.display.set_mode((screenw, screenh))
    bg_levels_main = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\bg level.webp')
    bg_levels_main = pygame.transform.scale(bg_levels_main, (screenw, screenh))


    back_right_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\right back.png')
    back_right_rect = back_right_img.get_rect()
    back_right_img = pygame.transform.scale(back_right_img, (200 , 200))
    back_right_rect = pygame.Rect(back_right_rect.x, back_right_rect.y, 200, 200)
    back_right_rect.center = (screenw//2 + 550 , screenh//2 + 250)

    mars_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\mars.png')
    mars_img = pygame.transform.scale(mars_img, (400 , 400))
    mars_rect = mars_img.get_rect()
    mars_rect = pygame.Rect(mars_rect.x, mars_rect.y, 300 ,300)
    mars_rect.center = (screenw//2 - 400 , screenh//2 - 100 )

    jupiter_img = pygame.image.load(r'C:\Users\noohy\Desktop\Final legislator\solar\img\jupiter.png')
    jupiter_img = pygame.transform.scale(jupiter_img, (400 , 400))
    jupiter_rect = jupiter_img.get_rect()
    jupiter_rect = pygame.Rect(jupiter_rect.x, jupiter_rect.y, 300 ,300)
    jupiter_rect.center =(screenw//2 + 200, screenh//2 - 100 )

    def draw_bg ():

        screen.blit(bg_levels_main, (0, 0))
        screen.blit(mars_img, mars_rect)
        screen.blit(back_right_img, back_right_rect)
        screen.blit(jupiter_img, jupiter_rect)
    run = True
    while run :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_right_rect.collidepoint(event.pos):
                    main()
                    pygame.quit()
                    sys.exit()
                elif mars_rect.collidepoint(event.pos):
                    game()
                    pygame.quit()
                    sys.exit()
                elif jupiter_rect.collidepoint(event.pos):
                    game()
                    pygame.quit()
                    sys.exit()

        draw_bg()
        pygame.display.update()
main()
