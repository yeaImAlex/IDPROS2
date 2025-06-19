#Pi
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from object_following_ros2.utils.Locomotion import MotorControl

class MotorNode(Node):
    def __init__(self):
        super().__init__('motor_node')
        self.motor = MotorControl()
        self.create_subscription(String, 'motor_command', self.callback, 10)
        self.timer = self.create_timer(0.1, self.update)

    def callback(self, msg):
        cmd = msg.data.strip()
        if cmd == "forward":
            self.motor.move_forward(0.7)
        elif cmd == "left":
            self.motor.turn_left(0.6)
        elif cmd == "right":
            self.motor.turn_right(0.6)
        else:
            self.motor.stop_motor()

    def update(self):
        self.motor.ramp_to_target()

def main():
    rclpy.init()
    rclpy.spin(MotorNode())
    rclpy.shutdown()
