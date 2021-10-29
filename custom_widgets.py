import tkinter as tk
from tkinter import ttk

from color_manipulations import ColorManipulations
from color_manipulations import ColorManipulations
from color_scheme import ColorScheme

class LabelledCheckbutton(tk.Frame):
    def __init__(self, text="...", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = ttk.Label(self, text=text, background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color),font='Cantarell 12')
        self.checkbutton = CheckbuttonAnimated(self)
    def pack(self, *args, **kwargs):
        self.label.pack(side="right",padx=(10, 30),pady=(10, 10))
        self.checkbutton.pack(side="left",padx=(30, 10),pady=(10, 10))
        super().pack(*args, **kwargs)
        return self

class LabelledButton(tk.Frame):
    def __init__(self, text="...", command=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = ttk.Label(self, text=text, background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color),font='Cantarell 12')
        self.button = ButtonAnimated(self, command=command)

    def pack(self, *args, **kwargs):
        self.label.pack(side="right", padx=(10, 30), pady=(10, 10))
        self.button.pack(side="left", padx=(30, 10), pady=(10, 10))
        super().pack(*args, **kwargs)
        return self

class LabelledInputField(tk.Frame):
    def __init__(self, text="...", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = ttk.Label(self, text=text, background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color),font='Cantarell 12')
        self.inputfield = tk.Text(self, height=1, width=4,font='Cantarell 12')
        #self.button = ButtonAnimated(self,background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
    def pack(self, *args, **kwargs):
        self.label.pack(side="left", anchor="w",padx=(30, 0),pady=(10, 10))
        self.inputfield.pack(side="right",padx=(5, 30),pady=(10, 10))
        #self.button.pack(side="right", anchor="e",padx=(10, 10),pady=(10, 0))
        super().pack(*args, **kwargs)
        return self
class LabelStyled(tk.Frame):
    def __init__(self, text="...", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = ttk.Label(self, text=text, background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color),font='Cantarell 12 bold')
        #self.button = ButtonAnimated(self,background=ColorManipulations.rgb_to_hex_color(ColorScheme.background_color))
    def pack(self, *args, **kwargs):
        self.label.pack(side="top", anchor="w",padx=(30, 30),pady=(20, 10))
        #self.button.pack(side="right", anchor="e",padx=(10, 10),pady=(10, 0))
        super().pack(*args, **kwargs)
        return self


class CheckbuttonAnimated(ttk.Checkbutton):
    def rgb_to_hex_color(self, rgb):
        rgb_int=(int(rgb[0]),int(rgb[1]),int(rgb[2]))
        return ("#%02x%02x%02x" % rgb_int)


    def anim_scale(self, k):
        return int(k*self.anim_state)

    def get_dynamic_image(self):
        on=ColorScheme.off_color
        off=ColorScheme.on_color
        switch=ColorManipulations.color_shift(on,off,self.anim_state)
        bg=ColorManipulations.shade(ColorScheme.background_color) #self.color_shift(off,on)
        shade=ColorManipulations.light(switch)
        img=tk.PhotoImage(width=48, height=24)
        img.put(self.rgb_to_hex_color(ColorScheme.background_color), to=(0, 0, 48,24))
        img.put(self.rgb_to_hex_color(switch), to=(self.anim_scale(24), 0, 25+self.anim_scale(24),24))
        for i in range(0, 24):
            img.put(self.rgb_to_hex_color(ColorManipulations.color_shift(shade,bg,i/24)),to=(i+self.anim_scale(24)+25, 0, 48,24))
            img.put(self.rgb_to_hex_color(ColorManipulations.color_shift(shade,bg,i/24)),to=(0, 0, max(0,self.anim_scale(24)-i),24))
        return img

    def animate(self):
        if self.state_bool:
            self.anim_goal=1
        else:
            self.anim_goal=0
        img=self.get_dynamic_image()
        self.image=img
        self.selectimage=img
        self.configure(image=img,selectimage=img)
        self.anim_state+=(self.anim_goal-self.anim_state)/5
        if abs(self.anim_state-self.anim_goal)>0.01:
            self.after(33, self.animate)

    def animated_command(self):
        self.state_bool=not self.state_bool
        if self.command_on_click is not None:
            self.command_on_click()
        self.animate()

    def __init__(self, master=None, cnf={}, command=None, **kw):
        self.command_on_click = command
        self.anim_state=0
        self.anim_goal=0
        self.state_bool=True
        tk.Checkbutton.__init__(self, indicatoron=False,command=self.animated_command, master=master, cnf=cnf,
                                image=self.get_dynamic_image(), highlightthickness = 0,selectimage=self.get_dynamic_image(),bd=0, **kw)
        self.animate()


class ButtonAnimated(ttk.Button):
    def rgb_to_hex_color(self, rgb):
        rgb_int=(int(rgb[0]),int(rgb[1]),int(rgb[2]))
        return ("#%02x%02x%02x" % rgb_int)


    def anim_scale(self, k, state=None):
        if state is None:
            return int(k*self.anim_state)
        else:
            return int(k * state)

    def get_dynamic_image(self):
        img=tk.PhotoImage(width=48, height=24)
        if self.state_bool:
            on=ColorScheme.dark_color
            off=ColorScheme.on_color
            switch=ColorManipulations.color_shift(on,off,self.anim_state)
            bg=ColorManipulations.light(ColorScheme.background_color) #self.color_shift(off,on)
            shade=ColorManipulations.light(switch)
            img.put(self.rgb_to_hex_color(ColorScheme.background_color), to=(0, 0, 48,24))
            img.put(self.rgb_to_hex_color(switch), to=(self.anim_scale(24*3), 0, 49+self.anim_scale(24*3),24))
            for i in range(0, 24):
                img.put(self.rgb_to_hex_color(ColorManipulations.color_shift(shade,bg,i/24)),to=(i+self.anim_scale(24*3)+25, 0, 48,24))
                img.put(self.rgb_to_hex_color(ColorManipulations.color_shift(shade,bg,i/24)),to=(0, 0, max(0,self.anim_scale(24*3)-i),24))
        else:
            on=ColorScheme.dark_color
            off=ColorScheme.off_color
            switch=ColorManipulations.color_shift(on,off,self.anim_state)
            bg=ColorManipulations.shade(ColorScheme.background_color) #self.color_shift(off,on)
            shade=ColorManipulations.light(switch)
            img.put(self.rgb_to_hex_color(ColorScheme.background_color), to=(0, 0, 48,24))
            img.put(self.rgb_to_hex_color(switch), to=(max(0,24-self.anim_scale(24)-24), 0, 24-self.anim_scale(24),24))
            for i in range(0, 24):
                img.put(self.rgb_to_hex_color(ColorManipulations.color_shift(shade,bg,i/24)),to=(i+self.anim_scale(24*3)+24, 0, 48,24))
                # img.put(self.rgb_to_hex_color(ColorManipulations.color_shift(shade,bg,i/24)),to=(0, 0, max(0,self.anim_scale(24*3)-i),24))
        return img

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


    def animated_command(self):
        self.state_bool=not self.state_bool
        if self.command_on_click is not None:
            self.command_on_click()
        self.animate()

    def __init__(self, master=None, cnf={}, command=None, **kw):
        self.command_on_click = command
        self.anim_state=0
        self.anim_goal=0
        self.state_bool=True
        tk.Checkbutton.__init__(self, indicatoron=False,command=self.animated_command, master=master, cnf=cnf,
                                image=self.get_dynamic_image(), highlightthickness = 0,selectimage=self.get_dynamic_image(),bd=0, **kw)
        self.animate()

