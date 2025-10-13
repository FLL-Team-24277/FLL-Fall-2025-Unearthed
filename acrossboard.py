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
    br.driveArcDist(
        radius=-550, dist=-850, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=200, speedPct=80)
    br.driveForDistance(
        distance=-418, speedPct=80, then=Stop.NONE, waiting=True
    )
    # br.turnInPlace(angle=-55, speedPct=45)
    # br.driveForDistance(distance=40, speedPct=80, then=Stop.BRAKE, waiting=True)
    # br.moveRightAttachmentMotorForDegrees(degrees=-380, speedPct=100)
    # br.driveForDistance(distance=-700, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.driveArcDist(
        radius=150, dist=-230, speedPct=80, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=-150, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.driveForDistance(
        distance=80, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-200, speedPct=100)
    br.waitForMillis(millis=600)
    br.moveRightAttachmentMotorForDegrees(degrees=210, speedPct=100)
    # Lifty thing
    br.turnInPlace(angle=-37, speedPct=45)
    br.moveRightAttachmentMotorForDegrees(degrees=-220, speedPct=80)
    br.driveForDistance(
        distance=100, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=40, speedPct=80)
    br.driveForDistance(
        distance=140, speedPct=40, then=Stop.BRAKE, waiting=False
    )
    br.moveRightAttachmentMotorForDegrees(degrees=100, speedPct=80)
    br.waitForMillis(millis=1000)
    # Who lived here
    br.driveForDistance(
        distance=-100, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.turnInPlace(angle=-67, speedPct=45)
    br.driveForDistance(
        distance=230, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-100, speedPct=80)
    br.driveForDistance(
        distance=-78, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=200, speedPct=80)
    # home
    br.driveArcDist(
        radius=280, dist=400, speedPct=80, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=600, speedPct=80, then=Stop.BRAKE, waiting=True
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
