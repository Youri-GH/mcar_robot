import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class SlaveNode(Node):
    def __init__(self):
        super().__init__('slave')
        self.pose_subscriber = self.create_subscription(
            Pose, '/turtle1/pose', self.master_pose_callback, 10)
        self.cmd_publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.master_pose = None

    def master_pose_callback(self, pose):
        self.master_pose = pose
        self.follow_master()

    def follow_master(self):
        if self.master_pose is None:
            return

        msg = Twist()
        # Suivre en ligne droite vers la position maître
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.cmd_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SlaveNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
