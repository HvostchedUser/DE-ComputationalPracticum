from model import Grapher
from practicum_window import PracticumWindow

if __name__ == '__main__':
    grapher=Grapher("3*y**(2/3)", "(x-1)**3")

    window = PracticumWindow(grapher)

    window.mainloop()
