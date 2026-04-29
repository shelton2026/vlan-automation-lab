\# VLAN Automation Lab



\## Overview

This is my first network automation project using Python and Netmiko.



The script connects to a Cisco switch and automates VLAN creation and port assignment.



\---



\## What the script does

\- Creates VLAN 10 and VLAN 20

\- Assigns ports to VLANs

\- Verifies configuration



\---



\## Technologies

\- Python

\- Netmiko

\-PNET




\---



\## How to run

pip install -r requirements.txt  

python vlan\_automation.py

The following configuration was applied manually before running the automation script:

## 🔧 Switch Configuration (Manual Setup)

```cisco
conf t
hostname SW1

vlan 99
name MANAGEMENT

interface vlan 99
ip address 192.168.94.139 255.255.255.0
no shutdown

ip default-gateway 192.168.94.1

line vty 0 4
password bobby14
login
transport input telnet

enable secret bobby14

end
wr

\---



\## What I learned

\- Basics of network automation

\- Using Python to send commands to a switch

\- Troubleshooting connectivity issues

