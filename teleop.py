# inclue code to help us talk to the robot
from lib2to3.pgen2.token import RPAR
import libhousy
import time
start_time = time.time()
last_count = 0

def autoLaunch(robot: libhousy.robot):
    global start_time, last_count
    if robot.controller.getButton(robot.controller.Button.X) >=.8:
        robot.shootWheel.Set(1)
    else:
        robot.shootWheel.Set(0)
        robot.pickupMotor.Set(0)
        robot.pickupPneumatic.Retract()
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)

    if time.time() - start_time > 0.5:
        start_time = time.time()
        if robot.shootCounter.Get() - last_count  > 900:
            robot.beltZ1.Set(-0.8)
            robot.beltZ2.Set(-0.8)
            robot.beltZ3.Set(1)
            robot.upperTension.Extend()
            robot.lowerTension.Retract()
        last_count = robot.shootCounter.Get()

def main(robot: libhousy.robot):
    
    autoLaunch(robot)
    
    stickY = robot.controller.getAxis(robot.controller.Axis.lStickY)
    stickX = robot.controller.getAxis(robot.controller.Axis.lStickX)
    lPower = stickY+stickX
    rPower = stickY-stickX
    if lPower > 1: 
        lPower = 1
    if rPower > 1:
        rPower = 1
    if lPower < -1: 
        lPower = -1
    if rPower < -1:
        rPower = -1
        
    robot.lDrive.Set(lPower)
    robot.rDrive.Set(rPower)
