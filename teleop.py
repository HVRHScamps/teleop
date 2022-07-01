# inclue code to help us talk to the robot
import libhousy

def pickup(robot):
    print("running pickup mode")
    robot.pickupMotor.Set(1)
    robot.pickupPneumatic.Extend()
    robot.beltZ1.Set(-0.8)
    robot.beltZ2.Set(0)
    robot.beltZ3.Set(0)
    robot.upperTension.Retract()
    robot.lowerTension.Extend()

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    if robot.controller.getAxis(robot.controller.Axis.lTrigger) > 0.8:
        pickup(robot)
   
    else:
        robot.pickupMotor.Set(0)
        robot.pickupPneumatic.Retract()
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)