# Local Website Blocking

# preference = whether to block specific website or from database. (out of 1,2,3)
def preference() :
    while True:
        default_address = input('''
What would you prefer: 
1) To only restrict access to the specific websites that you've identified (Type 1) OR
2) Only block harmful websites from known database (Type 2)
3) Or do both                             
''')
        if default_address.isdigit() :
                default_address = int(default_address)
                if default_address == 1 :
                        break
                elif default_address == 2 :
                        break
                elif default_address == 3 :
                        break
                else :
                    print("Enter appropriate number.")
        else :
            print("Please enter a number.")
    return default_address

# user_system = Operating system of the user
def user_system():
    while True:
        Operating_System = input("You are using which Operating System: Windows or Linux: ")
        Operating_System = Operating_System.lower()
          
        if Operating_System == "linux":
            break
        elif Operating_System == "windows" :
            break
        else:
            print("Please enter appropriate OS.")

    return Operating_System

# It takes the input of sites that user wants to block
def user_site_input():
    HtmlFile = input("Enter the list of websites that you need to block. Websites should be seperated with spaces: ")
    n = HtmlFile.count(" ") + 1 
    HtmlFile = HtmlFile[0:].split(" ")
    return HtmlFile, n

# To remove https, http from the local database attached
# Local database was updated at 2023-11-25
def refining_database():
    with open("URLhaus_database.txt", "rt") as fin:
        with open("block_url.txt", "wt") as fout:
            for line in fin:
                fout.write(line.replace('http://', ''))
                fout.write(line.replace('https://', ''))

# to read sites from database
def reading_database():
    read_file = open("block_url.txt", 'r', encoding='utf-8', errors='ignore')
    source_code = read_file.read() 
    n = source_code.count("\n") + 1
    source_code = source_code[0:].split("\n")
    return source_code, n

refining_database()

Operating_System = user_system()
user_preference = preference()

if Operating_System == "linux" :
    if user_preference == 1:
        HtmlFile, n = user_site_input()
        for i in range(0,n):
            with open('/etc/hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
    elif user_preference == 2 :
        HtmlFile, n = reading_database()
        for i in range(0,n):
            with open('/etc/hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
    else :
        HtmlFile, n = user_site_input()
        for i in range(0,n):
            with open('/etc/hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")

        HtmlFile, n = reading_database()
        for i in range(0,n):
            with open('/etc/hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
else :
    if user_preference == 1:
        HtmlFile, n = user_site_input()
        for i in range(0,n):
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
    elif user_preference == 2 :
        HtmlFile, n = reading_database()
        for i in range(0,n):
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
    else :
        HtmlFile, n = user_site_input()
        for i in range(0,n):
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
        HtmlFile, n = reading_database()
        for i in range(0,n):
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
