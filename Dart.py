#desc: Dart class
#ref: Combinatorial Maps: Efficient Data Structures for Computer Graphics and Image Processing, p158, data structure Dart (Listing 5.1)
#date: 03/02/2023
#author: L.L.

class Dart:
##beta[0] : next
##beta[1] : pred
##beta[2] : involution

    def __init__(self, numberDim, nbMark):
        self.betas = []
        self.marks = []
        for i in range(0, numberDim+1):
            self.betas.append(None)
        for i in range(0, nbMark):
            self.marks.append(False)

    #
    # def __repr__(self):
    #     return str("beta 0 " + str(self.betas[0]) + "beta 1" + str(self.betas[1])  )


class myDart(Dart):


    def __init__(self, numberDim, nbMark, id : int, x:float=0, y:float=0):
        super(myDart, self).__init__(numberDim, nbMark)
        self.properties = dict()
        self.properties["id"] = id
        self.properties["x_pos"] = x
        self.properties["y_pos"] = y
        self.properties["type"] = "Tree" #mettre jargon pour désigner les différents éléments


    def __int__(self,numberDim, nbMark, properties:dict):
        super(myDart, self).__init__(numberDim, nbMark)
        self.properties = properties
    def __repr__(self):
            return str( "id "+ str(self.properties["id"]))


    def getCoordinates(self):
        return [self.properties["x_pos"], self.properties["y_pos"]]

