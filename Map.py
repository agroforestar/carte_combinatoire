#desc: Map class
#ref: Combinatorial Maps: Efficient Data Structures for Computer Graphics and Image Processing, p158, data structure Dart (Listing 5.1)
#date: 03/02/2023
#author: L.L.
#TODO : fonction 1 brin par 2 autres brins pondéré par un paramètre (0 et t) qui correspondra plus tard au coord de l'intersection
#TODO : faire ex avec 2 carré : a. on les sibdivisent par 2 puis on les merge b. idem mais avec des trous dans les carrés
from multipledispatch import dispatch  # importing the module
from Dart import *
import uuid
import numpy as np
NB_MARKS = 8 #taille allouee du tableau au dart
N_DIM = 2  #nombre de dimension de la carte
DUMMY = 99999

#ref: Listing 5.2
class nMap:
    ## Construtor based on algorithme 22 (Damiand & Lienhardt 2014)
    def __init__(self, id= uuid.uuid4()):
        self.id = id
        self.nbd = 0
        self.darts = []
        self.freeMarks = []
        self.faces = []
        self.bfaces = []
        self.null_dart = myDart(N_DIM, NB_MARKS)
        for i in range(0, N_DIM+1):
            self.null_dart.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            self.freeMarks.append(i)
            self.null_dart.marks[i] = False

    ## @desc Indicate a free index, based on algorithme 23 (Daminand & Lienhardt 2014)
    # @return an index if available (else -1)
    def reserveMarkMap(self):
        if len(self.freeMarks) == 0:
            return -1
        i = self.freeMarks.pop()
        return i

    ## @desc: make given index available based on algorithme 24 (Daminad & Lienhardt 2014)
    def freeMarkMap(self, i:int):
        self.freeMarks.append(i)

    ## based on algorithm 25 (Daminad & Lienhardt 2014)
    # @return boolean value of index i in on dart d
    def isMarkedMap(self, d:Dart, i:int):
        return d.marks[i]


    ## @desc set value True of index i in on dart d, based on algorithm 26 (Damiand & Lienhardt 2014)
    def markMap(self, d:Dart, i:int):
        d.marks[i] = True


    # based on algorithm 27 (Damiand & Lienhardt 2014)
    # @desc set value False of index i in on dart d
    def unmarkMap(self, d:Dart, i:int):
        d.marks[i] = False


    # based on algorithm 28 (Diamiand & Lienhardt 2014)
    # @desc Sélectionne la permutation en fonction du raang involution, (Si sur beta1 -> beta0, beta0->beta1, beta2->beta2)
    # rem : pas clair sur le paramètre i (varie entre 0 et N_DIM)
    def inv(self, i:int):
        if i == 0:
            return 1
        elif i == 1:
            return 0
        return i

    # based en algorithm 29(Damiand & Lienhardt 2014)
    # @desc: Run through all  the darts of 〈βi1, ..., βik 〉(d). (parcours d'orbite généralisé)
    #     # @param self: current map;
    # @param d ∈ self.Darts: the starting dart;
    # @param (i1, ..., ik): a valid sequence of permutation (coding by integers between 0 and N_DIM).
    def genericIter(self, d:Dart, operation:list):
        ma = self.reserveMarkMap()
        p = []
        p.append(d)
        self.markMap(d, ma)
        self.markMap(self.null_dart, ma)
        while len(p)>0:
            cur = p.pop()
            for j in range(0, len(operation)):
                if not self.isMarkedMap(cur.betas[operation[j]], ma):
                    self.markMap(cur.betas[operation[j]], ma)
                    #TO DO
                p.append(cur.betas[operation[j]])

        for j in range(0, len(operation)): #Unmark all marked darts
            if self.isMarkedMap(cur.betas[operation[j]], ma):
                self.unmarkMap(cur.betas[operation[j]], ma)
        ma = self.null_dart
        self.freeMarkMap(ma)

    # based on algorithm 30 (Damiand & Lienhardt 2014)
    #à revoir et faire pap a pas dans le cas du 2D map
    def vertexIter(self, d:Dart):
        ma = self.reserveMarkMap()
        p = [d]
        self.markMap(d, ma)
        self.markMap(self.null_dart, ma)
        while len(p)>0:
            cur = p.pop()
            for i in range(1, N_DIM):
                for j in range(i+1, N_DIM +1):
                    if not self.isMarkedMap(cur.betas[j].betas[i], ma):
                        self.markMap(cur.betas[j].betas[i], ma)
                        p.append(cur.betas[j].betas[i])
                    if not self.isMarkedMap(cur.betas[self.inv(i)].betas[j], ma):
                        self.markMap(cur.betas[self.inv(i)].betas[j], ma)
                        p.append(cur.betas[self.inv(i)].betas[j])

        for i in range(0, N_DIM-1):
            for j in range(i + 1, N_DIM):
                if self.isMarkedMap(cur.betas[j].betas[i], ma):
                    self.unmarkMap(cur.betas[j].betas[i], ma)
                if self.isMarkedMap(cur.betas[self.inv(i)].betas[j], ma):
                    self.unmarkMap(cur.betas[self.inv(i)].betas[j], ma)
        self.freeMarkMap(ma)

    ## Print the list of darts in a list
    # @param dartlist : list of darts
    def printfDartList(self, dartlist: list[myDart]):
        for dart in dartlist:
            cur = dart
            print("Id:"+str(cur) + " b0:" + str(cur.betas[0]) + " b1:" + str(cur.betas[1])  + " b2:" + str(cur.betas[2]) + "props" + str(cur.properties))


    ## Parcours la carte et affiche dans la console le parcours basé sur l'algorithme 30 (Damiand & Lienhardt 2014)
    # @param d : Dart de départ
    def drawVertexIter(self, d: Dart):
            ma = self.reserveMarkMap()
            p = [d]
            self.markMap(d, ma)
            self.markMap(self.null_dart, ma)
            while len(p) > 0:
                cur = p.pop()
                print(str(cur) + " suivant " + str(cur.betas[0]) + "propertes" + str(cur.properties))
                for i in range(1, N_DIM ):
                        if not self.isMarkedMap(cur.betas[i], ma):
                            self.markMap(cur.betas[i], ma)
                            p.append(cur.betas[i])
                        if not self.isMarkedMap(cur.betas[self.inv(i)], ma):
                            self.markMap(cur.betas[self.inv(i)], ma)
                            p.append(cur.betas[self.inv(i)])
            for d in self.darts:
                self.unmarkMap(d, ma)

            self.freeMarkMap(ma)

    # @desc: create a dart in current map without connexion with other darts based on algorithm 35 (Damiand & Lienhardt 2014)
    # @param self: current map
    # @return new dart
    @dispatch()
    def createDartNMap(self):
        d = myDart(N_DIM, NB_MARKS)
        self.darts.append(d)
        for i in range(0, N_DIM+1):
            d.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            d.marks[i] = False
        self.nbd += 1
        d.num = self.nbd
        return d

    # @desc: create a dart from values in current map without connexion with other darts based on algorithm 35 (Damiand & Lienhardt 2014)
    # @param self: current map
    # @param id: id of the nex dart
    # @param x: x coordinate
    # @param y: y coordinate
    # @return new dart
    @dispatch(uuid.UUID, float, float)
    def createDartNMap(self, id : uuid.UUID, x:float, y:float):
        d = myDart.withValue(N_DIM, NB_MARKS, id, x, y)
        self.darts.append(d)
        for i in range(0, N_DIM+1):
            d.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            d.marks[i] = False
        self.nbd += 1
        d.num = self.nbd
        return d

    # @desc: create a dart from dict in current map without connexion with other darts based on algorithm 35 (Damiand & Lienhardt 2014)
    # @param self: current map
    # @param propoerties: dictionnary with values
    # @return new dart
    @dispatch(dict)
    def createDartNMap(self, properties:dict):
        d = myDart.withProperties(N_DIM, NB_MARKS, properties)
        self.darts.append(d)
        for i in range(0, N_DIM + 1):
            d.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            d.marks[i] = False
        self.nbd += 1
        d.num = self.nbd
        return d

    ## Create a new face in the current map
    # @param nbSegment : number of side
    # @param properties: list with darts values [d1, d2,...]
    # @param facename: indicate what the face representes (ex. Tree, crop...)
    # @return new face
    def createFace(self, nbSegment :int, properties:list, facename: str = "FaceGeneric"):
        listdarts = []
        for i in range(0, nbSegment):
            listdarts.append(self.createDartNMap(properties[i]))
        face = Face()
        face.name = facename
        # face.darts = listdarts
        # self.darts.append(listdarts)
        self.faces.append(face)
        self.bfaces.append(listdarts[0].num)
        face.dartid = listdarts[0].num
        self.buildPolygonBeta1(listdarts)
        return face

    ## Create a new face in the indicated hole
    # @param hole: hole to fill
    # @param facename: indicate what the face representes (ex. Tree, crop...)
    # @return new face
    def fillHoleFace(self, hole, facename: str = "FaceHoleGeneric"):
        listdarts = hole.getFaceBeta(hole.darts[0], 1)
        newdarts = []
        for dart in listdarts:
            nd = myDart.withProperties(N_DIM, NB_MARKS, dart.properties)
            newdarts.append(nd)
            # nd.properties["id"] = uuid.uuid4()
            nd.betas[2] = dart
            dart.betas[2] = nd
        newface = Face()
        #newface.darts = newdarts
        self.faces.append(newface)
        self.bfaces.append(newdarts[0].num)
        newface.dartid = newdarts[0].num
        # self.darts.append(newDarts)
        newface.buildPolygonBeta0(newdarts)
        newface.name = facename
        return newface

    ## Create a hole and a new face in the face
    # @param face: current face
    # @param nbSegment: side of the hole
    # @param properties: list with darts values [d1, d2,...]
    # @param nameface: indicate what the face representes (ex. Tree, crop...)
    # @return new face
    def createFilledGapFace(self, face, nbSegment: int, properties: list, nameface: str):
        listdarts: list[myDart] = []
        for i in range(0, nbSegment):
            listdarts.append(self.createDartNMap(properties[i]))
        newgap = Face()
        #newgap.darts = listdarts
        face.gap.append(newgap)
        #self.bfaces.append(listdarts[0].num)
        newgap.dartid = listdarts[0].num
        self.buildPolygonBeta0(listdarts)
        newgap.name = "Hole"+face.name
        newgap.ishole = 1

        # listdarts = hole.getFaceBeta(hole.darts[0], 0)
        newdarts: list[myDart] = []
        for dart in listdarts:
            # nd = myDart.withProperties(N_DIM, NB_MARKS, dart.properties)
            nd = self.createDartNMap(dart.properties)
            newdarts.append(nd)
            # nd.properties["id"] = uuid.uuid4()
            nd.betas[2] = dart
            dart.betas[2] = nd
        newface = Face()
        #newface.darts = newdarts
        self.bfaces.append(newdarts[0].num)
        newface.dartid = newdarts[0].num
        newface.name = nameface
        self.buildPolygonBeta1(newdarts)
        self.faces.append(newface)
        return newface

    ##  extract all darts without beta[2] issued from dart dstart
    # @param dstart: Starting dart
    # @return outdarts: darts without beta[2]
    def getUnconnectedBeta2(self, dstart:Dart):
        outdarts = []
        d = dstart
        dorig : myDart = self.null_dart
        n : int = 0
        while n == 0:
            if d.betas[2] == self.null_dart:
                dorig = d
                n = 1
            else:
                d = d.betas[1]
                if d == dstart:
                    n = -1

        if n == 0:
            d = dstart
            while n == 0:
                if d.betas[2] == self.null_dart:
                    # outdarts.append(d)
                    dorig = d
                    n = n + 1
                else:
                    d = d.betas[0]
                    if d == dstart:
                        n = -1

        if n == 1:
            thend: bool = False
            d = dorig
            no = 0
            while not thend:
                if d.betas[2] == self.null_dart:
                    outdarts.append(d)
                    no = no + 1
                else:
                    d = d.betas[2]
                d = d.betas[1]
                if d == dorig:
                    thend = True

        return outdarts

    ##  extract all darts without beta[2] issued from dart dstart
    # @param dstart: Starting dart
    # @return outdarts: darts without beta[2]
    def getUnconnectedBeta2Fast(self, dstart):
        outdarts = []
        no = 0
        for d in self.darts:
            if d.betas[2] == self.null_dart and d.deleted == 0:
                outdarts.append(d)
                no = no + 1

        return outdarts

    ## Create outisde Face of the map
    # @param d: Starting dart
    # @param mode:
    # @return oustide: outside face
    def createOutsideFace(self, d, mode):
        # retrieve all darts without beta2

        #listdarts = self.getUnconnectedBeta2(d)
        listdarts = self.getUnconnectedBeta2Fast(d)
        nb = len(listdarts)
        #connect darts
        #for i in range(0, nbSegment):
        #    listoutdarts.append(self.createDartNMap(properties[i]))

        xmin = 99999.0
        ymin = xmin
        xmax = -xmin
        ymax = xmax

        print("/// Outside  Nb darts : " + str(nb) + " ////")

        # listDarts = hole.getFaceBeta(hole.darts[0], 0)
        #newdarts = []
        for dart in listdarts:
            cur = dart
            print("Outside:" + " Id:" + str(cur) + " b0:" + str(cur.betas[0]) + " b1:" + str(
                   cur.betas[1]) + " b2:" + str(cur.betas[2]) + "props" + str(cur.properties) )
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y
            #nd = self.createDartNMap(dart.properties)
            #newdarts.append(nd)
            ## nd.properties["id"] = uuid.uuid4()
            #nd.betas[2] = dart
            #dart.betas[2] = nd

        print("Outside : "+str(xmin)+" , "+str(xmax)+" , "+str(ymin)+" , "+str(ymax))

        if mode == 0:
            nd = 0
            # newface.darts = newdarts
            #dar = self.createDartNMap(dart.properties)
            # newdarts.append(nd)
            ## nd.properties["id"] = uuid.uuid4()
            newdarts = []
            dpred = self.null_dart
            for dart in listdarts:
                dar = self.createDartNMap()
                dar.betas[2] = dart
                dart.betas[2] = dar
                dar.betas[0] = dpred
                newdarts.append(dar)
                if dpred != self.null_dart:
                    dpred.betas[1] = dar
                dpred = dar
                dar.properties["atyp"] = "BD_"+dart.properties["atyp"]
                dar.properties["x_pos"] = dart.properties["x_pos"]
                #dar.properties["y_pos"] = ymax + dart.properties["y_pos"]
                y = dart.properties["y_pos"]
                dar.properties["y_pos"] = y * (1 + 1.3*(y-ymin)/(ymax-ymin))
                cur = dar
                print("New Outside:" + " Id:" + str(cur) + " b0:" + str(cur.betas[0]) + " b1:" + str(
                    cur.betas[1]) + " b2:" + str(cur.betas[2]) + "props" + str(cur.properties))
            dpred.betas[1] = newdarts[0]
            newdarts[0].betas[0] = dpred

            #self.buildPolygonBeta0(newdarts)
            newface = Face()
            self.faces.append(newface)
            newface.name = "Outside"
            self.bfaces.append(newdarts[0].num)
            #self.buildPolygonBeta0(newdarts)

        if Face and mode == 1:
            outside = self.createFace(4, [{"id": uuid.uuid4(), "x_pos": xmin-1, "y_pos": ymin-1, "atyp": "ENV"},
                                          {"id": uuid.uuid4(), "x_pos": xmin-1, "y_pos": 3*ymax, "atyp": "ENV"},
                                          {"id": uuid.uuid4(), "x_pos": xmax+1, "y_pos": 3*ymax, "atyp": "ENV"},
                                          {"id": uuid.uuid4(), "x_pos": xmax+1, "y_pos": ymin-1, "atyp": "ENV"}], "System")
            #newface = Face()
            # newface.darts = newdarts
            #self.faces.append(newface)
            #newface.name = "Border"
            #newface.ishole = 1
            #self.bfaces.append(newdarts[0].num)
            #self.buildPolygonBeta0(newdarts)
            #outside.gap.append(newface)
            newface = outside

        return newface

    # based on algorithm 36 (Damiand & Lienhardt 2014)
    # @param d : dart to remove
    def removeIsolatedDartNMap(self, d:Dart):
        self.darts.remove(d)

    # based on algorithm 37 (Damiand & Lienhardt 2014)
    def __copy__(self):
        copy = nMap()
        copy.darts = None
        copy.freeMarks = self.freeMarks
        assoc = dict()
        assoc[self.null_dart] = copy.null_dart
        for d in self.darts:
            assoc[d] = copy.createDartNMap()
        k = N_DIM
        for d in self.darts:
            d_copy = assoc[d]
            for i in range(0, k):
                d_copy.betas[i] = assoc[d.betas[i]]
            for i in range(0, NB_MARKS-1):
                d_copy.marks[i] = d.marks[i]

    # based on algorithm 34 (Daminad & Lienhardt 2014)
    def isFreeNMap(self, d:Dart, i:int):
        if (d.betas[i] == self.null_dart):
            return True
        else:
            return False

    # based on algorithm 44 (Damiand & Lienhardt 2014)
    def oneSewMyMap(self, d1:Dart, d2:Dart):
        # if self.isFreeNMap(d1, 0)  :
            d1.betas[1] = d2
            d2.betas[0] = d1

    # Fixe le beta2 (le dart dans le sens inverse)
    # @param current: le dart traité
    # @param opp: le dart sur lequel beta2(current) doit renvoyer
    def setBeta2(self, current:Dart, opp : Dart):
        if current != self.null_dart:
            if opp != self.null_dart:
                current.betas[2] = opp
                opp.betas[2] = current
            else:
                print("The second dart is empty")
        else:
            print("The current dart is empty")

    # Determine if the dart is the beta2 of the given dart (test the coordinates)
    # @param current: current dart
    # @param d: tested dart
    # @return True : the coordinates are the same
    def isBeta2(self, curent:myDart, d:myDart):
        coord_current = curent.getCoordinates()
        coord_next = curent.betas[1].getCoordinates()
        coord_d = d.getCoordinates()
        coord_pred = d.betas[0].getCoordinates()
        if coord_d == coord_next and coord_current == coord_pred:
            return True
        else:
            return False

    # Create a polygon
    # @param listDart: list with all darts of the polygon
    def buildPolygonBeta0(self, listDart):
        lasrIndex = len(listDart)-1
        for i in range(0, lasrIndex):
            self.oneSewMyMap(listDart[i+1], listDart[i])
        self.oneSewMyMap(listDart[0], listDart[lasrIndex])

    # Create a polygon
    # @param listDart: list with all darts of the polygon
    def buildPolygonBeta1(self, listDart):
        lasrIndex = len(listDart)-1
        for i in range(0, lasrIndex):
            self.oneSewMyMap(listDart[i], listDart[i+1])
        self.oneSewMyMap(listDart[lasrIndex], listDart[0])

    # Renvoie tous les darts de la face dont le dart d appartient
    # @param d: Starting dart
    # @return face by the list of darts
    def getFace(self, d: Dart):
        ma = self.reserveMarkMap()
        p = [d]
        self.markMap(d, ma)
        self.markMap(self.null_dart, ma)
        dartFace = []
        while len(p) > 0:
            cur = p.pop()
            dartFace.append(cur)
            for i in range(1, N_DIM):
                if not self.isMarkedMap(cur.betas[i], ma):
                    self.markMap(cur.betas[i], ma)
                    p.append(cur.betas[i])
                if not self.isMarkedMap(cur.betas[self.inv(i)], ma):
                    self.markMap(cur.betas[self.inv(i)], ma)
                    p.append(cur.betas[self.inv(i)])
        for d in dartFace:
            self.unmarkMap(d, ma)
        self.freeMarkMap(ma)
        return dartFace

    # Renvoie les darts de la face à partir du dart d en suivant les beta (0 contour de la face, 1 contour intérieur)
    # @param d : Starting dart
    # @param beta: indicates which dart desired (0 : beta0, 1 beta1)
    # @return darts in the face
    def getFaceBeta(self, d: Dart, beta: int):
        ma = self.reserveMarkMap()
        p = [d]
        self.markMap(d, ma)
        self.markMap(self.null_dart, ma)
        dartsface = []
        while len(p) > 0:
            cur = p.pop()
            dartsface.append(cur)
            # for i in range(1, N_DIM):
            if not self.isMarkedMap(cur.betas[beta], ma):
                self.markMap(cur.betas[beta], ma)
                p.append(cur.betas[beta])
                # if not self.isMarkedMap(cur.betas[self.inv(i)], ma):
                #    self.markMap(cur.betas[self.inv(i)], ma)
                #    p.append(cur.betas[self.inv(i)])
        for d in dartsface:
            self.unmarkMap(d, ma)
        self.freeMarkMap(ma)
        return dartsface

    # Obtain all points of the face
    # @param d: Starting point
    # @param beta: indicates which dart desired (0 : beta0, 1 beta1)
    # @return list of coordinates
    def getCoordFromFace(self, d: Dart, beta: int):
        listdarts: list[myDart] = self.getFaceBeta(d, beta)
        coord = []
        for dart in listdarts:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        coord.append(coord[0])  # repeat the first point to create a 'closed loop'
        return coord


    def setCoordFaceCenter(self, d: Dart, beta: int):
        xs = 0
        ys = 0
        n = 0
        for dart in listdart:
            xs += dart.properties["x_pos"]
            ys += dart.properties["y_pos"]
            n += 1
        if n > 0:
            xs /= n
            ys /= n
        return xs, ys


    # Renvoit la liste des coordonées rattachées aux darts composant la face
    def getCoordMap(self):
        coord = []
        for dart in self.darts:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        return coord


    def getCoordListdarts(self, listdart, close: int):
        coord = []
        for dart in listdart:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        if close != 0:
            coord.append(coord[0])
        return coord



    def getCoordListdartsWithCtr(self, listdart):
        coord = self.getCoordListdarts(listdart, 0)
        xs, ys = zip(*coord)  # create lists of x and y values
        xm = np.mean(xs)
        ym = np.mean(ys)
        return coord, xm, ym



    def getCoordListdartsCenter(self, listdarts: list[myDart]):
        xs = 0
        ys = 0
        n = 0
        for dart in listdarts:
            xs += dart.properties["x_pos"]
            ys += dart.properties["y_pos"]
            n += 1
        if n > 0:
            xs /= n
            ys /= n
        return xs, ys



    def getCoordListdartsScaled(self, listdart, closed: int, coef: float):
        xs = []
        ys = []
        for dart in listdart:
            xs.append (dart.properties["x_pos"])
            ys.append (dart.properties["y_pos"])
        xm = np.mean(xs)
        ym = np.mean(ys)
        nxs = [coef * (x - xm) + xm for x in xs]
        nys = [coef * (y - ym) + ym for y in ys]
        if closed != 0 :
            nxs.append(nxs[0])
            nys.append(nys[0])
        return nxs, nys



    def reverseMapOld(self, d:Dart):
        face = self.getFace(d)
        for dart in face:
            temp = dart.betas[0]
            dart.betas[0] = dart.betas[1]
            dart.betas[1] = temp

    def reverseMap(self, d: Dart):
        listdarts: list[myDart] = self.getFaceBeta(d, 1)
        for dart in listdarts:
            if d.deleted == 0:
                temp = dart.betas[0]
                dart.betas[0] = dart.betas[1]
                dart.betas[1] = temp


    def getConnectedDart(self, cm:'nMap'):
        output = []
        fin = False
        i = 0
        print(self.darts)
        while not fin:
            print(i)
            d = self.darts[i]
            if d.deleted == 0:
                for d_prime in cm.darts:
                    d_next = d.betas[1]
                    d_pred = d.betas[0]
                    d_prime_next = d_prime.betas[1]
                    d_prime_pred = d_prime.betas[0]

                    if d.getCoordinates() == d_prime_next.getCoordinates() and d_next.getCoordinates() == d_prime.getCoordinates(): # cas où l'orientation des 2 cartes sont inversé
                        print("sens inverse inverse trouvé")
                        output.append(d)
                        output.append(d_prime)
                        fin = True
                    elif d.getCoordinates() == d_prime.getCoordinates() and d_next.getCoordinates() == d_prime_next.getCoordinates():
                        print("sens id inverse trouvé")
                        # MJ self.reverseMap(d_prime)
                        output.append(d)
                        # MJ output.append(d_prime.betas[1])
                        output.append(d_prime_next)
                        fin = True

            i = i+1
        return output

    def connectDartBeta2(self, cm:'nMap'):

        for d in self.darts:
            if d.betas[2] == self.null_dart and d.deleted == 0:
                d_next = d.betas[1]
                d_pred = d.betas[0]
                x = d.properties["x_pos"]
                y = d.properties["y_pos"]
                xn = d_next.properties["x_pos"]
                yn = d_next.properties["y_pos"]
                xp = d_pred.properties["x_pos"]
                yp = d_pred.properties["y_pos"]

                listdarts: list[myDart] = self.getFaceBeta(self.darts[cm.dartid], 0)
                for dm in listdarts:
                    if d.betas[2] == self.null_dart:
                        dm_next = dm.betas[1]
                        dm_pred = dm.betas[0]
                        xcm = dm.properties["x_pos"]
                        ycm = dm.properties["y_pos"]
                        xncm = dm_next.properties["x_pos"]
                        yncm = dm_next.properties["y_pos"]
                        xpcm = dm_pred.properties["x_pos"]
                        ypcm = dm_pred.properties["y_pos"]
                        dst = (x - xncm) * (x - xncm) + (y - yncm) * (y - yncm)
                        dste = (xn - xcm) * (xn - xcm) + (yn - ycm) * (yn - ycm)
                        if dst < 0.001 and dste < 0.001 :
                            d.betas[2] = dm
                            dm.betas[2] = d

    def connectDartBeta2Face(self, face:'Face'):

        for d in self.darts:
            if d.betas[2] == self.null_dart:
                d_next = d.betas[1]
                d_pred = d.betas[0]
                x = d.properties["x_pos"]
                y = d.properties["y_pos"]
                xn = d_next.properties["x_pos"]
                yn = d_next.properties["y_pos"]
                xp = d_pred.properties["x_pos"]
                yp = d_pred.properties["y_pos"]

                listdarts: list[myDart] = self.getFaceBeta(self.darts[face.dartid], 0)
                for dm in listdarts:
                    if d.betas[2] == self.null_dart:
                        dm_next = dm.betas[1]
                        dm_pred = dm.betas[0]
                        xcm = dm.properties["x_pos"]
                        ycm = dm.properties["y_pos"]
                        xncm = dm_next.properties["x_pos"]
                        yncm = dm_next.properties["y_pos"]
                        xpcm = dm_pred.properties["x_pos"]
                        ypcm = dm_pred.properties["y_pos"]
                        dst = (x - xncm) * (x - xncm) + (y - yncm) * (y - yncm)
                        dste = (xn - xcm) * (xn - xcm) + (yn - ycm) * (yn - ycm)
                        if dst < 0.01 and dste < 0.01 :
                            d.betas[2] = dm
                            dm.betas[2] = d



    #ref: Algorithme 40 (Damiand and Liendhard 2014)
    def mergeNMaps(self, cm: 'nMap'):
        #commun = self.getConnectedDart(cm)
        #self.setBeta2(commun[0], commun[1])
        self.connectDartBeta2(cm)
        merge = nMap()
        merge.faces = self.faces + cm.faces
        print(merge.faces)
        merge.freeMarks = list(set(self.freeMarks) & set(cm.freeMarks))
        assoc = dict()
        assoc[self.null_dart] = merge.null_dart
        assoc[cm.null_dart] = merge.null_dart
        unionDart = self.darts + cm.darts
        for d in unionDart:
            assoc[d] = merge.createDartNMap(d.properties)
        for d in unionDart:
            d_temp = assoc[d]
            for i in range(0, N_DIM+1):
                d_temp.betas[i] = assoc[d.betas[i]]
            for i in range(0, NB_MARKS):
                d_temp.marks[i] = d.marks[i]
        return merge


    #ref: Algorithme 40 (Damiand and Liendhard 2014)
    def mergeNMapsFace(self, face: 'Face'):
        #commun = self.getConnectedDart(cm)
        #self.setBeta2(commun[0], commun[1])
        self.connectDartBeta2Face(face)
        merge = nMap()
        merge.faces = self.faces + cm.faces
        print(merge.faces)
        merge.freeMarks = list(set(self.freeMarks) & set(cm.freeMarks))
        assoc = dict()
        assoc[self.null_dart] = merge.null_dart
        assoc[cm.null_dart] = merge.null_dart
        unionDart = self.darts + cm.darts
        for d in unionDart:
            assoc[d] = merge.createDartNMap(d.properties)
        for d in unionDart:
            d_temp = assoc[d]
            for i in range(0, N_DIM+1):
                d_temp.betas[i] = assoc[d.betas[i]]
            for i in range(0, NB_MARKS):
                d_temp.marks[i] = d.marks[i]
        return merge



# Hypothèse imposé : carte avec frontière  / Each Dart d, d.beta[2] != null
    #besoin de fonction de de correction lorsque l'hypothèse n'est pas remplie
    def orbit(self, d:Dart):
        current = d.betas[2]
        dartorbit = [current]
        while current != d:
            current = current.beta[0]
            dartorbit.append(current)
            current = current.beta[2]
            dartorbit.append(current)
        return dartorbit

    #hypthèse d : dart entrant dans l'orbit et les betas 2 sont fixé
    def crossOrbit(self, d:Dart):
        next = d.betas[0].betas[2].betas[0]
        return next

    # split a given dart in two
    def subdiveDart(self, d, fbeta: int, coef: float):
        nd = self.null_dart
        if coef > 0.0 and coef < 1.0 and (fbeta == 0 or fbeta == 1) :
            dnext = d.betas[fbeta]
            if dnext != self.null_dart:
                xpos: float = (dnext.properties["x_pos"] - d.properties["x_pos"])*coef + d.properties["x_pos"]
                ypos: float = (dnext.properties["y_pos"] - d.properties["y_pos"])*coef + d.properties["y_pos"]
                nd = self.createDartNMap(uuid.uuid4(),xpos, ypos)
                nd.betas[fbeta] = dnext
                nd.betas[1-fbeta] = d
                nd.betas[2] = self.null_dart
                d.betas[fbeta] = nd
                dnext.betas[1-fbeta] = nd

        return nd

    def subdiveDart2(self, d, fbeta: int, coef: float):
        nd = self.subdiveDart(d, fbeta, coef)
        if nd != self.null_dart and d.betas[2] != self.null_dart :
            nd2 = self.subdiveDart(d.betas[2], fbeta, coef)
            self.setBeta2(d.betas[2], nd)
            if nd2 != self.null_dart :
                self.setBeta2(d,nd2)
                #self.setBeta2(d.betas[2], nd)

    def deleteDart(self, d):
        if d != self.null_dart:
            d.betas[0] = self.null_dart
            d.betas[1] = self.null_dart
            d.betas[2] = self.null_dart
            d.deleted = 1
            d.properties["x_pos"] = -99999.99
            d.properties["y_pos"] = -99999.99

    def mergeTwoFacesInOne(self, face1, face2):
        done = 0
        dartface = []
        for dart in self.darts:
            dartface.append(-1)

        listdarts1: list[myDart] = self.getFaceBeta(self.darts[face1.dartid], 1)
        for dart in listdarts1:
            dartface[dart.num-1] = 1
        listdarts2: list[myDart] = self.getFaceBeta(self.darts[face2.dartid], 1)
        for dart in listdarts2:
            dartface[dart.num-1] = 2
        for dart in listdarts1:
            if dart.betas[2] != self.null_dart:
                 cur = dart.betas[2]
                 if dartface[dart.num-1] == 1 and dartface[cur.num-1] == 2:
                    print (" F1: "+str(dart.num) + " "+ str(self.darts[dart.num-1].num) + "   F2: "+str(cur.num) + " "+ str(self.darts[cur.num-1].num))
                    pred = dart.betas[0]
                    next = cur.betas[1]
                    pred.betas[1] = next
                    next.betas[0] = pred
                    pred = cur.betas[0]
                    next = dart.betas[1]
                    pred.betas[1] = next
                    next.betas[0] = pred
                    self.deleteDart(dart)
                    self.deleteDart(cur)
                    face2.dartid = cur.num
                    done += 1

    def mergeTwoFacesIntoOne(self, face1, face2):
        self.mergeTwoFacesInOne(face1,face2)
        face2.dartid = -1

    def createDual(self):
        dualmap = nMap()
        idface = []
        cxface = []
        cyface = []
        mkface = []
        dartface = []

        for dart in self.darts:
            dartface.append(-1)

        nbf = 0
        for face in self.faces:
            idface.append(nbf)
            listdarts: list[myDart] = self.getFaceBeta(self.darts[face.dartid], 1)
            xm, ym = self.getCoordListdartsCenter(listdarts)
            cxface.extend([xm])
            cyface.extend([ym])
            for fhole in face.gap:
                listdarts.extend (self.getFaceBeta(self.darts[fhole.dartid], 1))
            for dart in listdarts:
                nd = dart.num - 1
                dartface[nd] = nbf
                #cur = dart
                #print("Face:" + str(nbf) + " Id:" + str(cur) + " b0:" + str(cur.betas[0]) + " b1:" + str(
                #    cur.betas[1]) + " b2:" + str(cur.betas[2]) + "props" + str(cur.properties) + " " + str(face.name))
            for nface in self.faces:
                mkface.append(0)
            nbf += 1

        i = 0
        for face in self.faces:

            listdarts: list[myDart] = self.getFaceBeta(self.darts[face.dartid], 1)
            #xm, ym = self.getCoordListdartsCenter(listdarts)
            xm = cxface[i]
            ym = cyface[i]
            for dart in listdarts:
                b2dart = dart.betas[2]
                if b2dart != self.null_dart:
                    nd = b2dart.num - 1
                    j = dartface[nd]
                    if j != i and j >= 0:
                        if mkface[i*nbf+j] == 0:
                            mkface[i*nbf+j] = 1

                            newdart = dualmap.createDartNMap()
                            newdart.betas[0] = dualmap.null_dart
                            newdart.betas[1] = dualmap.null_dart
                            newdart.betas[2] = dualmap.null_dart
                            newdart.properties["x_pos"] = xm
                            newdart.properties["y_pos"] = ym
                            newdart.properties["atyp"] = "DUAL" + dart.properties["atyp"]
                            mkface[j * nbf + i] = 1
                            #listndarts: list[myDart] = self.getFaceBeta(b2dart, 1)
                            #xf, yf = self.getCoordListdartsCenter(listndarts)
                            xf = cxface[j]
                            yf = cyface[j]
                            new2dart = dualmap.createDartNMap()
                            new2dart.betas[0] = dualmap.null_dart
                            new2dart.betas[1] = dualmap.null_dart
                            new2dart.betas[2] = dualmap.null_dart
                            new2dart.properties["x_pos"] = xf
                            new2dart.properties["y_pos"] = yf
                            new2dart.properties["atyp"] = "DUAL" + b2dart.properties["atyp"]
                            newdart.betas[2] = new2dart
                            new2dart.betas[2] = newdart
                            #cur = dart
                            #print("Face:"+str(i)+" Id:" + str(cur) + " b0:" + str(cur.betas[0]) + " b1:" + str(
                            #    cur.betas[1]) + " b2:" + str(cur.betas[2]) + "props" + str(cur.properties) + " " + str(face.name))
                            #cur = b2dart
                            #print("Face:"+str(j)+" Id:" + str(cur) + " b0:" + str(cur.betas[0]) + " b1:" + str(
                            #    cur.betas[1]) + " b2:" + str(cur.betas[2]) + "props" + str(cur.properties) )
                            #newdart.num = 1000 + dart.num
            i += 1

        return dualmap


    def createSimpleDual(self):
        dualmap = nMap()
        for dart in self.darts:
            listdarts: list[myDart] = self.getFaceBeta(dart, 0)
            xm, ym = self.getCoordListdartsCenter(listdarts)
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            xd = 0.1*(x-xm) + xm
            yd = 0.1*(y-ym) + ym
            xd = xm
            yd = ym

            dtmp0 = dart.betas[0]
            dtmp1 = dart.betas[1]

            #if dtmp0.betas[2] != self.null_dart and dtmp1.betas[2] != self.null_dart :

            #if dtmp0 != self.null_dart and dtmp1 != self.null_dart :
            #if dtmp0.betas[2] != self.null_dart or dtmp1.betas[2] != self.null_dart :
            if True:
                newdart = dualmap.createDartNMap()
                if dtmp0.betas[2] != self.null_dart:
                   newdart.betas[0] = dtmp0.betas[2]
                else:
                    newdart.betas[0] = dualmap.null_dart
                if dtmp1.betas[2] != self.null_dart:
                    newdart.betas[1] = dtmp1.betas[2]
                else:
                    newdart.betas[1] = dualmap.null_dart
                if  dart.betas[2] != self.null_dart:
                    newdart.betas[2] = dart.betas[2]
                else:
                    newdart.betas[2] = dualmap.null_dart
                newdart.properties["x_pos"] = xd
                newdart.properties["y_pos"] = yd
                newdart.properties["atyp"] = "DUAL"+dart.properties["atyp"]
                newdart.num = 1000+dart.num
        return dualmap


class Face:

    def __init__(self):
        # super(Face, self).__init__()
        self.gap = []
        self.dartid: int = -1
        self.ishole: int = 0
        self.name: str = "Unknown"
        self.posx: float = DUMMY
        self.posy: float = DUMMY


    @classmethod
    def withDarts(cls, listDarts:list):
        new = cls()
        new.darts = listDarts

