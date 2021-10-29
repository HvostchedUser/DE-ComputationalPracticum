from model import Grapher
from practicum_window import PracticumWindow

if __name__ == '__main__':
    grapher=Grapher("3*y**(2/3)", "(x+c)**3", "y0**(1/3)-x0")

    window = PracticumWindow(grapher)

    window.mainloop()
