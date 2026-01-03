# FLL Fall 2025 - Unearthed 🏆

![FLL Team 24277](https://img.shields.io/badge/FLL%20Team-24277-orange)
![Season](https://img.shields.io/badge/Season-2025%20Unearthed-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/FLL-Team-24277/FLL-Fall-2025-Unearthed)
![GitHub contributors](https://img.shields.io/github/contributors/FLL-Team-24277/FLL-Fall-2025-Unearthed)
![GitHub license](https://img.shields.io/github/license/FLL-Team-24277/FLL-Fall-2025-Unearthed)

# Fall-2025-Unearthed, FLL Team 24277
Pybricks, VS Code setup, base robot, missions, and materials for the Fall 2025 FLL Season "Unearthed".

##  Introduction

We are not "giving away solutions" here. If you are looking for mission solutions, you'll just have to figure them out yourself :) [Read our statement on the FLL "Discovery" core value here.](https://github.com/FLL-Team-24277/FLL-Fall-2025-Unearthed/blob/main/help/github/discovery.md)

The instructions below will get team members up and running for FLL in a team collaboration environment using [pybricks libraries](https://github.com/pybricks), writing programs with Visual Studio Code, and using git/github for version control. The instructions are not perfect, and you will probably have some troubleshooting and adjustments along the way.

Very helpful page here about how to use pybricks with VS Code: https://pybricks.com/projects/tutorials/dev/tools/vscode/. Github link: https://github.com/pybricks/pybricks-micropython

## Instructions

Detailed instructions are [here](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial), but this is a quick summary

1. Install [necessary software](https://github.com/FLL-Team-24277/FLL-Fall-2025-Unearthed/blob/main/help/config/Software.md).
2. Each team member creates their own github account. REMINDER: Be sure to use an email account that they can check at school (github emails may be blocked). They will also have to set up two-factor authentication. Also recommend that the team member keep that github page open and logged in while completing these instructions because you will need it for authentication in step 9 below. Remind them to not forget their password or how they use 2FA!
3. Add each account as a collaborator for this project [here](https://github.com/FLL-Team-24277/FLL-Fall-2025-Unearthed/settings/access). Instructions [here](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository). The team member will need to confirm and accept the invitation. At that point they can push updates to the project.
4. Clone the season Repository. Clone this repository: [https://github.com/FLL-Team-24277/Fall-2025-Unearthed.git](https://github.com/FLL-Team-24277/FLL-Fall-2025-Unearthed.git) Save it somewhere on their computer.
5. Add a python virtual environment. Open a new terminal in the project folder and run `uv sync`, then make sure the environment is selected (look in the lower right corner). If there are executionPolicy errors, you will need to elevate the permissions for Powershell. Instructions [here](https://tecadmin.net/powershell-running-scripts-is-disabled-system/) (copied [here](https://github.com/FLL-Team-24277/FLL-Fall-2025-Unearthed/blob/main/help/config/executionPolicyError.md)), but basically just run `Set-ExecutionPolicy RemoteSigned` in an Administrative PowerShell. Keep the admin PowerShell running because you will need it later on.
6. Create a new python file, named `teamMemberName-test-mission.py`, copy and paste the code below, and save it, but don't try to run it just yet. Wait for the final step below. Note that after saving the file, the python Black Formatter should correct the "incorrect" spacing around the equals signs and commas.
7. Commit the changes, and push. It will probably prompt for github registration/login and then sync all files. This link may help: https://pages.nist.gov/git-novice-MSE/08-collab/. It may also ask you to set your git username and email. Open a terminal and run these two commands to set your username and email `git config --global user.name "FIRST_NAME LAST_NAME"`; and `git config --global user.email "MY_NAME@example.com"`
8. Install pybricks on each robot at https://pybricks.com/. If the computer has never connected to a pybricks hub, you will probably need to manually install the USB drivers, which will require the use of the windows Device Manager. To run device manager as an admin, run a powershell as an administrator, then type devmgmt.msc. Then complete the usual steps. Name the robot at this time. Avoid spaces and special characters in the robot name. Put a label sticker on the top of the robot with the robot name.
9. Create a user variable for the robot name. Set the variable `fllRobotName` to the name of the robot in the user's settings.json. The easy way to do this is to click on the fllRobotName button on the status bar. This should allow the keyboard binding and tasks to recognize the robot by name.
10. **RUN OUR PROGRAM!** Turn the robot on and ensure the keyboard shortcut `Ctrl-L` runs the command, which should also run their program. Also, `Ctrl-Shift-P` > `Tasks: Run task` should pop up a menu with the correct entry. Watch the terminal and make sure the robot name is correct. If not, recheck that you completed the previous step correctly and that you restarted VS Code.

## Example code for test program

~~~python
from base_robot import *

# Copy this text into a new mission file. Name it something like
# myname.py. You can name it pretty much anything, but don't use
# any spaces or punctuation, other than _ and -. The name MUST
# end with .py
#
# Weird spacing in the code below is intentional. It should be
# corrected automatically by the Black formatter if it is working
# correctly.
#
# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.
# Please delete all of these comments, and consider writing your
# own here.

# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run ( br: BaseRobot ) :  
    #   Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    br.driveForDistance(distance=250)     #    Drive distance
    br.turnInPlace( angle  = 90  )
    br.moveLeftAttachmentMotorForDegrees(degrees=-720)
    br.waitForForwardButton  ()
    br.moveRightAttachmentMotorForMillis(millis=1500)
    br.waitForMillis(millis=1000)
    br.moveLeftAttachmentMotorUntilStalled(stallPct=100)
    br.curve(radius=350, angle=70)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
~~~
