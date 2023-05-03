import matplotlib.pyplot as plt
from Map import *
import numpy as np

##desc: Class allowing draw combinatorial maps
#date: 07/02/2023
#author: L.L.
class Pencil:


    # Draw a face of a combinatorial map
    def drawSingleFace(self, face:Face):

        fig, ax = plt.subplots(1)
        colors = ['red', 'blue', 'green']
        ax.set_prop_cycle('color', colors)

        coord = face.getCoordFace()
        coord.append(coord[0])  # repeat the first point to create a 'closed loop'
        xs, ys = zip(*coord)  # create lists of x and y values
        xm = np.mean(xs)
        ym = np.mean(ys)
        coef = 0.9
        nxs = [coef * (x - xm) + xm for x in xs]
        nys = [coef * (y - ym) + ym for y in ys]
        plt.plot(nxs, nys, color = "red")
        print(coord)
        if len(face.gap) >0:
            for g in face.gap:
                coord = g.getCoordFace()
                print(coord)
                coord.append(coord[0])  # repeat the first point to create a 'closed loop'
                xs, ys = zip(*coord)  # create lists of x and y values
                xm = np.mean(xs)
                ym = np.mean(ys)
                coef = 1.1
                nxs = [coef * (x - xm) + xm for x in xs]
                nys = [coef * (y - ym) + ym for y in ys]
                plt.plot(nxs, nys, color="green" )
        plt.show()

    # Draw a face of a combinatorial map
    def drawFace(self, face:Face, ax:plt.Axes):

        coord = face.getCoordFace()
        coord.append(coord[0])  # repeat the first point to create a 'closed loop'
        xs, ys = zip(*coord)  # create lists of x and y values
        xm = np.mean(xs)
        ym = np.mean(ys)
        coef = 0.9
        nxs = [coef * (x - xm) + xm for x in xs]
        nys = [coef * (y - ym) + ym for y in ys]
        plt.plot(nxs, nys, color = "red")
        print(coord)
        if len(face.gap) >0:
            for g in face.gap:
                coord = g.getCoordFace()
                print(coord)
                coord.append(coord[0])  # repeat the first point to create a 'closed loop'
                xs, ys = zip(*coord)  # create lists of x and y values
                xm = np.mean(xs)
                ym = np.mean(ys)
                coef = 1.1
                nxs = [coef * (x - xm) + xm for x in xs]
                nys = [coef * (y - ym) + ym for y in ys]
                plt.plot(nxs, nys, color="green" )

    # Draw faces of a combinatorial map
    # input : list of faces
    def drawFaces(self, listFaces):
        plt.figure()
        for coord in listFaces:
            coord.append(coord[0])  # repeat the first point to create a 'closed loop'
            xs, ys = zip(*coord)  # create lists of x and y values
            for x, y in zip(xs, ys):
                plt.plot(x, y)
        plt.show()

    # Draw a combinatorial map with this different faces and gaps.
    def drawMap(self, map:nMap):
        # plt.figure()
        fig, ax = plt.subplots(1)
        colors = ['red', 'blue', 'green']
        ax.set_prop_cycle('color', colors)
        for f in map.faces:
            self.drawFace(f, ax)
        plt.show()