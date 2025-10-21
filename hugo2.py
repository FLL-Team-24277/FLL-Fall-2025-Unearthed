from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loa5ded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):


    br.driveForDistance(
        distance=-215, speedPct=80, then=Stop.NONE, waiting=True
    )
    br.moveRightAttachmentMotorForMillis(
        millis=4000, speedPct=5, waiting=False
    )
    # pos spd = lower arm
    # br.driveArcDist(radius=-175, dist=-700, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.curve(
        radius=-230, angle=-180, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.driveForDistance(distance=-5, speedPct=10, then=Stop.BRAKE, waiting=True)
    br.driveForDistance(distance=35, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.moveRightAttachmentMotorForMillis(millis=2500, speedPct=-20)
    br.driveForDistance(
       distance=300, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForMillis(millis=1700, speedPct=-80)
    br.moveLeftAttachmentMotorForMillis(millis=1700, speedPct=80)
    br.driveForDistance(distance=-300, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.driveArcDist(radius=-150, dist=400, speedPct=100, then=Stop.NONE, waiting=True)
    br.driveForDistance(
       distance=500, speedPct=100, then=Stop.BRAKE, waiting=True
    )

   # br.driveForDistance(
    #    distance=, speedPct=80, then=Stop.BRAKE, waiting=True
   # )


# br.moveRightAttachmentMotorForDegrees(degrees=-360, speedPct=30, waiting=True)
# br.driveForDistance(distance=220, speedPct=80, then=Stop.BRAKE, waiting=True)
# left attachment motor pos speed = raise; neg speed = lower
# br.moveLeftAttachmentMotorForMillis(millis=200, speedPct=40)
# br.moveLeftAttachmentMotorForMillis(millis=1300, speedPct=-100)
# br.moveLeftAttachmentMotorForMillis(millis=1300, speedPct=100)
# br.driveForDistance(
# distance=-100, speedPct=80, then=Stop.BRAKE, waiting=True)
# br.moveRightAttachmentMotorForDegrees(degrees=100, speedPct=80)


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
