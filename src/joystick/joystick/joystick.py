import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from labyrinth_msgs.msg import Servo

class ServoPublisher(Node):

    def __init__(self):
        super().__init__('servo_joystick')
        self.x = 0
        self.y = 0
        self.X_SCALE = 400
        self.Y_SCALE = 400
        self.pub_rate_hz = 50
        self.subscriber = self.create_subscription(Joy, 'joy', self.joystick_callback, 1)
        self.publisher = self.create_publisher(Servo, 'servos', 1)
        self.pub_timer = self.create_timer(1 / self.pub_rate_hz, self.publish_timer_callback)

    def joystick_callback(self, msg):
        self.x = msg.axes[0]
        self.y = msg.axes[1]

    def publish_timer_callback(self):
        servo = Servo()
        servo.theta0 = (int)(self.x * self.X_SCALE) + 1500
        servo.theta1 = (int)(self.y * self.Y_SCALE) + 1500
        self.publisher.publish(servo)

def main():
    rclpy.init()

    sp = ServoPublisher()

    rclpy.spin(sp)

    sp.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
