import pygame
import sys
from game import Game

pygame.init()

pygame.mixer.music.load("music/src_commonMain_resources_music_monkey_island_puzzler.mp3")
win_sound = pygame.mixer.Sound("sound/winbrass-39632.mp3")

title_font = pygame.font.Font("fonts/KOLAK.otf", 34)
time_font = pygame.font.Font("fonts/Vintage.ttf", 23)

Score_surface = title_font.render("Score", True, (255, 255, 255))
next_surface = title_font.render("Next", True, (255, 255, 255))

title_font = pygame.font.Font("fonts/KOLAK.otf", 30)

BestScore_surface = title_font.render("BestScore", True, (255, 255, 255))

title_font = pygame.font.Font("fonts/Salium.ttf", 40)

game_over_surface = title_font.render("GAME OVER", True, (0, 0, 0))

title_font = pygame.font.Font("fonts/KOLAK.otf", 24)

pause_surface = title_font.render("Pause : Space", True, (255, 255, 255))

exit_surface = title_font.render("ESC : EXIT", True, (255, 255, 255))

title_font = pygame.font.Font("fonts/KOLAK.otf", 30)

paused_surface = title_font.render("PAUSED", True, (0, 0, 0))

start_font = pygame.font.Font("fonts/Vintage.ttf", 25)

start_text = start_font.render("START", True, (100, 40, 0))

exit_font = pygame.font.Font("fonts/Vintage.ttf", 25)

exit_text = start_font.render("EXIT", True, (100, 40, 0))

score_rect = pygame.Rect(520, 75, 158, 60)
next_rect = pygame.Rect(520, 280, 170, 170)
start_rect = pygame.Rect(260, 290, 170, 60)
best_score_rect = pygame.Rect(520, 175, 158, 60)
exit_rect = pygame.Rect(260, 350, 170, 60)
music_rect = pygame.Rect(160, 20, 70, 70)
sound_rect = pygame.Rect(90, 20, 70, 70)
reset_rect = pygame.Rect(165, 375, 70, 70)
next_level_rect = pygame.Rect(265, 380, 100, 60)
setting_rect = pygame.Rect(20, 20, 70, 70)

screen = pygame.display.set_mode((700, 640))
pygame.display.set_caption("Donuts Crush game")

icon = pygame.image.load("icon/icon.png")
pygame.display.set_icon(icon)

background_image = pygame.image.load("images/background.png").convert_alpha()
background_image = pygame.transform.smoothscale(background_image, (500, 640))

background_of_back_image = pygame.image.load("images/1.jpg").convert_alpha()
background_of_back_image = pygame.transform.smoothscale(background_of_back_image, (640, 1280))

box_image = pygame.image.load("images/message_box.9.png").convert_alpha()
box_image = pygame.transform.smoothscale(box_image, (170, 60))

box_image_ = pygame.image.load("images/message_box.9.png").convert_alpha()
box_image_ = pygame.transform.smoothscale(box_image_, (100, 60))

game_over_box_image = pygame.image.load("images/message_box.9.png").convert_alpha()
game_over_box_image = pygame.transform.smoothscale(game_over_box_image, (260, 60))

next_box_image = pygame.image.load("images/message_box.9.png").convert_alpha()
next_box_image = pygame.transform.smoothscale(next_box_image, (170, 170))

setting_image_off = pygame.image.load("images/gui_settings.png").convert_alpha()
setting_image_off = pygame.transform.smoothscale(setting_image_off, (70, 70))
setting_image_on = pygame.image.load("images/gui_settings_on.png").convert_alpha()
setting_image_on = pygame.transform.smoothscale(setting_image_on, (70, 70))

music_image_on = pygame.image.load("images/gui_music_on.png").convert_alpha()
music_image_on = pygame.transform.smoothscale(music_image_on, (70, 70))
music_image_off = pygame.image.load("images/gui_music_off.png").convert_alpha()
music_image_off = pygame.transform.smoothscale(music_image_off, (70, 70))

sound_image_on = pygame.image.load("images/gui_sound_on.png").convert_alpha()
sound_image_on = pygame.transform.smoothscale(sound_image_on, (70, 70))
sound_image_off = pygame.image.load("images/gui_sound_off.png").convert_alpha()
sound_image_off = pygame.transform.smoothscale(sound_image_off, (70, 70))

reset_image = pygame.image.load("images/gui_restart_click.png").convert_alpha()
reset_image = pygame.transform.smoothscale(reset_image, (70, 70))

start_image = pygame.image.load("images/3.jpg").convert_alpha()
start_image = pygame.transform.smoothscale(start_image, (700, 640))

start_image_icon = pygame.image.load("images/22.png").convert_alpha()
start_image_icon = pygame.transform.smoothscale(start_image_icon, (200, 200))


def format_time(seconds):
    minutes = 0
    seconds = seconds % 60 - (game.level - 1) * 5
    if not (minutes < 0 or seconds < 0):
        return f"{minutes:01}:{seconds:02}"


def draw_timer(screen, time_left):
    text = time_font.render(time_left, True, (0, 0, 0))
    screen.blit(text, (10, 10))


game = Game()

clock = pygame.time.Clock()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, game.get_speed_for_each_level())

game_started = False
paused = False
music = True
setting = False
Exit = False
time = False
next_level = False

start_time = 60
current_time = start_time
start_ticks = pygame.time.get_ticks()
pause_total_time = 0
pause_start_ticks = 0

music_image = music_image_on
sound_image = sound_image_on
setting_image = setting_image_off

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or Exit == 1:
            pygame.quit()
            sys.exit()

        if not game_started:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    if music:
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.2)
                    game_started = True
                if exit_rect.collidepoint(event.pos):
                    Exit = True
                if setting_rect.collidepoint(event.pos):
                    if setting:
                        setting = False
                        setting_image = setting_image_off
                    else:
                        setting = True
                        setting_image = setting_image_on
                if sound_rect.collidepoint(event.pos) and setting == 1:
                    if not game.sound:
                        game.sound = True
                        sound_image = sound_image_on
                    else:
                        game.sound = False
                        sound_image = sound_image_off

                if music_rect.collidepoint(event.pos) and setting == 1:
                    if not music:
                        music = True
                        music_image = music_image_on
                    else:
                        music = False
                        music_image = music_image_off

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rect.collidepoint(event.pos):
                    if game.game_over:
                        game.game_over = False
                        game.reset()
                        current_time = start_time
                        start_ticks = pygame.time.get_ticks()
                        pause_total_time = 0
                        pause_start_ticks = 0
                        time = False
                if next_level_rect.collidepoint(event.pos) and next_level == 1:
                    if game.game_over:
                        game.game_over = False
                        game.reset()
                        current_time = start_time
                        start_ticks = pygame.time.get_ticks()
                        pause_total_time = 0
                        pause_start_ticks = 0
                        time = False
                        game.level = game.level + 1
                        if game.level > 3:
                            game.level = 1
                        with open("level.txt", "w") as wfp:
                            wfp.write(str(game.level))
                        pygame.time.set_timer(GAME_UPDATE, game.get_speed_for_each_level())
                        next_level = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.game_over == 0:
                    paused = not paused
                    if paused:
                        pause_start_ticks = pygame.time.get_ticks()
                    else:
                        pause_total_time += pygame.time.get_ticks() - pause_start_ticks
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT and game.game_over == 0 and time == 0:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == 0 and time == 0:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == 0 and time == 0:
                    game.move_down()
            if not paused:
                if event.type == GAME_UPDATE and game.game_over == 0 and time == 0:
                    game.move_down()

    level_surface = title_font.render(f"Level {game.level}", True, (0, 0, 0))

    if game_started == 1:
        if paused == 0:
            if time == 0:
                seconds_elapsed = (pygame.time.get_ticks() - start_ticks - pause_total_time) / 1000
                current_time = start_time - int(seconds_elapsed)
                if current_time - (game.level - 1) * 5 <= 0:
                    time = 1
                    win_sound.play()

                if game.score >= game.best_score:
                    with open("score.txt", "w") as wfp:
                        wfp.write(str(game.score))
                game.best_score = game.get_best_socre()
                score_value_surface = title_font.render(str(game.score), True, (0, 0, 0))
                best_score_value_surface = title_font.render(str(game.best_score), True, (0, 0, 0))

                screen.blit(background_of_back_image, (80, 0))

                screen.blit(box_image, (0, 0))

                screen.blit(background_image, (0, 0))
                screen.blit(Score_surface, (545, 40))
                screen.blit(level_surface, (200, 30))
                draw_timer(screen, format_time(current_time))
                screen.blit(BestScore_surface, (528, 140))
                screen.blit(next_surface, (558, 240))
                screen.blit(pause_surface, (520, 510))
                screen.blit(exit_surface, (540, 550))
                screen.blit(box_image, score_rect)
                screen.blit(box_image, best_score_rect)
                screen.blit(next_box_image, next_rect)

                screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                              centery=score_rect.centery))
                screen.blit(best_score_value_surface, best_score_value_surface.get_rect(centerx=best_score_rect.centerx,
                                                                                        centery=best_score_rect.centery))
                game.draw(screen)

                if game.game_over == 1:
                    time = 1
                    screen.blit(game_over_box_image, (140, 315))
                    screen.blit(game_over_surface, (150, 320))
                    screen.blit(reset_image, reset_rect)
            elif game.game_over != 1:
                next_level = True
                game.game_over = 1
                time = 1
                screen.blit(game_over_box_image, (140, 315))
                screen.blit(game_over_surface, (150, 320))
                screen.blit(reset_image, reset_rect)
                screen.blit(box_image_, next_level_rect)
                screen.blit(title_font.render("Next", True, (0, 0, 0)), (279, 390))

        else:
            screen.blit(paused_surface, (200, 300))
    else:
        screen.blit(start_image, (0, 0))
        screen.blit(start_image_icon, (240, 70))

        screen.blit(box_image, start_rect)
        screen.blit(start_text, (277, 295))

        screen.blit(box_image, exit_rect)
        screen.blit(exit_text, (290, 355))

        screen.blit(setting_image, setting_rect)

        if setting == 1:
            screen.blit(sound_image, sound_rect)

            screen.blit(music_image, music_rect)

    pygame.display.update()
    clock.tick(60)
