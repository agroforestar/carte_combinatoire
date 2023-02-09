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
    d1 = am.createDartNMap(1, 0.0, 0.0)
    d2 = am.createDartNMap(2, 0.0, 3.0)
    d3 = am.createDartNMap(3, 2.0, 3.0)
    d4 = am.createDartNMap(4, 2.0, 0.0)
    dart_used = [d1, d2, d3, d4]
    am.createOnePolygon(dart_used)
    am.drawVertexIter(d1)
    f1 = am.getFace(d1)

    print("/// Rectangle de culture  ////")
    crop = nMap()
    d5 = crop.createDartNMap(5, 2.0, 3.0)
    d6 = crop.createDartNMap(6, 0.0, 3.0)
    d7 = crop.createDartNMap(7, 0.0, 6.0)
    d8 = crop.createDartNMap(8, 2.0, 6.0)
    #bis = [d5, d6, d7, d8]
    bis = [d5, d8, d7, d6]
    crop.createOnePolygon(bis)
    crop.drawVertexIter(d5)
    f2 = crop.getFace(d5)
    print(crop.darts)
    map = am.mergeNMaps(crop)
    print(map.darts)
    for d in map.darts:
        print(d.betas[2])

    print(map.getFace(d1))
    print(map.getFace(d7))

    # print("/// Line 2  ////")
    # d12 = am.createDartNMap(12, 2.0, 9.0)
    # d11 = am.createDartNMap(11, 0.0, 9.0)
    # d10 = am.createDartNMap(10, 0.0, 6.0)
    # d9 = am.createDartNMap(9, 2.0, 6.0)
    # ter = [d9, d10, d11, d12]
    # am.createOnePolygon(ter)
    # am.drawVertexIter(d9)
    # f3 = am.getFace(d9)
    # print(f3)
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
    # coordF1 = am.getCoordFace(f1)
    # coordF2 = am.getCoordFace(f2)
    # coordF3 = am.getCoordFace(f3)
    # coordF4 = am.getCoordFace(f4)
    #
    #
    #
    # pencil = Pencil()
    # # pencil.drawFace(coordF1)
    # # pencil.drawFace(coordF2)
    # # pencil.drawFace(coordF3)
    #
    # pencil.drawFaces([coordF1, coordF2, coordF3, coordF4])



