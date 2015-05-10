import dynamixel
import sys
import time

serial = dynamixel.SerialStream(port=sys.argv[1],
                                baudrate=1000000,
                                timeout=1)
net = dynamixel.DynamixelNetwork(serial)

pan = dynamixel.Dynamixel(1, net)
net._dynamixel_map[1] = pan

tilt = dynamixel.Dynamixel(2, net)
net._dynamixel_map[2] = tilt

pan.torque_enable = True
tilt.torque_enable = True

pan.moving_speed = 100
tilt.moving_speed = 100

pan.goal_position = 512
tilt.goal_position = 512

net.synchronize()
