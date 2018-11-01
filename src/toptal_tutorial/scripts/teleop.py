#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from functools import partial


def joy_callback(cmd_vel, data):
    cmd_vel.linear.x = data.axes[1]
    cmd_vel.angular.z = data.axes[0]


def main():
    rospy.init_node('teleop')

    cmd_vel = Twist()

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1000)
    rospy.Subscriber('joy', Joy, partial(joy_callback, cmd_vel))

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(cmd_vel)
        rate.sleep()


if __name__ == '__main__':
    main()