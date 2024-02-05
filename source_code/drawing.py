import matplotlib.pyplot as plt


class Draw_plots():

    @staticmethod
    def point_graph(x_axis: list, y_axis: list):
        plt.scatter(x_axis, y_axis)
        plt.show()
