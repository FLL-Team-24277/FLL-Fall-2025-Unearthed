from pybricks.pupdevices import Motor, ColorSensor

from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Side,
    Stop,
    Color,
    Button,
    Icon,
)
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks import version
from utils import *

# All default constant percentages will be defined here
DEFAULT_MED_MOT_SPEED_PCT = 90  # normal attachment moter speed, % value
DEFAULT_MED_MOT_ACCEL_PCT = 80
DEFAULT_BIG_MOT_SPEED_PCT = 80  # normal wheels moter speed, % value
DEFAULT_BIG_MOT_ACCEL_PCT = 7
DEFAULT_TURN_SPEED_PCT = 45  #
DEFAULT_TURN_ACCEL_PCT = 45  #
DEFAULT_STALL_PCT = 50
CURRENT_PYBRICKS_VERSION = "ci-release-86-v3.6.1 on 2025-03-11"


class BaseRobot:
    """
    BaseRobot provides a comprehensive set of methods and attributes for \
        controlling an FLL Team 24277 robot using the pybricks library.
    This class abstracts common robot operations such as driving, turning, \
        and manipulating attachments, as well as color detection and user \
        input handling. It is designed to simplify mission programming and \
        ensure consistent robot behavior.
    Features:
    - Initializes motors, sensors, and color profiles for reliable operation.
    - Provides high-level movement commands (drive, turn, curve, arc) with \
        support for speed, acceleration, and gyro control.
    - Includes methods for precise control of left and right attachment \
        motors (by degrees, time, or until stalled).
    - Supports color detection with custom HSV profiles for robust field \
        color recognition.
    - Offers utility methods for waiting (delays, button presses) to \
        synchronize robot actions with user input or field events.
    - Allows easy mapping between custom color profiles and pybricks default \
        colors for hub light feedback.
    Example usage:
        >>> from base_robot import *
        >>> br = BaseRobot()
        >>> br.driveForDistance(distance=200, speedPct=80)
        >>> br.moveLeftAttachmentMotorForDegrees(degrees=90)
    Attributes:
        hub (PrimeHub): The main hub object for robot control.
        leftDriveMotor (Motor): Motor controlling the left drive wheel.
        rightDriveMotor (Motor): Motor controlling the right drive wheel.
        robot (DriveBase): DriveBase object for coordinated driving.
        leftAttachmentMotor (Motor): Motor for the left attachment.
        rightAttachmentMotor (Motor): Motor for the right attachment.
        colorSensor (ColorSensor): Color sensor for field color detection.
        sensorColors (list[Color]): List of custom color profiles detectable \
            by the color sensor.
        myColor2DefaultColorDict (dict[Color, Color]): Mapping from custom \
            color profiles to pybricks default colors.
    Note:
        - All movement methods accept optional parameters for speed, \
            acceleration, and waiting for completion.
        - Color profiles should be calibrated for your specific field and \
            lighting conditions.
        - Use the provided snippet names (e.g., 'dfd', 'lmd') for quick code \
            insertion in compatible editors.
    """

    # type ignore comments needed to supress type checking errors within
    # pybricks library. These are not needed in the actual code, but
    # are needed for type checking tools like mypy or pyright.
    # https://github.com/orgs/pybricks/discussions/2164
    def __init__(self):
        """
        Initializes the BaseRobot with all hardware components, sensor \
            calibration, and configuration settings.
        - Sets up the PrimeHub with specified orientation.
        - Prints firmware version and battery voltage information.
        - Initializes drive motors, attachment motors, and drive base with \
            default speed and acceleration settings.
        - Configures color sensor and calibrates custom HSV color values for \
            mission-specific color detection.
        - Sets up a list of detectable colors for the color sensor.
        - Maps custom sensor colors to default Pybricks colors for hub \
            light feedback.
        """
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)  # type: ignore
        print(version[2])
        if version[2] != CURRENT_PYBRICKS_VERSION:
            print(
                "* * * Expected Pybricks version " + CURRENT_PYBRICKS_VERSION
            )
        v: int = self.hub.battery.voltage()
        vPct: int = RescaleBatteryVoltage(v)
        print(str(v))
        print(f"Battery voltage %: {vPct / 100 :.2%}")
        self._version: str = "1.0 09/11/2024"
        self.leftDriveMotor: Motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor: Motor = Motor(Port.A)
        self.robot: DriveBase = DriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,  # defined in utils.py
            AXLE_TRACK,  # defined in utils.py
        )
        # default speeds were determined by testing
        self.robot.settings(
            straight_speed=RescaleStraightSpeed(DEFAULT_BIG_MOT_SPEED_PCT),
            straight_acceleration=RescaleStraightAccel(
                DEFAULT_BIG_MOT_ACCEL_PCT
            ),
            turn_rate=RescaleTurnSpeed(DEFAULT_TURN_SPEED_PCT),
            turn_acceleration=RescaleTurnAccel(DEFAULT_TURN_ACCEL_PCT),
        )

        self.leftAttachmentMotor: Motor = Motor(Port.B)
        self.rightAttachmentMotor: Motor = Motor(Port.D)
        self.leftAttachmentMotor.control.limits(acceleration=20000)
        self.rightAttachmentMotor.control.limits(acceleration=20000)

        self.colorSensor: ColorSensor = ColorSensor(Port.F)

        # HSV values were found by testing. Default hsv-values are provided
        # in comments. Theoretically, the farther apart the hsv-values are,
        # the less likely two colors can get "confused"
        # Use the colorTest.py program to get the color sensor values

        # type: ignore comments needed to supress type checking errors.
        # Result of a known bug in the pybricks library.
        # https://github.com/orgs/pybricks/discussions/2098

        # WHITE default: h=0,s=0,v=100
        Color.SENSOR_WHITE = Color(h=0, s=0, v=100)  # type: ignore

        # RED default: h=0,s=100,v=100
        Color.SENSOR_RED = Color(h=353, s=82, v=92)  # type: ignore

        # YELLOW default: h=60,s=100,v=100
        Color.SENSOR_YELLOW = Color(h=60, s=60, v=100)  # type: ignore

        # GREEN default: h=120,s=100,v=100
        Color.SENSOR_GREEN = Color(h=156, s=66, v=66)  # type: ignore

        # BLUE default: h=240,s=100,v=100
        Color.SENSOR_BLUE = Color(h=216, s=84, v=83)  # type: ignore

        # MAGENTA default: h=300,s=100,v=100
        Color.SENSOR_MAGENTA = Color(h=333, s=75, v=78)  # type: ignore

        # ORANGE default: h=30,s=100,v=100
        Color.SENSOR_ORANGE = Color(h=8, s=75, v=100)  # type: ignore

        # DARKGRAY default: h=0,s=0,v=50
        Color.SENSOR_DARKGRAY = Color(h=192, s=21, v=64)  # type: ignore

        # NONE default: h=0,s=0,v=0
        Color.SENSOR_NONE = Color(h=170, s=26, v=15)  # type: ignore

        # LIME default: h=92, s=57, v=93
        Color.SENSOR_LIME = Color(h=92, s=55, v=93)  # type: ignore

        # Put the custom colors in a list. Best practice is to only use
        # colors that we are using for actual missions.
        self.sensorColors: list[Color] = [
            Color.SENSOR_WHITE,  # type: ignore
            Color.SENSOR_RED,  # type: ignore
            Color.SENSOR_YELLOW,  # type: ignore
            Color.SENSOR_GREEN,  # type: ignore
            Color.SENSOR_BLUE,  # type: ignore
            Color.SENSOR_MAGENTA,  # type: ignore
            Color.SENSOR_ORANGE,  # type: ignore
            Color.SENSOR_DARKGRAY,  # type: ignore
            Color.SENSOR_NONE,  # Do not comment this out # type: ignore
            Color.SENSOR_LIME,  # type: ignore
        ]

        # Set the detectable colors using our list
        self.colorSensor.detectable_colors(self.sensorColors)

        # Translates our custom colors into the default pybricks colors
        # It doesn't matter if there are extra colors in here that won't be
        # detected. Used to set the hub light color to match the color sensor
        self.myColor2DefaultColorDict: dict[Color, Color] = {
            Color.SENSOR_GREEN: Color.GREEN,  # type: ignore
            Color.SENSOR_RED: Color.RED,  # type: ignore
            Color.SENSOR_YELLOW: Color.YELLOW,  # type: ignore
            Color.SENSOR_BLUE: Color.BLUE,  # type: ignore
            Color.SENSOR_MAGENTA: Color.MAGENTA,  # type: ignore
            Color.SENSOR_WHITE: Color.WHITE,  # type: ignore
            Color.SENSOR_ORANGE: Color.ORANGE,  # type: ignore
            Color.SENSOR_DARKGRAY: Color.GRAY,  # type: ignore
            Color.SENSOR_NONE: Color.NONE,  # type: ignore
            Color.SENSOR_LIME: Color.CYAN,  # type: ignore
        }

    def moveLeftAttachmentMotorForDegrees(
        self,
        degrees: int,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        waiting: bool = True,
    ):
        """
        Moves the left attachment motor for a set amount of degrees

        Snippet: lmd

        Example:

        >>> moveLeftAttachmentMotorForDegrees(degrees=50, speedPct=50)
        >>> moveLeftAttachmentMotorForDegrees(degrees=50, waiting=False)
        
        Args:

        degrees: (REQUIRED integer, != 0): how much the left attachment motor \
        will turn. Positive numbers move the motor right; negative numbers \
        turn it to the left

        speedPct: (OPTIONAL integer, > 0): this controls how fast the motor \
        will move

        waiting: (OPTIONAL bool): this tells the robot if it should wait for \
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.
        """
        # now the real work begins!
        speed = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run_angle(
            speed=speed, rotation_angle=degrees, wait=waiting
        )

    def moveLeftAttachmentMotorForMillis(
        self,
        millis: int,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        waiting: bool = True,
    ):
        """
        Moves the left attachment motor for a set amount of time

        Snippet: lmm

        Example:

        >>> moveLeftAttachmentMotorForMillis(millis=500, speedPct=50)
        >>> moveLeftAttachmentMotorForMillis(millis=500, then=STOP.BRAKE)
        >>> moveLeftAttachmentMotorForMillis(millis=500, wait=False)

        Args:

        millis: (REQUIRED integer, > 0): how many miliseconds the left \
        attachment motor will turn for. A millisecond is 0.001 of a second, \
        so 5000 is 5 seconds.

        speedPct: (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        waiting: (OPTIONAL bool): this tells the robot if it should wait for 
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        """
        speed: int = RescaleMedMotSpeed(speedPct)
        self.leftAttachmentMotor.run_time(
            speed=speed, time=millis, wait=waiting
        )

    def moveLeftAttachmentMotorUntilStalled(
        self,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        stallPct: int = DEFAULT_STALL_PCT,
    ):
        """
        Moves the left attachment motor until it stalls

        Snippet: lams

        Example:

        >>> moveLeftAttachmentMotorUntilStalled(speedPct=50, stallPct=75)

        Args:

        speedPct: (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        stallPct: (OPTIONAL integer, 1 to 100): How much torque before 
        stopping and then continuing with the next line of code. Lower \
        numbers means stopping with less torque.
        """

        speed: int = RescaleMedMotSpeed(speedPct)
        load: int = RescaleMedMotTorque(stallPct)
        self.leftAttachmentMotor.run(speed)
        while abs(self.leftAttachmentMotor.load()) < load:
            wait(25)
        self.leftAttachmentMotor.hold()

    def moveRightAttachmentMotorForDegrees(
        self,
        degrees: int,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        waiting: bool = True,
    ):
        """
        Moves the right attachment motor for a set amount of degrees

        Snippet: rmd

        Example:

        >>> moveRightAttachmentMotorForDegrees(degrees=50, speedPct=50)
        >>> moveRightAttachmentMotorForDegrees(degrees=50, waiting=False)
        
        Args:

        degrees: (REQUIRED integer, != 0): how much the right attachment motor \
        will turn. Positive numbers move the motor right; negative numbers \
        turn it to the left.

        speedPct: (OPTIONAL integer, > 0): this controls how fast the motor \
        will move

        waiting: (OPTIONAL bool): this tells the robot if it should wait for \
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.
        """
        # now the real work begins!
        speed = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run_angle(
            speed=speed, rotation_angle=degrees, wait=waiting
        )

    def moveRightAttachmentMotorForMillis(
        self,
        millis: int,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        waiting: bool = True,
    ):
        """
        Moves the right attachment motor for a set amount of time

        Snippet: rmm

        Example:

        >>> moveRightAttachmentMotorForMillis(millis=500, speedPct=50)
        >>> moveRightAttachmentMotorForMillis(millis=500, then=STOP.BRAKE)
        >>> moveRightAttachmentMotorForMillis(millis=500, wait=False)

        Args:

        millis: (REQUIRED integer, > 0): how many miliseconds the right \
        attachment motor will turn for. A millisecond is 0.001 of a second, \
        so 5000 is 5 seconds.

        speedPct: (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        waiting: (OPTIONAL bool): this tells the robot if it should wait for \
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        """
        speed: int = RescaleMedMotSpeed(speedPct)
        self.rightAttachmentMotor.run_time(
            speed=speed, time=millis, wait=waiting
        )

    def moveRightAttachmentMotorUntilStalled(
        self,
        speedPct: int = DEFAULT_MED_MOT_SPEED_PCT,
        stallPct: int = DEFAULT_STALL_PCT,
    ):
        """
        Moves the right attachment motor until it stalls

        Snippet: rams

        Example:

        >>> moveRightAttachmentMotorUntilStalled(speedPct=50, stallPct=75)

        Args:

        speedPct (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        stallPct (OPTIONAL integer, 1 to 100): How much torque before stopping \
        and then continuing with the next line of code. Lower numbers means \
        stopping with less torque.
        """

        speed: int = RescaleMedMotSpeed(speedPct)
        load: int = RescaleMedMotTorque(stallPct)
        self.rightAttachmentMotor.run(speed)
        while abs(self.rightAttachmentMotor.load()) < load:
            wait(25)
        self.rightAttachmentMotor.hold()

    def driveForDistance(
        self,
        distance: int,
        speedPct: int = DEFAULT_BIG_MOT_SPEED_PCT,
        then: Stop = Stop.BRAKE,
        gyro: bool = True,
        accelerationPct: int = DEFAULT_BIG_MOT_ACCEL_PCT,
        wallsquare: bool = False,
        waiting: bool = True,
    ):
        """Drive the robot for a specified distance

        Snippet: dfd
        
        Example:
        >>> br.driveForDistance(distance=100, speedPct=80) # drive 100mm at 80% speed
        >>> br.driveForDistance(distance=100, speedPct=80, then=Stop.BRAKE, continuing=True)

        Args:

        distance: (REQUIRED integer, != 0): how far the robot will move in \
        millimeters. Positive numbers move it forward; negative numbers \
        move the robot backward \

        speedPct: (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        then: (OPTIONAL, Stop.HOLD|Stop.BRAKE|Stop.NONE|Stop.COAST): What the \
        drive motors will do after the robot has driven the distance. \
        Stop.BRAKE, Passively resist small external forces. \
        Stop.HOLD, Keep controlling the motor to hold it at the commanded \
        angle. \
        Stop.COAST, Allow the motor to coast freely until it stops. \
        Stop.NONE, Do not control the motor at all (use when chaining drive \
            commands).

        waiting: (OPTIONAL bool): this tells the robot if it should wait for \
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        gyro: (OPTIONAL bool): Use the gyro. Defaults to True. Set to False \
        when you do not want to use the gyro such as when you are wall \
        following.

        accelerationPct: (OPTIONAL int > 0) How fast the robot accelerates

        wallsquare: (OPTIONAL bool): If True, the robot will back up very \
        briefly before driving forward. Useful to take the slack out of the \
        motors and square up against a wall. \
        """
        speed = RescaleStraightSpeed(speedPct)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        if wallsquare == True:
            self.robot.drive(RescaleStraightSpeed(-60), 0)
            wait(150)
            self.robot.brake()

        self.robot.settings(
            straight_acceleration=acceleration, straight_speed=speed
        )
        self.robot.straight(distance, then, waiting)

    def driveForMillis(
        self,
        millis: int,
        speedPct: int = DEFAULT_BIG_MOT_SPEED_PCT,
        gyro: bool = True,
        accelerationPct: int = DEFAULT_BIG_MOT_ACCEL_PCT,
    ):
        """Drives the robot for the given amount of millis 

        Snippet: dfm

        Example:
        >>> br.driveForMillis(millis=1000) # drive the robot for one sec
        
        Args:

        millis: (REQUIRED integer, > 0): how many miliseconds the \
        robot will drive. A millisecond is 0.001 of a second, \
        so 5000 millis is 5 seconds.

        speedPct: (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the robot will drive. Positive numbers move the robot forward, \
        negative numbers move it backwards.

        gyro: (OPTIONAL bool): Use the gyro. Defaults to True. Set to False \
        when you do not want to use the gyro such as when you are wall \
        following.

        accelerationPct: (OPTIONAL int > 0) How fast the robot accelerates
        """
        speed = RescaleStraightSpeed(speedPct)
        acceleration = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_acceleration=acceleration)
        self.robot.drive(speed, 0)
        wait(millis)
        self.robot.brake()

    def waitForMillis(self, millis: int):
        """Wait for a specified number of milliseconds before continuing

        Snippet: wfm

        Example:
        >>> waitForMillis(1000) # wait for 1 second
        >>> waitForMillis(500)  # wait for half second

        Args:
        millis (REQUIRED integer): Number of milliseconds to wait. \
        1000 milliseconds = 1 second
        """
        wait(time=millis)

    def waitForForwardButton(
        self,
    ):
        """Pause program execution until the forward (LEFT) button is \
        pressed. This is typically used at the start of a mission to wait \
        for user confirmation before starting.

        Snippet: wfb

        Example:
        >>> waitForForwardButton() # wait for button press to continue

        Args:
        None

        """
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.LEFT in pressed:
                break
            wait(10)

    def waitForBackButton(
        self,
    ):
        """Pause program execution until the back (RIGHT) button is \
        pressed. This is typically used at the start of a mission to wait \
        for user confirmation before starting.

        Snippet: wbb

        Example:
        >>> waitForBackButton() # wait for button press to continue

        This is typically used at the start of a mission to wait for
        user confirmation before starting.
        """
        while True:
            pressed = self.hub.buttons.pressed()
            if Button.RIGHT in pressed:
                break
            wait(10)

    def turnInPlace(
        self,
        angle: int,
        speedPct: int = DEFAULT_TURN_SPEED_PCT,
        gyro: bool = True,
        waiting: bool = True,
        then: Stop = Stop.BRAKE,
        accelerationPct: int = DEFAULT_TURN_ACCEL_PCT,
    ):
        """Turn the robot in place by a specified angle

        Snippet: tip

        Example:
        >>> turnInPlace(90) # turn 90 degrees right
        >>> turnInPlace(-45) # turn 45 degrees left
        >>> turnInPlace(180, speedPct=30) # slow 180 degree turn

        Args:

        angle (REQUIRED integer): How many degrees to turn. \
            Positive numbers turn right, negative numbers turn left.

        speedPct: (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the robot will turn. Positive numbers turn the robot to the right; \
        negative numbers turn it to the left. Default is DEFAULT_TURN_SPEED_PCT.

        gyro: (OPTIONAL bool): Use the gyro. Defaults to True. Rarely set to \
        False only when you do not want to use the gyro for some reason

        waiting: (OPTIONAL bool): this tells the robot if it should wait for \
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        then: (OPTIONAL, Stop.HOLD|Stop.BRAKE|Stop.NONE|Stop.COAST): What the \
        drive motors will do after the robot has turned in place. \
        Stop.BRAKE (Default), Passively resist small external forces. \
        Stop.HOLD, Keep controlling the motor to hold it at the commanded \
        angle. \
        Stop.COAST, Allow the motor to coast freely until it stops. \
        Stop.NONE, Do not control the motor at all (use when chaining drive \
            commands).

        accelerationPct: (OPTIONAL int > 0) How fast the robot accelerates
        """
        speed = RescaleTurnSpeed(speedPct)
        acceleration = RescaleTurnAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(
            straight_acceleration=acceleration, straight_speed=speed
        )
        self.robot.turn(angle, then, waiting)

    def curve(
        self,
        radius: int,
        angle: int,
        speedPct: int = DEFAULT_BIG_MOT_SPEED_PCT,
        then: Stop = Stop.BRAKE,
        waiting: bool = True,
        gyro: bool = True,
        accelerationPct: int = DEFAULT_TURN_ACCEL_PCT,
    ):
        """Drive the robot in a curve, given the radius and angle

        Snippet: cur

        Example:

        >>> curve(radius= 350, angle= 60 ↱) # curve forward to the right
        >>> curve(radius=-350, angle= 60 ↰) # curve forward to the left
        >>> curve(radius= 350, angle=-60 ↳) # curve backward to the right
        >>> curve(radius=-350, angle=-60 ↲) # curve backward to the left

        Args:

        radius (REQUIRED, integer): How tight of a curve. POS = Forward; \
        NEG = Reverse

        angle (REQUIRED, integer): Number of degrees to drive along the curve. \
        POS = right; NEG = left

        speedPct (OPTIONAL, integer > 0): How fast to drive. Defaults to \
        DEFAULT_BIG_MOT_SPEED_PCT.

        then: (OPTIONAL, Stop.HOLD|Stop.BRAKE|Stop.NONE|Stop.COAST): What the \
        drive motors will do after the robot has turned in place. \
        Stop.BRAKE (Default), Passively resist small external forces. \
        Stop.HOLD, Keep controlling the motor to hold it at the commanded \
        angle. \
        Stop.COAST, Allow the motor to coast freely until it stops. \
        Stop.NONE, Do not control the motor at all (use when chaining drive \
            commands).

        waiting: (OPTIONAL bool): this tells the robot if it should wait for \
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        gyro (bool, optional): Use the gyro. Defaults to True.

        accelerationPct: (OPTIONAL int > 0) How fast the robot accelerates

        """
        speed = RescaleStraightSpeed(speedPct)
        acceleration = RescaleTurnAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(
            straight_acceleration=acceleration, straight_speed=speed
        )
        self.robot.arc(radius=radius, angle=angle, then=then, wait=waiting)

    def driveArcDist(
        self,
        radius: int,
        dist: int,
        speedPct: int = DEFAULT_BIG_MOT_SPEED_PCT,
        accelerationPct: int = DEFAULT_BIG_MOT_ACCEL_PCT,  # Changed from accelPct
        gyro: bool = True,
        then: Stop = Stop.BRAKE,
        waiting: bool = True,
    ):
        """Drive the robot in an arc for a specified distance and radius

        Snippet: dad

        Example:
        >>> driveArcDist(radius=350, dist=-60 ↰) # curve forward to the left
        >>> driveArcDist(radius=350, dist=60 ↱) # curve forward to the right
        >>> driveArcDist(radius=-350, dist=-60 ↲) # curve backward to the left
        >>> driveArcDist(radius=-350, dist=60 ↳) # curve backward to the right

        Args:
        
        radius (REQUIRED integer): Radius of the arc in mm. \
        Positive = forward arc, negative = backward arc.

        dist (REQUIRED integer): Distance to drive along the arc in mm.

        speedPct: (OPTIONAL integer, -100 to 100, except 0): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.

        then: (OPTIONAL, Stop.HOLD|Stop.BRAKE|Stop.NONE|Stop.COAST): What the \
        drive motors will do after the robot has driven the distance. \
        Stop.BRAKE, Passively resist small external forces. \
        Stop.HOLD, Keep controlling the motor to hold it at the commanded \
        angle. \
        Stop.COAST, Allow the motor to coast freely until it stops. \
        Stop.NONE, Do not control the motor at all (use when chaining drive \
            commands).

        waiting: (OPTIONAL bool): this tells the robot if it should wait for \
        the next line of code or run both lines of code at the same time. \
        Default is True, which means wait on this line until it is \
        complete.

        gyro: (OPTIONAL bool): Use the gyro. Defaults to True. Set to False \
        when you do not want to use the gyro such as when you are wall \
        following.

        accelerationPct: (OPTIONAL int > 0) How fast the robot accelerates
        """
        speed = RescaleStraightSpeed(speedPct)
        accel = RescaleStraightAccel(accelerationPct)
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_speed=speed, straight_acceleration=accel)
        self.robot.arc(radius=radius, distance=dist, then=then, wait=waiting)


# This BaseRobot class file is not meant to be run like the mission files.
# But if someone does try (accidentally probably) to run it, show this
# error message.
if __name__ == "__main__":
    print("Don't run the BaseRobot class file. Nothing to do here.")
    print("You probably meant to run one of the mission files.")
