import pygame
import json

pygame.init()

# Screen dimensions
screenw = 1280
screenh = 720

# Create screen object
screen = pygame.display.set_mode((screenw, screenh), pygame.FULLSCREEN)

# Fonts
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 60)

# Load assets
shop_background = pygame.image.load(r'shop/Shop final.jpg')
shop_background_rect = shop_background.get_rect()
score_bar = pygame.image.load(r'assets/Quality Box.png')
coin_img = pygame.image.load(r'assets/Coins.png')
coin_img = pygame.transform.scale(coin_img, (100, 100))
back_right_img = pygame.image.load(r'assets/Arrow.png')
back_right_rect = back_right_img.get_rect(center=(screenw // 2 - 450, screenh // 2 + 280))

trader = [pygame.image.load(f'shop/{s}.png') for s in range(1, 4)]
trader1 = pygame.image.load(r'shop/1.png')
sin = pygame.image.load(r'shop/Coming Soon.png')

# Set this to False initially
coming_soon = False
coming_soon_start_time = 0

# Animation control variables
animation_speed = 30
animation_counter = 0


# Load data from JSON
def load_data():
    """تحميل البيانات من ملف JSON"""
    try:
        with open('score.json', 'r') as score_file:
            data = json.load(score_file)
        print("البيانات تم تحميلها بنجاح.")
        print(data)
    except FileNotFoundError:
        print("الملف غير موجود. يبدأ من النقطة 0.")
        data = {'coin_num': 0}  # إذا لم يكن الملف موجودًا، نبدأ ببيانات جديدة
    except Exception as e:
        print(f'خطأ في التحميل: {e}')
        data = {'coin_num': 0}  # في حالة الخطأ، نبدأ بقيمة جديدة
    return data  # إرجاع البيانات المحملة أو الجديدة


# تحميل البيانات
data = load_data()

num_trader = 0


# Function to draw the shop screen
def draw_shop_screen():
    global trader, num_trader, coming_soon, animation_counter, coming_soon_start_time

    # Display background and trader images
    screen.blit(shop_background, (0, 0))
    screen.blit(back_right_img, back_right_rect)

    # Render and display the coin number from the JSON data
    font = pygame.font.Font(r'fonts/comic.ttf', 50)
    text = font.render(str(data['coin_num']), True, (255, 255, 255))  # Corrected text rendering
    screen.blit(text, (300, 5))  # Display the coin number at this position

    if not coming_soon:
        screen.blit(trader1, (150, 185))

    # Handle trader animation if "coming soon" is triggered
    if coming_soon:
        animation_counter += 1
        if animation_counter >= animation_speed:
            num_trader += 1
            if num_trader >= len(trader):
                num_trader = 0
            animation_counter = 0  # إعادة تعيين العداد
        screen.blit(trader[num_trader], (150, 185))
        screen.blit(sin, (400, 100))

        # Stop "Coming Soon" after 5 seconds
        if pygame.time.get_ticks() - coming_soon_start_time > 5000:  # 5000 مللي ثانية = 5 ثوانٍ
            coming_soon = False
            coming_soon_start_time = 0  # Reset the start time when the animation ends

    pygame.display.update()  # Update the screen


# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_right_rect.collidepoint(event.pos):
                import main

                main.main()
                run = False
            if shop_background_rect.collidepoint(event.pos):
                coming_soon = True  # Start animation when background is clicked
                coming_soon_start_time = pygame.time.get_ticks()  # Reset the timer when animation starts

    # Draw the shop screen
    draw_shop_screen()

pygame.quit()
