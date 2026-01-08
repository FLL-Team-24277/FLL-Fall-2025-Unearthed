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
    br.driveForDistance(
        distance=520, speedPct=75, then=Stop.BRAKE, waiting=True  # 540
    )
    br.moveLeftAttachmentMotorForMillis(
        millis=550, speedPct=-100, waiting=False
    )
    br.moveRightAttachmentMotorForMillis(
        millis=6000, speedPct=-300, waiting=True
    )
    br.moveLeftAttachmentMotorForMillis(millis=1000, speedPct=100)
    br.driveForDistance(
        distance=-600, speedPct=100, then=Stop.BRAKE, waiting=True
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
