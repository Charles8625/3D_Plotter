import os
import sys


class ButtonActions:


    def x_display(self):
        x = 'x'
        self.z_funcTextEdit.insertPlainText(x)

    def y_display(self):
        y = 'y'
        self.z_funcTextEdit.insertPlainText(y)

    def star_display(self):
        star = '*'
        self.z_funcTextEdit.insertPlainText(star)

    def sin_display(self):
        sin = 'sin'
        self.z_funcTextEdit.insertPlainText(sin)

    def lpar_display(self):
        left_p = '('
        self.z_funcTextEdit.insertPlainText(left_p)

    def rpar_display(self):
        right_p = ')'
        self.z_funcTextEdit.insertPlainText(right_p)

    def clear_display(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def close_prog(self):
        sys.exit()

    def graph_pressed(self):
        from graphs import Graphs
        from numpy import arange
        g = Graphs()
        x_func = arange(-3.0, 3.0, 0.01)
        y_func = arange(-3.0, 3.0, 0.01)
        g.contour_graph(x_func, y_func)
        g.surface_plot(x_func, y_func)
        # The text from the z function display
        variable = str(self.z_funcTextEdit.toPlainText())
        # I want this value to be sent to the z_func method within the Graphs class
        return variable

    def enter(self):
        # num = self.smooth_textEdit.toPlainText()
        variable = str(self.z_funcTextEdit.toPlainText())
        return variable

# Another Test
