#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
#from std_msgs.msg import float64
from std_msgs.msg import Float64
from gpiozero import CPUTemperature


class TemperatureNode(Node):
  def __init__(self):
    super().__init__('temp_sensor')
    # create publisher
    self.temp = CPUTemperature()
    self.pub_temp = self.create_publisher(Float64 ,'rpi_temp', 10)
    time_period = 1
    self.timer = self.create_timer(time_period, self.publish_temp)
    

  def publish_temp(self):
    msg = Float64()
    msg.data = self.temp.temperature
    self.pub_temp.publish(msg)
    self.get_logger().info('Temperature: "%s"' % msg.data)

def main(args=None):
  rclpy.init(args=args)
  temp_sensor = TemperatureNode()
  rclpy.spin(temp_sensor)
  rclpy.shutdown()


if __name__ == '__main__':
	main()





