import pygame
import sys
from moviepy.editor import VideoFileClip
import numpy as np

def play_credit_scene(screen_width, screen_height):
    pygame.init()

    # إعداد الشاشة
    video_screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Credit Scene")

    # تحميل الفيديو
    credit_scene = VideoFileClip('assets/Credit Scene3.mp4')
    credit_scene.preview()
    pygame.mixer.quit()
    fps = credit_scene.fps

    # إعداد كائن الساعة للتحكم في معدل الإطارات
    clock = pygame.time.Clock()

    # عرض الفيديو
    for frame in credit_scene.iter_frames(fps=fps):
        frame = np.array(frame)  # تحويل الإطار إلى مصفوفة NumPy
        frame = np.rot90(frame)  # تدوير الإطار للتأكد من التوافق مع Pygame
        frame = pygame.surfarray.make_surface(frame)  # تحويل المصفوفة إلى سطح Pygame
        video_screen.blit(frame, (0, 0))
        pygame.display.update()

        # معالجة الأحداث أثناء عرض الفيديو
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(fps)  # التحكم في معدل الإطارات للتأكد من عرض الفيديو بشكل صحيح

    pygame.quit()
