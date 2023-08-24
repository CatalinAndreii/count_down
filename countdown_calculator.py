import time
user = int(input("How many seconds? :"))

for i in range(user + 1):
    print(user)
    time.sleep(1)
    user -= 1

print("Happy birthday!")

