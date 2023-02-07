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
    d1 = am.createDartNMap(1, 0, 0)
    d2 = am.createDartNMap(2, 0, 3)
    d3 = am.createDartNMap(3, 2, 3)
    d4 = am.createDartNMap(4, 2, 0)
    dart_used = [d1, d2, d3, d4]
    am.createOnePolygon(dart_used)
    am.drawVertexIter(d1)
    f1 = am.getFace(d1)
    print(f1)

    print("/// Rectangle de culture  ////")
    d5 = am.createDartNMap(8, 2, 3)
    d6 = am.createDartNMap(5, 0, 3)
    d7 = am.createDartNMap(6, 0, 6)
    d8 = am.createDartNMap(7, 2, 6)
    bis = [d5, d6, d7, d8]
    am.createOnePolygon(bis)
    am.drawVertexIter(d5)
    f2 = am.getFace(d5)
    print(f2)

    print("/// Line 2  ////")
    d12 = am.createDartNMap(12, 2, 9)
    d11 = am.createDartNMap(11, 0, 9)
    d10 = am.createDartNMap(10, 0, 6)
    d9 = am.createDartNMap(9, 2, 6)
    ter = [d9, d10, d11, d12]
    am.createOnePolygon(ter)
    am.drawVertexIter(d9)
    f3 = am.getFace(d9)
    print(f3)

    am.setBeta2(d4, d5)
    am.setBeta2(d8, d9)
    print(am.getFace(d4.betas[2]))

    coordF1 = am.getCoordFace(f1)
    coordF2 = am.getCoordFace(f2)
    coordF3 = am.getCoordFace(f3)

    pencil = Pencil()
    # pencil.drawFace(coordF1)
    # pencil.drawFace(coordF2)
    # pencil.drawFace(coordF3)

    pencil.drawFaces([coordF1, coordF2, coordF3])



