import pygame
import webbrowser
import sys
import load_images
from setting import SoundSettings

pygame.mixer.init()
pygame.mixer.quit()
pygame.init()


sound_settings = SoundSettings()
sound_settings.main_music()

screenw = 1280
screenh = 720
screen = pygame.display.set_mode((screenw, screenh), pygame.FULLSCREEN)
pygame.display.set_caption('cosmic')
icon = pygame.image.load(r'assets/Logo.jpg')
pygame.display.set_icon(icon)

def main():
    import levels
    import setting

    load_images.images_main()

    run = True
    while run:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if load_images.play_rect.collidepoint(event.pos):
                    from setting import sound  # تأخير الاستيراد هنا
                    sound.play_clicking_sound()
                    levels.level()
                    run = False
                elif load_images.shop_rect.collidepoint(event.pos):
                    import shop
                    shop.draw_shop_screen()
                elif load_images.setting_rect.collidepoint(event.pos):
                    from setting import sound  # تأخير الاستيراد هنا
                    sound.play_clicking_sound()
                    setting.sound_settings.run()
                elif load_images.exit_rect.collidepoint(event.pos):
                    from setting import sound  # تأخير الاستيراد هنا
                    sound.play_clicking_sound()
                    pygame.quit()
                    sys.exit()
                elif load_images.youtube_rect.collidepoint(event.pos):
                    from setting import sound  # تأخير الاستيراد هنا
                    sound.play_clicking_sound()
                    webbrowser.open("https://www.youtube.com/@fninjaf1875")
                elif load_images.X_rect.collidepoint(event.pos):
                    from setting import sound  # تأخير الاستيراد هنا
                    sound.play_clicking_sound()
                    webbrowser.open("https://x.com/CellsCreat36254?t=7Ze_s_JPNiywk35wVkjLeA&s=09")
                elif load_images.instgram_rect.collidepoint(event.pos):
                    from setting import sound  # تأخير الاستيراد هنا
                    sound.play_clicking_sound()
                    webbrowser.open("https://www.instagram.com/creative__cells/")

        # رسم الشاشة الرئيسية
        load_images.draw_screen_main(screen)
        pygame.display.update()

main()
