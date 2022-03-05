import socket

# Port Configuration and port list
port_min = 0
port_max = 1000
open_ports = []

# Get IP to scan
target_ip = input("Enter IP to scan: ")

# Basic port scan, open ports will be added to the open ports list
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)  # Allows time for connections, slightly more accurate with this.
            s.connect((target_ip, port))
            open_ports.append(port)
    except:
        pass

# Print out open ports only
for port in open_ports:
    print(f"Port {port} is open on {target_ip}.")
    