import sys, pygame
import numpy as np
import random
import time
import itertools
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def generate_solution(game_array):
    available_direction = ["down", "right"]
    solution_array = game_array
    top_left_value = random.randint(1,3)
    solution_array[0, 0] = top_left_value
    original_direction = random.choice(available_direction)
    solution_steps = []
    if original_direction == "right":
        current_index = [0, top_left_value]
        starting_index = [0, top_left_value]
    else:
        current_index = [top_left_value, 0]
        starting_index = [top_left_value, 0]
    solution_steps.append(top_left_value)
    solution_steps.append(original_direction)

    print(current_index)
    while current_index != [6, 6]:
        if current_index[0] != 6 and current_index[1] != 6:
            direction = random.choice(available_direction)
            if direction == "right":
                available_moves = 7 - current_index[1] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0], current_index[1] + movement]
            elif direction == "down":
                available_moves = 7 - current_index[0] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0] + movement, current_index[1]]
        else:
            if current_index[0] == 6 and current_index[1] != 6:
                direction = "right"
                available_moves = 7 - current_index[1] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0], current_index[1] + movement]
            elif current_index[0] != 6 and current_index[1] == 6:
                direction = "down"
                available_moves = 7 - current_index[0] - 1
                movement = random.randint(1, available_moves)
                current_index = [current_index[0] + movement, current_index[1]]
            else:
                continue
        solution_steps.append(movement)
        solution_steps.append(direction)
        solution_array[starting_index[0], starting_index[1]] = movement
        starting_index = current_index
    for x in range(7):
        for y in range(7):
            if solution_array[x,y] == 0:
                solution_array[x, y] = random.randint(1,4)
    print(solution_steps)
    return(solution_array)


class Button:

    def __init__(self, text, width, height, pos, array_position, game_array):
        # Core attributes
        self.pressed = False
        self.position = array_position
        # top rectangle
        self.width = width
        self.height = height
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#04581F'
        self.game_array = game_array
        self.pos = pos
        self.clicked = False
        # text
        self.text = text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        buttons.append(self)

    def change_text(self, newtext):
        self.text_surf = gui_font.render(newtext, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, show_numbers, current_colour):
        if (self.position == [0 + (game_array[0, 0]), 0] or self.position == [0, 0 + (game_array[0, 0])]) and not(current_colour is None):
            pygame.draw.rect(screen, current_colour, self.top_rect)
            screen.blit(self.text_surf, self.text_rect)
            self.check_click()
        else:
            if self.position == [0,0]:
                top_left_image_url = resource_path('top_left.png')
                top_left_image = pygame.image.load(top_left_image_url).convert_alpha()
                top_left_image = pygame.transform.scale(top_left_image, (self.height, self.width) )
                self.image_rect = top_left_image.get_rect(topleft=(self.pos))
                screen.blit(top_left_image,(self.image_rect))
                self.check_click()
            elif self.position == [6,6]:
                bottom_right_image_url = resource_path('bottom_right.png')
                bottom_right_image = pygame.image.load(bottom_right_image_url).convert_alpha()
                bottom_right_image = pygame.transform.scale(bottom_right_image, (self.height, self.width))
                self.image_rect = bottom_right_image.get_rect(topleft=self.pos)
                screen.blit(bottom_right_image,(self.image_rect))
                self.check_click()
            elif self.position in starting_position and show_numbers == True:
                pygame.draw.rect(screen, self.top_color, self.top_rect)
                screen.blit(self.text_surf, self.text_rect)
                self.check_click()

            elif show_numbers:
                pygame.draw.rect(screen, self.top_color, self.top_rect)
                screen.blit(self.text_surf, self.text_rect)
                self.check_click()
            else:
                pygame.draw.rect(screen, self.top_color, self.top_rect)
                self.check_click()


    def check_click(self):
        global starting_position_new_version
        global wrong_counter
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                if self.pressed and not self.clicked:
                    self.pressed = False
                    """
                    if ([starting_position[0][0] + int(game_array[starting_position[0][0], starting_position[0][1]]), starting_position[0][1]] == self.position)\
                            or ([starting_position[0][0], starting_position[0][1] + int(game_array[starting_position[0][0], starting_position[0][1]])] == self.position)\
                            :
                        del starting_position[0]
                        starting_position.insert(0, self.position)
                        self.top_color = '#00FF00'
                    elif ([starting_position[1][0] + int(game_array[starting_position[1][0], starting_position[1][1]]), starting_position[1][1]] == self.position)\
                            or ([starting_position[1][0], starting_position[1][1] + int(game_array[starting_position[1][0], starting_position[1][1]])] == self.position):
                        del starting_position[1]
                        starting_position.insert(1, self.position)
                        self.top_color = '#00FF00'
                    """
                    if ([starting_position_new_version[0] + int(game_array[starting_position_new_version[0], starting_position_new_version[1]]),
                         starting_position_new_version[1]] == self.position) \
                            or ([starting_position_new_version[0], starting_position_new_version[1] + int(
                        game_array[starting_position_new_version[0], starting_position_new_version[1]])] == self.position) \
                            :
                        starting_position_new_version = self.position
                        starting_position.insert(0, self.position)
                        self.top_color = '#00FF00'
                    elif ([starting_position_new_version[0] + int(game_array[starting_position_new_version[0], starting_position_new_version[1]]),
                           starting_position_new_version[1]] == self.position) \
                            or ([starting_position_new_version[0], starting_position_new_version[1] + int(
                        game_array[starting_position_new_version[0], starting_position_new_version[1]])] == self.position):
                        starting_position_new_version = self.position
                        self.top_color = '#00FF00'
                    else:
                            self.top_color = '#FF0000'
                            wrong_counter += 1

                    self.clicked = True
        for i in starting_position:
            if i == [6, 6]:
                bg_url = resource_path('network access granted.png')
                bg = pygame.image.load(bg_url)
                bg = pygame.transform.scale(bg, (screen.get_height(), screen.get_width()))
                screen.blit(bg, (0, 0))
        if wrong_counter == 3:
            failed_bg_url = resource_path('network_failed.png')
            failed_bg = pygame.image.load(failed_bg_url)
            failed_bg = pygame.transform.scale(failed_bg, (screen.get_height(), screen.get_width()))
            screen.blit(failed_bg, (0, 0))


def buttons_draw(condition, current_color):
    for b in buttons:
        b.draw(condition, current_color)


buttons = []
game_array = np.zeros((7,7))
wrong_counter = 0

pygame.init()
screen_width = 622
screen_height = 622
screen_size_ratio = 622/7
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)

game_array = generate_solution(game_array)
starting_position = [[0], [0 , 0 + int(game_array[0, 0])]]
starting_position_new_version = [0, 0]
print(starting_position)
colors = itertools.cycle(['#08581D', '#75D26E'])
base_color = next(colors)
next_color = next(colors)
current_color = base_color
FPS = 60
change_every_x_seconds = 0.5
number_of_steps = change_every_x_seconds * FPS
step = 1

for x in range(7):
    for y in range(7):
        button = Button(str(int((game_array[x, y]))), screen_size_ratio - 7 , screen_size_ratio - 7,
                        ((5 + x * screen_size_ratio), (5 + y * screen_size_ratio)), [x, y], game_array)

start_ticks=pygame.time.get_ticks()
while True:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#272E39')
    if seconds < 3:
        failed_bg_url = resource_path('start.png')
        failed_bg = pygame.image.load(failed_bg_url)
        failed_bg = pygame.transform.scale(failed_bg, (screen.get_height(), screen.get_width()))
        screen.blit(failed_bg, (0, 0))

    elif seconds < 9:
        step += 1
        if step < number_of_steps:
            # (y-x)/number_of_steps calculates the amount of change per step required to
            # fade one channel of the old color to the new color
            # We multiply it with the current step counter
            current_color = [x + (((y - x) / number_of_steps) * step) for x, y in
                             zip(pygame.color.Color(base_color), pygame.color.Color(next_color))]
        else:
            step = 1
            base_color = next_color
            next_color = next(colors)
        buttons_draw(True, current_color)
        first = True
    elif seconds < 18:
        buttons_draw(False, None)

    else:
        failed_bg_url = resource_path('network_failed.png')
        failed_bg = pygame.image.load(failed_bg_url)
        failed_bg = pygame.transform.scale(failed_bg, (screen.get_height(), screen.get_width()))
        screen.blit(failed_bg, (0, 0))
    pygame.display.update()
    clock.tick(60)
