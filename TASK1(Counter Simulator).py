import tkinter as tk
from tkinter import ttk
from collections import deque

class CounterSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter Simulator")

        self.n = 3
        self.state = 0
        self.clock_speed = 1
        self.is_running = True
        self.clock_high = True

        self.clock_wave = deque(maxlen=50)
        self.input_wave = deque(maxlen=50)
        self.output_wave = deque(maxlen=50)

        self.x = True
        self.y = False

        self.create_ui()
        self.update_clock()

    def create_ui(self):
        # Sidebar controls
        controls_frame = tk.Frame(self.root, bg="#f0f0f0", padx=15, pady=15)
        controls_frame.pack(side=tk.LEFT, fill=tk.Y)

        # On/Off switch
        self.on_off_var = tk.BooleanVar(value=self.is_running)
        on_off_button = ttk.Checkbutton(controls_frame, text="On/Off", variable=self.on_off_var, command=self.toggle_clock)
        on_off_button.pack(pady=5)

        # Bit size selector
        ttk.Label(controls_frame, text="Bit Size:").pack(pady=5)
        self.bit_size_selector = ttk.Combobox(controls_frame, values=[2, 3, 4], state="readonly")
        self.bit_size_selector.set(self.n)
        self.bit_size_selector.bind("<<ComboboxSelected>>", self.change_bit_size)
        self.bit_size_selector.pack(pady=5)

        # Reset button
        reset_button = ttk.Button(controls_frame, text="Reset", command=self.reset_counter)
        reset_button.pack(pady=5)

        # Clock speed slider
        ttk.Label(controls_frame, text="Clock Speed:").pack(pady=5)
        self.clock_speed_var = tk.DoubleVar(value=self.clock_speed)
        clock_speed_slider = ttk.Scale(controls_frame, from_=1, to=10, variable=self.clock_speed_var, command=self.update_clock_speed)
        clock_speed_slider.pack(pady=5)
        self.clock_speed_label = ttk.Label(controls_frame, text=f"Clock Speed: {self.clock_speed} Hz")
        self.clock_speed_label.pack(pady=5)

        # Input X controls
        input_controls_frame = tk.Frame(controls_frame)
        input_controls_frame.pack(pady=10)
        ttk.Button(input_controls_frame, text="X = 0", command=lambda: self.set_input_x(False)).pack(side=tk.LEFT, padx=5)
        ttk.Button(input_controls_frame, text="X = 1", command=lambda: self.set_input_x(True)).pack(side=tk.LEFT, padx=5)

        # Main display
        display_frame = tk.Frame(self.root, padx=15, pady=15)
        display_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # State display
        self.state_label = ttk.Label(display_frame, text="State: 000", font=("Arial", 14))
        self.state_label.pack(pady=10)

        self.y_label = ttk.Label(display_frame, text="Y: 0", font=("Arial", 14))
        self.y_label.pack(pady=10)

        # Waveform display
        self.clock_canvas = tk.Canvas(display_frame, width=600, height=50, bg="white")
        self.clock_canvas.pack(pady=5)
        self.input_canvas = tk.Canvas(display_frame, width=600, height=50, bg="white")
        self.input_canvas.pack(pady=5)
        self.output_canvas = tk.Canvas(display_frame, width=600, height=50, bg="white")
        self.output_canvas.pack(pady=5)

    def toggle_clock(self):
        self.is_running = self.on_off_var.get()

    def change_bit_size(self, event):
        self.n = int(self.bit_size_selector.get())
        self.reset_counter()

    def update_clock_speed(self, value):
        self.clock_speed = int(float(value))
        self.clock_speed_label.config(text=f"Clock Speed: {self.clock_speed} Hz")

    def set_input_x(self, value):
        self.x = value

    def reset_counter(self):
        self.state = 0
        self.y = False
        self.clock_wave.clear()
        self.input_wave.clear()
        self.output_wave.clear()
        self.update_display()

    def update_display(self):
        state_bin = format(self.state, f"0{self.n}b")
        self.state_label.config(text=f"State: {state_bin}")
        self.y_label.config(text=f"Y: {int(self.y)}")

        self.draw_wave(self.clock_canvas, self.clock_wave)
        self.draw_wave(self.input_canvas, self.input_wave)
        self.draw_wave(self.output_canvas, self.output_wave)

    def update_state(self):
        self.state = (self.state + 1) % (1 << self.n)
        self.y = self.state == 0


    def update_waves(self):
        self.clock_wave.append(1 if self.clock_high else 0)
        self.input_wave.append(1 if self.x else 0)
        self.output_wave.append(1 if self.y else 0)

    def draw_wave(self, canvas, wave):
        canvas.delete("all")
        if not wave:
            return

        width = canvas.winfo_width()
        step = width / len(wave)
        high_y = 10
        low_y = 40

        for i in range(len(wave) - 1):
            x1 = i * step
            x2 = (i + 1) * step
            y1 = high_y if wave[i] else low_y
            y2 = high_y if wave[i + 1] else low_y

            canvas.create_line(x1, y1, x2, y1, fill="black", width=2)
            if y1 != y2:
                canvas.create_line(x2, y1, x2, y2, fill="black", width=2)

    def update_clock(self):
        if self.is_running:
            self.clock_high = not self.clock_high
            self.update_waves()
            if not self.clock_high:
                self.update_state()
            self.update_display()
        self.root.after(int(1000 / (self.clock_speed * 2)), self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterSimulator(root)
    root.mainloop()
