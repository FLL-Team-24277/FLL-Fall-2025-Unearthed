from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    br.moveLeftAttachmentMotorForMillis(millis=290, speedPct=90, waiting=False)
    br.driveArcDist(radius=100, dist=-200, speedPct=100, then=Stop.BRAKE, waiting=True)
    # Stop.NONE
    br.driveForDistance(distance=-50, speedPct=100, then=Stop.BRAKE, waiting=True)
    # br.moveRightAttachmentMotorForDegrees(degrees=150, speedPct=80, waiting=False)
    br.driveForDistance(distance=600, speedPct=100, then=Stop.BRAKE, waiting=True)
    br.turnInPlace(angle=30, speedPct=100)
    br.moveRightAttachmentMotorForMillis(millis=400, speedPct=80)
    br.driveForDistance(distance=200, speedPct=100, then=Stop.BRAKE, waiting=True)
    br.moveRightAttachmentMotorForMillis(millis=400, speedPct=-80)
    # br.driveForDistance(distance=50, speedPct=100, then=Stop.BRAKE, waiting=True)
    # br.moveLeftAttachmentMotorForMillis(millis=800, speedPct=-100)
    # br.waitForMillis(millis=800)
    br.moveLeftAttachmentMotorForMillis(millis=800, speedPct=-80)
    # br.driveForDistance(distance=100, speedPct=100, then=Stop.BRAKE, waiting=True)
    br.moveRightAttachmentMotorForMillis(millis=200, speedPct=-80)
    # br.driveForDistance(distance=-100, speedPct=100, then=Stop.BRAKE, waiting=True)
    # br.turnInPlace(angle=-50, speedPct=45,waiting=True)
    # br.moveRightAttachmentMotorForMillis(millis=400, speedPct=-60)
    # br.waitForMillis(millis=950)
    br.driveForDistance(distance=-200, speedPct=100, then=Stop.NONE, waiting=True)
    # br.turnInPlace(angle=-40, speedPct=100)
    br.driveArcDist(radius=300, dist=-250, speedPct=100, then=Stop.NONE, waiting=True)
    br.driveForDistance(distance=-400, speedPct=100, then=Stop.BRAKE, waiting=True)
# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
