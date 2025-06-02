# port_scanner
This is a simple Python-based port scanner designed to identify open TCP ports on a specified target. It takes a target IP or hostname and a port range, then attempts to connect to each port to determine if it is open.

----Features:
 
Accepts target IP or hostname input

Scans custom port ranges

Identifies open TCP ports using socket.connect_ex()

Includes timeout handling for fast scanning

Measures total scan duration

----Why I Built This
 
As part of my journey into cybersecurity, I created this tool to deepen my understanding of network scanning, port enumeration, and how attackers and defenders interact with services on a network. This project demonstrates my ability to:

Work with low-level networking concepts in Python

Use common security techniques in a legal, ethical lab environment

Build foundational tools used in real-world recon and pentesting workflows

----Learning Outcomes
 
By building this scanner from scratch, I’ve learned:

How TCP connections are initiated

The importance of ports in service discovery

How scanning plays a role in the reconnaissance phase of an attack or assessment

This script is meant for educational and ethical use only — useful for home labs, testing, and skill development.
