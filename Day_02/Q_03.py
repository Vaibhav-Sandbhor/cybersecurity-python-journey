ports=[21,22,23,80,443]
for port in ports:
    if port in [21,22]:
        print(f"Risky: {port}")
    