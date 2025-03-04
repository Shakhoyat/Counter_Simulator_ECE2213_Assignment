# Counter Simulator TASK1

## Overview
The **Counter Simulator** is a Python-based graphical application built using `tkinter`. It simulates a simple counter with adjustable bit size, clock speed, and input toggling, providing a visual representation of clock pulses, input states, and output signals.

## Features
- **Clock Pulse Simulation**: The counter operates with a toggling clock signal.
- **Bit Size Selection**: Users can select between 2-bit, 3-bit, and 4-bit counters.
- **State Representation**: Displays the current state in binary format.
- **Adjustable Clock Speed**: Users can modify the clock speed (1 Hz to 10 Hz).
- **Waveform Display**: Visual representation of clock, input, and output signals.
- **Reset Functionality**: Resets the counter to its initial state.
- **User Controls**:
    - Toggle ON/OFF switch
    - Set input X to 0 or 1
    - Adjust clock speed with a slider

## Installation & Usage
### Prerequisites
Ensure you have Python installed (Python 3.x recommended).

### Steps to Run
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the script using:
     ```bash
     python counter_simulator.py
     ```

## How It Works
- The counter increments based on the clock pulses.
- The number of states depends on the selected bit size (`2^n` states).
- The waveform display updates dynamically based on clock pulses, input changes, and counter state.
- The **Y output** turns `1` when the counter reaches state `0`.

## UI Controls
| Control | Description |
|---------|-------------|
| **On/Off Switch** | Starts or stops the counter simulation |
| **Bit Size Selector** | Choose between 2-bit, 3-bit, or 4-bit counters |
| **Reset Button** | Resets the counter to `000` state |
| **Clock Speed Slider** | Adjusts the clock frequency |
| **X Input Buttons** | Sets input X to `0` or `1` |

## Screenshots
*(Include screenshots of the UI if available)*


# State Machine Simulation TASK 2

## Overview
The **State Machine Simulation** is a Python-based GUI application built using `tkinter`. It allows users to simulate a simple state machine by selecting input values and computing the next state based on predefined boolean logic.

## Features
- **User Input Selection**: Users can set values for A, B, C, and X using dropdowns.
- **State Computation**: Computes the next state and output based on boolean logic.
- **Truth Table Generation**: Displays the complete truth table for all possible input combinations.
- **Graphical Interface**: A simple and interactive UI with dropdowns, buttons, and result display.

## Installation & Usage
### Prerequisites
Ensure you have Python installed (Python 3.x recommended).

### Steps to Run
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the script using:
   ```bash
   python state_machine.py
   ```

## How It Works
- Users select values for A, B, C, and X from dropdown menus.
- Clicking **Compute Next State & Output** applies boolean logic to determine the next state values (`A(t+1)`, `B(t+1)`, `C(t+1)`) and output `Y`.
- Clicking **Generate Truth Table** opens a new window displaying the complete state transition table.
- The output and next state values are displayed in a label below the buttons.

## UI Controls
| Control | Description |
|---------|-------------|
| **Dropdowns (A, B, C, X)** | Selects the current state and input values |
| **Compute Button** | Computes the next state and output |
| **Truth Table Button** | Displays the complete truth table in a new window |

## Screenshots


## License
This project is licensed under the MIT License.

## Author
Developed by Roll:2107104(Shakhoyat Rahman)
