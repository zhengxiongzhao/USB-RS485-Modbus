import serial
import time
import binascii


PORT='/dev/tty.usbserial-0001'
BAUDRATE = 9600
ser = serial.Serial(PORT, BAUDRATE, timeout=1)
print(ser)
print(PORT, 'port open :', ser.isOpen())


cmd_string= '01040000000271CB'

print('Send String is ', cmd_string)
send_string = bytearray.fromhex(cmd_string)
ser.write(send_string)

time.sleep(1)
count=ser.inWaiting()
print(count)


response = ser.readline()
print ("response:", response)

result = binascii.hexlify(bytearray(response))
print ("response 16 binary :", result)
print('Return Str Length is :', len(result))

result_list = bytearray(response)
print('Result 16 binary : ', result_list[3:5].hex(), result_list[5:7].hex() )
print('Result 10 binary : ', int(result_list[3:5].hex(), 16) / 10
    ,  int(result_list[5:7].hex(), 16) / 10  )
