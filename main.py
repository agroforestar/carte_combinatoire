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


    print("/// Triangle ////")
    d1 = am.createDartNMap(1, 0, 0)
    d2 = am.createDartNMap(2, 0, 1)
    d3 = am.createDartNMap(3, 1, 1)
    dart_used = [d1, d2, d3]
    am.createOnePolygon(dart_used)
    am.drawVertexIter(d1)
    f1 = am.getFace(d1)
    print(f1)

    print("/// Rectangle  ////")
    d4 = am.createDartNMap(4, 2, 2)
    d5 = am.createDartNMap(5, 2, 3)
    d6 = am.createDartNMap(6, 3, 3)
    d7 = am.createDartNMap(7, 3, 2)
    bis = [d4, d5, d6, d7]
    am.createOnePolygon(bis)
    am.drawVertexIter(d4)
    f2 = am.getFace(d4)
    print(f2)

    am.setBeta2(d1, d4)
    print(am.getFace(d4.betas[2]))

    coord = am.getCoordFace(f2)
    pencil = Pencil()
    pencil.drawFace(coord)



