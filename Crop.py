from Plant import Plant

class Crop(Plant):
    def __init__(self, specie, Xcoord, Ycoord):
        super().__init__(specie, Xcoord, Ycoord)

    def __repr__(self):
        return repr((self.X, self.Y))