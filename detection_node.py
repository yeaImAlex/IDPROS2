#laptop
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ultralytics import YOLO
import cv2

class DetectionNode(Node):
    def __init__(self):
        super().__init__('detection_node')
        self.publisher_ = self.create_publisher(String, 'robot_command', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

        self.model = YOLO("best.pt")  # Replace with your actual model path
        self.cap = cv2.VideoCapture(0)
        self.get_logger().info("DetectionNode initialized.")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        results = self.model(frame)
        detections = results[0].boxes

        command = "stop"
        for det in detections:
            xyxy = det.xyxy[0].cpu().numpy()
            conf = det.conf.item()
            if conf < 0.5:
                continue

            x1, y1, x2, y2 = map(int, xyxy[:4])
            center_x = (x1 + x2) // 2
            frame_w = frame.shape[1]
            deviation = center_x - frame_w // 2
            height = y2 - y1

            if height > 150:
                command = "collect"
            elif deviation > 40:
                command = "right"
            elif deviation < -40:
                command = "left"
            else:
                command = "forward"
            break

        self.publisher_.publish(String(data=command))

def main():
    rclpy.init()
    node = DetectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
