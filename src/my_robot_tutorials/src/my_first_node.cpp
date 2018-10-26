#include <ros/ros.h>

int main(int argc, char ** argv)
{
	ros::init(argc, argv, "my_first_cpp_node");
	ros::NodeHandle nh;
	ROS_INFO("Node has been started");

	ros::Rate rate(10);// 10 Hz

	while (ros::ok())
	{
		ROS_INFO("Hello");
		rate.sleep();// attempts to complete each loop in 0.1 seconds
	}
}


/* 
...make sure to Declare C++ Executable in:

~/catkin_ws/src/my_robot_tutorials/CMakeList.txt

(...look under the "BUILD" heading)
*/


