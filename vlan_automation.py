from netmiko import ConnectHandler
import time

switch = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.94.139",
    "username": "",
    "password": "bobby14",
    "secret": "",
    "fast_cli": False,
}

commands = [
    "enable",
    "bobby14",
    "conf t",

    "vlan 10",
    "name USERS",

    "vlan 20",
    "name SERVERS",

    "interface e0/1",
    "description PC1_USERS",
    "switchport mode access",
    "switchport access vlan 10",
    "no shutdown",

    "interface e0/2",
    "description PC2_SERVERS",
    "switchport mode access",
    "switchport access vlan 20",
    "no shutdown",

    "end",
    "wr",
]

conn = ConnectHandler(**switch)

for cmd in commands:
    conn.write_channel(cmd + "\n")
    time.sleep(1)
    print(conn.read_channel())

conn.write_channel("show vlan brief\n")
time.sleep(2)
print(conn.read_channel())

conn.disconnect()