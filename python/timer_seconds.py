import time

def user_timer():
    user_time = int(input("Please enter where you want to start:"))

    for user_seconds in range(user_time,0,-1):
        print(    user_seconds , "seconds remaining")
        time.sleep(1)
    print("Time ended!")
    
user_timer()

repeat = input("Do you want to use timer again(Y/N)?")
if repeat.lower() == "y":
    user_timer()

print("Alright have a good time!")