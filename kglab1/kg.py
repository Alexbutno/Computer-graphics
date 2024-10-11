import tkinter as tk
from tkinter import ttk, colorchooser
import colorsys


class ColorConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Converter")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        self.create_widgets()
        self.update_colors()

    def create_widgets(self):
        self.rgb_frame = ttk.LabelFrame(self.root, text="RGB")
        self.rgb_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.r_var = tk.DoubleVar(value=255)
        self.g_var = tk.DoubleVar(value=255)
        self.b_var = tk.DoubleVar(value=255)

        self.r_entry = ttk.Entry(self.rgb_frame, textvariable=self.r_var)
        self.g_entry = ttk.Entry(self.rgb_frame, textvariable=self.g_var)
        self.b_entry = ttk.Entry(self.rgb_frame, textvariable=self.b_var)

        self.r_entry.grid(row=0, column=0, sticky="ew")
        self.g_entry.grid(row=0, column=1, sticky="ew")
        self.b_entry.grid(row=0, column=2, sticky="ew")

        self.r_entry.bind("<KeyRelease>", self.update_colors)
        self.g_entry.bind("<KeyRelease>", self.update_colors)
        self.b_entry.bind("<KeyRelease>", self.update_colors)

        self.r_slider = tk.Scale(self.rgb_frame, from_=0, to=255, variable=self.r_var, command=self.update_colors)
        self.g_slider = tk.Scale(self.rgb_frame, from_=0, to=255, variable=self.g_var, command=self.update_colors)
        self.b_slider = tk.Scale(self.rgb_frame, from_=0, to=255, variable=self.b_var, command=self.update_colors)

        self.r_slider.grid(row=1, column=0, sticky="ew")
        self.g_slider.grid(row=1, column=1, sticky="ew")
        self.b_slider.grid(row=1, column=2, sticky="ew")

        self.cmyk_frame = ttk.LabelFrame(self.root, text="CMYK")
        self.cmyk_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.c_var = tk.DoubleVar(value=100)
        self.m_var = tk.DoubleVar(value=100)
        self.y_var = tk.DoubleVar(value=100)
        self.k_var = tk.DoubleVar(value=100)

        self.c_entry = ttk.Entry(self.cmyk_frame, textvariable=self.c_var)
        self.m_entry = ttk.Entry(self.cmyk_frame, textvariable=self.m_var)
        self.y_entry = ttk.Entry(self.cmyk_frame, textvariable=self.y_var)
        self.k_entry = ttk.Entry(self.cmyk_frame, textvariable=self.k_var)

        self.c_entry.grid(row=0, column=0, sticky="ew")
        self.m_entry.grid(row=0, column=1, sticky="ew")
        self.y_entry.grid(row=0, column=2, sticky="ew")
        self.k_entry.grid(row=0, column=3, sticky="ew")

        self.c_entry.bind("<KeyRelease>", self.update_rgb_from_cmyk)
        self.m_entry.bind("<KeyRelease>", self.update_rgb_from_cmyk)
        self.y_entry.bind("<KeyRelease>", self.update_rgb_from_cmyk)
        self.k_entry.bind("<KeyRelease>", self.update_rgb_from_cmyk)

        self.c_slider = tk.Scale(self.cmyk_frame, from_=0, to=100, variable=self.c_var, command=self.update_rgb_from_cmyk)
        self.m_slider = tk.Scale(self.cmyk_frame, from_=0, to=100, variable=self.m_var, command=self.update_rgb_from_cmyk)
        self.y_slider = tk.Scale(self.cmyk_frame, from_=0, to=100, variable=self.y_var, command=self.update_rgb_from_cmyk)
        self.k_slider = tk.Scale(self.cmyk_frame, from_=0, to=100, variable=self.k_var, command=self.update_rgb_from_cmyk)

        self.c_slider.grid(row=1, column=0, sticky="ew")
        self.m_slider.grid(row=1, column=1, sticky="ew")
        self.y_slider.grid(row=1, column=2, sticky="ew")
        self.k_slider.grid(row=1, column=3, sticky="ew")

        self.hsv_frame = ttk.LabelFrame(self.root, text="HSV")
        self.hsv_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.h_var = tk.DoubleVar(value=360)
        self.s_var = tk.DoubleVar(value=1)
        self.v_var = tk.DoubleVar(value=1)

        self.h_entry = ttk.Entry(self.hsv_frame, textvariable=self.h_var)
        self.s_entry = ttk.Entry(self.hsv_frame, textvariable=self.s_var)
        self.v_entry = ttk.Entry(self.hsv_frame, textvariable=self.v_var)

        self.h_entry.grid(row=0, column=0, sticky="ew")
        self.s_entry.grid(row=0, column=1, sticky="ew")
        self.v_entry.grid(row=0, column=2, sticky="ew")

        self.h_entry.bind("<KeyRelease>", self.update_rgb_from_hsv)
        self.s_entry.bind("<KeyRelease>", self.update_rgb_from_hsv)
        self.v_entry.bind("<KeyRelease>", self.update_rgb_from_hsv)

        self.h_slider = tk.Scale(self.hsv_frame, from_=0, to=360, variable=self.h_var, command=self.update_rgb_from_hsv)
        self.s_slider = tk.Scale(self.hsv_frame, from_=0, to=1, resolution=0.01, variable=self.s_var, command=self.update_rgb_from_hsv)
        self.v_slider = tk.Scale(self.hsv_frame, from_=0, to=1, resolution=0.01, variable=self.v_var, command=self.update_rgb_from_hsv)

        self.h_slider.grid(row=1, column=0, sticky="ew")
        self.s_slider.grid(row=1, column=1, sticky="ew")
        self.v_slider.grid(row=1, column=2, sticky="ew")

        self.color_display = tk.Canvas(self.root, width=100, height=100, bg='white')
        self.color_display.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

        self.color_picker_button = ttk.Button(self.root, text="Choose Color", command=self.pick_color)
        self.color_picker_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose color")[0]
        if color_code:
            r, g, b = map(int, color_code)
            self.r_var.set(r)
            self.g_var.set(g)
            self.b_var.set(b)
            self.update_colors()

    def update_colors(self, *args):
        r = self.r_var.get()
        g = self.g_var.get()
        b = self.b_var.get()

        c = 1 - (r / 255)
        m = 1 - (g / 255)
        y = 1 - (b / 255)
        k = min(c, m, y)

        if k < 1:
            c = (c - k) / (1 - k)
            m = (m - k) / (1 - k)
            y = (y - k) / (1 - k)
        else:
            c = m = y = 0

        self.c_var.set(round(c * 100, 0))
        self.m_var.set(round(m * 100, 0))
        self.y_var.set(round(y * 100, 0))
        self.k_var.set(round(k * 100, 0))

        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        self.h_var.set(round(h * 360, 0))
        self.s_var.set(round(s, 2))
        self.v_var.set(round(v, 2))

        self.color_display.configure(bg=f'#{int(r):02x}{int(g):02x}{int(b):02x}')

    def update_rgb_from_cmyk(self, *args):
        try:
            c = float(self.c_entry.get())
            m = float(self.m_entry.get())
            y = float(self.y_entry.get())
            k = float(self.k_entry.get())

            self.c_var.set(c)
            self.m_var.set(m)
            self.y_var.set(y)
            self.k_var.set(k)

            r = 255 * (1 - c / 100) * (1 - k / 100)
            g = 255 * (1 - m / 100) * (1 - k / 100)
            b = 255 * (1 - y / 100) * (1 - k / 100)

            self.r_var.set(round(r))
            self.g_var.set(round(g))
            self.b_var.set(round(b))

            self.update_colors()
        except ValueError:
            pass

    def update_rgb_from_hsv(self, *args):
        h = self.h_var.get() / 360
        s = self.s_var.get()
        v = self.v_var.get()

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        self.r_var.set(round(r * 255))
        self.g_var.set(round(g * 255))
        self.b_var.set(round(b * 255))

        self.update_colors()


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorConverterApp(root)
    root.mainloop()