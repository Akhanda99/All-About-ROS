#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def cpcontroller():
    rospy.init_node('velocity_publisher', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    for i in range(1,4):
        rate.sleep()

        speed= Twist()

        speed.linear.x=4.0
        speed.angular.z=0.0

        rospy.loginfo(speed)
        pub.publish(speed)
        rate.sleep()
        if i%2==0:
            speed.linear.x=0
            speed.angular.z=2.14
        else:
            speed.linear.x=0.0
            speed.angular.z=2.0

        rospy.loginfo(speed)
        pub.publish(speed)
        rate.sleep()


if __name__ == '__main__':
    try:
        cpcontroller()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")