# USB-RS485-Modbus

USB RS485 Hex Modbus 温湿度传感器 采集

## 设备

1. 温湿度传感器
2. USB 转 RS-485 转接器
3. 驱动 [CP210x USB 至 UART 桥 VCP 驱动器](https://cn.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

## Example

```bash
$ python main.py
Serial<id=0x10f711b80, open=True>(port='/dev/tty.usbserial-0001', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False)
/dev/tty.usbserial-0001 port open : True
Send String is  01040000000271CB
9
response: b'\x01\x04\x04\x01\x0c\x01\xa3{\x92'
response 16 binary : b'010404010c01a37b92'
Return Str Length is : 18
Result 16 binary :  010c 01a3
Result 10 binary :  26.8 41.9
```

## 协议

![image](https://user-images.githubusercontent.com/16016074/117657097-bf3f3480-b1cb-11eb-989c-3d38669b3ae3.png)
