import pygame
import os
try:
    from snake import Snake
    from fruit import Fruit
except ImportError:
    from .snake import Snake
    from .fruit import Fruit


class Game():
    def __init__(self, width, height, rows=20):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.rows = rows
        self.score = 0
        self.entities = []
        self.spacing_x = self.width // self.rows
        self.spacing_y = (self.height//10*9) // self.rows
        self.game = True
        self.clock = pygame.time.Clock()
        self.score_font = pygame.font.Font(None, 50)
        with open(os.path.join("snake-game", "high_score.txt"), "r") as file:
            self.high_score = int(file.read())
        
        self.snake = Snake(body=[], rows=self.rows)
        self.entities.append(self.snake)
        self.fruit = Fruit(rows=self.rows)
        self.entities.append(self.fruit)

        pygame.display.set_caption("Snake Game")

        self.window = pygame.display.set_mode((self.width, self.height))
        self.score_surface = pygame.Surface((self.width, self.height // 10))
        self.game_surface = pygame.Surface((self.width, self.height//10 * 9))

        self.game_loop()

    def game_loop(self):
        ''' Starts the game loop where everything happens '''
        while self.game:
            pygame.time.delay(50)
            self.clock.tick(10)
            self.snake.move("")
            self.check_death()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.handle_keys(event.key)

    def draw(self):
        ''' Draws game-related items on the window '''
        self.draw_score()
        self.draw_game()
        pygame.display.flip()

    def draw_score(self):
        ''' Displays game score '''
        if self.score > self.high_score:
            self.high_score = self.score
            with open(os.path.join("snake-game", "high_score.txt"), "w") as file:
                file.write(str(self.high_score))
        self.score_surface.fill((0, 0, 0))
        text = self.score_font.render(f"High Score: {self.high_score}       Score: {self.score}",
                           1, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.score_surface.get_width() // 2,
                           self.score_surface.get_height() // 2)

        self.score_surface.blit(text, textRect)
        self.window.blit(self.score_surface, (0, 0))

    def draw_game(self):
        ''' Displays rest of game '''
        self.game_surface.fill((0, 0, 0))
        for count_x in range(self.rows):
            for count_y in range(self.rows):
                rect = pygame.Rect((count_x * self.spacing_x, count_y * self.spacing_y), (self.spacing_x, self.spacing_y))
                pygame.draw.rect(self.game_surface, (255, 255, 255), rect, 1)

        for entity in self.entities:
            if isinstance(entity, Snake):
                for cube in entity.body:
                    pygame.draw.rect(self.game_surface, (0, 255, 0),
                                     (cube.x * self.spacing_x,
                                      cube.y * self.spacing_y,
                                      self.spacing_x - 1, self.spacing_y - 1))
                    if self.fruit.is_collide(cube):
                        self.snake.extend()
                        self.fruit.new_fruit()
                        self.score += 1
            elif isinstance(entity, Fruit):
                pygame.draw.rect(self.game_surface, (255, 0, 0),
                                 (entity.x * self.spacing_x,
                                  entity.y * self.spacing_y,
                                  self.spacing_x - 1, self.spacing_y - 1))

        self.window.blit(self.game_surface, (0, self.score_surface.get_height()))

    def handle_keys(self, key):
        ''' Handles key input. Moves snake using arrow keys or WASD '''
        if key == pygame.K_UP:   # Up arrow key
            self.snake.move("up")
        elif key == pygame.K_DOWN:  # Down arrow key
            self.snake.move("down")
        elif key == pygame.K_RIGHT:  # Right arrow key
            self.snake.move("right")
        elif key == pygame.K_LEFT:  # Left arrow key
            self.snake.move("left")
        elif key == pygame.K_w:  # W key
            self.snake.move("up")
        elif key == pygame.K_a:   # A key
            self.snake.move("left")
        elif key == pygame.K_s:  # S key
            self.snake.move("down")
        elif key == pygame.K_d:  # D key
            self.snake.move("right")
        elif key == pygame.K_x or key == pygame.K_ESCAPE:  # X key or Esc
            self.game = False
            pygame.quit()

    def check_death(self):
        ''' Checks whether snake is dead. If so, resets stats. '''
        # Check whether snake head occupies same space as part of snake body
        head = self.snake.head
        bodyPos = []
        if len(self.snake.body) > 1:
            for c in self.snake.body[1:]:
                bodyPos.append((c.x, c.y))
            if (head.x, head.y) in bodyPos:
                print(f"Your final score was {self.score}")
                self.score = 0
                self.entities = []
                del self.snake
                self.snake = Snake(body=[], rows=self.rows)
                self.fruit.new_fruit()
                self.entities.append(self.snake)
                self.entities.append(self.fruit)
