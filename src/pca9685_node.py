import rospy
from std_msgs.msg import Int32MultiArray
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio

pca = None

# Setup the PCA9685
def setup_pca():
    global pca
    i2c_bus = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c_bus)
    pca.frequency = 60

# Set the PWM channels to the values in the Int32MultiArray
# The Int32MultiArray should have 16 values
# Each value should be between 0 and 65535
# Values of -1 are kept the same as previous values
def set_pwm(data):
    channels = data.data
    for i in range(0, 16):
        if(channels[i] != -1):
            pca.channels[i].duty_cycle = channels[i]    
    rospy.loginfo("Set pwm: %s", channels)
        
def pwm_subscriber():
    rospy.init_node("pwm_control_node", anonymous=True)
    rospy.Subscriber("pwm_control_topic", Int32MultiArray, set_pwm)
    rospy.spin()

if __name__ == '__main__':
    try:
        setup_pca()
        pwm_subscriber()
    except rospy.ROSInterruptException:
        pass