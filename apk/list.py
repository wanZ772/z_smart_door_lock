import serial.tools.list_ports  # For listing available serial ports
import serial  # For serial communication


# List ports for user to select
a = serial.tools.list_ports.comports()
ports=[]
for w in a:
    ports.append((w.vid, w.device, w.serial_number))

ports.sort(key=lambda ports: ports[1])

print('\nDetected the following serial ports:')
i = 0
for w in ports:
    print('%d)\t%s\t(USB VID=%04X)\t Serial#:=%s' % (i, w[1], w[0] if (type(w[0]) is int) else 0, w[2]))
    i = i + 1
total_ports = i  # now i= total ports