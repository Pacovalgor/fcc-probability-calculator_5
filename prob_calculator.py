import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        colors = []
        for c, i in kwargs.items():
            for x in range(i):
                colors.append(c)
        self.contents = colors
      

    def draw(self, number):
        num = min(number, len(self.contents))
        balls = []
        for _ in range(num):
            index = random.randint(0, len(self.contents)-1)
            balls.append(self.contents.pop(index))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    checks = 0
    for _ in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        balls = hatCopy.draw(num_balls_drawn)
        correctColors = 0
        for color in expected_balls.keys():
            if balls.count(color) >= expected_balls[color]:
                correctColors += 1
        if correctColors == len(expected_balls):
            checks += 1
    probability = float(checks) / num_experiments
    return (probability)
