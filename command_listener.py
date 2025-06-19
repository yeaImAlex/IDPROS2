#Pi
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandListener(Node):
    def __init__(self):
        super().__init__('command_listener')
        self.motor_pub = self.create_publisher(String, 'motor_command', 10)
        self.mech_pub = self.create_publisher(String, 'mechanism_command', 10)
        self.create_subscription(String, 'robot_command', self.callback, 10)
        self.get_logger().info("CommandListener ready.")

    def callback(self, msg):
        cmd = msg.data.strip()
        if cmd == "collect":
            self.motor_pub.publish(String(data="stop"))
            self.mech_pub.publish(String(data="activate"))
        else:
            self.motor_pub.publish(String(data=cmd))

def main():
    rclpy.init()
    rclpy.spin(CommandListener())
    rclpy.shutdown()
