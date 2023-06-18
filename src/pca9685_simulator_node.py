import rospy
from std_msgs.msg import Int32MultiArray
from random import randint

def pwm_publisher():
    rospy.init_node("pwm_test_publisher", anonymous=True)
    pub = rospy.Publisher("pwm_control_topic", Int32MultiArray, queue_size=10)
    rate = rospy.Rate(1)  # Publish at 1Hz (1 message per second)

    while not rospy.is_shutdown():
        data = Int32MultiArray()
        data.data = [randint(0, 4095) for _ in range(16)]  # Generate random numbers between 0 and 4095

        pub.publish(data)
        rospy.loginfo("Published pwm: %s", data.data)

        rate.sleep()

if __name__ == '__main__':
    try:
        pwm_publisher()
    except rospy.ROSInterruptException:
        pass
