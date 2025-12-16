from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    ###                 ACROSS BOARD
    # to
    br.rightAttachmentMotor.run(MED_MOT_MAX_SPEED_DEGSEC)
    br.driveArcDist(radius=500, dist=150, speedPct=80, then=Stop.NONE, waiting=True)
    # br.driveForDistance(distance=200, speedPct=80, then=Stop.NONE, waiting=True)
    br.driveForDistance(distance=400, speedPct=20, then=Stop.BRAKE, waiting=True)
    br.rightAttachmentMotor.run(-MED_MOT_MAX_SPEED_DEGSEC)
    # br.moveRightAttachmentMotorForMillis(millis=6000, speedPct=80, waiting=False)

    br.driveForDistance(distance=350, speedPct=20, then=Stop.BRAKE, waiting=True)
    br.waitForMillis(millis=2000)
    br.driveArcDist(radius=-1000, dist=-1000, speedPct=20, then=Stop.BRAKE, waiting=True,gyro=False)
    br.rightAttachmentMotor.stop()
    # br.driveForDistance(distance=-1000, speedPct=80, then=Stop.BRAKE, waiting=True)

# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
