# !/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

class Test():
    def __init__(self):
        self.val=[]

    def callback(self,data):
        self.val=data.ranges

    def listener(self):
        rospy.init_node('get_laser_data')
        rospy.Subscriber('/front/scan',LaserScan,self.callback)
        rospy.spin()

    def shutdown(self):
        rospy.loginfo('Size:{}'.format(len(self.val)))
        # rospy.loginfo(self.val)
        
if __name__ =='__main__':
    T=Test()
    T.listener()
    rospy.on_shutdown(T.shutdown)
