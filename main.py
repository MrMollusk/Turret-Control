import pygame
import RPi.GPIO as GPIO
from time import sleep

#Upper snake case for constants
#BASE PINS
DIR_BASE = 23  # Direction pin for base motor
PUL_BASE = 22  # Pulse pin for base motor
DIR_ARM = 27   # Direction pin for arm motor
PUL_ARM = 17   # Pulse pin for arm motor

#Using BCM numbering scheme
GPIO.setmode(GPIO.BCM)

#Set DIR and PUL pins as output
GPIO.setup(DIR_BASE, GPIO.OUT)
GPIO.setup(PUL_BASE, GPIO.OUT)
GPIO.setup(DIR_ARM, GPIO.OUT)
GPIO.setup(PUL_ARM, GPIO.OUT)

#Python having these libraries seems like too much abstraction tbh
pygame.init()

controller = pygame.joystick.Joystick(0)
controller.init()

#Functions and variables in snake case
def pulse(pul_pin, count, speed):
    #Motor control pulses
    for i in range(count):
        GPIO.output(pul_pin, GPIO.HIGH)
        sleep(speed)
        GPIO.output(pul_pin, GPIO.LOW)
        sleep(speed)

def motor_control(x_input, dir_pin, pul_pin):

    #Joystick has input between -1 and 1
    #Multiply by 100 to scale so stepper motor can use with a max of 100 steps
    speed = int(x_input * 100)

    #Debugging motor speed
    print(f"Speed: {speed}")

    #Forward
    if speed > 0:
        GPIO.output(dir_pin, GPIO.HIGH)
        pulse(pul_pin, speed, 0.01)

    #Reverse
    elif speed < 0:
        GPIO.output(dir_pin, GPIO.LOW)
        pulse(pul_pin, -speed, 0.01)

    else:
        #Motor stops if sspeed is 0
        GPIO.output(pul_pin, GPIO.LOW)

try:
    while True:
        pygame.event.pump()

        #0 and 1 used for left joystick
        #Axis values for base motor
        x_axis = controller.get_axis(0)
        #Axis values for arm motor
        y_axis = controller.get_axis(1)

        #Prints axis values for debugging, controller used has slight drift :(
        print(f"X-axis: {x_axis}, Y-axis: {y_axis}")

        motor_control(x_axis, DIR_BASE, PUL_BASE)
        motor_control(y_axis, DIR_ARM, PUL_ARM)

        #Added because the processor got so hot with overloading
        sleep(0.01)

#Stops program when ctrl + c pressed
except KeyboardInterrupt:
    print("Exiting")


finally:
    #Resource freeing
    GPIO.cleanup()
    pygame.quit()
