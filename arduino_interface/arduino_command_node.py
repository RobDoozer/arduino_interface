import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import serial

class ArduinoCommandNode(Node):
    def __init__(self):
        super().__init__('arduino_command_node')
        try:
            self.ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
            self.get_logger().info('Serielle Verbindung geöffnet.')
        except serial.SerialException as e:
            self.get_logger().error(f'Konnte serielle Verbindung nicht öffnen: {e}')
            rclpy.shutdown()
            return

        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/freigegebener_fahrbefehl',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        if len(msg.data) < 2:
            self.get_logger().warn('Ungültige Daten empfangen.')
            return

        forward = msg.data[0]
        rotate = msg.data[1]

        # Kommando-String für Arduino
        serial_command = f'CMD,{forward:.2f},{rotate:.2f}\r\n'
        try:
            self.ser.write(serial_command.encode('utf-8'))
            self.get_logger().info(f'An Arduino gesendet: {serial_command.strip()}')
        except Exception as e:
            self.get_logger().error(f'Senden fehlgeschlagen: {e}')

        # Antwort vom Arduino lesen
        if self.ser.in_waiting > 0:
            try:
                response = self.ser.readline().decode('utf-8', errors='ignore').strip()
                self.get_logger().info(f'Arduino Antwort: {response}')
            except Exception as e:
                self.get_logger().warn(f'Fehler beim Lesen der Antwort: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = ArduinoCommandNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Beendet durch Benutzer.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

