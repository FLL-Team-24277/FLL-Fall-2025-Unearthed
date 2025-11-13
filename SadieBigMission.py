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
    # br.driveForDistance(distance=20, speedPct=80, then=Stop.NONE, waiting=True)
    # br.moveRightAttachmentMotorForDegrees(degrees=-300, speedPct=80)
    # br.driveForDistance(
    #     distance=40, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    # br.waitForMillis(millis=1000)
    # br.moveRightAttachmentMotorForDegrees(degrees=300, speedPct=50)
    # br.driveForDistance(
    #     distance=-200, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    # br.waitForForwardButton()
    # ###                                         GREEN MISSION

    br.moveRightAttachmentMotorForDegrees(
        degrees=-195, speedPct=30, waiting=False
    )
    br.driveForDistance(distance=665, speedPct=100, then=Stop.BRAKE, gyro=True)
    br.turnInPlace(angle=-44, speedPct=45)
    br.moveRightAttachmentMotorForDegrees(degrees=10, speedPct=80)
    br.driveForDistance(
        distance=140, speedPct=81, then=Stop.NONE, waiting=True
    )
    # Hello!!
    br.driveForDistance(
        distance=220, speedPct=100, then=Stop.NONE, waiting=False
    )
    br.moveRightAttachmentMotorForDegrees(degrees=-20, speedPct=80)
    br.driveForDistance(
        distance=30, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    # From
    br.moveRightAttachmentMotorForDegrees(
        degrees=190, speedPct=20, waiting=False
    )
    br.driveForDistance(
        distance=-60, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    # br.moveLeftAttachmentMotorForDegrees(degrees=-100, speedPct=40)

    br.driveArcDist(
        radius=-400, dist=-800, speedPct=80, then=Stop.NONE, waiting=True
    )
    br.driveForDistance(
        distance=-150, speedPct=80, then=Stop.BRAKE, waiting=True
    )
    # br.waitForForwardButton()

    # ###                     DELIVERY 1

    # br.driveForDistance(
    #     distance=485, speedPct=80, then=Stop.BRAKE, waiting=True
    # )
    # br.moveRightAttachmentMotorForDegrees(degrees=250, speedPct=80)
    # br.driveForDistance(
    #     distance=-495, speedPct=80, then=Stop.BRAKE, waiting=True
    # )


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
