import tkinter as tk
from tkinter import ttk

class StateMachineGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("State Machine Simulation")
        self.geometry("450x300")
        self.pack_propagate(False)
        self.grid_propagate(False)

        # Header label
        header_label = tk.Label(self, text="State Machine Simulation", font=("Arial", 16))
        header_label.pack(pady=5)

        # Input frame
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10, fill="x")

        # Dropdowns for A, B, C, X
        self.comboA = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboA.set("0")
        self.comboB = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboB.set("0")
        self.comboC = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboC.set("0")
        self.comboX = ttk.Combobox(input_frame, values=["0", "1"], state="readonly", width=5)
        self.comboX.set("0")

        # Arrange dropdowns in grid
        tk.Label(input_frame, text="A:").grid(row=0, column=0, padx=5, pady=5)
        self.comboA.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(input_frame, text="B:").grid(row=0, column=2, padx=5, pady=5)
        self.comboB.grid(row=0, column=3, padx=5, pady=5)
        tk.Label(input_frame, text="C:").grid(row=0, column=4, padx=5, pady=5)
        self.comboC.grid(row=0, column=5, padx=5, pady=5)
        tk.Label(input_frame, text="X:").grid(row=0, column=6, padx=5, pady=5)
        self.comboX.grid(row=0, column=7, padx=5, pady=5)

        # Compute button
        compute_button = ttk.Button(self, text="Compute Next State & Output", command=self.compute_next_state)
        compute_button.pack(pady=10)

        # Truth table button
        truth_table_button = ttk.Button(self, text="Generate Truth Table", command=self.generate_truth_table)
        truth_table_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(self, text="Result will appear here", font=("Arial", 12), wraplength=400, justify="center")
        self.result_label.pack(pady=10)

    def compute_next_state(self):
        # Get the inputs
        A = int(self.comboA.get())
        B = int(self.comboB.get())
        C = int(self.comboC.get())
        X = int(self.comboX.get())

        # Convert to boolean for easier logic handling
        a = A == 1
        b = B == 1
        c = C == 1
        x = X == 1

        # Boolean logic for the state machine
        a_next = (a and b) or (a and c and not x) or (b and not c and x)
        b_next = (not a and b and x) or (c and not x) or (b and c)
        c_next = (a and not b and x) or (not a and not c and x) or (a and b and not x)
        y = a and b and c and x

        # Convert booleans back to integers
        A_next = 1 if a_next else 0
        B_next = 1 if b_next else 0
        C_next = 1 if c_next else 0
        Y = 1 if y else 0

        # Update the result label
        self.result_label.config(text=f"A(t+1) = {A_next}, B(t+1) = {B_next}, C(t+1) = {C_next}, Y = {Y}")

    def generate_truth_table(self):
        # Create a new window for the truth table
        table_window = tk.Toplevel(self)
        table_window.title("Truth Table")
        table_window.geometry("600x400")

        # Text widget to display the truth table
        text_widget = tk.Text(table_window, wrap="none")
        text_widget.pack(expand=True, fill="both")

        # Generate truth table
        header = "A B C X | A(t+1) B(t+1) C(t+1) Y\n" + "-" * 35 + "\n"
        rows = []
        for A in [0, 1]:
            for B in [0, 1]:
                for C in [0, 1]:
                    for X in [0, 1]:
                        # Boolean logic
                        a = A == 1
                        b = B == 1
                        c = C == 1
                        x = X == 1

                        a_next = (a and b) or (a and c and not x) or (b and not c and x)
                        b_next = (not a and b and x) or (c and not x) or (b and c)
                        c_next = (a and not b and x) or (not a and not c and x) or (a and b and not x)
                        y = a and b and c and x

                        A_next = 1 if a_next else 0
                        B_next = 1 if b_next else 0
                        C_next = 1 if c_next else 0
                        Y = 1 if y else 0

                        rows.append(f"{A} {B} {C} {X} | {A_next} {B_next} {C_next} {Y}\n")

        # Insert the truth table into the text widget
        text_widget.insert("1.0", header + "".join(rows))
        text_widget.config(state="disabled")

if __name__ == "__main__":
    app = StateMachineGUI()
    app.mainloop()
