import pygame
import json
import load_images

pygame.init()
pygame.mixer.init()

def save_volumes(key, value):
    try:
        with open('volume_settings.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data[key] = value
    with open('volume_settings.json', 'w') as file:
        json.dump(data, file, indent=4)  # Added indent for readability
    print(f"Saved {key}: {value} to volume_settings.json")  # Print statement for debugging

def load_volumes(key, default):
    try:
        with open('volume_settings.json', 'r') as file:
            data = json.load(file)
            value = data.get(key, default)
            print(f"Loaded {key}: {value} from volume_settings.json")  # Print statement for debugging
            return value
    except FileNotFoundError:
        print(f"File not found. Returning default for {key}: {default}")  # Print statement for debugging
        return default

class SoundF:
    def __init__(self):
        pygame.mixer.init()
        self.clicking_sound = pygame.mixer.Sound(r'sound/menu-click-89198.mp3')
        self.clicking_game = pygame.mixer.Sound(r'sound/button-124476.mp3')
        self.clicking_volume = 1.0

    def play_clicking_sound(self):
        self.clicking_sound.set_volume(self.clicking_volume)
        self.clicking_sound.play()

    def play_clicking_game(self):
        self.clicking_game.set_volume(self.clicking_volume)
        self.clicking_game.play()

sound = SoundF()

class SoundSettings:
    def __init__(self):
        # Load volume settings
        self.clicking_sound_volume_level = load_volumes("clicking_volume_level", 0.5)
        self.sound_bar_volume_level = load_volumes("bg_volume_level", 0.5)
        self.sound_bar_volume_level_main = load_volumes("background_main", 0.5)

        # Load images
        self.mute_img_fx = pygame.image.load(r'assets/No Sound Icon.png')
        self.not_mute_img_fx = pygame.image.load(r'assets/Sound Icon.png')
        self.mute_img = pygame.image.load(r'assets/No music icon.png')
        self.not_mute_img = pygame.image.load(r'assets/music icon.png')

        # Initialize other attributes
        self.sound_bar_width, self.sound_bar_height = 300, 100
        self.sound_bar_x, self.sound_bar_y = 0, 0
        self.clicking_sound_bar_y = 0

        self.mute_button_width, self.mute_button_height = self.mute_img.get_width(), self.mute_img.get_height()
        self.mute_button_x, self.mute_button_y = 0, 0

        self.mute_button_fx_width, self.mute_button_fx_height = self.mute_img_fx.get_width(), self.mute_img_fx.get_height()
        self.mute_button_fx_x, self.mute_button_fx_y = 0, 0

        self.dragging_sound = False
        self.dragging_clicking_sound = False
        self.muted_music = False
        self.mute_effect = False

        self.sound_bar = pygame.image.load(r'assets/Slider.png')
        self.slide_bar = pygame.image.load(r'assets/Slider Head.png')
        self.slide_bar = pygame.transform.scale(self.slide_bar, (110, 85))

        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)

        self.sound_bar_rect = self.sound_bar.get_rect()
        self.slide_bar_rect = self.slide_bar.get_rect()

        self.sound_bar_x = (self.screen_width - self.sound_bar_width) // 2
        self.sound_bar_y = (self.screen_height - self.sound_bar_height) // 2 - 250
        self.clicking_sound_bar_y = self.sound_bar_y + 150

        self.mute_button_x = (self.screen_width - self.mute_button_width) // 2 - 220
        self.mute_button_y = self.sound_bar_y + self.sound_bar_height - 80

        self.mute_button_fx_x = (self.screen_width - self.mute_button_fx_width) // 2 - 220
        self.mute_button_fx_y = self.sound_bar_y + self.sound_bar_height + 60

        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.sound_bar_volume_level_main)
        sound.clicking_volume = self.clicking_sound_volume_level

    def main_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(r'sound/lady-of-the-80x27s-128379.mp3')
        pygame.mixer.music.set_volume(self.sound_bar_volume_level_main)
        pygame.mixer.music.play(loops=-1)

    def background_sound_play(self, loops=0):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(r'sound/the_end_of_a_dream-236209.mp3')
        pygame.mixer.music.set_volume(self.sound_bar_volume_level)
        pygame.mixer.music.play(loops)

    def game_over(self, loops=0):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(r'sound/kl-music-box-game-over-ii-152200.mp3')
        pygame.mixer.music.set_volume(self.sound_bar_volume_level)
        pygame.mixer.music.play(loops)

    def draw_sound_bars(self):
        self.screen.blit(self.sound_bar, (self.sound_bar_x, self.sound_bar_y))
        filled_width = self.sound_bar_volume_level * self.sound_bar_width
        slide_bar_x = self.sound_bar_x + int(filled_width) - (self.slide_bar_rect.width // 2 - 55)
        self.screen.blit(self.slide_bar, (slide_bar_x, self.sound_bar_y))

        self.screen.blit(self.sound_bar, (self.sound_bar_x, self.clicking_sound_bar_y))
        filled_width = self.clicking_sound_volume_level * self.sound_bar_width
        slide_bar_x = self.sound_bar_x + int(filled_width) - (self.slide_bar_rect.width // 2 - 55)
        self.screen.blit(self.slide_bar, (slide_bar_x, self.clicking_sound_bar_y))

    def draw_mute_button(self):
        if self.muted_music:
            self.screen.blit(self.mute_img, (self.mute_button_x, self.mute_button_y))
        else:
            self.screen.blit(self.not_mute_img, (self.mute_button_x, self.mute_button_y))
        if self.mute_effect:
            self.screen.blit(self.mute_img_fx, (self.mute_button_fx_x, self.mute_button_fx_y))
        else:
            self.screen.blit(self.not_mute_img_fx, (self.mute_button_fx_x, self.mute_button_fx_y))

    def save_volumes(self):
        print("Saving volumes...")
        save_volumes("bg_volume_level", self.sound_bar_volume_level)
        save_volumes("clicking_volume_level", self.clicking_sound_volume_level)
        save_volumes("background_main", self.sound_bar_volume_level_main)

    def run(self):
        load_images.images_settings()
        load_images.draw_settings(self.screen)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting...")
                    self.save_volumes()
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if load_images.back_right_rect.collidepoint(event.pos):
                        sound.play_clicking_sound()
                        return

                    if self.sound_bar_x <= event.pos[0] <= self.sound_bar_x + self.sound_bar_width:
                        if self.sound_bar_y <= event.pos[1] <= self.sound_bar_y + self.sound_bar_height:
                            self.dragging_sound = True
                        elif self.clicking_sound_bar_y <= event.pos[1] <= self.clicking_sound_bar_y + self.sound_bar_height:
                            self.dragging_clicking_sound = True

                    elif self.mute_button_x <= event.pos[0] <= self.mute_button_x + self.mute_button_width and self.mute_button_y <= event.pos[1] <= self.mute_button_y + self.mute_button_height:
                        self.muted_music = not self.muted_music
                        pygame.mixer.music.set_volume(0 if self.muted_music else self.sound_bar_volume_level)

                    elif self.mute_button_fx_x <= event.pos[0] <= self.mute_button_fx_x + self.mute_button_fx_width and self.mute_button_fx_y <= event.pos[1] <= self.mute_button_fx_y + self.mute_button_fx_height:
                        self.mute_effect = not self.mute_effect
                        sound.clicking_volume = 0 if self.mute_effect else self.clicking_sound_volume_level

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragging_sound = False
                    self.dragging_clicking_sound = False

                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging_sound:
                        if self.sound_bar_x <= event.pos[0] <= self.sound_bar_x + self.sound_bar_width:
                            self.sound_bar_volume_level = (event.pos[0] - self.sound_bar_x) / self.sound_bar_width
                            self.sound_bar_volume_level = max(0.0, min(1.0, self.sound_bar_volume_level))
                            if not self.muted_music:
                                pygame.mixer.music.set_volume(self.sound_bar_volume_level)

                    if self.dragging_clicking_sound:
                        if self.sound_bar_x <= event.pos[0] <= self.sound_bar_x + self.sound_bar_width:
                            self.clicking_sound_volume_level = (event.pos[0] - self.sound_bar_x) / self.sound_bar_width
                            self.clicking_sound_volume_level = max(0.0, min(1.0, self.clicking_sound_volume_level))
                            if not self.mute_effect:
                                sound.clicking_volume = self.clicking_sound_volume_level

            self.screen.blit(load_images.background_settings, (0, 0))
            self.draw_sound_bars()
            self.draw_mute_button()
            load_images.draw_settings(self.screen)
            pygame.display.flip()

        pygame.mixer.quit()
        pygame.quit()

sound_settings = SoundSettings()
