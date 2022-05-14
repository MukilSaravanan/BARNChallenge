#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np

class Jackal():
    def __init__(self):
        rospy.init_node('rand_cmd_vel_pub')
        self.vt=[]
        self.zt=[]
        self.dataset=[0]*(720+3)

    def rand_cmd_vel_publisher(self):
        pub=rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist,queue_size=10)
        rate=rospy.Rate(10)

        while not rospy.is_shutdown():
            pass

    def collect_data(self):
        rospy.Subscriber('/front/scan',LaserScan,self.laser_scan_callback)
        rospy.Subscriber('/jackal_velocity_controller/cmd_vel',Twist,self.cmd_vel_callback)
        rospy.spin()

    def cmd_vel_callback(self,data):
        self.vt=data.linear.x,data.linear.y,data.angular.z
        self.dataset[720:723]=self.vt

    def laser_scan_callback(self,data):
        self.zt=list(data.ranges)
        self.dataset[0:720]=self.zt

    def shutdown(self):
        # rospy.loginfo('Size:{}'.format(len(self.dataset)))
        rospy.loginfo('Size:{}'.format(self.dataset))
        rospy.loginfo('Shutting down...')

if __name__=='__main__':
    try:
        J=Jackal()
        J.collect_data()
        rospy.on_shutdown(J.shutdown)
    except rospy.ROSInterruptException:
        pass
