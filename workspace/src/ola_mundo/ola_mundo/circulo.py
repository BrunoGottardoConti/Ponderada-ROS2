import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class Turtlebot(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1/50, self.move_circle)  # 50Hz
        self.linear_speed = 2 * math.pi * 1 * 2  # f * r
        self.angular_speed = 2 * math.pi * 1

    def move_circle(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.linear_speed
        vel_msg.angular.z = self.angular_speed
        self.publisher.publish(vel_msg)

def main():
    rclpy.init()
    turtlebot = Turtlebot()
    try:
        rclpy.spin(turtlebot)
    except KeyboardInterrupt:
        pass
    finally:
        turtlebot.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

