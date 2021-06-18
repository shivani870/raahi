import math
import random

class coordinates_generator:

    def __init__(self, count=0, radius=0, center=None):
        self.center = center if center != None else {'lat': 34.2157, 'lng': 75.5041}
        self.radius = radius if radius != 0 else 1000
        self.count = count if count != 0 else 1

    def generateRandomPoints(self):
        points = []
        for i in range(0, self.count):
            points.append(self.__generateRandomPoint())
        
        return points

    def __generateRandomPoint(self):
        x0 = self.center['lng']
        y0 = self.center['lat']

        #Convert radius from meters to degrees
        rd = self.radius / 111300

        u = random.random()
        v = random.random()

        w = rd * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)

        xp = x / math.cos(y0)

        return {'lat': y + y0, 'lng': xp + x0}
