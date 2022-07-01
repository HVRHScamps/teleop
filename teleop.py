# inclue code to help us talk to the robot
import libhousy
import time
start_time = time.time()
last_count = 0

def autoLaunch(robot):
    global start_time, last_count
    if robot.controller.getButton(robot.controller.Button.B) >=.8:
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
    # Here is where your recurring code will go
   

    
