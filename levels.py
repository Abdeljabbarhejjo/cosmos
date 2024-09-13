import pygame
import sys
import load_images

pygame.init()

def level():
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


    move = False
    reverse = False
    returning = False
    speed = 100
    speed_reverse = 100
    return_speed = 100

    load_images.images_levels()

    original_mars_pos = load_images.mars_rect.x
    original_jupiter_pos = load_images.jupiter_rect.x

    mars_target_x = load_images.jupiter_rect.x
    jupiter_target_x = load_images.mars_rect.x

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if load_images.back_right_rect and load_images.back_right_rect.collidepoint(event.pos):
                    from setting import sound
                    sound.play_clicking_sound()
                    import main
                    main.main()
                elif load_images.mars_rect and load_images.mars_rect.collidepoint(event.pos):
                    from setting import sound
                    sound.play_clicking_game()
                    from game_play_F import type2
                    run = False
                    type2()
                elif load_images.back_right_c_rect and load_images.back_right_c_rect.collidepoint(event.pos):
                    from setting import sound
                    sound.play_clicking_sound()
                    move = True
                    reverse = False
                    returning = False
                elif load_images.back_right_r_rect and load_images.back_right_r_rect.collidepoint(event.pos):
                    from setting import sound
                    sound.play_clicking_sound()
                    move = True
                    reverse = True
                    returning = False

        if move:
            if reverse:
                if load_images.mars_rect.x > mars_target_x:
                    load_images.mars_rect.x -= speed_reverse
                if load_images.jupiter_rect.x < jupiter_target_x:
                    load_images.jupiter_rect.x += speed_reverse
                if load_images.mars_rect.x <= mars_target_x and load_images.jupiter_rect.x >= jupiter_target_x:
                    move = False
                    returning = True
            else:
                if load_images.mars_rect.x < mars_target_x:
                    load_images.mars_rect.x += speed
                if load_images.jupiter_rect.x > jupiter_target_x:
                    load_images.jupiter_rect.x -= speed
                if load_images.mars_rect.x >= mars_target_x and load_images.jupiter_rect.x <= jupiter_target_x:
                    move = False
        if returning:
            if load_images.mars_rect.x < original_mars_pos:
                load_images.mars_rect.x += return_speed
            if load_images.mars_rect.x > original_mars_pos:
                load_images.mars_rect.x -= return_speed
            if load_images.jupiter_rect.x < original_jupiter_pos:
                load_images.jupiter_rect.x += return_speed
            if load_images.jupiter_rect.x > original_jupiter_pos:
                load_images.jupiter_rect.x -= return_speed

            if abs(load_images.mars_rect.x - original_mars_pos) <= return_speed and abs(load_images.jupiter_rect.x - original_jupiter_pos) <= return_speed:
                load_images.mars_rect.x = original_mars_pos
                load_images.jupiter_rect.x = original_jupiter_pos
                returning = False

        load_images.draw_bg(screen)
        pygame.display.update()
        pygame.time.delay(30)
