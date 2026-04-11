name = "Vaibhav"
age = 21
favorite_tool = "nmap"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Tool: {favorite_tool}")

ip1 = "192.168.1.1"
port1 = 80
status1 = "OPEN"

print(f"[INFO] IP: {ip1} | Port: {port1} | Status: {status1}")

ip2 = "192.168.1.10"
port2 = 22
status2 = "FAILED"

print(f"[ALERT] IP: {ip2} | Port: {port2} | Status: {status2}")

if port2 == 22:
    print("SSH Port Detected")

if status2 == "FAILED":
    print("Alert")