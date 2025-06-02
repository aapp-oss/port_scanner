import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) #set time for quick scans

        try:
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
                open_ports.append(port)
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.error:
            print(f"Could not connect to {target}:{port}.")
        finally:
            s.close()

    return open_ports

if __name__ == "__main__":
    target = input("Enter the target IP address or hostname: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("End port: "))

    start_time = datetime.now()
    open_ports = scan_ports(target, start_port, end_port)
    end_time = datetime.now()

    print(f"\nScan completed in {end_time - start_time}.")
    print(f"Open ports: {open_ports if open_ports else 'None found.'}")

