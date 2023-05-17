# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from Parseur import *
# from Crop import *
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
   # print(sorted(trees, key=lambda tree: tree.X))

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

def createExample():

    am = nMap()

    print("/// Line 1 ////")
    line1 = am.createFace(4, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0},
                              {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 3.0},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0}], "Line 1")

    am.drawVertexIter(line1.darts[0])
    # f1 = am.getFace(line1.darts[0])
    #
    # line1.createGap(4, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 0.5}, {"id": 10, "x_pos": 1.25, "y_pos": 2.0},
    #                     {"id": 11, "x_pos": 1.75, "y_pos": 2.0}, {"id": 12, "x_pos": 1.75, "y_pos": 0.5}], "Tree")
    # line1.createGap(4, [{"id": 17, "x_pos": 0.25, "y_pos": 0.5}, {"id": 18, "x_pos": 0.25, "y_pos": 2.0},
    #                     {"id": 19, "x_pos": 0.75, "y_pos": 2.0}, {"id": 20, "x_pos": 0.75, "y_pos": 0.5}], "Tree")

    am.createFilledGapFace(line1, 4, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 0.5}, {"id": 10, "x_pos": 1.25, "y_pos": 2.0},
                        {"id": 11, "x_pos": 1.75, "y_pos": 2.0}, {"id": 12, "x_pos": 1.75, "y_pos": 0.5}], "Tree")
    am.createFilledGapFace(line1, 4, [{"id": 17, "x_pos": 0.25, "y_pos": 0.5}, {"id": 18, "x_pos": 0.25, "y_pos": 2.0},
                        {"id": 19, "x_pos": 0.75, "y_pos": 2.0}, {"id": 20, "x_pos": 0.75, "y_pos": 0.5}], "Tree")


    print("/// Rectangle de culture  ////")
    crop = nMap()
    cropFace = crop.createFace(4, [{"id": 5, "x_pos": 2.0, "y_pos": 3.0}, {"id": 6, "x_pos": 0.0, "y_pos": 3.0},
                                   {"id": 7, "x_pos": 0.0, "y_pos": 6.0}, {"id": 8, "x_pos": 2.0, "y_pos": 6.0}])
    crop.drawVertexIter(cropFace.darts[0])
    f2 = crop.getFace(cropFace.darts[0])

    map = am.mergeNMaps(crop)



    if True:

        print("/// Line 2  ////")
        line2 = nMap()
        line2Face = line2.createFace(4, [{"id": 13, "x_pos": 2.0, "y_pos": 6.0}, {"id": 14, "x_pos": 0.0, "y_pos": 6.0},
                                         {"id": 15, "x_pos": 0.0, "y_pos": 9.0}, {"id": 16, "x_pos": 2.0, "y_pos": 9.0}])
        # line2.drawVertexIter(line2Face.darts[0])
        f3 = line2.getFace(line2Face.darts[0])
        # print(f3)

        # line2Face.createGap(3, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 7.5},
        #                         {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 8.5},
        #                         {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 6.5}], "Tree")
        # line2Face.createGap(3, [{"id": uuid.uuid4(), "x_pos": 0.25, "y_pos": 7.5},
        #                         {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 8.5},
        #                         {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 6.5}], "Tree")
        #

        line2.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 7.5},
                                {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 8.5},
                                {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 6.5}], "Tree")
        line2.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 0.25, "y_pos": 7.5},
                                {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 8.5},
                                {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 6.5}], "Tree")

        map = map.mergeNMaps(line2)


    outside = map.createOutsideFace(map.darts[0])

    pencil = Pencil()

    pencil.drawMapDartsFig(map)
    pencil.initFig()
    # pencil.drawFaceDarts (outside, 1)

    pencil.drawSingleFaceDarts(line1, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(cropFace, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(line2Face, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(outside, 1, 1.1, "blue", "purple")
    pencil.showFig()

    ### scene 2
    am_growth = nMap()
    print("/// Line 1 ////")
    line1 = am_growth.createFace(4, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0},
                                     {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 3.0},
                                     {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0},
                                     {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0}], "Line 1")

    am_growth.createFilledGapFace(line1, 4, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 0.5}, {"id": 10, "x_pos": 1.25, "y_pos": 2.0},
                        {"id": 11, "x_pos": 1.75, "y_pos": 2.0}, {"id": 12, "x_pos": 1.75, "y_pos": 0.5}], "Tree")
    am_growth.createFilledGapFace(line1, 4, [{"id": 17, "x_pos": 0.25, "y_pos": 0.5}, {"id": 18, "x_pos": 0.25, "y_pos": 2.0},
                        {"id": 19, "x_pos": 0.75, "y_pos": 2.0}, {"id": 20, "x_pos": 0.75, "y_pos": 0.5}], "Tree")

    print("/// Rectangle de culture  ////")
    crop = nMap()
    cropFace = crop.createFace(4, [{"id": 5, "x_pos": 2.0, "y_pos": 3.0}, {"id": 6, "x_pos": 0.0, "y_pos": 3.0},
                                   {"id": 7, "x_pos": 0.0, "y_pos": 6.0}, {"id": 8, "x_pos": 2.0, "y_pos": 6.0}])

    map_growth = am_growth.mergeNMaps(crop)

    print("/// Line 2  ////")
    line2 = nMap()
    line2Face = line2.createFace(4, [{"id": 13, "x_pos": 2.0, "y_pos": 6.0}, {"id": 14, "x_pos": 0.0, "y_pos": 6.0},
                                     {"id": 15, "x_pos": 0.0, "y_pos": 9.0}, {"id": 16, "x_pos": 2.0, "y_pos": 9.0}])
    # line2.drawVertexIter(line2Face.darts[0])
    line2.createFilledGapFace(line2Face, 5, [{"id": uuid.uuid4(), "x_pos": 1.0, "y_pos": 7.5},
                            {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 9},
                            {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 9},
                            {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 6},
                            {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 6}], "Tree")
    # treeBoutside = line2.createFace(3, [{"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 9},
    #                                 {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 9},
    #                                 {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 10}])
    # line2Face.mergeNMaps(treeBoutside)
    line2.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 0.15, "y_pos": 7.5},
                            {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 8.5},
                            {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 6.5}], "Tree")

    map_growth = map_growth.mergeNMaps(line2)

    pencil.initFig()
    pencil.drawMap(map_growth)
    pencil.showFig()


def createTest():

    am = nMap()
    #
    carre = am.createFace(4,[{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0},
                         {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 3.0},
                         {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0},
                         {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0}], "Carre")

    triang = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 1.6, "y_pos": 1.5},
                         {"id": uuid.uuid4(), "x_pos": 1.8, "y_pos": 1.5},
                         {"id": uuid.uuid4(), "x_pos": 1.7, "y_pos": 1.7}], "Triangle")


    myhole = am.createFilledGapFace(carre, 4, [{"id": uuid.uuid4(), "x_pos": 1.0, "y_pos": 1.0},
                         {"id": uuid.uuid4(), "x_pos": 1.0, "y_pos": 2.0},
                         {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 2.0},
                         {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 1.0}], "carre")

    #
    #
    pencil = Pencil()
    #
    # # carre.gap[0].drawVertexIter(carre.gap[0].darts[0])
    #
    pencil.initFig()
    # pencil.drawSingleFace(triang)
    pencil.drawFaceDarts(triang, 2)
    pencil.showFig()
    pencil.drawMapDartsFig(am)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ### scene 1

    createExample()

    createTest()
