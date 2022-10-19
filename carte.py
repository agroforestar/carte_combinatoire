from enum import Enum
from typing import List, Union, Optional, Tuple, Set, Dict, Callable
import networkx as nx
import matplotlib.pyplot as plt

class Vertex(object):
    indexMaxUsed: int = -1

    def __init__(self, index: int = -1):
        if index == -1:
            index = Vertex.indexMaxUsed + 1
        if index > Vertex.indexMaxUsed :
            Vertex.indexMaxUsed = index
        self.id = index

class Label(Enum):
    Frontier = 0
    In = 1

class Dart(object):
    indexMaxUsed:int = -1

    def __init__(self, index: int = -1, type: Label = Label.Frontier):
        self.beta0 = None # link to the next
        self.beta1 = None # link to the dual
        self.label:Label = type
        self.sourceVertex : Vertex = None
        self.destVertex : Vertex =None
        if index == -1:
            index = Dart.indexMaxUsed + 1
        if index > Dart.indexMaxUsed :
            Dart.indexMaxUsed = index
        self.id = index

    def __repr__(self):
        return str(self.id)+"->"+str(self.beta0.id)+"|"+str(self.beta1.id)

class Carte:
    root: Optional[Dart]

    def __init__(self):
        self.root = None

    def addFace(self, numberOfEdge:int = 3, adjacentDarts: Dart=None):
        if numberOfEdge < 3 :
            raise Exception("Need at least 3 adges to create a new face")
        if adjacentDarts is None:
            adjacentDarts = []
        else:
            adjacentDarts = [adjacentDarts]
        nbEdgesToCreate = numberOfEdge - len(adjacentDarts)
        newDarts = [Dart() for _ in range(2*nbEdgesToCreate)]

        if self.root is None:
            entryDart = newDarts[0]
            exitDart = newDarts[-1]
            self.root = newDarts[1] #Why ?
        elif len(adjacentDarts) > 0:
            entryDart = self.getFace(adjacentDarts[0])[-1]
            exitDart = adjacentDarts[-1].beta0
        else:
            raise Exception("Either you are creating a new graph, either you define at least one edge to paste the "
                            "new face to. ")
        for i in range(len(newDarts)//2):
            newDarts[2 * i].beta1 = newDarts[2 * i + 1]
            newDarts[2 * i + 1 ].beta1 = newDarts[2 * i]
            if i == 0:
                newDarts[1].beta0 = exitDart
                newDarts[0].beta0 = newDarts[2] if len(newDarts) > 2 else adjacentDarts[0]
            elif i == (len(newDarts) // 2 -1 ):
                newDarts[2 * i].beta0 = entryDart if len(adjacentDarts) == 0 else adjacentDarts[0]
                newDarts[2 * i +1].beta0 = newDarts[2*i-1]
            else:
                newDarts[ 2 * i].beta0 = newDarts[2* (i+1)]
                newDarts[2 * i + 1].beta0 = newDarts[2 * i - 1]

        if len(adjacentDarts) > 0:
            adjacentDarts[-1].beta0 = newDarts[0]
            entryDart.beta0 = newDarts[-1]
        return newDarts

    def getAllBrins(self) -> List[Dart]:
        seenBrins: List[Dart] = []
        unseenBrins: Set[Dart] = set()
        unseenBrins.add(self.root)

        while len(unseenBrins) > 0:
            current = unseenBrins.pop()
            seenBrins.append(current)
            if current.beta1 not in seenBrins:
                unseenBrins.add(current.beta1)
            if current.beta0 not in seenBrins:
                unseenBrins.add(current.beta0)
        return seenBrins

    def getFace(self, start:Dart) -> List[Dart]:
        current = start.beta0
        listDart = [start]
        while current not in listDart:
            listDart.append(current)
            current = current.beta0
        return listDart

    def getAllFaces(self) -> List[List[Dart]]:
        faces: List[List[Dart]] = []
        unseenBrins = self.getAllBrins()
        while len(unseenBrins) > 0:
            current = unseenBrins.pop()
            face = self.getFace(current)
            for brin in face:
                if brin in unseenBrins:
                    unseenBrins.remove(brin)
            if len(face) > 1:
                faces.append(face)
        return faces

    def exteriorFace(self) -> List[Dart]: # a recoder car méthode non adaptée à ma situation
        faces = sorted(self.getAllFaces(), key = lambda l: len(l))
        return faces[-1]
