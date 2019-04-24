import sys, os, socket

class Ssh_Util:

    def port_scan(self, remote_host_ip):
        def print_box(print_line):
            print("-" * 78)
            print(print_line)
            print("-" * 78)
        # Validate the IP of the remote host
        # remote_host_ip = "172.28.25.122"		

        # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
        try:
            from_port = 1
            to_port = 200
            print("Scanning Port range - {} to {}.".format(from_port, to_port))
            for port in range(from_port, to_port):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remote_host_ip, port))
                ssh = False
                http = False
                other_ports = False
                port_list = []
                if result == 0:
                    if port == 22:
                        print("\n\t\t\tPort {} - open for SSH!\n".format(port))
                        ssh = True
                        sock.close()
                    elif port == 80:
                         print("\n\t\t\tPort {} - open for HTTP!\n".format(port))
                         http = True
                         sock.close()
                    else:
                        print("\n\t\t\tPort {} - open!".format(port))
                        other_ports = True
                        port_list = [port]
                        sock.close()
                        print("\n\t\t\tThe connection to {} over Port {} has now been closed".format(remote_host_ip, port))
            # Printing the information to screen
            print_box("Scanning Completed for {}".format(remote_host_ip))
            print("\t\t\tSummary")
            if ssh:
                print("\tPort 22, Is open for SSH!")
            if http:
                print("\tPort 80, Is open for HTTP!")
            if other_ports:
                for item in port_list:
                    print("\tPort {} is Open.".format(item))
            if not other_ports:
                print("\tNo other Ports are available!")
                print("-" * 78)
    
        except socket.error:
            print("Couldn't connect to server")
            sys.exit()
                
                
def main():
 # Initialize the ssh object
    ssh_obj = Ssh_Util()
    print(" ")
    print(" ")
    print(" ")
    print("Scanning the Production Web Server")
    ssh_obj.port_scan("172.28.25.116")
    print(" ")
    print(" ")
    print(" ")
    print("Scanning the Production API Server")
    ssh_obj.port_scan("172.28.25.115")

main()