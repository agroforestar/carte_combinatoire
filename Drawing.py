import matplotlib.pyplot as plt
class Pencil:


    def drawFace(self, coord:list):
        coord.append(coord[0])  # repeat the first point to create a 'closed loop'

        xs, ys = zip(*coord)  # create lists of x and y values

        plt.figure()
        plt.plot(xs, ys)
        plt.show()  # if you need.