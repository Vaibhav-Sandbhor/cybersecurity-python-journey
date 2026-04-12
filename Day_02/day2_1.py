names = ["Vaibhav", "Amit", "Rahul"]

for name in names:
    print(f"Hello: {name}")

ports = [22, 21, 443, 80]

for port in ports:
    print(f"Checking port: {port}")

    if port == 21:
        print(f"{port} - Risky")
    elif port in [22, 80]:
        print(f"{port} - Medium")
    elif port == 443:
        print(f"{port} - Safe")