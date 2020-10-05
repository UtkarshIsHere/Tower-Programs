#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_D, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from time import sleep

#Initialize the tank driving
arm = LargeMotor(OUTPUT_D)
steering_tank = MoveSteering(OUTPUT_C, OUTPUT_B)
tank = MoveTank(OUTPUT_C, OUTPUT_B)


tank.on_for_seconds(25, 25, 3.6, brake=True, block=False)
tank.on_for_seconds(-25, -25, 3.6, brake=True, block=False)

steering_tank.on_for_degrees(100, SpeedPercent(25), 20 , brake=True)

arm.on_for_rotations(SpeedPercent(-10), 0.3)

tank.on(-25, -25)
sleep(10)

