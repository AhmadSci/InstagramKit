import random
import string
from os import system
system("title " + "@0c9zd - UserGen")
import time

print("""

▒█░▒█ █▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▄▀█ █▀▀ 　 ▒█░░░ ░▀░ █▀▀ ▀▀█▀▀ 　 ▒█▀▄▀█ █▀▀█ █░█ █▀▀ █▀▀█ 
▒█░▒█ ▀▀█ █▀▀ █▄▄▀ █░░█ █▄▄█ █░▀░█ █▀▀ 　 ▒█░░░ ▀█▀ ▀▀█ ░░█░░ 　 ▒█▒█▒█ █▄▄█ █▀▄ █▀▀ █▄▄▀ 
░▀▄▄▀ ▀▀▀ ▀▀▀ ▀░▀▀ ▀░░▀ ▀░░▀ ▀░░░▀ ▀▀▀ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ░░▀░░ 　 ▒█░░▒█ ▀░░▀ ▀░▀ ▀▀▀ ▀░▀▀
""")
print("""
Cᴏᴅᴇᴅ Bʏ Aʜᴍᴇᴅ Iɴsᴛᴀ: @c9zd
""")
while 1:
    try:
        user_len = int(input("User Length: ")) #variable input from user to know the length of the username
    except:
        print("Input Must Be Numerical!?")
        continue
    else:
        break

if user_len == 2:
    num_q = input("Want Numbers in user? "+ "(y/n) ").lower()
    thing_q = input("Want \"_\" in user? "+ "(y/n) ").lower()
    name_of_folder = input("File Name: ")
else :
    num_q = input("Want Numbers in user? "+ "(y/n) ").lower()
    thing_q = input("Want Punctuations in user? "+ "(y/n) ").lower()
    name_of_folder = input("File Name: ")


while 1:
    try:
        user_count = int(input("Number of Users: "))/4 #another variablr input to know how many useres he wants to generate
    except:
        print("Input Must Be Numerical!?")
        continue
    else:
        break

things = "._"
things_2 = "_"
if ".txt" in name_of_folder:
    folder = open(name_of_folder, "w+")
else:
    folder = open(name_of_folder+ ".txt", "w+")

def all_gen():
    for user in range(user_len):
            le = 1
            while le <= user_count:
                user = string.ascii_lowercase + string.digits + random.choice(things)
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
                le += 1
    folder.close()
    print("Done!")

def user_only_gen():
    for user in range(user_len):
            le = 1
            while le <= user_count:
                user = string.ascii_lowercase
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
                le += 1
    folder.close()
    print("Done!")

def twos_user___gen():
    for user in range(user_len):
            le = 1
            while le <= user_count:
                user = string.ascii_lowercase + things_2
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
                le += 1
    folder.close()
    print("Done!")

def user_num_gen():
    for user in range(user_len):
            le = 1
            while le <= user_count:
                user = string.ascii_lowercase + string.digits 
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
                le += 1
    folder.close()
    print("Done!")

def user_punc_gen():
    for user in range(user_len):
            le = 1
            while le <= user_count:
                user = string.ascii_lowercase  + random.choice(things)
                folder.write("".join(random.choice(user) for i in range(user_len)) + "\n")
                le += 1
    folder.close()
    print("Done!")

if user_len == 2:
    if num_q =="n" and thing_q == "n":
        user_only_gen()
    elif num_q == "y" and thing_q == "n":
        user_num_gen()
    elif num_q == "y" and thing_q == "y":
        all_gen()
    elif num_q == "n" and thing_q == "y":
        twos_user___gen()
else:
    if num_q =="n" and thing_q == "n":
        user_only_gen()
    elif num_q == "y" and thing_q == "n":
        user_num_gen()
    elif num_q == "y" and thing_q == "y":
        all_gen()
    elif num_q == "n" and thing_q == "y":
        user_punc_gen()

while 1:
    clean = input("want to clean up the List? (y/n) ")
    if clean == "y" or "n" :
        break
    else:
        print("ONLY ENTER Y OR N")

cleaning = ".."
bad_word = "."
if ".txt" in name_of_folder:
    if clean == "y":
        with open(name_of_folder) as oldfile, open('CleanList.txt', 'w') as newfile:
            for line in oldfile:
                if not cleaning in line:
                    #newfile.write(line)
                    if not ("." in line.lstrip()[0]):
                        #newfile.write(line)
                        if not ("." in line.strip()[user_len-1]):
                            #newfile.write(line)
                            if not line.isdigit():
                                newfile.write(line)
        print("Cleaned!")

    else:
        print("")
else:
    if clean == "y":
        with open(name_of_folder+ ".txt") as oldfile, open('CleanList.txt', 'w') as newfile:
            for line in oldfile:
                if not cleaning in line:
                    #newfile.write(line)
                    if not ("." in line.lstrip()[0]):
                        #newfile.write(line)
                        if not ("." in line.strip()[user_len-1]):
                            #newfile.write(line)
                            if not line.isdigit():
                                newfile.write(line)
        print("Cleaned!")

    else:
        print("")
    

while 1:
    q = input("Want another list? "+ "(y/n) ").lower()
    if q == "y":
        while 1:
            try:
                user_len = int(input("User Length: ")) 
            except:
                print("Input Must Be Numerical!?")
                continue
            else:
                break
        if user_len == 2:
            num_q = input("Want Numbers in user? "+ "(y/n) ").lower()
            thing_q = input("Want \"_\" in user? "+ "(y/n) ").lower()
            name_of_folder = input("File Name: ")
        else :
            num_q = input("Want Numbers in user? "+ "(y/n) ").lower()
            thing_q = input("Want Punctuations in user? "+ "(y/n) ").lower()
            name_of_folder = input("File Name: ")
        while 1:
            try:
                user_count = int(input("Number of Users: "))/4
            except:
                print("Input Must Be Numerical!?")
                continue
            else:
                break
        if ".txt" in name_of_folder:
            folder = open(name_of_folder, "w+")
        else:
            folder = open(name_of_folder+ ".txt", "w+")
        if user_len == 2:
            if num_q =="n" and thing_q == "n":
                user_only_gen()
            elif num_q == "y" and thing_q == "n":
                user_num_gen()
            elif num_q == "y" and thing_q == "y":
                all_gen()
            elif num_q == "n" and thing_q == "y":
                twos_user___gen()
        else:
            if num_q =="n" and thing_q == "n":
                user_only_gen()
            elif num_q == "y" and thing_q == "n":
                user_num_gen()
            elif num_q == "y" and thing_q == "y":
                all_gen()
            elif num_q == "n" and thing_q == "y":
                user_punc_gen()
        while 1:
            clean = input("want to clean up the List? (y/n) ")
            if clean == "y" or "n" :
                break
            else:
                print("ONLY ENTER Y OR N")
        if ".txt" in name_of_folder:
            if clean == "y":
                with open(name_of_folder) as oldfile, open('CleanList.txt', 'w') as newfile:
                    for line in oldfile:
                        if not cleaning in line:
                            #newfile.write(line)
                            if not ("." in line.lstrip()[0]):
                                #newfile.write(line)
                                if not ("." in line.strip()[user_len-1]):
                                    #newfile.write(line)
                                    if not line.isdigit():
                                        newfile.write(line)
                print("Cleaned!")

            else:
                print("")
        else:
            if clean == "y":
                with open(name_of_folder+ ".txt") as oldfile, open('CleanList.txt', 'w') as newfile:
                    for line in oldfile:
                        if not cleaning in line:
                            #newfile.write(line)
                            if not ("." in line.lstrip()[0]):
                                #newfile.write(line)
                                if not ("." in line.strip()[user_len-1]):
                                    #newfile.write(line)
                                    if not line.isdigit():
                                        newfile.write(line)
                print("Cleaned!")

            else:
                print("")
    else:
        print("Closing in 3 Seconds")
        time.sleep(3)
        break
