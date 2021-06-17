import math
import random

def generateRandomPoints(center, radius, count):
    points = []
    for i in range(0, count):
        points.append(generateRandomPoint(center, radius))
    
    return points

def generateRandomPoint(center, radius):
    x0 = center['lng']
    y0 = center['lat']

    #Convert radius from meters to degrees
    rd = radius / 111300

    u = random.random()
    v = random.random()

    w = rd * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    xp = x / math.cos(y0)

    return {'lat': y + y0, 'lng': xp + x0}
