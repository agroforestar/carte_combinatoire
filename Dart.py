#desc: Dart class
#ref: Combinatorial Maps: Efficient Data Structures for Computer Graphics and Image Processing, p158, data structure Dart (Listing 5.1)
#date: 03/02/2023
#author: L.L.
import uuid
from multipledispatch import dispatch

"""Implementation of dart concept from Damiand and Liendhardt (2014) where :  
 - beta[0] : pred
 - beta[1] : next
 - beta[2] : involution
"""
class Dart:

    ## Constructor
    # @param numberDim : n dimension of the map and is the size of beta
    # @param nbMark : size of the table marks
    def __init__(self, numberDim, nbMark):
        self.betas = []
        self.marks = []
        self.num : int = -1
        self.deleted = 0
        for i in range(0, numberDim+1):
            self.betas.append(None)
        for i in range(0, nbMark):
            self.marks.append(False)

    #
    # def __repr__(self):
    #     return str("beta 0 " + str(self.betas[0]) + "beta 1" + str(self.betas[1])  )

"""Implementation of dart concept with adaptation to agroforestry
"""
class myDart(Dart):
    ## Constructor
    # @param numberDim : n dimension of the map and is the size of beta
    # @param nbMark : size of the table marks
    def __init__(self, numberDim, nbMark):
        super(myDart, self).__init__(numberDim, nbMark)
        self.properties = dict()
        self.properties["id"] = uuid.uuid4()
        self.properties["atyp"] = "UNKNOWN"

    ## Constructor with values already defined
    # @param numberDim : n dimension of the map and is the size of beta
    # @param nbMark : size of the table marks
    # @param id : Dart's id
    # @param x : x-coordinate of the dart's origin
    # @param y : y-coordinate of the dart's origin
    @classmethod
    def withValue(self, numberDim, nbMark, id : uuid.UUID, x:float=0, y:float=0):
        new = self(numberDim, nbMark)
        new.properties = dict()
        new.properties["id"] = id
        new.properties["x_pos"] = x
        new.properties["y_pos"] = y
        new.properties["atyp"] = "UNKNOWN" #mettre jargon pour désigner les différents éléments
        return new

    ## Constructor with values already defined in a dictionnary
    # @param numberDim : n dimension of the map and is the size of beta
    # @param nbMark : size of the table marks
    # @param properties : contains all propoerties of the dart
    @classmethod
    def withProperties(self, numberDim, nbMark, properties:dict):
        new = self(numberDim, nbMark)
        new.properties = properties
        return new


    def __repr__(self):
        # return str("id " + str(self.properties["id"]))
        return str( ""+ str(self.num)+" ")

    ## @return a table with xy-coordinates
    def getCoordinates(self):
        return [self.properties["x_pos"], self.properties["y_pos"]]


    ## Divide the current dart in 2. The division is made in the middle
    def selfDivision(self):
        next = self.withValue(8, 2, uuid.uuid4(), self.properties["x_pos"]/2, self.properties["y_pos"]/2 )
        print(self.betas[2].properties)
        next.marks = self.marks.copy()
        next.betas[0] = self.betas[0]
        next.betas[1] = self
        next.betas[2] = self.betas[2]
        self.betas[0] = next
        return next

