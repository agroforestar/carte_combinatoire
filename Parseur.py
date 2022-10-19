from Plant import Plant
from Tree import Tree

dictionnaryForm = {
    "circle": "Tree",
    "rectangle": "Crop"
}
dictionnaryColor = {
    "seagreen": "IUGRE", # code EPPO pour le noyer
    "yellow": "TRZAX" #code EPPO pour le blé tendre
}

def read(name):
    fichier = open(name, "r")
    plants = list()
    for line in fichier:
        element = line.strip("\n").split(" ")
        if(element[-1] != str(0)):
            if(dictionnaryForm[element[0]] == "Crop"):
                plants.append(Plant(dictionnaryColor[element[1]], element[2], element[3]))
            else:
                plants.append(Tree(dictionnaryColor[element[1]], element[2], element[3]))
    return plants