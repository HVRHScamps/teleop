import libhousy
#You can define helper functions here, make sure to but them *above* the main function
def main(robot: libhousy.robot):
    #Here is where your recurring code will go
    print("Hello World!")
    if  robot.controller.getAxis(robot.controller.Axis.rStickX) >0.8:
        robot.rDrive.Set(-0.7)
        robot.lDrive.Set(0.7)
    elif robot.controller.getAxis(robot.controller.Axis.rStickX) <-0.8:
        robot.rDrive.Set(0.7)
        robot.lDrive.Set(-0.7)
    elif robot.controller.getAxis(robot.controller.Axis.lStickY) >0.8:
        robot.rDrive.Set(0.7)
        robot.lDrive.Set(0.7)
    elif robot.controller.getAxis(robot.controller.Axis.lStickY) <-0.8:
        robot.rDrive.Set(-0.7)
        robot.lDrive.Set(-0.7)
    else: 
        robot.rDrive.Set(0)
        robot.lDrive.Set(0)