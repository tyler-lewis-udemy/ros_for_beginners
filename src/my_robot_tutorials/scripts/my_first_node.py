#!/usr/bin/env python

import rospy

if __name__=='__main__':
	rospy.init_node('my_first_python_node')
	rospy.loginfo("This node has been started.")

	rate = rospy.Rate(10)# 10 Hz

	while not rospy.is_shutdown():
		rospy.loginfo("Hello")
		rate.sleep() # sleep for 0.1 seconds


		