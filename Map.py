#desc: Map class
#ref: Combinatorial Maps: Efficient Data Structures for Computer Graphics and Image Processing, p158, data structure Dart (Listing 5.1)
#date: 03/02/2023
#author: L.L.

from Dart import *
NB_MARKS = 8 #taille allouee du tableau au dart
N_DIM = 2  #nombre de dimension de la carte

#ref: Listing 5.2
class nMap:


    # ref: algorithme 22 (Daminad & Lienhardt 2014)
    # desc: constructor + initialisation
    def __init__(self):
        self.darts = []
        self.freeMarks = []
        self.null_dart  = Dart(N_DIM, NB_MARKS)
        for i in range(0, N_DIM+1):
            self.null_dart.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            self.freeMarks.append(i)
            self.null_dart.marks[i] = False

    #desc: return an index if available (else -1)
    # ref: algorithme 23 (Daminad & Lienhardt 2014)
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
        d.marks[i]= False


    # ref: algorithme 28 (iaminad & Lienhardt 2014)
    # desc: Sélectionne la permutation en fonction du raang involution, (Si sur beta1 -> beta0, beta0->beta1, beta2->beta2)
    #rem : pas clair sur le paramètre i (varie entre 0 et N_DIM)
    def inv(self, i:int):
        if i==0:
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
    def createDartNMap(self):
        d = myDart(N_DIM, NB_MARKS)
        self.darts.append(d)
        for i in range(0, N_DIM+1):
            d.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            d.marks[i] = False
        return d


    def createDartNMap(self, id:int, x:float, y:float):
        d = myDart(N_DIM, NB_MARKS, id, x, y)
        self.darts.append(d)
        for i in range(0, N_DIM+1):
            d.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            d.marks[i] = False
        return d

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


    def oneSewMyMap(self, d1:Dart, d2:Dart):
        # if self.isFreeNMap(d1, 0)  :
            d1.betas[0] = d2
            d2.betas[self.inv(0)] = d1


    def setBeta2(self, current:Dart, inv : Dart):
        current.betas[2] = inv
        inv.betas[2] = current

    def createOnePolygon(self, listDart):
        lasrIndex = len(listDart)-1
        for i in range(0, lasrIndex):
            self.oneSewMyMap(listDart[i], listDart[i+1])
        self.oneSewMyMap(listDart[lasrIndex], listDart[0])


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
            for d in self.darts:
                self.unmarkMap(d, ma)
            self.freeMarkMap(ma)
            return dartFace


    def getCoordFace(self, face:list):
        coord = []
        for dart in face:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        return coord