import pygame
import random
import sys
from Credit_scene import play_credit_scene

pygame.init()

# إعداد الشاشة
screenw = 1280
screenh = 720
screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("game")
background = pygame.image.load(r'assets/Maras Bg.png')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 60)

# الألوان
GREEN = (100, 200, 3)
GREEN_HIGHLIGHT = (50, 255, 50)
RED = (200, 0, 0)

speed = 10
ask = False
rock = False
y_question = False

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

colliding = True
rects = []
random_question = ""
selected_question_text = ""
font2 = pygame.font.Font(None,70)
can_ask = True
image_hero1 = [pygame.image.load(f'img hero/{i * 1}.png') for i in range (1,15)]
image_hero = [pygame.transform.scale(image, (100 ,150 )) for image in image_hero1]
enemy_move = 0
enemy1 = [pygame.image.load(f'enemy/{z * 1}.png') for z in range (1 ,13)]
moves += 1
if moves == 15:
    moves = 0
enemy_moves = 0


rocks1 = pygame.image.load("assets/Big ROCK.png")
rocck = [pygame.transform.scale(rocks1, (250, 250))]

shild1 = [pygame.image.load(f"assets/Shield {i*1}.png") for i in range(1,5)]
shild = [pygame.transform.scale(shild1[i],(250,250) )for i in range(1,4)]

boxs = pygame.image.load(r"assets/box.png")
boxs = pygame.transform.scale(boxs, (200, 195))

x= 100
y = 300
# إعدادات الصخور
rockk_x, rockk_y = screenw + 200, y
rock_speed = 20
liqued_brain = True
def choice_obstacle():
    global y_question, liqued_brain, rock
    y_question = False
    liqued_brain = False
    rock = False
    rand_choice_obstacle = random.choice(['y_question', 'liqued_brain', 'rock'])
    if rand_choice_obstacle == 'liqued_brain':
        y_question = False
        liqued_brain = True
        rock = False
    elif rand_choice_obstacle == 'y_question':
        y_question = True
        liqued_brain = False
        rock = False
    elif rand_choice_obstacle == 'rock':
        y_question = False
        liqued_brain = False
        rock = True
choice_obstacle()

questions_box = pygame.image.load(r"assets/question box.png")
can_damjed = True
pouse = False
# كلاس الأسئلة
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
        for i1, rect1 in enumerate(self.rects):
            color = GREEN_HIGHLIGHT if rect1.collidepoint(mouse_pos2) else GREEN
            text = font.render(self.answers[i1], True, color)
            screen.blit(text, (rect1.x, rect1.y))

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
radius = 80
# سمك الحدود
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
def damjed():
    global x,y,can_damjed,draw_circle
    if can_damjed:
        x -= 150
        can_damjed = False
    draw_circle = True
def type2():
    global can_ask, answe, correct_rect, random_question, selected_question_text, colliding,can_health

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
    for rect1f in rects33:
        if rect1f is not None:
            screen.blit(boxs, rect1f.topleft)

    for h, answer in enumerate(answers):
        text = font2.render(answer, True, BLACK)
        screen.blit(text, (x2 + 70, 180 + h * 200))

    rects34 = [rect7 for rect7 in rects33 if rect7 and not player.colliderect(rect7)]

    if can_health and any(player.colliderect(rect132) for rect132 in rects34):
        can_health = False
    screen.blit(random_question, (600, 60))
# إعدادات العدو
x1 = screenw + 200
y1 = y
moves = 1
shild_moves = 0


background_scroll = 0
speed_scroll = 30
Space = 0
speed_Space = 0.2
background_scroll_Big = 0
speed_scroll_BIg = 2
Big_Mountains = pygame.image.load(r'assets/Big Mountains.png')
Space_bg = pygame.image.load(r'assets/Space BG.jpg')


def game_screen():
    global speed_scroll, Space, speed_Space, background_scroll, x, y, x1, y1, ask, enemy_moves, moves, rockk_x, rockk_y, shild_moves, draw_circle, player_rect, can_damjed, background_scroll_Big
    if not pouse:
        moves += 1
        if moves == 14:
            moves = 0
        # رسم خلفية الفضاء
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
        screen.blit(background, (background_scroll, 0))
        screen.blit(background, (background_scroll + screenw, 0))
        background_scroll -= speed_scroll
        if abs(background_scroll) >= screenw:
            background_scroll = 0

        screen.blit(image_hero[moves], (x, y))

        if draw_circle:
            screen.blit(shild[shild_moves], (x - 75, y - 50))
            shild_moves += int(0.9)
            if shild_moves == 4:
                shild_moves = 0

        x1 -= 15
        if x1 < -200:
            x1 = screenw + 100
            y1 = y
            draw_circle = False
            can_damjed = True

        if rock:
            rockk_x -= speed_scroll
            if rockk_x < -300:
                rockk_x = screenw + 300
                rockk_y = y
            rock_image = rocck[0]
            screen.blit(rock_image, (rockk_x, rockk_y))
            rock_rect = pygame.Rect(rockk_x, rockk_y, 250, 175)
            if can_damjed and player_rect.colliderect(rock_rect):
                damjed()

        if liqued_brain:
            screen.blit(enemy1[enemy_moves], (x1, y1))
            if enemy_moves == 11:
                enemy_moves = 0
            else:
                enemy_moves += 1

    if ask:
        screen.blit(questions_box, (500, 100))
        question_manager.draw()

        pygame.display.update()

    pygame.display.update()
start_time = pygame.time.get_ticks()
video_played = False

jumping = False
jump_speed = 15
gravity = 1
jump_height = jump_speed

dash_active = False
dash_duration = 200
dash_speed = 20
can_dash = True
cooldown_time = 2000
cooldown_start = 0
acceleration = 0.5
max_speed = 10
deceleration = 0.1
collision_cooldown = 0
running = True
while running:
    clock.tick(30)
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000

    if elapsed_time >= 60 and not video_played:
        play_credit_scene(screenw, screenh)
        video_played = True

    player_rect = pygame.Rect(x, y, 70, 140)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(question_manager.rects):
                if rect.collidepoint(mouse_pos):
                    selected_answer = question_manager.answers[i]
                    if question_manager.check_answer(selected_answer):
                        correct_anw()
                        ask = False
                    else:
                        wrong_anw()
                        ask = False

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
            move_y = -speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y < screenh - 150:
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
                pouse1()

        if x1 == -300 or rockk_x == -300 or x2 == -300:
            choice_obstacle()

        if y_question:
            x2 -= speed1
            rects3 = [pygame.Rect(x2 + 5, 100, 200, 190), pygame.Rect(x2 + 5, 300, 200, 190),
                      pygame.Rect(x2 + 5, 500, 200, 190)]
            for rect1 in rects3:
                if rect1 is not None:
                    screen.blit(boxs, rect1.topleft)
            type2()
        if rock:
            rockk_x -= speed1
            rock_image = rocck[0]
            screen.blit(rock_image, (rockk_x, rockk_y))
            rock_rect = pygame.Rect(rockk_x, rockk_y, 250, 175)
            if can_damjed and player_rect.colliderect(rock_rect):
                damjed()

        if liqued_brain:
            if not draw_circle:
                if player_rect.colliderect(player):
                    pouse = True
                    pouse1()
                    ask = True

    game_screen()
