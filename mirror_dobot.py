from pydobot import Dobot
import time

# TwinArm-AI physical robot mirroring program
# Leader: /dev/ttyACM0
# Follower: /dev/ttyACM1

leader = Dobot(port='/dev/ttyACM0')
follower = Dobot(port='/dev/ttyACM1')

print("Mirror started")

Y_OFFSET = -6   # adjust after calibration
FIXED_R = 0

while True:
    pose = leader.pose()

    x = pose[0]
    y = pose[1]
    z = pose[2]

    # Core mirroring logic is preserved exactly as requested
    follower.move_to(x, y + Y_OFFSET, z, FIXED_R, wait=False)

    time.sleep(0.05)
