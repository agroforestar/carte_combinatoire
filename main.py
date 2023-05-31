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


def createPmaExample():
    pma = nMap()

    print("/// LSA 1 ////")
    lsa1face = pma.createFace(4, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0},
                              {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 18.0},
                              {"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 18.0},
                              {"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 0.0}], "LSA-1")

    tre1_1 = pma.createFilledGapFace(lsa1face, 4, [{"id": uuid.uuid4(), "x_pos": 1, "y_pos": 1},
                                          {"id": uuid.uuid4(), "x_pos": 1, "y_pos": 3},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 3},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 1}], "Tree_1-1")

    tre1_2 = pma.createFilledGapFace(lsa1face, 4, [{"id": uuid.uuid4(), "x_pos": 1, "y_pos": 5},
                                          {"id": uuid.uuid4(), "x_pos": 1, "y_pos": 8},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 8},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 5}], "Tree_1-2")

    tre1_3 = pma.createFilledGapFace(lsa1face, 4, [{"id": uuid.uuid4(), "x_pos": 1, "y_pos": 10},
                                          {"id": uuid.uuid4(), "x_pos": 1, "y_pos": 14},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 14},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 10}], "Tree_1-3")

    cropface = pma.createFace(4, [{"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 0.0},
                              {"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 18.0},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 18.0},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 0.0}], "Crop")

    lsa2face = pma.createFace(4, [{"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 0.0},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 18.0},
                              {"id": uuid.uuid4(), "x_pos": 12.0, "y_pos": 18.0},
                              {"id": uuid.uuid4(), "x_pos": 12.0, "y_pos": 0.0}], "LSA-2")



    tre2_1 = pma.createFilledGapFace(lsa2face, 4, [{"id": uuid.uuid4(), "x_pos": 9, "y_pos": 1},
                                          {"id": uuid.uuid4(), "x_pos": 9, "y_pos": 3},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 3},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 1}], "Tree_2-1")

    tre2_2 = pma.createFilledGapFace(lsa2face, 4, [{"id": uuid.uuid4(), "x_pos": 9, "y_pos": 5},
                                          {"id": uuid.uuid4(), "x_pos": 9, "y_pos": 8},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 8},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 5}], "Tree_2-2")

    tre2_2 = pma.createFilledGapFace(lsa2face, 4, [{"id": uuid.uuid4(), "x_pos": 9, "y_pos": 10},
                                          {"id": uuid.uuid4(), "x_pos": 9, "y_pos": 14},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 14},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 10}], "Tree_2-3")

    pma.connectDartBeta2Face(cropface)

    outside = pma.createOutsideFace(pma.darts[0])


    pencil = Pencil()

    pencil.drawMapDartsFig(pma)

def createExample():

    am = nMap()

    print("/// Line 1 ////")
    line1Face = am.createFace(4, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0},
                              {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 3.0},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0}], "Line 1")

    # am.drawVertexIter(line1Face.darts[0])
    # f1 = am.getFace(line1Face.darts[0])

    am.createFilledGapFace(line1Face, 4, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 0.5}, {"id": 10, "x_pos": 1.25, "y_pos": 2.0},
                        {"id": 11, "x_pos": 1.75, "y_pos": 2.0}, {"id": 12, "x_pos": 1.75, "y_pos": 0.5}], "Tree")
    am.createFilledGapFace(line1Face, 4, [{"id": 17, "x_pos": 0.25, "y_pos": 0.5}, {"id": 18, "x_pos": 0.25, "y_pos": 2.0},
                        {"id": 19, "x_pos": 0.75, "y_pos": 2.0}, {"id": 20, "x_pos": 0.75, "y_pos": 0.5}], "Tree")


    print("/// Rectangle de culture  ////")
    cropFace = am.createFace(4, [{"id": 5, "x_pos": 2.0, "y_pos": 3.0}, {"id": 6, "x_pos": 0.0, "y_pos": 3.0},
                                   {"id": 7, "x_pos": 0.0, "y_pos": 6.0}, {"id": 8, "x_pos": 2.0, "y_pos": 6.0}])
    # cropFace.drawVertexIter(cropFace.darts[0])
    # f2 = am.getFace(cropFace.darts[0])

    #map = am.mergeNMaps(crop)
    am.connectDartBeta2Face(cropFace)


    print("/// Line 2  ////")

    line2Face = am.createFace(4, [{"id": 13, "x_pos": 2.0, "y_pos": 6.0}, {"id": 14, "x_pos": 0.0, "y_pos": 6.0},
                                  {"id": 15, "x_pos": 0.0, "y_pos": 9.0}, {"id": 16, "x_pos": 2.0, "y_pos": 9.0}])
    # line2.drawVertexIter(line2Face.darts[0])
    # f3 = am.getFace(line2Face.darts[0])
    # print(f3)

    am.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 7.5},
                                {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 8.5},
                                {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 6.5}], "Tree")

    am.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 0.25, "y_pos": 7.5},
                                {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 8.5},
                                {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 6.5}], "Tree")

    am.connectDartBeta2Face(line2Face)


    outside = am.createOutsideFace(am.darts[0])

    pencil = Pencil()

    pencil.drawMapDartsFig(am)

    pencil.initFig()
    pencil.drawSingleFaceDarts(am, line1Face, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(am, cropFace, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(am, line2Face, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(am, outside, 1, 1.1, "blue", "purple")
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
    # crop = nMap()
    cropFace = am_growth.createFace(4, [{"id": 5, "x_pos": 2.0, "y_pos": 3.0}, {"id": 6, "x_pos": 0.0, "y_pos": 3.0},
                                   {"id": 7, "x_pos": 0.0, "y_pos": 6.0}, {"id": 8, "x_pos": 2.0, "y_pos": 6.0}])

    #map_growth = am_growth.mergeNMaps(cropFace)
    #map_growth = am_growth.mergeNMaps(am_growth)
    am_growth.connectDartBeta2Face(cropFace)

    print("/// Line 2  ////")
    #line2 = nMap()
    line2Face = am_growth.createFace(4, [{"id": 13, "x_pos": 2.0, "y_pos": 6.0}, {"id": 14, "x_pos": 0.0, "y_pos": 6.0},
                                     {"id": 15, "x_pos": 0.0, "y_pos": 9.0}, {"id": 16, "x_pos": 2.0, "y_pos": 9.0}])
    # am_growth.drawVertexIter(line2Face.darts[0])
    am_growth.createFilledGapFace(line2Face, 5, [{"id": uuid.uuid4(), "x_pos": 1.0, "y_pos": 7.5},
                            {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 9},
                            {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 9},
                            {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 6},
                            {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 6}], "Tree")
    # treeBoutside = line2.createFace(3, [{"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 9},
    #                                 {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 9},
    #                                 {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 10}])
    # am_growth.mergeNMaps(treeBoutside)
    am_growth.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 0.15, "y_pos": 7.5},
                            {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 8.5},
                            {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 6.5}], "Tree")

    #am_growth.mergeNMaps(line2Face)
    #am_growth.mergeNMaps(am_growth)
    am_growth.connectDartBeta2Face(line2Face)

    pencil.initFig()
    pencil.drawMap(am_growth)
    pencil.showFig()


def createTest():

    am = nMap()
    #
    carre = am.createFace(4,[{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0},
                         {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 4.0},
                         {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 4.0},
                         {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 0.0}], "Carre")

    triang = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 2, "y_pos": 2},
                         {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 2},
                         {"id": uuid.uuid4(), "x_pos": 2, "y_pos": 3}], "Triangle")


    myhole = am.createFilledGapFace(carre, 4, [{"id": uuid.uuid4(), "x_pos": 1.0, "y_pos": 1.0},
                         {"id": uuid.uuid4(), "x_pos": 1.0, "y_pos": 3.0},
                         {"id": uuid.uuid4(), "x_pos": 2.5, "y_pos": 3.0},
                         {"id": uuid.uuid4(), "x_pos": 2.5, "y_pos": 1.0}], "carre")

    am.subdiveDart2(am.darts[myhole.dartid], 1, 0.3)

    am.drawVertexIter (am.darts[triang.dartid])

    am.subdiveDart(am.darts[triang.dartid], 1, 0.5)

    #
    pencil = Pencil()
    #
    # # carre.gap[0].drawVertexIter(carre.gap[0].darts[0])
    #
    pencil.initFig()
    # pencil.drawSingleFace(am, triang)
    pencil.drawFaceDarts(am, triang, 2)
    pencil.showFig()
    pencil.drawMapDartsFig(am)

    am.drawVertexIter (am.darts[triang.dartid])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ### scene 1

    createPmaExample()

    #createExample()

    #createTest()
