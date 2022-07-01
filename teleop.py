# inclue code to help us talk to the robot
from lib2to3.pgen2.token import RPAR
import libhousy

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
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
