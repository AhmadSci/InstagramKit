try:
    import requests
    import uuid
    import random
    import time
    import os
    from os import system
    system("title " + "@c9zd - UserChecker V1")
    import colorama
    from colorama import Fore , Back
    colorama.init(autoreset=True)
    
except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()
    
print("""
                                                                       .  
░█─░█ █▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▄▀█ █▀▀  ░█▀▀█ █──█ █▀▀ █▀▀ █─█ █▀▀ █▀▀█   
░█─░█ ▀▀█ █▀▀ █▄▄▀ █──█ █▄▄█ █─▀─█ █▀▀  ░█─── █▀▀█ █▀▀ █── █▀▄ █▀▀ █▄▄▀   
─▀▄▄▀ ▀▀▀ ▀▀▀ ▀─▀▀ ▀──▀ ▀──▀ ▀───▀ ▀▀▀  ░█▄▄█ ▀──▀ ▀▀▀ ▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀   
                                                                          """, 
Fore.WHITE + "                                                 Credit @c9zd")
print(Fore.GREEN + "14-Day + Availability Checker By A7mad,", Fore.RED+"Free And Not For Sale\n")

#random characters
rnd = "abcdefghijklmnopqrwstuvwxyz1234567890" 

while 1: #User Chooses the file conotaining the Usernames to check
    try:
        file = input("File Containing Usernames: ")
        if ".txt" not in file:
            ggg = open(file+".txt", "r")
            break
        elif ".txt" in file:
            ggg = open(file, "r")
            break
    except FileNotFoundError:
        print("File Not Found Try Again.")


while 1: #Main Loop


#random inputs for the API
    email = random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+"@gmail.com"
    password = random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)+random.choice(rnd)
#random inputs for the API


#reading each username from the file
    username = ggg.readline().split("\n")[0] 

#to exit when there are no more usernames
    if username == "":
        print("Done Checking\nClick Enter To Exit")
        input()
        exit()
    uid = str(uuid.uuid4())
        
    
    url = "https://i.instagram.com/api/v1/accounts/create_validated/" #API link
        
#Headers
    hd_login = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com'
    }

#Input Data
    data = {
        "device_id": uid,
        "uuid": uid,
        "email": email,
        "password": password,
        "_csrftoken": "missing",
        "firt_name": "Soud",
        "username": username
    }
#Calling request function with the given data
    req = requests.post(url, data=data, headers=hd_login)
        
#Checker
    if "username_held_by_others" in req.text: #checks if the username is held ny other users
        print(Fore.CYAN+f"14 Day!! >> @{username}")
        #print(req.text)
        with open("14-Day.txt", "a") as dd:
            dd.write(f"{username}\n")
        
    elif "username_is_taken" in req.text: #checks if the username is completely taken
        print(Fore.RED+f"Taken >> @{username}")
        #print(req.text)
        with open("Not 14-Day.txt", "a") as dd:
            dd.write(f"{username}\n")
            
    elif "username_has_special_char" in req.text or "username_only_has_number" in req.text: #checks for any other errors
        print(Fore.RED+f"Error >>  @{username}")
        #print(req.text)
    
    elif "Another account is using" in req.text: #checks if the random email belongs to anyone
        print(Fore.RED+f"Email Taken >>  @{username}")
        print(req.text)

    elif "Please wait a few minutes" in req.text: #checks weather you've been blocked or not
        print(Fore.RED+f"Error >>  @{username}")
        print(req.text)
        print(Fore.RED + f"You've Been Blocked for Today.")
        print(Fore.RED + f"Exiting in 3 Seconds.")
        time.sleep(3)
        break
        
    else: #any other eroor means the username is available
        print(Fore.GREEN+f"Available >> @{username}")
        print(req.text)
        with open("Available-Not 14-Day.txt", "a") as dd:
            dd.write(f"{username}\n")
            
    time.sleep(5)