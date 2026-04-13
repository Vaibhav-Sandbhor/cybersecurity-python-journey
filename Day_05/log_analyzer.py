failed_count = 0
ip_count = {}
threshold = 2

with open("c:/Python/Day_05/log.txt", "r") as file:
    for line in file:
        if "FAILED" in line:
            failed_count += 1
            print(line.strip())

            ip = line.split(" - ")[0]

            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

print("\nTotal Failed Attempts:", failed_count)

print("\nIP Attempt Count:")
for ip, count in ip_count.items():
    print(f"{ip} → {count}")

for ip, count in ip_count.items():
    if count > threshold:
        print(f"⚠️ ALERT: {ip} has {count} failed attempts")