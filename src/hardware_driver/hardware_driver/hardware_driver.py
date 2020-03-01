import rclpy
from rclpy.node import Node
from labyrinth_msgs.msg import Servo
from adafruit_servokit import ServoKit

class ServoDriver(Node):

    def __init__(self):
        super().__init__('servo_driver')
        self.subscriber = self.create_subscription(Servo, 'servos', self.servo_callback)
        self.kit = ServoKit(channels=16)
        self.theta0 = self.kit.servo[0]
        self.theta1 = self.kit.servo[1]

        self.max_pulse = 1900
        self.zero_pulse = 1500
        self.min_pulse = 1100

        self.theta0.set_pulse_width_range(self.min_pulse, self.max_pulse)
        self.theta1.set_pulse_width_range(self.min_pulse, self.max_pulse)

        self.theta0.angle = self.zero_pulse
        self.theta1.angle = self.zero_pulse

    def servo_callback(self, msg):
        self.set_pulse(self.theta0, msg.theta0)
        self.set_pulse(self.theta1, msg.theta1)

    def set_pulse(self, theta, pulse_ms):
        if pulse_ms > self.max_pulse:
            theta.angle = self.max_pulse
        elif pulse_ms < self.min_pulse:
            theta.angle = self.min_pulse
        else:
            theta.angle = pulse_ms


def main():

    rclpy.init()

    sd = ServoDriver()

    rclpy.spin(sd)

    sd.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
