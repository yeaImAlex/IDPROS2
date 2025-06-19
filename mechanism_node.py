import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from object_following_ros2.utils.shovel import ShovelServo
from object_following_ros2.utils.ConveyorBelt import ConveyorBelt
from time import sleep

class MechanismNode(Node):
    def __init__(self):
        super().__init__('mechanism_node')
        self.shovel = ShovelServo()
        self.conveyor = ConveyorBelt()
        self.create_subscription(String, 'mechanism_command', self.callback, 10)

    def callback(self, msg):
        if msg.data.strip() == "activate":
            self.shovel.set_angle(150)
            self.conveyor.turn_on()
            sleep(2)
            self.shovel.set_angle(0)
            self.conveyor.turn_off()

def main():
    rclpy.init()
    rclpy.spin(MechanismNode())
    rclpy.shutdown()
