# inclue code to help us talk to the robot

import libhousy
first = True
p = 0.05
def holdStill(robot):
    global first
    if first:
        robot.rDriveEncoder.Reset()
        robot.lDriveEncoder.Reset()
        first = False 

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
      

def main(robot: libhousy.robot):
    if robot.controller.getButton(robot.controller.Button.X):
        holdStill(robot)