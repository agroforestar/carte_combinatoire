#desc: Dart class
#ref: Combinatorial Maps: Efficient Data Structures for Computer Graphics and Image Processing, p158, data structure Dart (Listing 5.1)
#date: 03/02/2023
#author: L.L.

class Dart:


    def __init__(self, numberDim, nbMark):
        self.betas = []
        self.marks = []
        for i in range(0, numberDim):
            self.betas.append(None)
        for i in range(0, nbMark):
            self.marks.append(None)

    #
    # def __repr__(self):
    #     return str("beta 0 " + str(self.betas[0]) + "beta 1" + str(self.betas[1])  )


class myDart(Dart):


    def __init__(self, numberDim, nbMark, id : int, x:float=0, y:float=0):
        super(myDart, self).__init__(numberDim, nbMark)
        self.properties = dict()
        # for i in range(0, numberDim):
        #     self.betas.append(None)
        # for i in range(0, nbMark):
        #     self.marks.append(None)
        self.num = id
        self.properties["x_pos"] = x
        self.properties["y_pos"] = y
        self.properties["type"] = "Tree" #mettre jargon pour désigner les différents éléments

    def __repr__(self):
            return str( "id "+ str(self.num)+" / ")


