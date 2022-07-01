# inclue code to help us talk to the robot
import libhousy

def holdStill(robot):
    def main(robot: libhousy.robot):
    
        if robot.controller.getButton(robot.controller.Button.x):
            first = True

p = 0.05
def main(robot: libhousy.robot):
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
    
    # After everything is done, we tell the main program to stop us
    #return libhousy.DONE
