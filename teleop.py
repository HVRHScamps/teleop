import libhousy
import time
hs_first = True
p = 0.05
start_time = time.time()
last_count = 0
def holdStill(robot: libhousy.robot):
    global hs_first
    if hs_first:
        robot.rDriveEncoder.Reset()
        time.sleep(0.1)
        robot.lDriveEncoder.Reset()
        time.sleep(0.1)
        hs_first = False 

    if robot.rDriveEncoder.Get() > 2:
        error = 0.0 - robot.rDriveEncoder.Get()
        speed = error * p 
        robot.rDrive.Set(speed)
    elif robot.rDriveEncoder.Get() < -2:
        error = 0.0 - robot.rDriveEncoder.Get()
        speed = error * p 
        robot.rDrive.Set(speed)
    else: 
        robot.rDrive.Set(0)

    if robot.lDriveEncoder.Get() > 2:
        robot.lDrive.Set(-.5)
        error = 0.0 - robot.lDriveEncoder.Get()
        speed = error * p
        robot.lDrive.Set(speed)
    elif robot.lDriveEncoder.Get() < -2:
        error = 0.0 - robot.lDriveEncoder.Get()
        speed = error * p
        robot.lDrive.Set(speed)
    else:
        robot.lDrive.Set(0)
     

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

def pickup(robot: libhousy.robot):
    print("running pickup mode")
    robot.pickupMotor.Set(1)
    robot.pickupPneumatic.Extend()
    robot.beltZ1.Set(-0.8)
    robot.beltZ2.Set(0)
    robot.beltZ3.Set(0)
    robot.upperTension.Retract()
    robot.lowerTension.Extend()

def main(robot: libhousy.robot):
    global hs_first
    if robot.controller.getAxis(robot.controller.Axis.lTrigger) > 0.8:
        pickup(robot)
    elif robot.controller.getButton(robot.controller.Button.X):
        autoLaunch(robot)
    else:
        robot.shootWheel.Set(0)
        robot.pickupMotor.Set(0)
        robot.pickupPneumatic.Retract()
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)
    
    
    if robot.controller.getButton(robot.controller.Button.X):
        holdStill(robot)
    else:
        hs_first = True
    
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

