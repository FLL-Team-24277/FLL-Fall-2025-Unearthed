from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(
    left_motor, right_motor, wheel_diameter=56, axle_track=112
)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
# drive_base.use_gyro(True)

drive_base.settings(straight_speed=977, straight_acceleration=9775)
# Drive forward by 500mm (half a meter).
drive_base.straight(100)

drive_base.settings(straight_speed=977, straight_acceleration=9775)
# Drive forward by 500mm (half a meter).
drive_base.straight(-100)
