import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MasterNode(Node):
    def __init__(self):
        super().__init__('master')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_turtle)

    def move_turtle(self):
        msg = Twist()
        msg.linear.x = 2.0  # Déplacement linéaire
        msg.angular.z = 1.0  # Rotation
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MasterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
