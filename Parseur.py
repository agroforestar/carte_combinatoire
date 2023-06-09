import math

from Map import *
import os


class Plant:
    def __init__(self, data):
        split = str(data).replace('\n', '').split(';')

        self.x = int(split[1])
        self.y = int(split[2])

        self.uCode = split[0]
        self.type = 'p'

        if len(split) > 3:
            split[3] = split[3].replace('[', '').replace(']', '')
            surf = split[3].split(',')

            self.xMin = int(surf[0])
            self.yMin = int(surf[1])

            self.xMax = int(surf[2])
            self.yMax = int(surf[3])

            self.type = 'a'


def ReadTxt(path):
    lines = []
    if os.path.isfile(path):
        with open(path, 'r') as r:
            lines = r.readlines()
            r.close()
    return lines


def GetPointsFromPoint(point_central, distance):
    x_central, y_central = point_central

    points = []
    for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
        x = x_central + dx * distance
        y = y_central + dy * distance
        points.append((x, y))

    return points


def GetPointsFromArea(plant):
    return [(plant.xMin, plant.yMin), (plant.xMin, plant.yMax), (plant.xMax, plant.yMax), (plant.xMax, plant.yMin)]


def Convert(plants, map):
    index = 0

    for plant in plants:
        pos_central = (plant.x, plant.y)

        if plant.type == 'p':
            points = GetPointsFromPoint(pos_central, 0.5)
            print(points)
        else:
            points = GetPointsFromArea(plant)
            print(points)
        map.createFace(4, [{"id": uuid.uuid4(), "x_pos": points[0][0], "y_pos": points[0][1]},
                           {"id": uuid.uuid4(), "x_pos": points[1][0], "y_pos": points[1][1]},
                           {"id": uuid.uuid4(), "x_pos": points[2][0], "y_pos": points[2][1]},
                           {"id": uuid.uuid4(), "x_pos": points[3][0], "y_pos": points[3][1]}],
                       f"{plant.uCode}-{index}")
        index += 1

    return map


def Parse(path, nMap):
    lines = ReadTxt(path)

    plants = []
    for line in lines:
        plants.append(Plant(line))
    nMap = Convert(plants, nMap)

    return nMap
