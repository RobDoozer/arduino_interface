import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        self.publisher_ = self.create_publisher(String, 'serial_command', 10)
        self.get_logger().info('Gib einen Befehl ein (z. B. "PWM_LF,150"). Beenden mit Strg+C')

    def send_command(self):
        while rclpy.ok():
            try:
                cmd = input('Befehl: ')
                msg = String()
                msg.data = cmd.strip()
                self.publisher_.publish(msg)
                self.get_logger().info(f'Gesendet: "{msg.data}"')
            except (KeyboardInterrupt, EOFError):
                self.get_logger().info('Beendet.')
                break

def main(args=None):
    rclpy.init(args=args)
    node = CommandPublisher()
    node.send_command()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
