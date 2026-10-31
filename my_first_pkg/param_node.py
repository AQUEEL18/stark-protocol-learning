import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ParamNode(Node):

    def __init__(self):
        super().__init__('param_node')
        self.declare_parameter('message', 'Hello from Aqueel')
        self.declare_parameter('rate_hz', 1.0)

        rate = self.get_parameter('rate_hz').value
        self.publisher = self.create_publisher(String, 'my_topic', 10)
        self.timer = self.create_timer(1.0 / rate, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        text = self.get_parameter('message').value
        msg.data = f'{text} - count: {self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = ParamNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()