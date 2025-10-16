from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    ###                   GRABBY/LIFTY/SPINNY THINGY
    br.driveForDistance(
        distance=180, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.turnInPlace(angle=15, speedPct=100)
    # br.driveArcDist(radius=2000, dist=180, speedPct=80, then=Stop.BRAKE, waiting=True)

    br.moveRightAttachmentMotorForDegrees(degrees=-280, speedPct=80)
    br.waitForMillis(millis=300)
    br.moveRightAttachmentMotorForDegrees(degrees=15, speedPct=80)
    br.turnInPlace(angle=-160, speedPct=100, then=Stop.NONE)
    br.driveForDistance(
        distance=400, speedPct=100, then=Stop.BRAKE, waiting=True
    )
    br.waitForForwardButton()

    ###                                         GREEN MISSION

    br.moveRightAttachmentMotorForDegrees(
        degrees=-195, speedPct=50, waiting=False
    )
    br.driveForDistance(distance=675, speedPct=100, then=Stop.BRAKE, gyro=True)
    br.turnInPlace(angle=-46, speedPct=45)
    br.moveRightAttachmentMotorForDegrees(degrees=7, speedPct=80)
    br.driveForDistance(
        distance=140, speedPct=81, then=Stop.NONE, waiting=True
    )
    # Hello!!
    br.driveForDistance(
        distance=220, speedPct=100, then=Stop.NONE, waiting=False
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-10, speedPct=80)
    br.driveForDistance(
        distance=30, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    # From
    br.moveRightAttachmentMotorForDegrees(
        degrees=190, speedPct=20, waiting=False
    )
    br.driveForDistance(
        distance=-152, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    # br.moveLeftAttachmentMotorForDegrees(degrees=-100, speedPct=40)

    br.driveArcDist(
        radius=-400, dist=-800, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.waitForForwardButton()

    ###                     DELIVERY 1

    br.driveForDistance(
        distance=465, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=250, speedPct=80)
    br.driveForDistance(
        distance=-485, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    ###                 ACROSS BOARD
    br.waitForBackButton()
    # to
    br.driveArcDist(
        radius=-550, dist=-850, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=200, speedPct=80)
    br.driveForDistance(
        distance=-410, speedPct=80, then=Stop.NONE, waiting=True
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
    br.driveForDistance(
        distance=-10, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-220, speedPct=80)
    br.driveForDistance(
        distance=160, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=40, speedPct=80)
    br.driveForDistance(
        distance=80, speedPct=40, then=Stop.BRAKE, waiting=False
    )
    br.moveRightAttachmentMotorForDegrees(degrees=100, speedPct=80)
    br.waitForMillis(millis=1000)
    # Who lived here
    br.driveForDistance(
        distance=-100, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.turnInPlace(angle=-65, speedPct=45)
    br.driveForDistance(
        distance=230, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-110, speedPct=80)
    br.driveForDistance(
        distance=-78, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    br.moveRightAttachmentMotorForDegrees(degrees=200, speedPct=80)
    # home
    br.driveArcDist(
        radius=280, dist=400, speedPct=80, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=800, speedPct=80, then=Stop.BRAKE, waiting=True
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
