import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from color_manipulations import ColorManipulations
from color_scheme import ColorScheme
from custom_widgets import LabelledCheckbutton, LabelledInputField, LabelledButton, LabelStyled
from model import Grapher


class PracticumWindow(tk.Tk):
    def __init__(self,grapher:Grapher):
        super(PracticumWindow, self).__init__()
        self.grapher=grapher
        self.fig = Figure(figsize=(10, 8), dpi=100,
                     facecolor=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color_2))

        self.config(bg=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.wm_title("DE Assignment")

        left_side = tk.Frame(master=self, width=00, height=0,
                             background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        left_side.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        right_side = tk.Frame(master=self, width=900, height=1000,
                              background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color_2))
        right_side.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

        # graph_label=ttk.Label(right_side, text="Error graph:", background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        # graph_label.pack(anchor='w')
        self.eq_t = LabelStyled(master=left_side,text="Equation: 3 ∙ y^(⅔)",
                                 background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.eq_t.pack(anchor='w')


        self.eq_in = LabelStyled(master=left_side,text="Equation parameters:",
                                 background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.eq_in.pack(anchor='w')

        self.x0l = LabelledInputField("x₀ =", master=left_side,
                                   background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.x0l.inputfield.insert("end","2")
        self.x0l.pack(anchor='w')
        self.y0l = LabelledInputField("y₀ =", master=left_side,
                                   background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.y0l.inputfield.insert("end","1")
        self.y0l.pack(anchor='w')
        self.xl = LabelledInputField("X =", master=left_side,
                                   background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.xl.inputfield.insert("end","7")
        self.xl.pack(anchor='w')
        self.nl = LabelledInputField("N =", master=left_side,
                                   background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.nl.inputfield.insert("end","10")
        self.nl.pack(anchor='w')


        gtp = LabelStyled(master=left_side,text="Error range parameters:",
                                 background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        gtp.pack(anchor='w')


        self.n0g = LabelledInputField("n₀ =", master=left_side,
                                   background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.n0g.inputfield.insert("end","2")
        self.n0g.pack(anchor='w')
        self.ng = LabelledInputField("N =", master=left_side,
                                   background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.ng.inputfield.insert("end","20")
        self.ng.pack(anchor='w')


        vmp = LabelStyled(master=left_side,text="Plot:",
                                 background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        vmp.pack(anchor='w')

        self.rk_button = LabelledCheckbutton("Runge-Kutta method", master=left_side,
                                        background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.rk_button.pack(anchor="w")
        self.eu_button = LabelledCheckbutton("Euler method", master=left_side,
                                        background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.eu_button.pack(anchor="w")
        self.ie_button = LabelledCheckbutton("Improved Euler method", master=left_side,
                                        background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        self.ie_button.pack(anchor="w")


        lb = LabelledButton("Update the equation", master=left_side,
                            background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color), command=self.replot_canvas)
        lb.pack(anchor='w', side="bottom")

        self.err_range_button = LabelledCheckbutton("Show error in range", master=left_side,
                                             background=ColorManipulations.rgb_to_hex_color(
                                                 ColorScheme.background_color))
        self.err_range_button.checkbutton.state_bool=False
        self.err_range_button.pack(anchor="w", side="bottom")
        self.err_button = LabelledCheckbutton("Show errors of numerical methods", master=left_side,
                                             background=ColorManipulations.rgb_to_hex_color(
                                                 ColorScheme.background_color))
        self.err_button.checkbutton.state_bool=False
        self.err_button.pack(anchor="w", side="bottom")
        self.sol_button = LabelledCheckbutton("Show solutions", master=left_side,
                                             background=ColorManipulations.rgb_to_hex_color(
                                                 ColorScheme.background_color))
        self.sol_button.pack(anchor="w", side="bottom")

        ctrls_t = LabelStyled(master=left_side,text="Controls:",
                                 background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
        ctrls_t.pack(anchor='w', side="bottom")


        self.canvas = FigureCanvasTkAgg(self.fig, master=right_side)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, right_side)
        toolbar.config(background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color_2))
        for child in toolbar.winfo_children():
            child.config(background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color_2))
        toolbar.update()
        toolbar.pack(padx=(70, 70), pady=(0, 10))
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.replot_canvas()

        def on_key_press(event):
            key_press_handler(event, self.canvas, toolbar)

        self.canvas.mpl_connect("key_press_event", on_key_press)


    def perform_plots(self):
        t = np.arange(0, 3, .01)
        self.fig.clear()
        ax = self.fig.add_subplot(111)

    def replot_canvas(self):
        self.fig.clf()
        plot_amount=0
        if self.sol_button.checkbutton.state_bool:
            plot_amount+=1
        if self.err_button.checkbutton.state_bool:
            plot_amount+=1
        if self.err_range_button.checkbutton.state_bool:
            plot_amount+=1

        if plot_amount==0:
            self.canvas.draw()
            return
        plot_cur=0

        axes=self.fig.subplots(nrows=1, ncols=plot_amount)
        if plot_amount == 1:
            axes=[axes]
        self.fig.subplots_adjust(left=0.08, bottom=0.05, right=0.95, top=0.95, wspace=0.23, hspace=0.23)
        try:
            if self.sol_button.checkbutton.state_bool:
                ax = axes[plot_cur]
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                plot_cur+=1
                ax.title.set_text("Solutions")
                self.grapher.plot_solution(ax, "Exact solution",
                                           float(self.x0l.inputfield.get("1.0",tk.END)),
                                           float(self.y0l.inputfield.get("1.0",tk.END)),
                                           float(self.xl.inputfield.get("1.0",tk.END)),
                                           float(self.nl.inputfield.get("1.0",tk.END)))
                if self.eu_button.checkbutton.state_bool:
                    self.grapher.plot_solution(ax, "Euler method",
                                              float(self.x0l.inputfield.get("1.0", tk.END)),
                                              float(self.y0l.inputfield.get("1.0", tk.END)),
                                              float(self.xl.inputfield.get("1.0", tk.END)),
                                              int(self.nl.inputfield.get("1.0", tk.END)))
                if self.ie_button.checkbutton.state_bool:
                    self.grapher.plot_solution(ax, "Improved Euler method",
                                              float(self.x0l.inputfield.get("1.0", tk.END)),
                                              float(self.y0l.inputfield.get("1.0", tk.END)),
                                              float(self.xl.inputfield.get("1.0", tk.END)),
                                              int(self.nl.inputfield.get("1.0", tk.END)))
                if self.rk_button.checkbutton.state_bool:
                    self.grapher.plot_solution(ax, "Runge-Kutta method",
                                              float(self.x0l.inputfield.get("1.0", tk.END)),
                                              float(self.y0l.inputfield.get("1.0", tk.END)),
                                              float(self.xl.inputfield.get("1.0", tk.END)),
                                              int(self.nl.inputfield.get("1.0", tk.END)))
                ax.legend()
                ax.grid()
            if self.err_button.checkbutton.state_bool:
                ax = axes[plot_cur]
                ax.set_xlabel("x")
                ax.set_ylabel("e")
                plot_cur+=1
                ax.title.set_text("Errors")
                if self.eu_button.checkbutton.state_bool:
                    self.grapher.plot_error(ax, "Euler method",
                                              float(self.x0l.inputfield.get("1.0", tk.END)),
                                              float(self.y0l.inputfield.get("1.0", tk.END)),
                                              float(self.xl.inputfield.get("1.0", tk.END)),
                                              int(self.nl.inputfield.get("1.0", tk.END)))
                if self.ie_button.checkbutton.state_bool:
                    self.grapher.plot_error(ax, "Improved Euler method",
                                              float(self.x0l.inputfield.get("1.0", tk.END)),
                                              float(self.y0l.inputfield.get("1.0", tk.END)),
                                              float(self.xl.inputfield.get("1.0", tk.END)),
                                              int(self.nl.inputfield.get("1.0", tk.END)))
                if self.rk_button.checkbutton.state_bool:
                    self.grapher.plot_error(ax, "Runge-Kutta method",
                                              float(self.x0l.inputfield.get("1.0", tk.END)),
                                              float(self.y0l.inputfield.get("1.0", tk.END)),
                                              float(self.xl.inputfield.get("1.0", tk.END)),
                                              int(self.nl.inputfield.get("1.0", tk.END)))
                ax.legend()
                ax.grid()
            if self.err_range_button.checkbutton.state_bool:
                ax = axes[plot_cur]
                ax.set_xlabel("n")
                ax.set_ylabel("E")
                plot_cur += 1
                ax.title.set_text("Errors in range")
                if self.eu_button.checkbutton.state_bool:
                    self.grapher.plot_error_ranged(ax, "Euler method",
                                            float(self.x0l.inputfield.get("1.0", tk.END)),
                                            float(self.y0l.inputfield.get("1.0", tk.END)),
                                            float(self.xl.inputfield.get("1.0", tk.END)),
                                            int(self.nl.inputfield.get("1.0", tk.END)),
                                            int(self.n0g.inputfield.get("1.0", tk.END)),
                                            int(self.ng.inputfield.get("1.0", tk.END)))
                if self.ie_button.checkbutton.state_bool:
                    self.grapher.plot_error_ranged(ax, "Improved Euler method",
                                            float(self.x0l.inputfield.get("1.0", tk.END)),
                                            float(self.y0l.inputfield.get("1.0", tk.END)),
                                            float(self.xl.inputfield.get("1.0", tk.END)),
                                            int(self.nl.inputfield.get("1.0", tk.END)),
                                            int(self.n0g.inputfield.get("1.0", tk.END)),
                                            int(self.ng.inputfield.get("1.0", tk.END)))
                if self.rk_button.checkbutton.state_bool:
                    self.grapher.plot_error_ranged(ax, "Runge-Kutta method",
                                            float(self.x0l.inputfield.get("1.0", tk.END)),
                                            float(self.y0l.inputfield.get("1.0", tk.END)),
                                            float(self.xl.inputfield.get("1.0", tk.END)),
                                            int(self.nl.inputfield.get("1.0", tk.END)),
                                            int(self.n0g.inputfield.get("1.0", tk.END)),
                                            int(self.ng.inputfield.get("1.0", tk.END)))

                ax.legend()
                ax.grid()
        except Exception as e: print(e)

        self.canvas.draw()

