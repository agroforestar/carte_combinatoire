#desc: Map class
#ref: Combinatorial Maps: Efficient Data Structures for Computer Graphics and Image Processing, p158, data structure Dart (Listing 5.1)
#date: 03/02/2023
#author: L.L.
from multipledispatch import dispatch  # importing the module
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
    @dispatch()
    def createDartNMap(self):
        d = myDart(N_DIM, NB_MARKS)
        self.darts.append(d)
        for i in range(0, N_DIM+1):
            d.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            d.marks[i] = False
        return d

    @dispatch(int, float, float)
    def createDartNMap(self, id:int, x:float, y:float):
        d = myDart(N_DIM, NB_MARKS, id, x, y)
        self.darts.append(d)
        for i in range(0, N_DIM+1):
            d.betas[i] = self.null_dart
        for i in range(0, NB_MARKS):
            d.marks[i] = False
        return d

    @dispatch(dict)
    def createDartNMap(self, properties:dict):
        d = myDart(N_DIM, NB_MARKS, properties)
        self.darts.append(d)
        for i in range(0, N_DIM + 1):
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

    # ref: algorithme 44 (Daminad & Lienhardt 2014)
    def oneSewMyMap(self, d1:Dart, d2:Dart):
        # if self.isFreeNMap(d1, 0)  :
            d1.betas[0] = d2
            d2.betas[self.inv(0)] = d1

    # Fixe le beta2 (le dart dans le sens inverse)
    # input : current le date traité
    #          inv le dart sur lequel beta2(current) doit renvoyer
    def setBeta2(self, current:Dart, inv : Dart):
        if len(self.getFace(current)) > 0:
            if len(self.getFace(inv)) > 0:
                current.betas[2] = inv
                inv.betas[2] = current
            else:
                print("The second dart is not in face")
        else:
            print("The current dart is not in face")


    def isBeta2(self, curent:Dart, d:Dart):
        coord_current = curent.getCoordinates()
        coord_next = curent.betas[0].getCoordinates()
        coord_d = d.getCoordinates()
        coord_pred = d.betas[1].getCoordinates()
        if coord_d == coord_next and coord_current == coord_pred:
            return True
        else:
            return False

    # Créer un polygone
    # input : list contenant tous les darts du polybone
    def createOnePolygon(self, listDart):
        lasrIndex = len(listDart)-1
        for i in range(0, lasrIndex):
            self.oneSewMyMap(listDart[i], listDart[i+1])
        self.oneSewMyMap(listDart[lasrIndex], listDart[0])

    # Renvoit tous les darts de la face dont le dart d appartient
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


    # Renvoit la liste des coordonées rattachées aux darts composant la face
    def getCoordFace(self, face:list):
        coord = []
        for dart in face:
            x = dart.properties["x_pos"]
            y = dart.properties["y_pos"]
            coord.append([x, y])
        return coord

    def reverseMap(self, d:Dart):
        face = self.getFace(d)
        for dart in face:
            temp = dart.betas[0]
            dart.betas[0] = dart.betas[1]
            dart.betas[1] = temp

    def getConnectedDart(self, cm:'nMap'):
        output = []
        fin = False
        i = 0

        while not fin:
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
                    self.reverseMap(d_prime)

                    output.append(d)
                    output.append(d_prime.betas[1])
                    fin = True
            i = i+1
        return output


    #ref: Algorithme 40 (Damiand and Liendhard 2014)
    def mergeNMaps(self, cm: 'nMap'):
        commun = self.getConnectedDart(cm)
        self.setBeta2(commun[0], commun[1])
        merge = nMap()
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

