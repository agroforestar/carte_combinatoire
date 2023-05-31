import matplotlib.pyplot as plt
from Map import *
import numpy as np

##desc: Class allowing draw combinatorial maps
#date: 07/02/2023
#author: L.L.
class Pencil:

    # Draw a simple dart
    def drawSingleDartArrow(self, m: nMap, d: myDart, coef :float, func, col):
        if d != m.null_dart:
            x = d.properties["x_pos"]
            y = d.properties["y_pos"]
            if d.betas[func] != m.null_dart:
                nx = d.betas[func].properties["x_pos"] - x
                ny = d.betas[func].properties["y_pos"] - y
                if nx*nx + ny*ny < 0.001:
                    nx += 0.01
                    ny += 0.01
                line = plt.arrow (x+nx*0.05, y+ny*0.05, nx*(coef-0.125), ny*(coef-0.125), head_width=0.06, head_length=0.06)
                plt.setp(line, 'color', col)

    def drawSingleDartMarker(self, m: nMap, d: myDart, coef :float, func, col, mark):
        if d != m.null_dart:
            x = d.properties["x_pos"]
            y = d.properties["y_pos"]
            if d.betas[1] != m.null_dart:
                nx = d.betas[1].properties["x_pos"] - x
                ny = d.betas[1].properties["y_pos"] - y
                if nx*nx + ny*ny < 0.001:
                    nx += 0.01
                    ny += 0.01
                x = x + nx * coef
                y = y + ny * coef
                if d.betas[func] != m.null_dart:
                    plt.plot(x, y, color=col, marker=mark, markersize=6)
                else:
                    plt.plot(x, y, color=col, marker='o', markersize=6)
            else:
                mk = plt.plot(x, y, color='red', marker='o', markersize=6)



    # Draw a face of a combinatorial map
    def drawSingleFaceFig(self, map: nMap, face:Face):

        fig, ax = plt.subplots(1)
        colors = ['red', 'blue', 'green']
        ax.set_prop_cycle('color', colors)

        self.drawSingleFace(map, face)

        plt.show()

    def drawSingleFace(self, map: nMap, face:Face):
        #coord = face.getCoordFace()
        #coord.append(coord[0])  # repeat the first point to create a 'closed loop'

        listdarts: list[myDart] = map.getFaceBeta(map.darts[face.dartid], 1)
        coord = []
        for dart in listdarts:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        coord.append(coord[0])  # repeat the first point to create a 'closed loop'


        xs, ys = zip(*coord)  # create lists of x and y values
        xm = np.mean(xs)
        ym = np.mean(ys)
        coef = 0.9
        nxs = [coef * (x - xm) + xm for x in xs]
        nys = [coef * (y - ym) + ym for y in ys]
        plt.plot(nxs, nys, color = "red")
        print(coord)
        if len(face.gap) > 0:
            for g in face.gap:

                listdartsg: list[myDart] = map.getFaceBeta(map.darts[g.dartid], 0)
                gcoord = []
                for gdart in listdartsg:
                    x = gdart.properties["x_pos"]
                    y = gdart.properties["y_pos"]
                    gcoord.append([x, y])
                gcoord.append(gcoord[0])  # repeat the first point to create a 'closed loop'


                #coord = g.getCoordFace()
                #print(coord)
                #coord.append(coord[0])  # repeat the first point to create a 'closed loop'
                xs, ys = zip(*gcoord)  # create lists of x and y values
                xm = np.mean(xs)
                ym = np.mean(ys)
                coef = 1.1
                nxs = [coef * (x - xm) + xm for x in xs]
                nys = [coef * (y - ym) + ym for y in ys]
                plt.plot(nxs, nys, color="green" )



    # Draw a face of a combinatorial map
    def drawFaceDarts(self, map:nMap, face:Face, beta):

        self.drawSingleFaceDarts(map, face, beta, 0.95, 'red', 'orange')
        # print(coord)
        if len(face.gap) > 0:
            for gapface in face.gap:
                self.drawSingleFaceDarts(map, gapface, beta, 1.045, 'blue', 'purple')


    # Draw a face of a combinatorial map
    def drawFaceDartsFig(self, map:nMap, face: Face):

        self.initFig()
        self.drawFaceDarts(map, face)
        self.showFig()


    def drawSingleFaceDartsFig(self, map: nMap, face: Face, beta, coef: float, col1, col2):

        fig, ax = plt.subplots(1)
        colors = ['red', 'blue', 'green']
        ax.set_prop_cycle('color', colors)

        self.drawSingleFaceDarts(map, face, beta, coef, col1, col2)

        plt.show()


    # drawSingleFaceDarts displays darts issued from Face, applying successive beta funcs 0 or 1
    # with beta > 1 then Faces is drawn using beta[1] orbit and an estimated beta[2] arrow is displayed
    def drawSingleFaceDarts(self, map: nMap, face:Face, beta, coef:float, col1, col2):

        drawbeta2 = 0
        if beta > 1:
            drawbeta2 = 1
            beta = 1

        dart = map.darts[face.dartid]
        listdarts: list[myDart] = map.getFaceBeta(dart, beta)
        x = []
        y = []
        sx = []
        sy = []
        b2 = []
        n = 0
        numd = []
        for dart in listdarts:
            x.append(dart.properties["x_pos"])
            y.append(dart.properties["y_pos"])
            numd.append(dart.num)
            bok = 0;
            if len(dart.betas) > 2:
                bok = 1
                if dart.betas[2] != 0 :
                    bok = 2
            b2.append(bok)
            n = n + 1

        xm = np.mean(x)
        ym = np.mean(y)
        nx = [coef * (x - xm) + xm for x in x]
        ny = [coef * (y - ym) + ym for y in y]
        nx.append(nx[0])
        ny.append(ny[0])
        mx = [(2-coef) * (x - xm) + xm for x in x]
        my = [(2-coef) * (y - ym) + ym for y in y]
        mx.append(mx[0])
        my.append(my[0])
        i = 0
        px = [0,0]
        py = [0,0]

        while i < n:
            px[0] = nx[i]
            py[0] = ny[i]
            px[1] = nx[i+1]
            py[1] = ny[i+1]
            j = i % 2
            # line = plt.line(px, py)
            dline = plt.arrow (px[0], py[0], (px[1]-px[0])*0.91, (py[1]-py[0])*0.91, head_width=0.05, head_length=0.11)
            dtxt = plt.text(px[0]+(px[1]-px[0])*0.1, py[0]-0.1+(py[1]-py[0])*0.1, str(numd[i]))
            if j != 0:
               plt.setp(dline, 'color', col1)
               plt.setp(dtxt, 'color', col1)
            else:
               plt.setp(dline, 'color', col2)
               plt.setp(dtxt, 'color', col2)
            if drawbeta2 == 1 & b2[i] > 1:
                px[0] = nx[i] + (nx[i+1]- nx[i] ) * 0.45
                py[0] = ny[i] + (ny[i+1]- ny[i] ) * 0.45
                px[1] = mx[i] + (mx[i+1]- mx[i] ) * 0.45
                py[1] = my[i] + (my[i+1]- my[i] ) * 0.45
                # line = plt.line(px, py)
                line = plt.arrow(px[0], py[0], (px[1] - px[0]) * 0.91, (py[1] - py[0]) * 0.91, head_width=0.04, head_length=0.05)
            print(i, j, b2[i], px, py)
            i = i + 1



    # Draw a face of a combinatorial map
    def drawFace(self, map: nMap, face:Face):

        coord = map.getCoordFromFace(map.darts[face.dartid], 1)

        xs, ys = zip(*coord)  # create lists of x and y values
        xm = np.mean(xs)
        ym = np.mean(ys)
        coef = 0.9
        nxs = [coef * (x - xm) + xm for x in xs]
        nys = [coef * (y - ym) + ym for y in ys]
        plt.plot(nxs, nys, color = "red")
        print(coord)
        if len(face.gap) > 0:
            for g in face.gap:
                #gcoord = g.getCoordFace()
                #print(gcoord)
                #gcoord.append(gcoord[0])  # repeat the first point to create a 'closed loop'

                gcoord = map.getCoordFromFace(map.darts[g.dartid], 0)

                xs, ys = zip(*gcoord)  # create lists of x and y values
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


    def initFig(self):
        # plt.figure()
        fig, ax = plt.subplots(1)
        colors = ['red', 'blue', 'green']
        ax.set_prop_cycle('color', colors)

    def showFig(self):
        plt.show()


    # Draw a combinatorial map with this different faces and gaps.

    def drawMap(self, map:nMap):
        for f in map.faces:
            self.drawFace(map, f)

    def drawMapFig(self, map:nMap):
        # plt.figure()
        self.initFig()
        self.drawMap(map)
        self.showFig()

    def drawMapDarts(self, map: nMap):
        for f in map.faces:
            self.drawFaceDarts(map, f, 1)
        for d in map.darts:
            # self.drawSingleDartArrow(map, d, 0.48, 0, 'lightgrey')
            self.drawSingleDartArrow(map, d, 0.48, 1, 'grey')
            self.drawSingleDartMarker(map, d, 0.35, 2, 'green', '^')

    def drawMapDartsFig(self, map: nMap):
        self.initFig()
        self.drawMapDarts(map)
        self.showFig()

