from base_robot import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):

    br.driveArcDist(
        radius=-90, dist=50
        0, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.driveForDistance(distance=350, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.turnInPlace(angle=90, speedPct=45)
    

    #br.turnInPlace(angle=37, speedPct=45)
   # br.driveForDistance(distance=100, speedPct=80, then=Stop.BRAKE, waiting=True)
   # br.turnInPlace(angle=10, speedPct=45)
   # br.driveArcDist(radius=65, dist=-115, speedPct=80, then=Stop.BRAKE, waiting=True)
   # br.turnInPlace(angle=145, speedPct=45)
    #br.turnInPlace(angle=90, speedPct=45)
    #br.driveForDistance( distance=100, speedPct=80, then=Stop.BRAKE, waiting=True)

    # to
    # br.driveForDistance(distance=260, speedPct=80, then=Stop.NONE.BRAKE, waiting=True)
    # br.driveArcDist(radius=-90, dist=200, speedPct=80, then=Stop.NONE.BRAKE, waiting=True)
    # br.driveForDistance(distance=125, speedPct=80, then=Stop.BRAKE, waiting=True)


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
