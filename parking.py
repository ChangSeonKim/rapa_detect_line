import rospy
from geometry_msgs.msg import Twist
from rospy.topics import Publisher
from sensor_msgs.msg import LaserScan
import numpy as np
import math
# import math
cmd_vel = Twist()
def main():
    
    pub = rospy.Publisher('cmd_vel',Twist ,queue_size=10)
    relative_angle = math.radians(90) #목표각도
    angluar_speed = 1.0       #미는 힘
    duration = relative_angle / angluar_speed
    time2end = rospy.Time.now() +rospy.Duration(duration)
    
    cmd_vel.angular.z = angluar_speed
    while rospy.Time.now() < time2end:
        #pub.publish(cmd_vel)
        #rospy.sleep(0.01)
    # cmd_vel.angular.z = 0.0 #stop
        pass
def callback(data):
    laser_range=data.ranges[0:10] # 레이더릐 정면 부분
    laser_arr=np.array(laser_range)
    foward_detect=np.count_nonzero(laser_arr>=0.3)
    # laser_range2=data.ranges[175:185]
    #print('laser_range : ',laser_range)
    
    
    if foward_detect >0:
        print("move")
        cmd_vel.linear.x=0.1
    else:
        print('angle')
        #cmd_vel.linear.x=0.0
        relative_angle = math.radians(90) #목표각도
        angluar_speed = 1.0       #미는 힘
        duration = relative_angle / angluar_speed
        time2end = rospy.Time.now() +rospy.Duration(duration)
        while rospy.Time.now() < time2end:
        
            cmd_vel.angular.z = angluar_speed
            
    pub.publish(cmd_vel)
    
    pass
if __name__ == '__main__':
    rospy.init_node('parking')
    rospy.Subscriber('/scan',LaserScan,callback)
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    rospy.spin()


   
