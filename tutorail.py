import pygame
import time
import random
import math
pygame.init()

WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks!")

SCORE_FONT = pygame.font.SysFont("comics", 50)

COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 255, 255),
    (255, 165, 0),
    (255, 255, 255),
    (230, 230, 250),
    (255, 192, 203)
]

FPS = 60


class Projectile:
    WIDTH = 5
    HEIGHT = 10
    ALPHA_DECREMENT = 3

    def __init__(self, x, y, x_vel, y_vel, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.alpha = 255

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.alpha = max(0, self.alpha - self.ALPHA_DECREMENT)

    def draw(self, win):
        self.draw_rect_alpha(win, self.color + (self.alpha,), (self.x, self.y, self.WIDTH, self.HEIGHT))

    @staticmethod
    def draw_rect_alpha(surface, color, rect):
        # i have created an empty surface
        shap_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        # and pass that into the rectangle
        pygame.draw.rect(shap_surf, color, shap_surf.get_rect())
        surface.blit(shap_surf, rect)


class Firework:
    RADIUS = 10
    MAX_PROJECTILES = 50
    MIN_PROJECTILES = 25
    PROJECTILES_VEL = 4

    def __init__(self, x, y, y_vel, explode_height, color):
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.explode_height = explode_height
        self.color = color
        self.projectiles = []
        self.exploded = False

    def explode(self):
        self.exploded = True
        num_projectiles = random.randrange(self.MIN_PROJECTILES, self.MAX_PROJECTILES)
        self.create_circular_projectiles(num_projectiles)


    def create_circular_projectiles(self, num_projectiles):
        # get the angle different
        angle_dif = math.pi*4 / num_projectiles
        current_angle = 0
        # why we give like this one will go up and will go down
        vel = random.randrange(self.PROJECTILES_VEL - 1, self.PROJECTILES_VEL + 1)

        for _ in range(num_projectiles):
            # opposite side to the hypotenuse
            x_vel = math.sin(current_angle) * vel
            # adjacent side to the hypotenuse
            y_vel = math.cos(current_angle) * vel
            color = random.choice(COLORS)
            self.projectiles.append(Projectile(self.x, self.y, x_vel, y_vel, color))
            current_angle += angle_dif

    def move(self, max_width, max_height):
        if not self.exploded:
            self.y += self.y_vel
            if self.y <= self.explode_height:
                self.explode()

        projectiles_to_remove = []
        for projectile in self.projectiles:
            projectile.move()

            # if projectile.x >= max_width or projectile.x < 0:
            #     projectiles_to_remove.append(projectile)
            # elif projectile.y >= max_height or projectile.y < 0:
            #     projectiles_to_remove.append(projectile)

        for projectile in projectiles_to_remove:
            self.projectiles.remove(projectile)

    def draw(self, win):
        if not self.exploded:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.RADIUS)

        for projectile in self.projectiles:
            projectile.draw(win)


class Launcher:
    WIDTH = 20
    HEIGHT = 20
    COLOR = 'grey'
    RADIUS = 5
    fullName = "Antony Marshal"

    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        # which is used crate a new firework in ms
        self.frequency = frequency  # ms
        # by getting the time we can know when the next firework gonna fire
        self.start_time = time.time()
        # it's gonna contain all the firework
        self.fireworks = []

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))

        for firework in self.fireworks:
            firework.draw(win)

        color = random.choice(COLORS)
        name = SCORE_FONT.render(self.fullName, True, color)
        win.blit(name, (WIDTH - 300, HEIGHT // 2))

    def launch(self):
        color = random.choice(COLORS)
        explode_height = random.randrange(50, 400)
        firework = Firework(self.x + self.WIDTH / 2, self.y, -5, explode_height, color)
        self.fireworks.append(firework)

    # it's going to create a firework and move the firework
    # once the firework is of off the screen it will remove
    # that's why we use max_width & max_height
    def loop(self, max_width, max_height):
        # it determines if it should be launcher another firework
        current_time = time.time()
        # the way i determine how much time to elapsed
        time_elapsed = current_time - self.start_time
        # this lines of code for explode the firework every x seconds
        if time_elapsed * 1000 >= self.frequency:
            self.start_time = current_time
            self.launch()

        # move all of the fireworks
        firework_to_remove = []

        for firework in self.fireworks:
            firework.move(max_width, max_height)
            # if the firework got explode and projectiles has nothing
            if firework.exploded and len(firework.projectiles) == 0:
                firework_to_remove.append(firework)

        for firework in firework_to_remove:
            self.fireworks.remove(firework)


class Launcher1:
    WIDTH = 20
    HEIGHT = 20
    COLOR = 'grey'
    RADIUS = 5
    fullName = "Antony Marshal"

    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        # which is used crate a new firework in ms
        self.frequency = frequency  # ms
        # by getting the time we can know when the next firework gonna fire
        self.start_time = time.time()
        # it's gonna contain all the firework
        self.fireworks = []

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))

        for firework in self.fireworks:
            firework.draw(win)

        color = random.choice(COLORS)
        name = SCORE_FONT.render(self.fullName, True, color)
        win.blit(name, (WIDTH - 300, HEIGHT // 2))

    def launch1(self):
        color = random.choice(COLORS)
        explode_height = HEIGHT // 2
        firework = Firework(self.x + self.WIDTH/2, self.y, -5, explode_height, color)
        self.fireworks.append(firework)

    # it's going to create a firework and move the firework
    # once the firework is of off the screen it will remove
    # that's why we use max_width & max_height
    def loop1(self, max_width, max_height):
        # it determines if it should be launcher another firework
        current_time = time.time()
        # the way i determine how much time to elapsed
        time_elapsed = current_time - self.start_time
        # this lines of code for explode the firework every x seconds
        if time_elapsed * 1000 >= self.frequency:
            self.start_time = current_time
            self.launch1()

        # move all of the fireworks
        firework_to_remove = []

        for firework in self.fireworks:
            firework.move(max_width, max_height)
            # if the firework got explode and projectiles has nothing
            if firework.exploded and len(firework.projectiles) == 0:
                firework_to_remove.append(firework)

        for firework in firework_to_remove:
            self.fireworks.remove(firework)


def draw(launchers, launchers1):
    win.fill("black")

    for launcher in launchers:
        launcher.draw(win)

    for launcher in launchers1:
        launcher.draw(win)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    launchers = [Launcher(113, HEIGHT - Launcher.HEIGHT, 3000),
                 Launcher(246, HEIGHT - Launcher.HEIGHT, 4000),
                 Launcher(379, HEIGHT - Launcher.HEIGHT, 2000)]

    launchers1 = [Launcher1(625, HEIGHT - Launcher1.HEIGHT, 2000)]
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        for launcher in launchers:
            launcher.loop(WIDTH, HEIGHT)

        for launcher in launchers1:
            launcher.loop1(WIDTH, HEIGHT // 2)

        draw(launchers, launchers1)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
