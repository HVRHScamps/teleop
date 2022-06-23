import libhousy
#You can define helper functions here, make sure to but them *above* the main function
def main(robot: libhousy.robot):
    #Here is where your recurring code will go
    left_throttle = robot.controller.getAxis(robot.controller.Axis.lStickY) + robot.controller.getAxis(robot.controller.Axis.lStickX)
    right_throttle =robot.controller.getAxis(robot.controller.Axis.lStickY) - robot.controller.getAxis(robot.controller.Axis.lStickX)
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