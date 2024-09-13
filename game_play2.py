import pygame
import random
import sys
from setting import SoundSettings
pygame.mixer.quit()
pygame.init()

sound_settings = SoundSettings()
sound_settings.background_sound_play(loops=-1)

# إعداد الشاشة
screenw = 1280
screenh = 720
screen = pygame.display.set_mode((screenw, screenh),pygame.FULLSCREEN)
pygame.display.set_caption("game")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 60)

# الألوان
GREEN = (100, 200, 3)
GREEN_HIGHLIGHT = (50, 255, 50)
RED = (200, 0, 0)


coins_iamge1 = [pygame.image.load(f"coins/{f}.png") for f in range(1,25)]
coin_iamge = [pygame.transform.scale(coin,(70,70)) for coin in coins_iamge1]


speed = 10
rock = False
y_question = False
liqued_brain = False
ask = False

x = 100
y = 300

# تحميل الأعداء وتغيير حجمهم
rockk_x, rockk_y = screenw + 200, y
x1 = screenw + 200
x2 = screenw + 200

y1 = y
moves = 1
shild_moves = 0
player = pygame.Rect(100, 300, 70, 140)  # مستطيل يمثل اللاعب
correct_rect = pygame.Rect(0, 0, 0, 0)
speed1 = 20
answe = True
health = 100
can_health = True
# تحميل صور الحركة
image_paths = [f"img hero\\{i}.png" for i in range(1, 15)]
images = [pygame.transform.scale(pygame.image.load(img), (100, 140)) for img in image_paths]
colliding = True
rects = []
random_question = ""
selected_question_text = ""
font2 = pygame.font.Font(None,70)
can_ask = True

rocks1 = pygame.image.load("assets/Big ROCK.png")
rocck = [pygame.transform.scale(rocks1, (250, 250))]
def choice_obstacle():
    global y_question,liqued_brain,rock
    y_question = False
    liqued_brain = False
    rock = False
    rand_choice_obstacle = random.choice(['y_question','liqued_brain','rock'])
    if rand_choice_obstacle == 'liqued_brain':
        y_question = False
        liqued_brain = True
        rock = False
        print("l")
    if rand_choice_obstacle == 'y_question':
        y_question = True
        liqued_brain = False
        rock = False
        print("y")
    if rand_choice_obstacle == 'rock':
        y_question = False
        liqued_brain = False
        rock = True
        print("r")
choice_obstacle()
image_hero = []
for i in range(15):
    image1 = pygame.image.load(f"img hero/{i + 1}.png")
    immage = pygame.transform.scale(image1, (100, 150))
    image_hero.append(immage)

moves = 0
enemy = []
enemy_move = 0
for z in range(12):
    enemy1 = pygame.image.load(f"enemy/{z+1}.png")
    enemy.append(pygame.transform.scale(enemy1, (200, 200)))

shild = [pygame.image.load(f"assets/shield {i*1}.png") for i in range(1,5)]
shild = [pygame.transform.scale(shild[i],(250,250) )for i in range(1,4)]

boxs = pygame.image.load(r"assets/box.png")
boxs = pygame.transform.scale(boxs, (200, 195))

# إعدادات الصخور
rock_speed = 15

def timer1(time):
    timer_start = pygame.time.get_ticks()  # وقت البداية للمؤقت
    timer_duration = time  # مدة المؤقت بالميلي ثانية (مثلاً 5000 ميلي ثانية = 5 ثواني)
    current_time3 = pygame.time.get_ticks()  # الحصول على الوقت الحالي
    elapsed_time = current_time3 - timer_start
    if elapsed_time >= timer_duration:
        return True
    return False




questions_box = pygame.image.load(r"assets/question box.png")

can_damjed = True
pouse = False

class Queshins:
    def __init__(self, questions_and_answers1):
        self.questions_and_answers = questions_and_answers1
        self.current_question = None
        self.answers = []
        self.correct_answer = None
        self.rects = []
        self.randomize_question()

    def randomize_question(self):
        question_text, answers = random.choice(list(self.questions_and_answers.items()))
        self.current_question = question_text
        self.correct_answer = answers[1]
        random.shuffle(answers)
        self.answers = answers
        self.rects = [pygame.Rect(560, 300, 50, 50), pygame.Rect(560, 400, 50, 50),
                      pygame.Rect(740, 300, 50, 50), pygame.Rect(740, 400, 50, 50)]

    def check_answer(self, selected_answer1):
        return selected_answer1 == self.correct_answer

    def draw(self):
        question_text = font1.render(self.current_question, True, GREEN)
        screen.blit(question_text, (655, 140))

        # رسم الخيارات وتحديث الألوان بناءً على موضع الماوس
        mouse_pos2 = pygame.mouse.get_pos()
        for i1, rect15 in enumerate(self.rects):
            color = GREEN_HIGHLIGHT if rect15.collidepoint(mouse_pos2) else GREEN
            text = font.render(self.answers[i1], True, color)
            screen.blit(text, (rect15.x, rect15.y))


# إنشاء كائن من الفئة Queshins
questions_and_answers = {
    "6 x 3": ['15', '18', '20', '21'],
    "9 x 4": ['36', '32', '40', '28'],
    "8 x 7": ['49', '56', '63', '48'],
    "5 x 9": ['40', '45', '35', '50'],
    "7 x 6": ['42', '36', '48', '30'],
    "4 x 9": ['32', '36', '28', '40'],
    "3 x 8": ['24', '27', '21', '18'],
    "12 x 3": ['30', '36', '32', '40'],
    "11 x 5": ['55', '50', '45', '60'],
    "10 x 6": ['60', '66', '56', '72'],
    "9 x 7": ['63', '54', '56', '72'],
    "6 x 9": ['45', '54', '48', '42'],
    "8 x 4": ['28', '32', '36', '24'],
    "12 x 2": ['18', '20', '24', '22'],
    "5 x 8": ['40', '45', '35', '50']
}

question_manager = Queshins(questions_and_answers)


moves_coins = 0
coins_x = screenw + 200
# أضف قائمة للتحقق من حالة العملات
coins_collected = [False, False, False, False, False]


respawn_coins = False
coins_y = y - 200
coin_num = 0
coin_rects = []
def draw_coins():
    global coins_x, moves_coins, coin_num, coins_y,respawn_coins,coin_rects

    coins_x -= 15
    print(coins_collected)

    coin_rects = [
        pygame.Rect(coins_x, coins_y, 70, 70),
        pygame.Rect(coins_x + 75, coins_y, 70, 70),
        pygame.Rect(coins_x + 150, coins_y, 70, 70),
        pygame.Rect(coins_x + 225, coins_y, 70, 70),
        pygame.Rect(coins_x + 300, coins_y, 70, 70)
    ]

    # تحقق من التصادم وتحديث حالة العملات
    for i, coin_rect in enumerate(coin_rects):
        if player_rect.colliderect(coin_rect) and not coins_collected[i]:
            coins_collected[i] = True  # جمع العملة
            coin_num += 1


    # استخدم حالة العملات قبل رسمها
    for i, coin_rect in enumerate(coin_rects):
        if not coins_collected[i]:  # لا ترسم العملة إذا تم جمعها
            coin_image = coin_iamge[moves_coins]
            screen.blit(coin_image, coin_rect)

    moves_coins += 1
    if moves_coins >= len(coin_iamge):
        moves_coins = 0

thickness = 5
draw_circle = False
first_x = x
first_y = y

def correct_anw():
    global can_damjed,pouse,first_x,first_y,x,y,draw_circle
    draw_circle = True
    can_damjed = True
    pouse = False
    x = first_x
    y = first_y
def wrong_anw():
    global x,pouse,first_x,first_y,y,draw_circle
    x -= 100
    draw_circle = True
    pouse = False
    x =  first_x
    y = first_y
def pouse1():
    global x,y,x1,pouse,moves,y1,first_x,first_y
    first_x = x
    first_y = y
    x = 400
    y = 260
    x1 =820
    y1 = 250
    moves = 4
    pygame.display.update()
pause_menu = pygame.image.load(r'assets/Pause menu card.png')

play_img_pause = pygame.image.load(r'assets/Play button.png')
play_img_pause = pygame.transform.scale(play_img_pause,(350 , 130))
play_img_pause_rect = play_img_pause.get_rect(center=(screenw // 2, screenh // 2))

exit_pause = pygame.image.load(r'assets/Exit.png')
exit_pause = pygame.transform.scale(exit_pause,(350 , 130))
exit_pause_rect = exit_pause.get_rect(center=(screenw // 2, screenh // 2 + 200))

setting_pause = pygame.image.load(r'assets/Settings.png')
setting_pause = pygame.transform.scale(setting_pause,(350 , 130))
setting_pause_rect = setting_pause.get_rect(center=(screenw // 2, screenh // 2 + 100))
def draw_pause():
    global pause_menu, play_img_pause, play_img_pause_rect, exit_pause, setting_pause, exit_pause_rect, setting_pause_rect

    # Center the pause_menu image
    pause_menu_rect = pause_menu.get_rect(center=(screenw // 2, screenh // 2))
    screen.blit(pause_menu, pause_menu_rect.topleft)

    # Center the play_img_pause button
    play_img_pause_rect = play_img_pause.get_rect(center=(screenw // 2, screenh // 2- 130))
    screen.blit(play_img_pause, play_img_pause_rect.topleft)

    # Center the setting_pause button above the play_img_pause
    setting_pause_rect = setting_pause.get_rect(center=(screenw // 2, screenh // 2 ))
    screen.blit(setting_pause, setting_pause_rect.topleft)

    # Center the exit_pause button below the play_img_pause
    exit_pause_rect = exit_pause.get_rect(center=(screenw // 2, screenh // 2 + 130))
    screen.blit(exit_pause, exit_pause_rect.topleft)


def damjed():
    global x,y,can_damjed,draw_circle
    if can_damjed:
        x -= 150
        can_damjed = False
    draw_circle = True
def type2():
    global can_ask, answe, correct_rect, random_question, selected_question_text, colliding,can_health,rect33

    BLACK = (0, 0, 0)
    question_texts = [
        "6 x 3", "9 x 4", "8 x 7", "5 x 9",
        "7 x 6", "4 x 9", "3 x 8", "12 x 3",
        "11 x 5", "10 x 6", "7 x 8", "9 x 7",
        "6 x 9", "8 x 4", "12 x 2", "5 x 8"
    ]

    answers_dict = {
        "6 x 3": ['18', '16', '21'],
        "9 x 4": ['36', '32', '28'],
        "8 x 7": ['56', '49', '63'],
        "5 x 9": ['45', '40', '50'],
        "7 x 6": ['42', '48', '36'],
        "4 x 9": ['36', '32', '28'],
        "3 x 8": ['24', '27', '21'],
        "12 x 3": ['36', '30', '32'],
        "11 x 5": ['55', '50', '45'],
        "10 x 6": ['60', '56', '66'],
        "7 x 8": ['56', '42', '65'],
        "9 x 7": ['63', '72', '56'],
        "6 x 9": ['54', '45', '48'],
        "8 x 4": ['32', '28', '36'],
        "12 x 2": ['24', '20', '18'],
        "5 x 8": ['40', '48', '35']
    }

    if can_ask:
        # اختيار سؤال جديد عند استدعاء العائق
        random_index = random.randint(0, len(question_texts) - 1)
        random_question = font1.render(question_texts[random_index], True, BLACK)
        selected_question_text = question_texts[random_index]
        can_ask = False


    correct_answer = answers_dict[selected_question_text][-1]
    answers = answers_dict[selected_question_text]

    if answe:
        random.shuffle(answers)  # نعيد ترتيب الإجابات عشوائيًا
        answe = False

    num_anw = answers.index(correct_answer)
    correct = 100 + num_anw * 200
    correct_rect = pygame.Rect(x1, correct, 200, 195)

    rects33 = [pygame.Rect(x2 + 5, 110, 200, 190), pygame.Rect(x2 + 5, 310, 200, 190),
               pygame.Rect(x2 + 5, 510, 200, 190)]
    for h, answer in enumerate(answers):
        text = font2.render(answer, True, BLACK)
        screen.blit(text, (x2 + 70, 180 + h * 200))

    rects34 = [rect7 for rect7 in rects33 if rect7 and not player.colliderect(rect7)]

    if can_health and any(player.colliderect(rect132) for rect132 in rects34):
        can_health = False
    screen.blit(random_question, (600, 60))

options_pouse = False

enemy_moves = 0

player_think =  [pygame.image.load(f'Player think/{u}.png') for u in range(1,23)]
background = pygame.image.load(r'assets/Maras Bg.png')
bg_scroll = 0
scroll_speed = 50
Space = 0
speed_Space = 0.2
background_scroll_Big = 0
speed_scroll_BIg = 2
Big_Mountains = pygame.image.load(r'assets/Big Mountains.png')
Space_bg = pygame.image.load(r'assets/Space BG.jpg')
moves_player_think = 0

life_img = [pygame.image.load(f'health/{x}.png') for x in range(1 ,16)]
dead_img = [pygame.image.load(f'health/Dead {v}.png') for v in range(1,16)]
life = 0
dead = False
num_life = 3
num_dead = 0
if_dead = False

pause_button = pygame.image.load(r'assets/pause button.png')
pause_button = pygame.transform.scale(pause_button,(80,80))
pause_button_rect = pause_button.get_rect(topright=(1270, 10))
pause_button_rect.size = (80, 80)

def game_screen():
    global if_dead,dead,num_dead,num_life,life,rects33 ,player_think,moves_player_think,background_scroll_Big,Space,pouse,bg_scroll,scroll_speed,background,x, y, x1, y1,x2, ask, enemy_moves, moves, rockk_x, rockk_y, shild_moves, draw_circle, player_rect, can_damjed,can_ask,random_question,rock,liqued_brain,y_question
    if not options_pouse:
        screen.blit(background, (bg_scroll, 0))
        screen.blit(background, (bg_scroll + screenw, 0))

        # رسم 3 صور للحياة بجانب بعضها
        for i in range(3):  # نرسم 3 قلوب (حياة)
            if i < num_life:  # إذا كان القلب حي
                screen.blit(life_img[life], (10 + i * 100, 20))  # تعديل الموضع لكل صورة حياة
            else:  # إذا كان القلب ميت
                screen.blit(dead_img[life], (10 + i * 100, 20))  # رسم صورة الموت

        life += 1
        if life >= len(life_img):
            life = 0

        if dead:  # إذا كانت حالة الموت مفعلة
            if num_life > 0:  # إذا كانت هناك حياة متبقية
                num_life -= 1  # إنقاص عدد الحياة
                num_dead += 1  # زيادة عدد الموتى
                dead = False  # إيقاف حالة الموت بعد فقدان حياة

        if not pouse:
            screen.blit(Space_bg, (Space, 0))
            screen.blit(Space_bg, (Space + screenw, 0))
            Space -= speed_Space
            if Space <= -screenw:
                Space = 0
            # رسم الجبال الكبيرة
            screen.blit(Big_Mountains, (background_scroll_Big, 0))
            screen.blit(Big_Mountains, (background_scroll_Big + screenw, 0))
            background_scroll_Big -= speed_scroll_BIg
            if background_scroll_Big <= -screenw:
                background_scroll_Big = 0

            # رسم الخلفية العادية
            screen.blit(background, (bg_scroll, 0))
            screen.blit(background, (bg_scroll + screenw, 0))
            bg_scroll -= scroll_speed
            if abs(bg_scroll) >= screenw:
                bg_scroll = 0

            screen.blit(image_hero[moves], (x, y))

            if draw_circle:
                screen.blit(shild[shild_moves], (x - 75, y - 50))
                shild_moves += 1
                if shild_moves == len(shild) -1:
                    shild_moves = 0
        if y_question:
            x2 -= speed1
            rects3 = [pygame.Rect(x2 + 5, 100, 200, 190), pygame.Rect(x2 + 5, 300, 200, 190),
                      pygame.Rect(x2 + 5, 500, 200, 190)]
            for q,rect1 in enumerate(rects3):
                if correct_rect.colliderect(rect1):
                    rects3[q] = None
                    if rect1 is not None:
                        if player_rect.colliderect(rect1):
                            damjed()
                        screen.blit(boxs, rect1.topleft)
            type2()

        if rock:
            rockk_x -= scroll_speed
            if rockk_x < -300:
                rockk_x = screenw + 300
                rockk_y = y
                draw_circle = False
                can_damjed = True
                choice_obstacle()
            rock_image1 = rocck[0]
            screen.blit(rock_image1, (rockk_x, rockk_y))
            rock_rect2 = pygame.Rect(rockk_x, rockk_y, 250, 175)
            if can_damjed:
                if player_rect.colliderect(rock_rect2):
                    dead = True
                    damjed()

        screen.blit(enemy[enemy_moves], (x1, y1))
        if enemy_moves == 11:
            enemy_moves = 0
        else:
            enemy_moves += 1

        if not pouse:
            # رسم 3 صور للحياة بجانب بعضها
            for i in range(3):  # نرسم 3 قلوب (حياة)
                if i < num_life:  # إذا كان القلب حي
                    screen.blit(life_img[life], (10 + i * 100, 20))  # تعديل الموضع لكل صورة حياة
                else:  # إذا كان القلب ميت
                    screen.blit(dead_img[life], (10 + i * 100, 20))  # رسم صورة الموت

            life += 1
            if life >= len(life_img):
                life = 0

            if dead:  # إذا كانت حالة الموت مفعلة
                if num_life > 0:  # إذا كانت هناك حياة متبقية
                    num_life -= 1  # إنقاص عدد الحياة
                    num_dead += 1  # زيادة عدد الموتى
                    dead = False  # إيقاف حالة الموت بعد فقدان حياة

            moves += 1
            if moves == 15:
                moves = 0
            if y_question:
                x2 -= 10
                if x2 < -200:
                    x2 = screenw +100
                    draw_circle = False
                    can_ask = True
                    choice_obstacle()

            if liqued_brain:
                x1 -= 20
                if x1 < -200:
                    choice_obstacle()
                    x1 = screenw + 100
                    y1 = y
                    draw_circle = False
                    can_damjed = True

        if ask:
            screen.blit(questions_box, (500, 100))
            question_manager.draw()
            moves_player_think += 1
            if moves_player_think == 22:
                moves_player_think = 0
            screen.blit(player_think[moves_player_think],(350,220))

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if mouse_click[0]:  # إذا تم النقر بالزر الأيسر للماوس
            for i, rect in enumerate(question_manager.rects):
                if rect.collidepoint(mouse_pos):
                    if question_manager.check_answer(question_manager.answers[i]):
                        print("Correct answer!")
                        question_manager.randomize_question()  # تغيير السؤال عند الإجابة الصحيحة
                    else:
                        print("Incorrect answer!")

        #text = font.render(f"{coin_num}", True, (0, 26, 233))
        #screen.blit(text, (1100, 30))
        screen.blit(pause_button,pause_button_rect)
    if options_pouse:
        draw_pause()
    pygame.display.update()

jumping = False
jump_speed = 20
gravity = 0.8
jump_height = jump_speed

dash_active = False
dash_duration = 200
dash_speed = 30
can_dash = True
cooldown_time = 2000
cooldown_start = 0
acceleration = 0.6
max_speed = 15
deceleration = 0.1
collision_cooldown = 0
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button_rect.collidepoint(event.pos):
                options_pouse = True
            elif play_img_pause_rect.collidepoint(event.pos):
                options_pouse = False
            elif setting_pause_rect.collidepoint(event.pos):
                import setting
                from setting import sound  # تأخير الاستيراد هنا
                sound.play_clicking_sound()
                setting.sound_settings.run()
                continue
            elif exit_pause_rect.collidepoint(event.pos):
                import main
                main.main()
                continue
        if not options_pouse:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(question_manager.rects):
                    if rect.collidepoint(mouse_pos) and can_damjed:
                        selected_answer = question_manager.answers[i]
                        if question_manager.check_answer(selected_answer):
                            print("الإجابة صحيحة!")
                            correct_anw()
                            ask = False
                        else:
                            wrong_anw()
                            ask = False
                            print("الإجابة غير صحيحة!")
                            dead = True
    player_rect = pygame.Rect(x, y, 70, 140)

    if not pouse:
        keys = pygame.key.get_pressed()
        move_x = 0
        move_y = 0

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 0:
            speed = min(speed + acceleration, max_speed)
            move_x = -speed
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < screenw - 100:
            speed = min(speed + acceleration, max_speed)
            move_x = speed
        else:
            if speed > 0:
                speed = max(speed - deceleration, 0)

        if (keys[pygame.K_w] or keys[pygame.K_UP]) and y > 100:
            speed = min(speed + acceleration, max_speed)

            move_y = -speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y < screenh - 150:
            speed = min(speed + acceleration, max_speed)

            move_y = speed
        if keys[pygame.K_SPACE]:
            jumping = True
        dash_start_time = int()
        if keys[pygame.K_x] and can_dash:
            dash_active = True
            dash_start_time = pygame.time.get_ticks()
            can_dash = False

        if dash_active:

            dash_elapsed_time = pygame.time.get_ticks() - dash_start_time
            if dash_elapsed_time < dash_duration:
                if speed > 0:
                    x += move_x * (dash_speed / speed)
                    y += move_y * (dash_speed / speed)
                else:
                    x += move_x
                    y += move_y
            else:
                dash_active = False
                cooldown_start = pygame.time.get_ticks()
        else:
            x += move_x
            y += move_y


        if not can_dash:
            current_time = pygame.time.get_ticks()
            if current_time - cooldown_start >= cooldown_time:
                can_dash = True

        x = max(0, min(x, screenw - 100))
        y = max(0, min(y, screenh - 100))

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
        enemy_rect = pygame.Rect(x1, y1, 70, 140)

        if not draw_circle:
            if player_rect.colliderect(enemy_rect):
                pouse = True
                ask = True
                pouse1()

        if keys[pygame.K_y]:
            random_choice_obstacle = random.choice(["rock", "y_question", "liqued brian"])
            if random_choice_obstacle == "rock":
                rock = True
                liqued_brain = False
                y_question = False
            elif random_choice_obstacle == "liqued brian":
                rock = False
                liqued_brain = True
                y_question = False
            else:
                rock = False
                liqued_brain = False
                y_question = True
                can_ask = True

        if num_life == 0:
            if_dead = True
        if if_dead:
            import pouse_settings
            pouse_settings.dead()
            num_life = 3
            if_dead = False
            continue


    game_screen()
