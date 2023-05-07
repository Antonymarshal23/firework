import math
import random
from tutorail import Projectile, COLORS


def create_circular_projectiles(self, num_projectiles):
    # get the angle different
    angle_dif = math.pi * 4 / num_projectiles
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
