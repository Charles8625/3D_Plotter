from mpl_toolkits.mplot3d import Axes3D
from numpy import arange
from pylab import meshgrid, imshow, contour, colorbar, show
from matplotlib import cm
import matplotlib.pyplot as plt


class Graphs:

    xy_function_string = '(x*x)-y'

    def z_func(self, x, y, xy_func):
        func = xy_func
        return eval(func)

    # Displays a contour graph of the xy-function
    def contour_graph(self, x_c, y_c):
        xy_input = self.xy_function_string
        # used for the third value in arange
        # lines_2 = float(bfs.enter())
        x_two, y_two = meshgrid(x_c, y_c)
        z = self.z_func(x_two, y_two, xy_input)
        im = imshow(z, cmap=cm.RdGy)
        contour(z, arange(-1, 1.5, 0.1), linewidths=1, cmap=cm.bone)  # Needs to be adjustable
        title = plt.gcf()
        title.canvas.set_window_title('Contour Graph')
        colorbar(im)
        show()

    # Displays a surface plot of the xy-function
    def surface_plot(self, x_s, y_s):
        xy_input = self.xy_function_string
        # smooth = input("Smooth: ") used for rstride. Want to have this value change based on input from the user
        # smooth_2 = int(smooth) used for cstride. Want to have this value change based on input from the user
        x_s2, y_s2 = meshgrid(x_s, y_s)
        z_s = self.z_func(x_s2, y_s2, xy_input)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(x_s2, y_s2, z_s, rstride=35, cstride=35, cmap=cm.bone,
                               linewidth=0, antialiased=True)
        title = plt.gcf()
        title.canvas.set_window_title('Surface Plot')
        fig.colorbar(surf, shrink=0.5, aspect=10)
        show()