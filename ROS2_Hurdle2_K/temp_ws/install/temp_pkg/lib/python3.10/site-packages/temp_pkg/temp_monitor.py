import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class TempMonitorNode(Node):
    def __init__(self):
        #Call super
        super().__init__('temp_monitor')
        # Create publishers, subscribers, services, etc
        self.temp_subscriber_ = self.create_subscription(Float64, 'rpi_temp', self.callback_temp, 10)
        self.get_logger().info('Temperature Monitor has been started')

    # Callback for the subscriber
    def callback_temp(self, msg):
        self.get_logger().info('Temperature: ' + str(msg.data)) 

def main(args=None):
    rclpy.init(args=args)
    temp_monitor = TempMonitorNode()
    rclpy.spin(temp_monitor)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
