# arduino_interface
Schnittstelle zwischen ROS und Arduino (die aktuelle Version 
Anleitung:
1. pyserial Bibliothek installieren(falls nicht vorhanden):
   sudo apt update
   sudo apt install python3-pip
2. Workspace wechseln:
  cd ~/ros2_ws/src
3. Paket bauen:
  colcon build
4. sourcen
5. andere Nodes wie Entscheidungs Bridge und Controller zu ROS starten (dienen als Input)
6. USB Kabel an den Arduino anschließen
7. Node starten mit "ros2 run arduino_interface arduino_command_node"

   falls dieser Fehler kommt (der kommt sehr häufig):
   [ERROR] [1750179025.253228456] [arduino_command_node]: Konnte serielle Verbindung nicht öffnen: [Errno 2] could not open port /dev/ttyUSB1: [Errno 2] No such file or directory: '/dev/ttyUSB1'

-> USB Kabel aus und wieder einstecken und sofort darauf "sudo chmode 666 /dev/ttyUSB1" eingeben
  (am besten Befehl vor aus/einstecken eingeben sodass man nur auf Enter gehen muss)
