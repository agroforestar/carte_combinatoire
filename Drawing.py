import matplotlib.pyplot as plt
from Map import *
class Pencil:


    def drawFace(self, face:Face):
        coord = face.getCoordFace()
        coord.append(coord[0])  # repeat the first point to create a 'closed loop'
        xs, ys = zip(*coord)  # create lists of x and y values
        plt.plot(xs, ys)
        if len(face.gap) >0:
            for g in face.gap:
                coord = g.getCoordFace()
                coord.append(coord[0])  # repeat the first point to create a 'closed loop'
                xs, ys = zip(*coord)  # create lists of x and y values
                plt.plot(xs, ys)

    def drawFaces(self, listFaces):
        plt.figure()
        for coord in listFaces:
            coord.append(coord[0])  # repeat the first point to create a 'closed loop'
            xs, ys = zip(*coord)  # create lists of x and y values
            plt.plot(xs, ys)
        plt.show()

    def drawMap(self, map:nMap):
        plt.figure()
        print(map.faces)
        for f in map.faces:
            print(f.darts)
            self.drawFace(f)
        plt.show()