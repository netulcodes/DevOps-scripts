import socket

def scan_ports(host, ports):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            print(f"Port {port} is open")
        except:
            pass
        s.close()

scan_ports("127.0.0.1", range(20, 1024))
