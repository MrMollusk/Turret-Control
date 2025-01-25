# Raspberry Pi Motor Control Using Xbox One Controller

This program is designed to control two stepper motors using a Raspberry Pi and a joystick. The motors' directions and speeds are adjusted based on the joystick's axis input. The code uses the RPi.GPIO library to interface with the Raspberry Pi's GPIO pins, and pygame to read the joystick input.

# Prerequisites
- **Platform:** Raspberry Pi (tested on Raspberry Pi 3/4).

- **Libraries:**
  - RPi.GPIO for controlling the GPIO pins.
  - pygame for joystick input.

Install the required libraries with the following command:

```
pip install RPi.GPIO pygame
```

# Features
- **Joystick Control:** Adjusts motor direction and speed based on joystick input.
- **PWM Motor Control:** Uses pulse width modulation to control stepper motors.
- **GPIO Interface:** Directly controls stepper motors through Raspberry Pi GPIO pins.
- **Real-time Monitoring:** Prints joystick axis values and motor speeds for debugging.

# Hardware Setup
- **Raspberry Pi GPIO Pins:**
    - Pin 23: Direction pin for the base motor.
    - Pin 22: Pulse pin for the base motor.
    - Pin 27: Direction pin for the arm motor.
    - Pin 17: Pulse pin for the arm motor.

# Usage

1. **Joystick Movement:**
        - Moving the joystick left/right will control the base motor (connected to pins 23 and 22).
        - Moving the joystick up/down will control the arm motor (connected to pins 27 and 17).
2. The speed of the motors will be scaled based on the joystick axis input, ranging from -100 to 100 steps. A positive value indicates forward movement, while a negative value indicates reverse movement.
3. The program outputs the joystick axis values and motor speed to the terminal for debugging purposes.

# Running the program

Run the program using the following command:
```
python main.py
```
The motors will start responding to the joystick input as soon as the program is executed. You can stop the program by pressing Ctrl+C.

# Code Explanation
- **GPIO Pins:** The ```DIR_BASE```, ```PUL_BASE```, ```DIR_ARM```, and ```PUL_ARM``` constants define the GPIO pins connected to the direction and pulse pins of the motors.
- **Pulse Function:** The pulse() function generates a pulse signal to control the stepper motor’s movement.
- **Motor Control:** The motor_control() function receives joystick input (scaled between -1 and 1) and adjusts the motor’s speed and direction accordingly.
- **Joystick Handling:** The pygame library is used to handle the joystick input, and the program continually checks for joystick movement.

# Debugging
- The current joystick axis values (X-axis for base and Y-axis for arm) are printed to the terminal, allowing you to monitor the input and adjust motor speeds in real-time.

# Additional Notes
- If the Raspberry Pi processor overheats due to high processing demands, the program includes a sleep(0.01) delay to prevent overloading the CPU.

# Troubleshooting
- Ensure the motors are correctly wired to the Raspberry Pi GPIO pins.
- Make sure the joystick is connected and properly initialized before starting the program.

