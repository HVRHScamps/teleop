import libhousy
import time
#You can define helper functions here, make sure to but them *above* the main function
def launch(robot):
    robot.beltZ1.Set(-0.8)
    robot.beltZ2.Set(-0.8)
    robot.beltZ3.Set(1)
    robot.upperTension.Extend()
    robot.lowerTension.Retract()

def pickup(robot):
    robot.pickupMotor.Set(1)
    robot.pickupPneumatic.Extend()
    robot.beltZ1.Set(-0.8)
    robot.beltZ2.Set(-0.8)
    robot.beltZ3.Set(1)
    robot.upperTension.Retract()
    robot.lowerTension.Extend()

firstRun = True
lastCount = 0
ticks = 0
launchTimer = 0

def autoLaunch(robot: libhousy.robot):
    global firstRun, lastCount, ticks, launchTimer
    if firstRun:
        firstRun = False
        launchTimer = time.time()
    if robot.controller.getAxis(robot.controller.Axis.rTrigger) > 0.8:
       robot.shootWheel.Set(1)

    else:
        robot.shootWheel.Set(0)

    if time.time() - launchTimer >= 1:
        launchTimer = time.time()
        ticks = robot.shootCounter.Get() - lastCount
        lastCount = robot.shootCounter.Get()

    if ticks > 1800:
        launch(robot)

    else:
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)

def autoPickup(robot: libhousy.robot):
    if robot.controller.getAxis(robot.controller.Axis.lTrigger) > 0.8:
        pickup(robot)

    else:
        robot.pickupMotor.Set(0)
        robot.pickupPneumatic.Retract()
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)
    
def main(robot: libhousy.robot):
    autoLaunch(robot)
    autoPickup(robot)
    
    StickY=robot.controller.getAxis(robot.controller.Axis.lStickY)
    StickX= robot.controller.getAxis(robot.controller.Axis.lStickX)

    if (StickY>0.15 or StickY<-0.15) or (StickX>0.15 or StickX<-0.15):
        left_throttle = StickY + StickX
        right_throttle = StickY - StickX
        if left_throttle >1:
            left_throttle=1
        if right_throttle>1:
            right_throttle=1
        if  left_throttle<-1:
            left_throttle=-1
        if right_throttle<-1:
            right_throttle=-1
        robot.lDrive.Set(left_throttle)
        robot.rDrive.Set(right_throttle)
    else:
        robot.lDrive.Set(0)
        robot.rDrive.Set(0)


     







    

