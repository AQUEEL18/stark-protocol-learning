import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddClient(Node):

    def __init__(self):
        super().__init__('add_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the server...')

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node = AddClient()
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    result = node.send_request(a, b)
    node.get_logger().info(f'Result: {a} + {b} = {result.sum}')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()