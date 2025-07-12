import sys
import socket 
from datetime import datetime 
host= input("Enter a host to scan: ")
host_ip=socket.gethostbyname(host)
print(host)
print (host_ip)
start_port=20
end_port=1024
print(f"scanning ({host_ip})")
for port in range(start_port, end_port +1 ):
    try:
        print (f"\nchecking port {port}")
       
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
      
        result=s.connect_ex((host_ip, port))
        print(f"port {port} result: {result}")
        if result == 0:
            print(f"port {port} is OPEN")
            try: 
                banner= s.recv(1024).decode().strip()
                print(f"Banner: {banner}")
            except :
                print (" No banner recieved.")
        else: print(f"port {port}  is CLOSED")       
        s.close()
    except Exception as e:
        print(f"error checking port {port} : {e}")
end_time = datetime.now()
print (f"\nscan completed in : {end_time - start_time}")        
