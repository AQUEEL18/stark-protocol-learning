import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

    def __init__(self):
        super().__init__('my_first_node')
        self.get_logger().info('Node is alive!')
        self.count = 0
        self.publisher = self.create_publisher(String, 'my_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello from Aqueel - count: {self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()