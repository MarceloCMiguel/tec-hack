import socket
import sys

if len(sys.argv) == 4:
    ip = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    print(f"Checking open ports from ip {ip} in range {start}-{end} ")
else:
    sys.exit("Number of args wrong, must have ip, start port and end port (the max end port is 65535)")
def find_open_ports(ip,start,end):
        max_ports = 65535
        for i in range(int(start),int(end)):
                a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                location = (ip, i)
                result_of_check = a_socket.connect_ex(location)
                if result_of_check == 0:
                        try:
                                service = socket.getservbyport(i, "tcp")
                                print(f"Service {service} running in port {i}")

                        except:
                                print(f"Error to check service in port {i}, but it`s open")
                a_socket.close()
find_open_ports(ip, start, end)
