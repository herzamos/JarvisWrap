import math, pygame, random, time

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def is_right_of(self, q, r):
        return (q.x - self.x) * (r.y - self.y) < (q.y - self.y) * (r.x - self.x)

    def find_next(self, points):
        next = random.choice(points)
        while (next.x == self.x & next.y == self.y):
            next = random.choice(list)
        for point in points:
            if ((point.x == self.x & point.y == self.y) | (point.x == next.x & point.y == next.y)):
                continue
            if (point.is_right_of(self, next)):
                    next = point
        return next

    def find_next_and_draw(self, points, screen):
        next = random.choice(points)
        while (next.x == self.x & next.y == self.y):
            next = random.choice(list)
        for point in points:
            if ((point.x == self.x & point.y == self.y) | (point.x == next.x & point.y == next.y)):
                continue
            if (point.is_right_of(self, next)):
                    next = point
                    pygame.draw.line(screen, (0, 128, 0), (self.x, self.y), (next.x, next.y), 1)
                    pygame.display.flip()
                    time.sleep(0.1)
        return next

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

def generate_points(max_x, max_y):
    points = []
    for x in range(max_x//20, max_x - max_x//20):
        for y in range(max_y//20, max_y - max_y//20):
            if (random.randint(0, 10000) > 9996):
                points.append(Point(x, y))
    return points

def are_collinear(three_points):
    a, b, c = three_points  
    # better use math.isclose than == to check for floats
    return math.isclose((b-a).cross(c-a), 0.0)

def jarvis_wrap(now, points, screen):
    seq = []
    h = 0
    while True:
        seq.append(now)
        now = seq[h].find_next_and_draw(points, screen)
        pygame.draw.line(screen, (255, 0, 0), (seq[h].x, seq[h].y), (now.x, now.y), 1)
        pygame.display.flip()
        time.sleep(0.5)
        h += 1
        if (now == seq[0]):
            break
    return

def run_jarvis_wrap():
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    points = generate_points(500, 500)
    start = points[0]

    random.shuffle(points)

    to_draw = True
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        if (to_draw):
            for point in points:
                pygame.draw.circle(screen, (0, 0 , 0), (point.x, point.y), 1)
            jarvis_wrap(start, points, screen)
            to_draw = False
        
    pygame.quit()

if __name__ == "__main__":
    run_jarvis_wrap()