# Subnet Mask Calculator & Network Analyzer

## Objective
This project calculates subnet details such as network address, broadcast address, subnet mask, and usable hosts using an input IP address.

## Features
- Automatic classful subnet detection
- Network & broadcast address calculation
- First & last usable host
- Total and usable host count
- Binary representation of IP
- GUI version using Tkinter

## Technologies Used
- Python
- ipaddress module
- Tkinter

## Example Input
192.168.1.10

## Example Output
Subnet Mask: 255.255.255.0
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Usable Hosts: 254

## Project Structure
Subnet-Calculator/
│
├── subnet_calculator_classful.py
├── subnet_gui_classful.py
└── README.md

## Disclaimer
This project is for educational purposes only.