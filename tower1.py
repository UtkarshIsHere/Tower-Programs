#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_D, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from time import sleep
import sys

#Initialize the tank driving
arm = LargeMotor(OUTPUT_D)
steering_tank = MoveSteering(OUTPUT_C, OUTPUT_B)
tank = MoveTank(OUTPUT_C, OUTPUT_B)
gyro = GyroSensor(INPUT_2)
color = ColorSensor(INPUT_3)
color.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown') #To get the direct colour use: colors[color.value()]


#Go forward, 25% speed, and then go backwards at 25% speed, for 2 seconds
tank.on_for_seconds(25, 25, 2.2, brake=True, block=True)
tank.on_for_seconds(-25, -25, 2.2, brake=True, block=True)

#Return to home code
steering_tank.on_for_degrees(100, SpeedPercent(25), 70 , brake=True)

arm.on_for_rotations(SpeedPercent(-10), 0.3)

tank.on(-25, -25)

sleep(10)


