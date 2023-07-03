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

from drawModes import *
#DRAW_TXT = 0x0001
#DRAW_DART = 0x0010
#DRAW_FACE = 0x0100
#
#def checkDrawMode (val, mode):
#    if val&mode == mode:
#        return True
#    else:
#        return False
#

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
    lsa1face = pma.createFace(4, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 18.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 18.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 0.0, "atyp": "LSA"}], "LSA-1")

    tre1_1 = pma.createFilledGapFace(lsa1face, 4, [{"id": uuid.uuid4(), "x_pos": 1, "y_pos": 1, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 1, "y_pos": 3, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 3, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 1, "atyp": "TREE"}], "Tree_1-1")

    tre1_2 = pma.createFilledGapFace(lsa1face, 4, [{"id": uuid.uuid4(), "x_pos": 2, "y_pos": 5, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 2, "y_pos": 7, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 7, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 5, "atyp": "TREE"}], "Tree_1-2")

    tre1_2b = pma.createFace(4, [{"id": uuid.uuid4(), "x_pos": 1, "y_pos": 3.5, "atyp": "TREE"},
                                                   {"id": uuid.uuid4(), "x_pos": 1, "y_pos": 8.5, "atyp": "TREE"},
                                                   {"id": uuid.uuid4(), "x_pos": 4.5, "y_pos": 8.5, "atyp": "TREE"},
                                                   {"id": uuid.uuid4(), "x_pos": 4.5, "y_pos": 3.5, "atyp": "TREE"}],
                                     "Tree_1-2b")


    tre1_3 = pma.createFilledGapFace(lsa1face, 4, [{"id": uuid.uuid4(), "x_pos": 1, "y_pos": 10, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 1, "y_pos": 14, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 14, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 10, "atyp": "TREE"}], "Tree_1-3")

    cropface = pma.createFace(4, [{"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 0.0, "atyp": "CROP"},
                              {"id": uuid.uuid4(), "x_pos": 4.0, "y_pos": 18.0, "atyp": "CROP"},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 18.0, "atyp": "CROP"},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 0.0, "atyp": "CROP"}], "Crop")

    lsa2face = pma.createFace(4, [{"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 0.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 18.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 12.0, "y_pos": 18.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 12.0, "y_pos": 0.0, "atyp": "LSA"}], "LSA-2")



    tre2_1 = pma.createFilledGapFace(lsa2face, 4, [{"id": uuid.uuid4(), "x_pos": 9, "y_pos": 1, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 9, "y_pos": 3, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 3, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 1, "atyp": "TREE"}], "Tree_2-1")

    tre2_2 = pma.createFilledGapFace(lsa2face, 4, [{"id": uuid.uuid4(), "x_pos": 9, "y_pos": 5, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 9, "y_pos": 8, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 8, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 5, "atyp": "TREE"}], "Tree_2-2")

    tre2_2 = pma.createFilledGapFace(lsa2face, 4, [{"id": uuid.uuid4(), "x_pos": 9, "y_pos": 10, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 9, "y_pos": 14, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 14, "atyp": "TREE"},
                                          {"id": uuid.uuid4(), "x_pos": 11, "y_pos": 10, "atyp": "TREE"}], "Tree_2-3")

    pma.connectDartBeta2Face(cropface)

    outside = pma.createOutsideFace(pma.darts[0],0)


    pencil = Pencil()

    pencil.drawMapDartsFig(pma,1)
    #pencil.drawMapFig(pma,1)

def createExample():

    am = nMap()

    print("/// Line 1 ////")
    line1Face = am.createFace(4, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 3.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0, "atyp": "LSA"},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0, "atyp": "LSA"}], "Line 1")

    # am.drawVertexIter(line1Face.darts[0])
    # f1 = am.getFace(line1Face.darts[0])

    am.createFilledGapFace(line1Face, 4, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 0.5, "atyp": "TREE"},
                                          {"id": 10, "x_pos": 1.25, "y_pos": 2.0, "atyp": "TREE"},
                                          {"id": 11, "x_pos": 1.75, "y_pos": 2.0, "atyp": "TREE"},
                                          {"id": 12, "x_pos": 1.75, "y_pos": 0.5, "atyp": "TREE"}], "Tree")
    am.createFilledGapFace(line1Face, 4, [{"id": 17, "x_pos": 0.25, "y_pos": 0.5, "atyp": "TREE"},
                                          {"id": 18, "x_pos": 0.25, "y_pos": 2.0, "atyp": "TREE"},
                                          {"id": 19, "x_pos": 0.75, "y_pos": 2.0, "atyp": "TREE"},
                                          {"id": 20, "x_pos": 0.75, "y_pos": 0.5, "atyp": "TREE"}], "Tree")


    print("/// Rectangle de culture  ////")
    cropFace = am.createFace(4, [{"id": 5, "x_pos": 2.0, "y_pos": 3.0, "atyp": "CROP"},
                                 {"id": 6, "x_pos": 0.0, "y_pos": 3.0, "atyp": "CROP"},
                                 {"id": 7, "x_pos": 0.0, "y_pos": 6.0, "atyp": "CROP"},
                                 {"id": 8, "x_pos": 2.0, "y_pos": 6.0, "atyp": "CROP"}])
    # cropFace.drawVertexIter(cropFace.darts[0])
    # f2 = am.getFace(cropFace.darts[0])

    #map = am.mergeNMaps(crop)
    am.connectDartBeta2Face(cropFace)


    print("/// Line 2  ////")

    line2Face = am.createFace(4, [{"id": 13, "x_pos": 2.0, "y_pos": 6.0, "atyp": "LSA"},
                                  {"id": 14, "x_pos": 0.0, "y_pos": 6.0, "atyp": "LSA"},
                                  {"id": 15, "x_pos": 0.0, "y_pos": 9.0, "atyp": "LSA"},
                                  {"id": 16, "x_pos": 2.0, "y_pos": 9.0, "atyp": "LSA"}])
    # line2.drawVertexIter(line2Face.darts[0])
    # f3 = am.getFace(line2Face.darts[0])
    # print(f3)

    am.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 7.5, "atyp": "POND"},
                                {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 8.5, "atyp": "POND"},
                                {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 6.5, "atyp": "POND"}], "Pond")

    am.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 0.25, "y_pos": 7.5, "atyp": "SHRUB"},
                                {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 8.5, "atyp": "SHRUB"},
                                {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 6.5, "atyp": "SHRUB"}], "Shrub")

    am.connectDartBeta2Face(line2Face)


    outside = am.createOutsideFace(am.darts[0], 0)

    pencil = Pencil()

    pencil.drawMapDartsFig(am, 1)

    pencil.initFig()
    pencil.drawSingleFaceDarts(am, line1Face, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(am, cropFace, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(am, line2Face, 1, 0.9, "red", "orange")
    pencil.drawSingleFaceDarts(am, outside, 1, 1.1, "blue", "purple")
    pencil.showFig()

    ### scene 2
    am_growth = nMap()
    print("/// Line 1 ////")
    line1 = am_growth.createFace(4, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0, "atyp": "LSA"},
                                     {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 3.0, "atyp": "LSA"},
                                     {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0, "atyp": "LSA"},
                                     {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0, "atyp": "LSA"}], "Line 1")

    am_growth.createFilledGapFace(line1, 4, [{"id": uuid.uuid4(), "x_pos": 1.25, "y_pos": 0.5, "atyp": "TREE"},
                                            {"id": 10, "x_pos": 1.25, "y_pos": 2.0, "atyp": "TREE"},
                                            {"id": 11, "x_pos": 1.75, "y_pos": 2.0, "atyp": "TREE"},
                                            {"id": 12, "x_pos": 1.75, "y_pos": 0.5, "atyp": "TREE"}], "Tree")

    am_growth.createFilledGapFace(line1, 4, [{"id": 17, "x_pos": 0.25, "y_pos": 0.5, "atyp": "TREE"},
                                             {"id": 18, "x_pos": 0.25, "y_pos": 2.0, "atyp": "TREE"},
                                             {"id": 19, "x_pos": 0.75, "y_pos": 2.0, "atyp": "TREE"},
                                             {"id": 20, "x_pos": 0.75, "y_pos": 0.5, "atyp": "TREE"}], "Tree")

    print("/// Rectangle de culture  ////")
    # crop = nMap()
    cropFace = am_growth.createFace(4, [{"id": 5, "x_pos": 2.0, "y_pos": 3.0, "atyp": "CROP"},
                                        {"id": 6, "x_pos": 0.0, "y_pos": 3.0, "atyp": "CROP"},
                                        {"id": 7, "x_pos": 0.0, "y_pos": 6.0, "atyp": "CROP"},
                                        {"id": 8, "x_pos": 2.0, "y_pos": 6.0, "atyp": "CROP"}])

    #map_growth = am_growth.mergeNMaps(cropFace)
    #map_growth = am_growth.mergeNMaps(am_growth)
    am_growth.connectDartBeta2Face(cropFace)

    print("/// Line 2  ////")
    #line2 = nMap()
    line2Face = am_growth.createFace(4, [{"id": 13, "x_pos": 2.0, "y_pos": 6.0, "atyp": "LSA"},
                                         {"id": 14, "x_pos": 0.0, "y_pos": 6.0, "atyp": "LSA"},
                                         {"id": 15, "x_pos": 0.0, "y_pos": 9.0, "atyp": "LSA"},
                                         {"id": 16, "x_pos": 2.0, "y_pos": 9.0, "atyp": "LSA"}])
    # am_growth.drawVertexIter(line2Face.darts[0])
    am_growth.createFilledGapFace(line2Face, 5, [{"id": uuid.uuid4(), "x_pos": 1.0, "y_pos": 7.5, "atyp": "TREE"},
                                            {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 9, "atyp": "TREE"},
                                            {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 9, "atyp": "TREE"},
                                            {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 6, "atyp": "TREE"},
                                            {"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 6, "atyp": "TREE"}], "Tree")
    # treeBoutside = line2.createFace(3, [{"id": uuid.uuid4(), "x_pos": 1.75, "y_pos": 9},
    #                                 {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 9},
    #                                 {"id": uuid.uuid4(), "x_pos": 1.95, "y_pos": 10}])
    # am_growth.mergeNMaps(treeBoutside)
    am_growth.createFilledGapFace(line2Face, 3, [{"id": uuid.uuid4(), "x_pos": 0.15, "y_pos": 7.5, "atyp": "POND"},
                            {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 8.5, "atyp": "POND"},
                            {"id": uuid.uuid4(), "x_pos": 0.75, "y_pos": 6.5, "atyp": "POND"}], "Pond")

    #am_growth.mergeNMaps(line2Face)
    #am_growth.mergeNMaps(am_growth)
    am_growth.connectDartBeta2Face(line2Face)

    pencil.initFig()
    pencil.drawMap(am_growth,11)
    pencil.showFig()


def createTest(do_outside: int):

    am = nMap()
    #
    rect = am.createFace(4,[{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0, "atyp": "LSA"},
                         {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 4.0, "atyp": "LSA"},
                         {"id": uuid.uuid4(), "x_pos": 1.2, "y_pos": 4.0, "atyp": "LSA"},
                         {"id": uuid.uuid4(), "x_pos": 1.2, "y_pos": 0.0, "atyp": "LSA"}], "LSARect")

    carre = am.createFace(4,[{"id": uuid.uuid4(), "x_pos": 1.2, "y_pos": 0.0, "atyp": "CROP"},
                         {"id": uuid.uuid4(), "x_pos": 1.2, "y_pos": 4.0, "atyp": "CROP"},
                         {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 4.0, "atyp": "CROP"},
                         {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 0.0, "atyp": "CROP"}], "Crop")

    #rect2 = am.createFace(4,[{"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 0.0, "atyp": "LSA"},
    #                     {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 4.0, "atyp": "LSA"},
    #                     {"id": uuid.uuid4(), "x_pos": 4.2, "y_pos": 4.0, "atyp": "LSA"},
    #                     {"id": uuid.uuid4(), "x_pos": 4.2, "y_pos": 0.0, "atyp": "LSA"}], "LSARect")

    # # triang = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 2, "y_pos": 2},
    # #                     {"id": uuid.uuid4(), "x_pos": 3, "y_pos": 2},
    # #                     {"id": uuid.uuid4(), "x_pos": 2, "y_pos": 3}], "Triangle")

    am.connectDartBeta2Face(carre)


    #myhole = am.createFilledGapFace(carre, 4, [{"id": uuid.uuid4(), "x_pos": 1.8, "y_pos": 1.0},
    #                     {"id": uuid.uuid4(), "x_pos": 1.8, "y_pos": 3.0},
    #                     {"id": uuid.uuid4(), "x_pos": 2.5, "y_pos": 3.0},
    #                     {"id": uuid.uuid4(), "x_pos": 2.5, "y_pos": 1.0}], "Hole")

    #am.subdiveDart2(am.darts[2], 1, 0.5)

    if do_outside > 0:
        outside = am.createOutsideFace(am.darts[0],0)

    #am.drawVertexIter (am.darts[triang.dartid])

    #am.subdiveDart(am.darts[triang.dartid], 1, 0.5)

    #

    #
    # # carre.gap[0].drawVertexIter(carre.gap[0].darts[0])
    #

    am.printfDartList(am.darts)

    # am.mergeTwoFaces(am.darts[rect.dartid], am.darts[carre.dartid])

    print ("\n Now Dual map \n")

    # compute dual and print all dual contents
    ##dual_am = am.createSimpleDual()
    #dual_am = am.createDual()
    #dual_am.printfDartList(dual_am.darts)

    print ("\n Let's draw now  \n")

    pencil = Pencil()
    pencil.initFig()
    ## pencil.drawSingleFace(am, triang)
    #pencil.drawFaceDarts(am, triang, 2)
    #pencil.showFig()
    #pencil.drawMapDarts(am, 0)

    #pencil.drawMapDarts (am,1, 1)
    #am.mergeTwoFaces(am.darts[rect.dartid], am.darts[carre.dartid])
    am.printfDartList(am.darts)
    pencil.drawMapDarts (am, DRAW_FACE+DRAW_TXT+DRAW_DART)

    #pencil.drawDualMapDarts (dual_am, 1, 1)
    pencil.showFig()
    #am.drawVertexIter (am.darts[triang.dartid])



def createRect ( map:nMap, xo, yo, xf, yf, atype:str, name:str):
    face = map.createFace(4,[{"id": uuid.uuid4(), "x_pos": xo, "y_pos": yo, "atyp": atype},
                         {"id": uuid.uuid4(), "x_pos": xo, "y_pos": yf, "atyp": atype},
                         {"id": uuid.uuid4(), "x_pos": xf, "y_pos": yf, "atyp": atype},
                         {"id": uuid.uuid4(), "x_pos": xf, "y_pos": yo, "atyp": atype}], name)
    return face

def createHole ( map:nMap, fac:Face, xo, yo, xf, yf, atype:str, name:str):
    fhole = map.createFilledGapFace(fac, 4, [{"id": uuid.uuid4(), "x_pos": xo, "y_pos": yo, "atyp": atype},
                         {"id": uuid.uuid4(), "x_pos": xo, "y_pos": yf, "atyp": atype},
                         {"id": uuid.uuid4(), "x_pos": xf, "y_pos": yf, "atyp": atype},
                         {"id": uuid.uuid4(), "x_pos": xf, "y_pos": yo, "atyp": atype}], name)

    return fhole



def createPlantPhenomics(do_outside):

    am = nMap()
    #

    if True:
        rect1 = createRect (am, 0.0, 0.0, 2.0, 10.0, "LSA", "UVS1")
        myhole1 = createHole(am, rect1, 0.3, 1.0, 1.0, 1.7, "TREE", "Tree1")
        myhole2 = createHole(am, rect1, 0.3, 3.5, 1.0, 4.2, "TREE", "Tree2")
        myhole3 = createHole(am, rect1, 0.3, 6.0, 1.0, 6.7, "TREE", "Tree3")
        myhole4 = createHole(am, rect1, 0.3, 8.5, 1.0, 9.2, "TREE", "Tree4")

        carre = createRect(am, 2.0, 0.0, 8.0, 10.0, "CROP", "Crop")

        rect2 = createRect (am, 8.0, 0.0, 10.0, 10.0, "LSA", "UVS2")
        myhole5 = createHole(am, rect2, 8.5, 1.0, 9.5, 1.7, "TREE", "Tree5")
        myhole6 = createHole(am, rect2, 8.5, 3.5, 9.5, 4.2, "TREE", "Tree6")
        myhole7 = createHole(am, rect2, 8.5, 6.0, 9.5, 6.7, "TREE", "Tree7")
        myhole8 = createHole(am, rect2, 8.5, 8.5, 9.5, 9.2, "TREE", "Tree8")

        am.connectDartBeta2Face(carre)


    am.connectDartBeta2Face(carre)
    if do_outside:
        outside = am.createOutsideFace(am.darts[0],0)


    #am.printfDartList(am.darts)

    print ("\n Now Dual map \n")

    # compute dual and print all dual contents
    #dual_am = am.createSimpleDual()
    dual_am = am.createDual()
    #dual_am.printfDartList(dual_am.darts)

    print ("\n Let's draw now  \n")

    pencil = Pencil()
    pencil.initFig()

    #pencil.drawFaceDarts(am, rect1, 1, 1)
    pencil.drawMap(am, DRAW_FACE + DRAW_DART + DRAW_TXT)
    #pencil.drawMapDarts(am, DRAW_DART + DRAW_TXT)

    if do_outside > 0:
        pencil.drawFace(am, outside, DRAW_DART+DRAW_FACE+DRAW_TXT)

    print ("\n Let's draw now  \n")
    pencil.drawDualMapDarts (dual_am, DRAW_DART+DRAW_FACE)
    pencil.showFig()
    #am.drawVertexIter (am.darts[triang.dartid])




def createPlantPhenomics_croissance(do_outside, do_merge:int =0):

    am = nMap()
    #
    rect1_1 = am.createFace(5, [{"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 0.7, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 0.5, "y_pos": 2.0, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 3.3, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 1.05, "atyp": "Tree"}], "Tree1")


    # rect1_2 = am.createFace(5, [{"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 3.7, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 0.5, "y_pos": 5.0, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 6.3, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 6.0, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 4.0, "atyp": "Tree"}], "Tree2")

    rect1_3 = am.createFace(5, [{"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 6.7, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 0.5, "y_pos": 8.0, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 9.3, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 9, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 7.0, "atyp": "Tree"}], "Tree3")

    rect1_LSA = am.createFace(14, [{"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 0.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 0.0, "y_pos": 10.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 10.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 9.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 9.3, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 0.5, "y_pos": 8.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 6.7, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 7.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 3.3, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 0.5, "y_pos": 2.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 1.5, "y_pos": 0.7, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 1.05, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0, "atyp": "LSA"}],"UVS1")

    # rect1_2 = createHole(am, rect1_LSA, 0.3, 3.5, 1.0, 4.2, "Tree", "Tree2")

    mix_1 = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 1.05, "atyp": "Tree"}, # y = 1 ok mais mix connecté à l'outside  | y = 1.05 Bug index out of range
                              {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 2.0, "atyp": "Tree"},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0, "atyp": "Tree"}], "Mix1")

    # mix_2 = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 4.0, "atyp": "Tree"},
    #                           {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 5.0, "atyp": "Tree"},
    #                           {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 6.0, "atyp": "Tree"}], "Tree2")

    mix_3 = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 7.0, "atyp": "Tree"},
                              {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 8.0, "atyp": "Tree"},
                              {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 9.0, "atyp": "Tree"}], "Mix3")

    carre = am.createFace(16, [{"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 0.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 1.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 2.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 3.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 7.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 3.0, "y_pos": 8.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 9.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 2.0, "y_pos": 10.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 10.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 9.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 7.0, "y_pos": 8.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 7.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 3.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 7.0, "y_pos": 2.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 1.0, "atyp": "CROP"},
                               {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 0.0, "atyp": "CROP"}
                               ], "Crop")

    mix_4 = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 1.05, "atyp": "Tree"}, # y = 1 ok mais mix connecté à l'outside  | y = 1.05 Bug index out of range
                              {"id": uuid.uuid4(), "x_pos": 7.0, "y_pos": 2.0, "atyp": "Tree"},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 3.0, "atyp": "Tree"}], "Mix4")

    # mix_5 = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 4.0, "atyp": "Tree"},
    #                           {"id": uuid.uuid4(), "x_pos": 7.0, "y_pos": 5.0, "atyp": "Tree"},
    #                           {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 6.0, "atyp": "Tree"}], "Tree5")

    mix_6 = am.createFace(3, [{"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 7.0, "atyp": "Tree"},
                              {"id": uuid.uuid4(), "x_pos": 7.0, "y_pos": 8.0, "atyp": "Tree"},
                              {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 9.0, "atyp": "Tree"}], "Mix6")


    rect2_1 =  am.createFace(5, [{"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 0.7, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 9.5, "y_pos": 2.0, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 3.3, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 3.0, "atyp": "Tree"},
                                {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 1.05, "atyp": "Tree"}], "Tree4") #createRect(am, 8.0, 1.0, 10.0, 3.0, "TREE", "Tree4")


    # rect2_2 = am.createFace(5, [{"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 3.7, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 9.5, "y_pos": 5.0, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 6.3, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 6.0, "atyp": "Tree"},
    #                   {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 4.0, "atyp": "Tree"}], "Tree5")

    rect2_3 = am.createFace(5, [{"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 6.7, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 9.5, "y_pos": 8.0, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 9.3, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 9, "atyp": "Tree"},
                      {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 7.0, "atyp": "Tree"}], "Tree3")

    rect2_LSA =  am.createFace(14, [ {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 0.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 10.0, "y_pos": 0.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 10.0, "y_pos": 10.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 10.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 9.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 9.3, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 9.5, "y_pos": 8.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 6.7, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 7.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 3.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 3.3, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 9.5, "y_pos": 2.0, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.5, "y_pos": 0.7, "atyp": "LSA"},
                                   {"id": uuid.uuid4(), "x_pos": 8.0, "y_pos": 1.05, "atyp": "LSA"}
                                   ],"USV2")

    #createRect(am, 8.0, 9.0, 10.0, 10.0, "LSA", "LSA2_D")
    am.reverseMap(am.darts[rect2_LSA.dartid])
    # rect2_2 = createHole(am, rect2_LSA, 8.5, 3.5, 9.5, 4.2, "Tree", "Schrub2")

    am.reverseMap(am.darts[mix_1.dartid])
    # am.reverseMap(am.darts[mix_2.dartid])
    am.reverseMap(am.darts[mix_3.dartid])
    am.reverseMap(am.darts[rect2_3.dartid])
    am.reverseMap(am.darts[rect2_1.dartid])

    am.connectDartBeta2Face(carre)
    am.connectDartBeta2Face(rect1_1)


    # am.connectDartBeta2Face(rect1_2)
    am.connectDartBeta2Face(rect1_3)

    am.connectDartBeta2Face(rect2_1)
    # am.connectDartBeta2Face(rect2_2)

    am.connectDartBeta2Face(rect2_3)

    am.connectDartBeta2Face(rect1_LSA)

    am.connectDartBeta2Face(rect2_LSA)

    am.connectDartBeta2Face(mix_1)
    am.connectDartBeta2Face(mix_3)
    am.connectDartBeta2Face(mix_4)
    am.connectDartBeta2Face(mix_6)

    if do_merge == 1:
        am.mergeTwoFacesIntoOne(rect1_1, mix_1)
        # am.mergeTwoFacesIntoOne(rect1_2, mix_2)
        am.mergeTwoFacesIntoOne(rect1_3, mix_3)
        am.mergeTwoFacesIntoOne(rect2_1, mix_4)
        # am.mergeTwoFacesIntoOne(rect2_2, mix_5)
        am.mergeTwoFacesIntoOne(rect2_3, mix_6)

    if (do_outside):
        outside = am.createOutsideFace(am.darts[1],0)


    #am.printfDartList(am.darts)

    print ("\n Now Dual map \n")

    # compute dual and print all dual contents
    #dual_am = am.createSimpleDual()
    dual_am = am.createDual()
    #dual_am.printfDartList(dual_am.darts)

    print ("\n Let's draw now  \n")

    pencil = Pencil()
    pencil.initFig()

    pencil.drawMap(am, DRAW_TXT+DRAW_FACE+DRAW_DART)
    #pencil.drawMapDarts(am, DRAW_TXT+DRAW_FACE+DRAW_DART)
    if (do_outside):
        pencil.drawFace(am, outside, DRAW_TXT+DRAW_FACE)

    pencil.drawDualMapDarts (dual_am, 0)
    pencil.showFig()
    #am.drawVertexIter (am.darts[triang.dartid])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ### scene 1

    #createPmaExample()

    #createExample()

    outside = 0

    createTest(outside)
    createTest(1-outside)
    #
    createPlantPhenomics(outside)
    createPlantPhenomics(1-outside)

    createPlantPhenomics_croissance(outside,0)
    createPlantPhenomics_croissance(1-outside,0)
    createPlantPhenomics_croissance(outside,1)
    createPlantPhenomics_croissance(1-outside,1)

