import pygame
from . import snake
from . import fruit


class Game():
    def __init__(self, width, height, rows=20, score=0, entities=[],
                 fullscreen=False):
        self.width = width
        self.height = height
        self.rows = rows
        self.score = score
        self.highScore = 0
        self.entities = entities
        self.spacingX = self.width // self.rows
        self.spacingY = (self.height//10*9) // self.rows
        self.game = True
        self.clock = pygame.time.Clock()
        self.fullscreen = fullscreen

        pygame.init()
        pygame.font.init()

        pygame.display.set_caption("Snake Game")

        if self.fullscreen:
            self.width = pygame.display.Info().current_w
            self.height = pygame.display.Info().current_h
            self.spacingX = self.width // self.rows
            self.spacingY = (self.height//10*9) // self.rows

            self.window = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
            # pygame.display.toggle_fullscreen()
            # self.width, self.height = self.window.get_size()

        else:
            self.window = pygame.display.set_mode((self.width, self.height))
        # pygame.display.set_icon()


        self.scoreSurface = pygame.Surface((self.width,
                                            self.height // 10))
        self.gameSurface = pygame.Surface((self.width, self.height//10*9))

        self.snake = snake.Snake(body=[], rows=self.rows)
        self.entities.append(self.snake)
        self.fruit = fruit.Fruit(rows=self.rows)
        self.entities.append(self.fruit)

        self.gameLoop()

    def gameLoop(self):
        ''' Starts the game loop where everything happens '''
        while self.game:
            pygame.time.delay(50)
            self.clock.tick(10)
            self.snake.move("")
            self.checkDeath()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.handleKeys(event.key)

    def draw(self):
        ''' Draws game-related items on the window '''
        self.drawScore()
        self.drawGame()
        pygame.display.flip()

    def drawScore(self):
        ''' Displays game score '''
        if self.score > self.highScore:
            self.highScore = self.score
        self.scoreSurface.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(f"High Score: {self.highScore}       Score: {self.score}",
                           1, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.scoreSurface.get_width() // 2,
                           self.scoreSurface.get_height() // 2)

        self.scoreSurface.blit(text, textRect)
        self.window.blit(self.scoreSurface, (0, 0))

    def drawGame(self):
        ''' Displays rest of game '''
        self.gameSurface.fill((0, 0, 0))
        for num in range(self.rows):
            pygame.draw.line(self.gameSurface, (255, 255, 255),
                             (num * self.spacingX, 0),
                             (num * self.spacingX, self.height))
            pygame.draw.line(self.gameSurface, (255, 255, 255),
                             (0, num * self.spacingY),
                             (self.width, num * self.spacingY))

        for entity in self.entities:
            if isinstance(entity, snake.Snake):
                for c in entity.body:
                    pygame.draw.rect(self.gameSurface, (0, 255, 0),
                                     (c.x * self.spacingX,
                                      c.y * self.spacingY,
                                      self.spacingX, self.spacingY))
                    if self.fruit.isCollide(c):
                        self.snake.extend()
                        self.fruit.newFruit()
                        self.score += 1
            elif isinstance(entity, fruit.Fruit):
                pygame.draw.rect(self.gameSurface, (255, 0, 0),
                                 (entity.x * self.spacingX,
                                  entity.y * self.spacingY,
                                  self.spacingX, self.spacingY))

        self.window.blit(self.gameSurface, (0, self.scoreSurface.get_height()))

    def handleKeys(self, key):
        ''' Handles key input. Moves snake using arrow keys or WASD '''
        if key == 273:   # Up arrow key
            self.snake.move("up")
        elif key == 274:  # Down arrow key
            self.snake.move("down")
        elif key == 275:  # Right arrow key
            self.snake.move("right")
        elif key == 276:  # Left arrow key
            self.snake.move("left")
        elif key == 119:  # W key
            self.snake.move("up")
        elif key == 97:   # A key
            self.snake.move("left")
        elif key == 115:  # S key
            self.snake.move("down")
        elif key == 100:  # D key
            self.snake.move("right")
        elif key == 120:  # X key
            self.game = False
            pygame.quit()

    def checkDeath(self):
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
                self.snake = snake.Snake(body=[], rows=self.rows)
                self.fruit.newFruit()
                self.entities.append(self.snake)
                self.entities.append(self.fruit)
