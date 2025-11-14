from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    br.moveRightAttachmentMotorForMillis(
        millis=500, speedPct=50, waiting=False
    )
    br.moveLeftAttachmentMotorForMillis(
        millis=500, speedPct=-50, waiting=False
    )
    br.driveArcDist(
        radius=-336, dist=250, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-110, speedPct=20)
    br.driveForDistance(
        distance=150, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.waitForMillis(millis=250)
    br.moveRightAttachmentMotorForDegrees(degrees=-25, speedPct=80)
    br.moveLeftAttachmentMotorForDegrees(degrees=115, speedPct=100)
    br.moveLeftAttachmentMotorForMillis(
        millis=600, speedPct=-50, waiting=False
    )
    br.driveForDistance(
        distance=-95, speedPct=50, then=Stop.BRAKE, waiting=True
    )
    br.driveForDistance(
        distance=30, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=58, speedPct=80)
    br.driveForDistance(
        distance=-110, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-90, speedPct=80)
    # br.moveRightAttachmentMotorForMillis(millis=400, speedPct=80)
    br.turnInPlace(angle=10, speedPct=45)
    br.driveForDistance(
        distance=55, speedPct=80, then=Stop.NONE.BRAKE, waiting=True
    )
    br.turnInPlace(angle=-40, speedPct=45)
    br.driveForDistance(
        distance=-20, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.driveArcDist(
        radius=-210, dist=-410, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.waitForForwardButton()
    br.moveRightAttachmentMotorForDegrees(degrees=50, speedPct=80)
    br.driveArcDist(
        radius=-240, dist=282, speedPct=50, then=Stop.NONE, waiting=True
    )

    br.driveForDistance(
        distance=80, speedPct=650, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-20, speedPct=80)
    br.driveForDistance(
        distance=-25, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.turnInPlace(angle=-50, speedPct=45)
    br.turnInPlace(angle=46, speedPct=45)
    br.driveForDistance(
        distance=-650, speedPct=100, then=Stop.BRAKE, waiting=True
    )

    # br.moveRightAttachmentMotorForDegrees(degrees=-15, speedPct=80)
    # br.driveArcDist(radius=-90, dist=200, speedPct=80, then=Stop.NONE.BRAKE, waiting=True)
    # br.driveForDistance(distance=50, speedPct=80, then=Stop.BRAKE, waiting=True)


# br.driveArcDist(radius=97, dist=100, speedPct=80, then=Stop.BRAKE, waiting=True)
# br.driveForDistance(distance=49, speedPct=80, then=Stop.BRAKE, waiting=True)
# br.turnInPlace(angle=10, speedPct=45)
# br.turnInPlace(angle=-50, speedPct=45, then=Stop.NONE)
# br.turnInPlace(angle=65, speedPct=45, then=Stop.NONE)
# br.driveForDistance(distance=-550, speedPct=100, then=Stop.BRAKE, waiting=True)


# br.driveArcDist(radius=30, dist=175, speedPct=80, then=Stop.BRAKE, waiting=True)

# br.turnInPlace(angle=97, speedPct=45)
# br.moveRightAttachmentMotorForDegrees(degrees=-75, speedPct=100)
# br.driveForDistance(distance=81, speedPct=80, then=Stop.BRAKE, waiting=True)
# br.moveRightAttachmentMotorForDegrees(degrees=-75, speedPct=100)
# br.turnInPlace(angle=-70, speedPct=45)
# br.driveArcDist(radius=420, dist=-700, speedPct=100, then=Stop.BRAKE, waiting=True)

# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
# write new code for passive attatchment
