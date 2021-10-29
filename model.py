import numpy as np
from scipy.interpolate import interp1d


class ODE:
    def __init__(self, func_text):
        self.func_text = func_text

    def f(self, x, y):
        return eval(self.func_text)


class NumericSolution:
    def __init__(self, ode):
        self.ode = ode

    def get_value(self, x, y, h):
        raise NotImplementedError("Not implemented")


class RungeKuttaMethod(NumericSolution):
    def __init__(self, ode):
        super().__init__(ode)

    def get_value(self, x, y, h):
        k1 = self.ode.f(x, y)
        k2 = self.ode.f(x + h / 2, y + h * k1 / 2)
        k3 = self.ode.f(x + h / 2, y + h * k2 / 2)
        k4 = self.ode.f(x + h, y + h * k3)
        return (k1 + 2 * k2 + 2 * k3 + k4) * h / 6 + y


class ImprovedEulerMethod(NumericSolution):
    def __init__(self, ode: ODE):
        super().__init__(ode)

    def get_value(self, x, y, h):
        yn = y + h * self.ode.f(x, y)
        return (self.ode.f(x, y) + self.ode.f(x + h, yn)) * h / 2 + y


class EulerMethod(NumericSolution):
    def __init__(self, ode):
        super().__init__(ode)

    def get_value(self, x, y, h):
        return self.ode.f(x, y) * h + y


class ExactSolution:
    def __init__(self, solution_text, const_calc):
        self.solution_text = solution_text
        self.const_calc = const_calc

    def get_value(self, x, x0, y0):
        c=eval(self.const_calc)
        return eval(self.solution_text)


class Grapher:
    def __init__(self, func_text, exact_solution_text, const_calc_text):
        self.ode = ODE(func_text)
        self.solutions = dict()
        self.solutions["Exact solution"] = ExactSolution(exact_solution_text,const_calc_text)
        self.solutions["Runge-Kutta method"] = RungeKuttaMethod(self.ode)
        self.solutions["Euler method"] = EulerMethod(self.ode)
        self.solutions["Improved Euler method"] = ImprovedEulerMethod(self.ode)

    def scatter_points_solution(self, sol_name, x0, y0, X, N):
        h = (X - x0) / N
        tx = x0
        ty = y0
        x_list = [x0]
        y_list = [y0]
        for iteration in range(int(N)):

            x_list.append(tx + h)
            if sol_name == "Exact solution":
                ty = self.solutions[sol_name].get_value(tx+h, x0,y0)
                y_list.append(ty)
            else:
                ty = self.solutions[sol_name].get_value(tx, ty, h)
                # ty += val
                y_list.append(ty)
            tx += h
        return (x_list, y_list)

    def error_points(self, sol_name, x0, y0, X, N):
        (x_list_p, y_list_p) = self.scatter_points_solution("Exact solution", x0, y0, X, N)
        (x_list_m, y_list_m) = self.scatter_points_solution(sol_name, x0, y0, X, N)
        x_list = []
        y_list = []
        for i in range(len(x_list_p)):
            x_list.append(x_list_m[i])
            y_list.append(abs(y_list_m[i] - y_list_p[i]))
        return (x_list, y_list)

    def plot_solution(self, ax, sol_name, x0, y0, X, N):
        (x_list, y_list) = self.scatter_points_solution(sol_name, x0, y0, X, N)
        ax.plot(x_list, y_list, "-o", label=sol_name)

    def plot_error(self, ax, sol_name, x0, y0, X, N):
        (x_list, y_list) = self.error_points(sol_name, x0, y0, X, N)
        ax.plot(x_list, y_list, "-o", label=sol_name)

    def plot_error_ranged(self, ax, sol_name, x0, y0, X, N, N0g, ng):
        x_list = []
        y_list = []
        for i in range(N0g, ng):
            (x_p, y_p) = self.error_points(sol_name, x0, y0, X, i)
            x_list.append(i)
            y_list.append(max(y_p))
        ax.plot(x_list, y_list, "-o", label=sol_name)
