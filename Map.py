#desc: Map class
#ref: Combinatorial Maps: Efficient Data Structures for Computer Graphics and Image Processing, p158, data structure Dart (Listing 5.1)
#date: 03/02/2023
#author: L.L.
#TODO : fonction 1 brin par 2 autres brins pondéré par un paramètre (0 et t) qui correspondra plus tard au coord de l'intersection
#TODO : faire ex avec 2 carré : a. on les sibdivisent par 2 puis on les merge b. idem mais avec des trous dans les carrés
from multipledispatch import dispatch  # importing the module
from Dart import *
import uuid
NB_MARKS = 8 #taille allouee du tableau au dart
N_DIM = 2  #nombre de dimension de la carte

#ref: Listing 5.2
class nMap:
    # ref: algorithme 22 (Daminad & Lienhardt 2014)
    # desc: constructor + initialisation
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

    #desc: return an index if available (else -1)
    # ref: algorithme 23 (Daminand & Lienhardt 2014)
    def reserveMarkMap(self):
        if len(self.freeMarks) == 0:
            return -1
        i = self.freeMarks.pop()
        return i

    # ref: algorithme 24 (Daminad & Lienhardt 2014)
    #desc: make given index available
    def freeMarkMap(self, i:int):
        self.freeMarks.append(i)

    # ref: algorithme 25 (Daminad & Lienhardt 2014)
    #desc: retrun boolean value of index i in on dart d
    def isMarkedMap(self, d:Dart, i:int):
        return d.marks[i]


    # ref: algorithme 26 (Daminad & Lienhardt 2014)
    # desc: set value True of index i in on dart d
    def markMap(self, d:Dart, i:int):
        d.marks[i] = True


    # ref: algorithme 27 (Daminad & Lienhardt 2014)
    # desc: set value False of index i in on dart d
    def unmarkMap(self, d:Dart, i:int):
        d.marks[i] = False


    # ref: algorithme 28 (iaminad & Lienhardt 2014)
    # desc: Sélectionne la permutation en fonction du raang involution, (Si sur beta1 -> beta0, beta0->beta1, beta2->beta2)
    #rem : pas clair sur le paramètre i (varie entre 0 et N_DIM)
    def inv(self, i:int):
        if i == 0:
            return 1
        elif i == 1:
            return 0
        return i

    # ref: algorithme 29(Daminad & Lienhardt 2014)
    # desc: parcours d'orbite généralisé
    # Input:
    #       self: current map;
    #       d ∈ self.Darts: the starting dart;
    #       (i1, ..., ik): a valid sequence of permutation (coding by integers between 0 and N_DIM).
    # Output : Run through all  the darts of 〈βi1, ..., βik 〉(d).
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

    # ref: algorithme 30 (Daminad & Lienhardt 2014)
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

        # ref: algorithme 30 (Damiand & Lienhardt 2014)
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

    # ref: algorithme 35(Daminad & Lienhardt 2014)
    # desc: create a dart in current map without connexion with other darts
    # Input:
    #       self: current map
    # Output : new dart
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


    def createFace(self, nbSegment :int, properties:list, type: str = "Crop"):
        listdarts = []
        for i in range(0, nbSegment):
            listdarts.append(self.createDartNMap(properties[i]))
        face = Face()
        # face.darts = listdarts
        # self.darts.append(listdarts)
        self.faces.append(face)
        self.bfaces.append(listdarts[0].num)
        face.dartid = listdarts[0].num
        self.buildPolygonBeta1(listdarts)
        return face

    def fillHoleFace(self, hole):
        # listDarts = []
        # newGap = Face()
        # for i in range(0, nbSegment):
        #     listDarts.append(newGap.createDartNMap(properties[i]))
        # self.gap.append(newGap)
        # self.createOnePolygon(listDarts)
        listdarts = hole.getFaceBeta(hole.darts[0], 0)
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
        newface.buildPolygonBeta1(newdarts)
        return newface

    def createFilledGapFace(self, face, nbSegment: int, properties: list, objectType: str):
        listdarts: list[myDart] = []
        for i in range(0, nbSegment):
            listdarts.append(self.createDartNMap(properties[i]))
        newgap = Face()
        #newgap.darts = listdarts
        face.gap.append(newgap)
        #self.bfaces.append(listdarts[0].num)
        newgap.dartid = listdarts[0].num
        self.buildPolygonBeta0(listdarts)

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
        self.faces.append(newface)
        self.bfaces.append(newdarts[0].num)
        newface.dartid = newdarts[0].num
        self.buildPolygonBeta1(newdarts)
        self.faces.append(newface)
        return newface

    #
    #  extract all darts without beta[2] issued from dart dstart
    #

    def getUnconnectedBeta2(self, dstart):
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


    def createOutsideFace(self, d ):
        # retrieve all darts without beta2

        listdarts = self.getUnconnectedBeta2(d)
        nb = len(listdarts)
        #connect darts
        #for i in range(0, nbSegment):
        #    listoutdarts.append(self.createDartNMap(properties[i]))

        print("/// Outside  Nb darts : " + str(nb) + " ////")

        # listDarts = hole.getFaceBeta(hole.darts[0], 0)
        newdarts = []
        for dart in listdarts:
            nd = self.createDartNMap(dart.properties)
            newdarts.append(nd)
            # nd.properties["id"] = uuid.uuid4()
            nd.betas[2] = dart
            dart.betas[2] = nd
        newface = Face()
        # newface.darts = newdarts
        self.faces.append(newface)
        self.bfaces.append(newdarts[0].num)
        self.buildPolygonBeta1(newdarts)
        return newface

    # ref: algorithme 36 (Daminad & Lienhardt 2014)
    def removeIsolatedDartNMap(self, d:Dart):
        self.darts.remove(d)

    # ref: algorithme 37 (Daminad & Lienhardt 2014)
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

    # ref: algorithme 34 (Daminad & Lienhardt 2014)
    def isFreeNMap(self, d:Dart, i:int):
        if (d.betas[i] == self.null_dart):
            return True
        else:
            return False

    # ref: algorithme 44 (Damiand & Lienhardt 2014)
    def oneSewMyMap(self, d1:Dart, d2:Dart):
        # if self.isFreeNMap(d1, 0)  :
            d1.betas[0] = d2
            d2.betas[self.inv(0)] = d1

    # Fixe le beta2 (le dart dans le sens inverse)
    # input : current le date traité
    #          opp le dart sur lequel beta2(current) doit renvoyer
    def setBeta2(self, current:Dart, opp : Dart):
        if current != self.null_dart:
            if opp != self.null_dart:
                current.betas[2] = opp
                opp.betas[2] = current
            else:
                print("The second dart is empty")
        else:
            print("The current dart is empty")


    def isBeta2(self, curent:myDart, d:myDart):
        coord_current = curent.getCoordinates()
        coord_next = curent.betas[0].getCoordinates()
        coord_d = d.getCoordinates()
        coord_pred = d.betas[1].getCoordinates()
        if coord_d == coord_next and coord_current == coord_pred:
            return True
        else:
            return False

    # Créer un polygone
    # input : list contenant tous les darts du polygone
    def buildPolygonBeta0(self, listDart):
        lasrIndex = len(listDart)-1
        for i in range(0, lasrIndex):
            self.oneSewMyMap(listDart[i+1], listDart[i])
        self.oneSewMyMap(listDart[0], listDart[lasrIndex])

    def buildPolygonBeta1(self, listDart):
        lasrIndex = len(listDart)-1
        for i in range(0, lasrIndex):
            self.oneSewMyMap(listDart[i], listDart[i+1])
        self.oneSewMyMap(listDart[lasrIndex], listDart[0])

    # Renvoie tous les darts de la face dont le dart d appartient
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



    def getCoordFromFace(self, d: Dart, beta: int):
        listdarts: list[myDart] = self.getFaceBeta(d, beta)
        coord = []
        for dart in listdarts:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        coord.append(coord[0])  # repeat the first point to create a 'closed loop'
        return coord


    # Renvoit la liste des coordonées rattachées aux darts composant la face
    def getCoordMap(self):
        coord = []
        for dart in self.darts:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        return coord

    def reverseMapOld(self, d:Dart):
        face = self.getFace(d)
        for dart in face:
            temp = dart.betas[0]
            dart.betas[0] = dart.betas[1]
            dart.betas[1] = temp

    def reverseMap(self, d: Dart):
        listdarts: list[myDart] = self.getFaceBeta(d, 1)
        for dart in listdarts:
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
            for d_prime in cm.darts:
                d_next = d.betas[0]
                d_pred = d.betas[1]
                d_prime_next = d_prime.betas[0]
                d_prime_pred = d_prime.betas[1]

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
            if d.betas[2] == self.null_dart:
                d_next = d.betas[1]
                d_pred = d.betas[0]
                x = d.properties["x_pos"]
                y = d.properties["y_pos"]
                xn = d_next.properties["x_pos"]
                yn = d_next.properties["y_pos"]
                xp = d_pred.properties["x_pos"]
                yp = d_pred.properties["y_pos"]

                listdarts: list[myDart] = self.getFaceBeta(self.darts[cm.dartid], 1)
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

                listdarts: list[myDart] = self.getFaceBeta(self.darts[face.dartid], 1)
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
            nd2 = self.subdiveDart(d.betas[2], 1-fbeta, coef)
            if nd2 != self.null_dart :
                 self.setBeta2(d,nd2)
                 self.setBeta2(d.betas[2], nd)


class Face:

    def __init__(self):
        super(Face, self).__init__()
        self.gap = []
        self.dartid = -1;

    @classmethod
    def withDarts(cls, listDarts:list):
        new = cls()
        new.darts = listDarts

