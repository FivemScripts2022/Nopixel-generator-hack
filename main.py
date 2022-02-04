import sys, pygame
import numpy as np
import random


buttons = []
game_array = np.zeros((7,7))
def generate_solution(game_array):
    current_index = [0, 0]
    starting_index = [0, 0]
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
        # text
        self.text = text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        buttons.append(self)

    def change_text(self, newtext):
        self.text_surf = gui_font.render(newtext, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):

        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#04581F'
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                if self.pressed == True:
                    print('click')
                    self.pressed = False
                    print(self.position)
                    print(self.text)
                    print("below")
                    print([starting_position[0][0] + int(game_array[starting_position[0][0], starting_position[0][1]]), starting_position[0][1]])
                    if ([starting_position[0][0] + int(game_array[starting_position[0][0], starting_position[0][1]]), starting_position[0][1]] == self.position)\
                            or ([starting_position[0][0], starting_position[0][1] + int(game_array[starting_position[0][0], starting_position[0][1]])] == self.position)\
                            :
                        print("Yes")
                        del starting_position[0]
                        starting_position.insert(0, self.position)

                    elif ([starting_position[1][0] + int(game_array[starting_position[1][0], starting_position[1][1]]), starting_position[1][1]] == self.position)\
                            or ([starting_position[1][0], starting_position[1][1] + int(game_array[starting_position[1][0], starting_position[1][1]])] == self.position):
                        print("Yes")
                        del starting_position[1]
                        starting_position.insert(1, self.position)
                    else:
                        print("This is wrong")


        else:
            self.top_color = '#04581F'


pygame.init()
screen_width = 500
screen_height = 500
screen_size_ratio = 500/7
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)

game_array = generate_solution(game_array)
starting_position =[[0 + int(game_array[0,0]), 0], [0 , 0 + int(game_array[0,0])]]
print(starting_position)
for x in range(7):
    for y in range(7):
        button = Button(str(int((game_array[x,y]))), screen_size_ratio - 7 , screen_size_ratio - 7,
                        ((5 + x * screen_size_ratio), (5 + y * screen_size_ratio)), [x,y], game_array)

def buttons_draw():
    for b in buttons:
        b.draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#272E39')
    buttons_draw()

    pygame.display.update()
    clock.tick(60)
