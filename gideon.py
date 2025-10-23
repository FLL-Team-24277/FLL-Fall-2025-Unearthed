from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    br.moveRightAttachmentMotorForMillis(millis=600, speedPct=-80, waiting=False)

    dist = 45

    br.driveForDistance(
        distance=359, speedPct=70, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(
        degrees=-460, speedPct=25
    )  # lower the arm
    br.driveForDistance(
        distance=45, speedPct=25, then=Stop.BRAKE, waiting=True
    )
    for pushes in range(5):
        # br.driveForDistance(
        #     distance=dist, speedPct=100, then=Stop.BRAKE, waiting=True, accelerationPct=100
        # )
        br.driveForDistance(
            distance=dist,
            speedPct=100,
            then=Stop.BRAKE,
            waiting=True,
            accelerationPct=15
        )
        br.driveForDistance(
            distance=-dist,
            speedPct=100,
            then=Stop.BRAKE,
            waiting=True,
            accelerationPct=7,
        )

    br.driveForDistance(
        distance=-45, speedPct=25, then=Stop.BRAKE, waiting=True
    )
    br.moveLeftAttachmentMotorForDegrees(
        degrees=460, speedPct=80
    )  # raise the arm
    br.waitForMillis(millis=2000)
    br.driveArcDist(radius=1000, dist=200, speedPct=40)
    br.moveRightAttachmentMotorForMillis(millis=500, speedPct=80, waiting=False)

    br.driveForDistance(
        distance=-900, speedPct=80, then=Stop.BRAKE, waiting=True
    )


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method abe.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
