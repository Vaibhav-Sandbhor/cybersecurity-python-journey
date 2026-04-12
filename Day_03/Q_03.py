status = "FAILED"
attempts = int(input("Enter the number of attempts: "))

if status == "FAILED" and attempts > 2:
    print("ALERT")
elif status == "FAILED":
    print("Try Again")
else:
    print("Login Successful")