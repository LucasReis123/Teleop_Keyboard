import sys
import tty
import termios
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class KeyboardTeleop(Node):
    def __init__(self):
        super().__init__('keyboard_teleop')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist_msg = Twist()
        self.timer_ = self.create_timer(0.5, self.on_key_press)
        self.get_logger().info('Keyboard teleop node initialized.')
        self.inicia()

    def inicia(self):
        self.twist_msg.linear.z = 0.0
        self.twist_msg.linear.x = 0.0
        self.twist_msg.linear.y = 0.0
        self.twist_msg.angular.z = 0.0
        self.twist_msg.angular.x = 0.0
        self.twist_msg.angular.y = 0.0

    def on_key_press(self):
        settings = termios.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

        if key == 'a':
            self.twist_msg.linear.x += 2.0
        elif key == 'w':
            self.twist_msg.linear.y += 2.0
        elif key == 'd':
            self.twist_msg.linear.x += -2.0
        elif key == 's':
            self.twist_msg.linear.y += -2.0
        elif key == 'm':
            self.twist_msg.angular.z += 2.0
        elif key == 'q':
            self.inicia()

        self.publisher_.publish(self.twist_msg)


def main(args=None):
    rclpy.init(args=args)
    keyboard_teleop = KeyboardTeleop()
    rclpy.spin(keyboard_teleop)
    keyboard_teleop.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()