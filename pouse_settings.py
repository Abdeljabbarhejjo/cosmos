import pygame
import sys
from setting import SoundSettings

pygame.init()
pygame.mixer.init()

pygame.mixer.quit()

def dead():

    sound_settings = SoundSettings()
    sound_settings.game_over(loops=-1)

    screenw = 1280
    screenh = 720
    screen = pygame.display.set_mode((screenw, screenh), pygame.FULLSCREEN)

    dead_screen = [pygame.image.load(f'lose screen/Lose screen_{i:03}.jpg') for i in range(0, 79)]
    current_image_index = 0
    clock = pygame.time.Clock()

    # تحميل الصور
    play_img = pygame.image.load(r'lose screen/Retry.png')
    exit_img = pygame.image.load(r'lose screen/Quit.png')

    # الحصول على rect من الصورة لتحديد المساحة
    play_rect = play_img.get_rect(topleft=(545, 567))  # وضع زر إعادة المحاولة عند (580, 603)
    exit_rect = exit_img.get_rect(topleft=(570, 642))  # وضع زر الخروج عند (600, 682)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    from game_play_F import type2
                    type2()
                    pygame.init()
                    return
                elif exit_rect.collidepoint(event.pos):
                    from main import main
                    main()
                    pygame.init()
                    return

                    # عرض الصورة الحالية
        screen.blit(dead_screen[current_image_index], (0, 0))

        # رسم الأزرار على الشاشة
        screen.blit(play_img, play_rect.topleft)  # رسم زر إعادة المحاولة
        screen.blit(exit_img, exit_rect.topleft)  # رسم زر الخروج

        # تحديث الصورة بشكل دوري
        current_image_index = (current_image_index + 1) % len(dead_screen)

        clock.tick(24)
        pygame.display.flip()

dead()
