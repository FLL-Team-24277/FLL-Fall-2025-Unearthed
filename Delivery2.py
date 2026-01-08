from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    # to
    br.moveRightAttachmentMotorForMillis(millis=400, speedPct=-80,waiting=False)
    br.driveArcDist(
        radius=1850, dist=1090, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.driveForDistance(
        distance=-20, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.turnInPlace(angle=30, speedPct=45)
    br.moveRightAttachmentMotorForDegrees(
        degrees=50, speedPct=80, waiting=False
    )
    # br.turnInPlace(angle=10, speedPct=45)
    # br.waitForMillis(millis=500)
    br.turnInPlace(angle=-9, speedPct=45, waiting=False)
    br.moveRightAttachmentMotorForDegrees(degrees=170, speedPct=50)
    br.driveForDistance(
        distance=-200, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    # br.driveForDistance(
    #     distance=-250, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    # #flag
    # br.driveForDistance(distance=50, speedPct=80, then=Stop.BRAKE, waiting=True)
    # br.turnInPlace(angle=50, speedPct=45, then=Stop.NONE)
    # br.driveForDistance(distance=410, speedPct=80, then=Stop.NONE, waiting=True)
    # br.turnInPlace(angle=20, speedPct=45)
    # br.driveArcDist(radius=350, dist=290, speedPct=80, then=Stop.BRAKE, waiting=True)


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
