def check_port(port):
    if port == 21:
        return "Risky (FTP)"
    elif port in [22, 80]:
        return "Medium (SSH/HTTP)"
    elif port == 443:
        return "Safe (HTTPS)"
    else:
        return "Unknown"

port = int(input("Enter port number: "))
result = check_port(port)

print(f"{port} is {result}")