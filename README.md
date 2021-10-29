

Differential Equations

Computational practicum
Variant 17


Solution:

Initial Value Problem.

Nonlinear ODE of the first order

Let’s rewrite it in a more convenient way

Integrate left and right sides, variables separated

Find the integrals







find the constant





Is the solution.

The solution has no points of discontinuity. 

Application description:

	The application is intended to visually show the accuracy of various numerical methods compared to the exact solution.
	The application is capable of plotting graphs of solutions of this equation using multiple different methods including the exact solution which was found above and multiple numeric methods and graphs of errors of these methods.
	The application was built on Python programming language with SOLID and OOP design principles in mind. The interface was built with Tkinter library, the matplotlib library was used to generate plots. 
	Classes Grapher, ODE, NumericSolution and its subclasses do all the plotting and work with computational methods. Class PracticumWindow takes on the user interface routines. Also, there are multiple classes extending the default Tkinter widgets and some classes built to work with color to implement a color scheme for the GUI.

UML diagrams:
practicum_window.py
 
PracticumWindow is built on the 
top of the class Tk, which implements 
a root frame for the 
Tkinter GUI application. It contains 
lots of widgets and a grapher 
class instance. 
This class does all the plotting.














model.py
	NumericSolution is a superclass for all the numeric methods implemented in the application. It’s instances contain an equation itself and a method get_value purposed to find one particluar solution based on x, y (the previous solution), and h (the step size). Class Grapher makes plots of solutions, errors, and errors in specified range. error_points and scatter_points_solution functions find sets of points used to plot solution and error graphs respectively for the plot methods.

custom_widgets.py

This file contains all the modified and new Tkinter widgets used in this application. Three of these widgets are just a combination of a couple of the existing ones, three other widgets are a modified version of their superclasses with an altered appearance. 
ButtonAnimated and CheckbuttonAnimated are animated and themed versions of a Tkinter’s default button and checkbutton respectively. LabelStyled is a widget containing a label and implementing proper theming according to the ColorScheme. Labelled buttons and input field just represent proper colored widgets with labels.




color_scheme.py and color_manipulations.py

These files contain classes built for working with colors.
ColorManipulations supports getting the lighter and darker version of a color based on the (r,g,b) tuple, color_shift provides a smooth transition between two RGB colors based on the k (0 .. 1) variable, rgb_to_hex_color provides a translator from (r,g,b) to HEX format supported by Tkinter.

Screenshot of an application:


The left panel contains all the parameters of the program. There are four blocks of settings. 
Equation parameters block contains the settings used while building the solution graph.
Error range parameters block contains settings connected with «show error in range» functionality.
Plot block contains buttons that enable or disable a specified numeric method.

Controls block allows the user to enable or disable plotting of a specified graph and update the right panel with a blue button «Update the equation»

The right panel contains graphs and a toolbar where the user can see the coordinates of a mouse pointer in a graph, move, zoom, or save the plotting results to a file.

Code examples:

model.py, RungeKuttaMethod

class RungeKuttaMethod(NumericSolution):
    def __init__(self, ode):
        super().__init__(ode)

    def get_value(self, x, y, h):
        k1 = self.ode.f(x, y)
        k2 = self.ode.f(x + h / 2, y + h * k1 / 2)
        k3 = self.ode.f(x + h / 2, y + h * k2 / 2)
        k4 = self.ode.f(x + h, y + h * k3)
        return (k1 + 2 * k2 + 2 * k3 + k4) * h / 6 + y

custom_widgets.py, ButtonAnimated

def animate(self):
    if self.state_bool:
        self.anim_goal=1
    else:
        self.anim_goal=0
    img=self.get_dynamic_image()
    self.image=img
    self.selectimage=img
    self.configure(image=img,selectimage=img)
    self.anim_state+=(self.anim_goal-self.anim_state)/4
    if abs(self.anim_state-self.anim_goal)>0.01:
        self.after(33, self.animate)
    else:
        if self.anim_goal == 1:
            self.state_bool = False
            self.after(33, self.animate)

main.py

from model import Grapher
from practicum_window import PracticumWindow

if __name__ == '__main__':
    grapher=Grapher("3*y**(2/3)", "(x-1)**3")

    window = PracticumWindow(grapher)

    window.mainloop()

Full code: 
GitHub 
