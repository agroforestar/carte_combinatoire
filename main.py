# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Parseur import *
from Crop import *
from carte import *
import igraph as ig
import matplotlib.pyplot as plt

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
    g = Carte()
    g.addFace(4)
    print(g.getFace(g.root))
    g.addFace(4, g.exteriorFace()[0])
    g.addFace(4, g.exteriorFace()[0])
    g.addFace(4, g.exteriorFace()[0])
    g.addFace(4, g.exteriorFace()[0])
    print(g.getAllFaces())
    print(g.exteriorFace())


    representMap(g)
    #g.affectNodes()
    # g.collapse(g.root)
    # g.collapse(g.root)
   # g.debug(lambda l: l + 100)

    # plants = read("D:\Mes_Documents\code\openCVPyhton\data2.txt")
#    plants = [(1100, 864), (113, 857), (612, 853), (1102, 630), (115, 623), (614, 619), "Crop", <Plant.Plant object at 0x000001C016DDB460>, (1108, 405), (121, 398), (620, 394), (1115, 166), (128, 159), (627, 155)]

 #   findLines([tree for tree in plants if type(tree) == Tree].copy())


