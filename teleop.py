# inclue code to help us talk to the robot
import libhousy

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    print("Hello World!")
    
    # After everything is done, we tell the main program to stop us
    return libhousy.DONE
