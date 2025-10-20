from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    br.driveForDistance(
        distance=370, speedPct=100, then=Stop.BRAKE, waiting=True
    )
    # br.turnInPlace(angle=7, speedPct=45)
    br.moveRightAttachmentMotorForDegrees(
        degrees=-250, speedPct=100, waiting=True
    )
    br.waitForMillis(millis=300)
    # br.turnInPlace(angle=7, speedPct=100)
    br.moveRightAttachmentMotorForDegrees(degrees=230, speedPct=90)
    # br.turnInPlace(angle=-6, speedPct=45)
    # br.moveRightAttachmentMotorForDegrees(degrees=-130, speedPct=90)
    # br.waitForMillis(millis=600)
    # br.moveRightAttachmentMotorForDegrees(degrees=130, speedPct=90)
    # br.turnInPlace(angle=-4, speedPct=45)
    # br.moveRightAttachmentMotorForDegrees(degrees=-130, speedPct=90)
    br.driveForDistance(
        distance=-400, speedPct=80, then=Stop.BRAKE, waiting=True
    )


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
