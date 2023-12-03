# Local Website Blocking
import pandas as pd
import requests
import zipfile
import io
import os

# Website
zip_file_url = "https://urlhaus.abuse.ch/downloads/csv/" 

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

# Downlading Zip
def download_zip() :
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

# Retrieving Data
def retrieving_data():
    dataframe = pd.read_csv("csv.txt", skiprows=range(0, 8), usecols = ["url"])
    with open('block_url.txt', 'w') as f:
        df_string = dataframe.to_string(header=False, index=False)
        f.write(df_string)
    os.remove("csv.txt")
    with open("block_url.txt", "rt") as fin:
        with open("block_url0.txt", "wt") as fout:
            for line in fin:
                fout.write(line.replace('http://', '')) 
    with open("block_url0.txt", "rt") as fin:
        with open("block_url.txt", "wt") as fout:
            for line in fin:
                fout.write(line.replace('https://', ''))
    os.remove("block_url0.txt")

# to read sites from database
def reading_database():
    read_file = open("block_url.txt", 'r', encoding='utf-8', errors='ignore')
    source_code = read_file.read() 
    n = source_code.count("\n") + 1
    source_code = source_code[0:].split("\n")
    return source_code, n

# to read the host file if host is edited or not
def hosts_edited_not(user_or_database, host_file):
    with open(host_file,'r') as f:
        for (i, line) in enumerate(f):
            if user_or_database in line:
                return i
    return -1

download_zip()
retrieving_data()
Operating_System = user_system()
user_preference = preference()

if Operating_System == "linux" :

    if user_preference == 1:
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'hosts')
        if start == -1:
            # Starting USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")

        else :
            with open('hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)          

    elif user_preference == 2 :
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'hosts', 'r+') as fp:
                # read an store all lines into list
                lines = fp.readlines()
                # move file pointer to the beginning of a file
                fp.seek(0)
                # truncate the file
                fp.truncate()
                # start writing lines
                # iterate line and line number
                for number, line in enumerate(lines):
                    # delete line number start - 1 and end + 1
                    if number not in range(start , end + 1):
                        fp.write(line)
            # Starting database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")

    else :
    # Doing part 1
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'hosts')
        if start == -1:
            # Starting USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")
        else :
            with open('hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)
        
    # Doing Part 2
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'hosts', 'r+') as fp:
                # read an store all lines into list
                lines = fp.readlines()
                # move file pointer to the beginning of a file
                fp.seek(0)
                # truncate the file
                fp.truncate()
                # start writing lines
                # iterate line and line number
                for number, line in enumerate(lines):
                    # delete line number start - 1 and end + 1
                    if number not in range(start, end+1):
                        fp.write(line)
            # Starting database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
                
    os.remove('block_url.txt')

else:
    if user_preference == 1:
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            # Starting USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")

        else :
            with open('C:\Windows\System32\drivers\etc\hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)          

    elif user_preference == 2 :
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'C:\Windows\System32\drivers\etc\hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as fp:
                # read an store all lines into list
                lines = fp.readlines()
                # move file pointer to the beginning of a file
                fp.seek(0)
                # truncate the file
                fp.truncate()
                # start writing lines
                # iterate line and line number
                for number, line in enumerate(lines):
                    # delete line number start - 1 and end + 1
                    if number not in range(start , end + 1):
                        fp.write(line)
            # Starting database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")

    else :
    # Doing part 1
        start = hosts_edited_not("#### Websites Blocked by USER Starts", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            # Starting USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Starts")
            HtmlFile, n = user_site_input()
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending USER sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by USER Ends" + "\n")
        else :
            with open('C:\Windows\System32\drivers\etc\hosts', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#### Websites Blocked by USER Starts'):
                        HtmlFile, n = user_site_input()
                        for j in range(0,n):
                            lines[i] = lines[i].strip() + '\n' + "127.0.0.1 " + f"{HtmlFile[j]}" + '\n'
                f.seek(0)
                for line in lines:
                    f.write(line)
        
    # Doing Part 2
        start = hosts_edited_not("#### Websites Blocked by Database Starts", 'C:\Windows\System32\drivers\etc\hosts')
        end = hosts_edited_not("#### Websites Blocked by Database Ends", 'C:\Windows\System32\drivers\etc\hosts')
        if start == -1:
            HtmlFile, n = reading_database()
            # Starting database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
        else :
            HtmlFile, n = reading_database()
            with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as fp:
                # read an store all lines into list
                lines = fp.readlines()
                # move file pointer to the beginning of a file
                fp.seek(0)
                # truncate the file
                fp.truncate()
                # start writing lines
                # iterate line and line number
                for number, line in enumerate(lines):
                    # delete line number start - 1 and end + 1
                    if number not in range(start, end+1):
                        fp.write(line)
            # Starting database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Starts")
            for i in range(0,n):
                with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                    f.write("\n" + "127.0.0.1 " + f"{HtmlFile[i]}")
            # Ending database sites marker
            with open('C:\Windows\System32\drivers\etc\hosts', 'a', errors='ignore') as f:
                f.write("\n" + "#### Websites Blocked by Database Ends" + "\n")
                
    os.remove('block_url.txt')
