# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Parseur import *
from Crop import *
from carte import *
import igraph as ig
import matplotlib.pyplot as plt
from Map import *
from Drawing import *
import uuid

def findLines(trees):
    testedTree = list()
    current = trees.pop()
    testedTree.append(current)
    print(sorted(trees, key=lambda tree: tree.X))
    for tree in trees:
        print("e")

def representMap(map:Carte):
    darts = map.getAllBrins()
    g = ig.Graph(len(darts), [])
    print(g)
    for d in darts:
        g.add_edge(d.id, d.beta0.id)
    fig, ax = plt.subplots(figsize=(5, 5))
    ig.plot(
        g,
        target=ax,
        layout='kk',
        vertex_size=0.3,
        edge_width=4,
        vertex_label=range(g.vcount()),
        vertex_color="white",
    )
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    am = nMap()


    print("/// Line 1 ////")
    # d1 = am.createDartNMap(1, 0.0, 0.0)
    # d2 = am.createDartNMap(2, 0.0, 3.0)
    # d3 = am.createDartNMap(3, 2.0, 3.0)
    # d4 = am.createDartNMap(4, 2.0, 0.0)
    line1 = am.createFace(4, [{"id":uuid.uuid4(), "x_pos":0.0, "y_pos":0.0}, {"id":uuid.uuid4(), "x_pos":0.0, "y_pos":3.0}, {"id":uuid.uuid4(), "x_pos":2.0, "y_pos":3.0}, {"id":uuid.uuid4(), "x_pos":2.0, "y_pos":0.0}], "Line 1")

    am.drawVertexIter(line1.darts[0])
    f1 = am.getFace(line1.darts[0])

    line1.createGap(4, [{"id":uuid.uuid4(), "x_pos":1.5, "y_pos":0.5}, {"id":10, "x_pos":1.5, "y_pos":1.0}, {"id":11, "x_pos":2.0, "y_pos":1.0}, {"id":12, "x_pos":2.0, "y_pos":0.5}], "Tree")
    line1.createGap(4, [{"id":17, "x_pos":0.5, "y_pos":0.5}, {"id":18, "x_pos":0.5, "y_pos":1.0}, {"id":19, "x_pos":1.0, "y_pos":1.0}, {"id":20, "x_pos":1.0, "y_pos":0.5}], "Tree")

    print("/// Rectangle de culture  ////")
    crop = nMap()
    cropFace = crop.createFace(4, [{"id": 5, "x_pos":2.0, "y_pos":3.0}, {"id":6, "x_pos":0.0, "y_pos":3.0}, {"id":7, "x_pos":0.0, "y_pos":6.0}, {"id":8, "x_pos":2.0, "y_pos":6.0}])
    crop.drawVertexIter(cropFace.darts[0])
    f2 = crop.getFace(cropFace.darts[0])

    map = am.mergeNMaps(crop)

    print("/// Line 2  ////")
    line2 = nMap()
    line2Face = line2.createFace(4, [{"id": 13, "x_pos": 2.0, "y_pos": 6.0}, {"id": 14, "x_pos": 0.0, "y_pos": 6.0},
                                   {"id": 15, "x_pos": 0.0, "y_pos": 9.0}, {"id": 16, "x_pos": 2.0, "y_pos": 9.0}])
    line2.drawVertexIter(line2Face.darts[0])
    f3 = line2.getFace(line2Face.darts[0])
    print(f3)

    map = map.mergeNMaps(line2)
    #
    # print("/// Outside  ////")
    # d13 = am.createDartNMap(13, 0.0, 0.0)
    # d14 = am.createDartNMap(14, 0.0, 3.0)
    # d15 = am.createDartNMap(15, 0.0, 6.0)
    # d16 = am.createDartNMap(16, 0.0, 9.0)
    # d17 = am.createDartNMap(17, 2.0, 9.0)
    # d18 = am.createDartNMap(18, 2.0, 6.0)
    # d19 = am.createDartNMap(19, 2.0, 3.0)
    # d20 = am.createDartNMap(20, 2.0, 0.0)
    # d21 = am.createDartNMap(21, 2.0, 3.0)
    # d22 = am.createDartNMap(21, 2.0, 6.0)
    # outside = [d13, d14, d15, d16, d17, d18, d19, d20 ]
    # am.createOnePolygon(outside)
    # f4 = am.getFace(d13)
    # print(f4)
    #
    # am.setBeta2(d2, d6)
    # am.setBeta2(d8, d9)
    # print(am.getFace(d4.betas[2]))
    #
    # coordF1 = am.getCoordFace(line1.darts)
    # print(coordF1)
    # coordF2 = am.getCoordFace(f2)
    # coordF3 = am.getCoordFace(f3)
    # coordF4 = am.getCoordFace(f4)
    #
    #
    #
    pencil = Pencil()
    #pencil.drawFace(line1)
    pencil.drawMap(map)
    # # pencil.drawFace(coordF2)
    # # pencil.drawFace(coordF3)
    #
    # pencil.drawFaces([coordF1, coordF2, coordF3, coordF4])



